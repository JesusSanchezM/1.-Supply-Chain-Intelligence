import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def calculate_rfm_metrics(df):
    df = df.copy()

    if "TotalSum" not in df.columns:
        df["TotalSum"] = df["Quantity"] * df["Price"]

    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby("Customer ID")
        .agg(
            {
                "InvoiceDate": lambda x: (reference_date - x.max()).days,
                "Invoice": "nunique",
                "TotalSum": "sum",
            }
        )
        .rename(
            columns={
                "InvoiceDate": "Recency",
                "Invoice": "Frequency",
                "TotalSum": "Monetary",
            }
        )
    )

    return rfm


def prepare_rfm_for_clustering(rfm_df):
    rfm_log = np.log1p(rfm_df[["Recency", "Frequency", "Monetary"]])

    scaler = StandardScaler()
    scaled = scaler.fit_transform(rfm_log)

    scaled_df = pd.DataFrame(
        scaled,
        index=rfm_df.index,
        columns=["Recency", "Frequency", "Monetary"],
    )

    return scaled_df, scaler
