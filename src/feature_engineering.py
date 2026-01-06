# === IMPORTS ===
import pandas as pd

# === TIME-BASED FEATURE ENGINEERING ===


def add_time_features(df, date_col="InvoiceDate"):
    """
    Transforms the date column into categorical and numerical features
    to capture seasonality and consumption cycles.
    """
    # Ensure datetime format
    df[date_col] = pd.to_datetime(df[date_col])

    # --- Basic Seasonality ---
    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Day"] = df[date_col].dt.day
    df["Hour"] = df[date_col].dt.hour

    # --- Weekly Behavior ---
    # 0 = Monday, 6 = Sunday
    df["DayOfWeek"] = df[date_col].dt.dayofweek
    df["DayName"] = df[date_col].dt.day_name()
    df["IsWeekend"] = df["DayOfWeek"].apply(lambda x: 1 if x >= 5 else 0)

    # --- Economic/Payroll Cycles ---
    # Captures liquidity impact at the start/end of the month
    df["IsMonthStart"] = df[date_col].dt.is_month_start.astype(int)
    df["IsMonthEnd"] = df[date_col].dt.is_month_end.astype(int)

    # --- Operational Day Segments (Logistics) ---
    # Helps in warehouse shift planning
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
    Calculates Recency, Frequency, and Monetary metrics for each customer.
    Ensures 'TotalSum' is calculated if not present in the dataset.
    """
    # 1. Ensure TotalSum (Revenue per line) exists
    if "TotalSum" not in df.columns:
        print("⏳ 'TotalSum' not found. Calculating Revenue (Quantity * Price)...")
        df["TotalSum"] = df["Quantity"] * df["Price"]

    # 2. Setup Reference Date (Snapshot date)
    # Using max date + 1 day to ensure Recency > 0
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    # 3. Aggregate Data by Customer
    # We use 'Customer ID' as the primary key
    rfm = df.groupby("Customer ID").agg(
        {
            "InvoiceDate": lambda x: (reference_date - x.max()).days,
            "Invoice": "nunique",
            "TotalSum": "sum",
        }
    )

    # 4. Rename columns for business clarity
    rfm.rename(
        columns={
            "InvoiceDate": "Recency",
            "Invoice": "Frequency",
            "TotalSum": "Monetary",
        },
        inplace=True,
    )

    print("✅ RFM Metrics calculated successfully.")
    return rfm


# === INVENTORY INTELLIGENCE: ABC ANALYSIS ===


def perform_abc_analysis(df):
    """
    Categorizes products based on their revenue contribution (Pareto Principle).
    - Class A: Top 80% of revenue (High priority)
    - Class B: Next 15% of revenue (Medium priority)
    - Class C: Remaining 5% of revenue (Low priority/Tail)
    """
    # 1. Calculate Revenue per Product
    if "TotalSum" not in df.columns:
        df["TotalSum"] = df["Quantity"] * df["Price"]

    abc_df = (
        df.groupby("Description")["TotalSum"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    # 2. Calculate Cumulative Percentages
    abc_df["CumulativeRevenue"] = abc_df["TotalSum"].cumsum()
    total_revenue = abc_df["TotalSum"].sum()
    abc_df["Revenue_Share_Pct"] = (abc_df["CumulativeRevenue"] / total_revenue) * 100

    # 3. Assign ABC Classes
    def classify_abc(percentage):
        if percentage <= 80:
            return "A"
        elif percentage <= 95:
            return "B"
        else:
            return "C"

    abc_df["ABC_Class"] = abc_df["Revenue_Share_Pct"].apply(classify_abc)

    print("✅ ABC Analysis calculation complete.")
    return abc_df


# === BEHAVIORAL CORRELATION MODULE ===


def analyze_cancellation_correlation(rfm_df, cancellations_df):
    """
    Merges RFM segments with cancellation counts per customer.
    Uses targeted fillna to avoid Categorical type conflicts in scores.
    """
    # 1. Aggregate cancellations per customer
    canc_counts = (
        cancellations_df.groupby("Customer ID")
        .size()
        .reset_index(name="CancellationCount")
    )

    # 2. Prepare RFM for merging (ensure Customer ID is a column, not index)
    if rfm_df.index.name == "Customer ID":
        rfm_df = rfm_df.reset_index()

    # 3. Merge data
    correlation_df = pd.merge(rfm_df, canc_counts, on="Customer ID", how="left")

    # 4. Targeted Fillna: Only fill the numeric column to avoid categorical errors
    correlation_df["CancellationCount"] = correlation_df["CancellationCount"].fillna(0)

    print("✅ Cancellation correlation data merged without categorical conflicts.")
    return correlation_df


def calculate_price_elasticity(df):
    """
    Calculates basic price elasticity per SKU.
    Formula: % Change in Quantity / % Change in Price.
    """
    # Group by product and price to see volume variations
    elasticity_data = (
        df.groupby(["Description", "Price"])["Quantity"].sum().reset_index()
    )

    # Calculate percentage changes per group
    elasticity_data["Pct_Change_Q"] = elasticity_data.groupby("Description")[
        "Quantity"
    ].pct_change()
    elasticity_data["Pct_Change_P"] = elasticity_data.groupby("Description")[
        "Price"
    ].pct_change()

    # Calculate Elasticity (avoiding division by zero)
    elasticity_data["Elasticity"] = (
        elasticity_data["Pct_Change_Q"] / elasticity_data["Pct_Change_P"]
    )

    # Filter for valid values
    final_elasticity = elasticity_data.dropna(subset=["Elasticity"])

    print("✅ Price elasticity metrics calculated.")
    return final_elasticity
