# === IMPORTS ===
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# === TIME-BASED FEATURE ENGINEERING ===
def add_time_features(df, date_col="InvoiceDate"):
    """
    Transforms the date column into categorical and numerical features
    to capture seasonality and consumption cycles.
    """
    df[date_col] = pd.to_datetime(df[date_col])

    # Basic Seasonality
    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Day"] = df[date_col].dt.day
    df["Hour"] = df[date_col].dt.hour

    # Weekly Behavior
    df["DayOfWeek"] = df[date_col].dt.dayofweek
    df["DayName"] = df[date_col].dt.day_name()
    df["IsWeekend"] = df["DayOfWeek"].apply(lambda x: 1 if x >= 5 else 0)

    # Economic/Payroll Cycles
    df["IsMonthStart"] = df[date_col].dt.is_month_start.astype(int)
    df["IsMonthEnd"] = df[date_col].dt.is_month_end.astype(int)

    # Operational Day Segments (Logistics)
    df["DayPart"] = pd.cut(
        df["Hour"],
        bins=[0, 6, 12, 18, 24],
        labels=["Early Morning", "Morning", "Afternoon", "Evening"],
        right=False,
    )
    return df


# === RFM CALCULATION MODULE ===
def calculate_rfm_metrics(df):
    """
    Calculates Recency, Frequency, and Monetary metrics per customer.
    Uses 'nunique' for Frequency to avoid per-item inflation.
    """
    if "TotalSum" not in df.columns:
        df["TotalSum"] = df["Quantity"] * df["Price"]

    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("Customer ID").agg(
        {
            "InvoiceDate": lambda x: (reference_date - x.max()).days,
            "Invoice": "nunique",
            "TotalSum": "sum",
        }
    )

    rfm.rename(
        columns={
            "InvoiceDate": "Recency",
            "Invoice": "Frequency",
            "TotalSum": "Monetary",
        },
        inplace=True,
    )

    print(f"✅ RFM metrics calculated for {len(rfm)} unique customers.")
    return rfm


# === AI-DRIVEN CLUSTERING MODULE ===
def prepare_rfm_for_clustering(rfm_df):
    """
    Applies Log Transformation and Standard Scaling to RFM data.
    """
    # Log transform to handle skewness
    rfm_log = np.log1p(rfm_df[["Recency", "Frequency", "Monetary"]])

    # Standard Scaling
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_log)

    scaled_df = pd.DataFrame(
        rfm_scaled, index=rfm_df.index, columns=["Recency", "Frequency", "Monetary"]
    )
    return scaled_df, scaler


# === INVENTORY INTELLIGENCE: ABC ANALYSIS ===
def perform_abc_analysis(df):
    """
    Categorizes products (SKUs) based on revenue contribution (Pareto 80/20).
    """
    if "TotalSum" not in df.columns:
        df["TotalSum"] = df["Quantity"] * df["Price"]

    abc_df = (
        df.groupby("Description")["TotalSum"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    abc_df["CumulativeRevenue"] = abc_df["TotalSum"].cumsum()
    total_revenue = abc_df["TotalSum"].sum()
    abc_df["Revenue_Share_Pct"] = (abc_df["CumulativeRevenue"] / total_revenue) * 100

    def classify_abc(percentage):
        if percentage <= 80:
            return "A"
        elif percentage <= 95:
            return "B"
        else:
            return "C"

    abc_df["ABC_Class"] = abc_df["Revenue_Share_Pct"].apply(classify_abc)
    print("✅ ABC Analysis complete.")
    return abc_df


# === OPTIONAL: PRICE ELASTICITY ===
def calculate_price_elasticity(df):
    elasticity_data = (
        df.groupby(["Description", "Price"])["Quantity"].sum().reset_index()
    )
    elasticity_data["Pct_Change_Q"] = elasticity_data.groupby("Description")[
        "Quantity"
    ].pct_change()
    elasticity_data["Pct_Change_P"] = elasticity_data.groupby("Description")[
        "Price"
    ].pct_change()
    elasticity_data["Elasticity"] = (
        elasticity_data["Pct_Change_Q"] / elasticity_data["Pct_Change_P"]
    )
    return elasticity_data.dropna(subset=["Elasticity"])
