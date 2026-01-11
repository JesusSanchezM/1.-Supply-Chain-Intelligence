import pandas as pd


def perform_abc_analysis(df):
    df = df.copy()

    if "TotalSum" not in df.columns:
        df["TotalSum"] = df["Quantity"] * df["Price"]

    abc = (
        df.groupby("Description")["TotalSum"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    abc["CumulativeRevenue"] = abc["TotalSum"].cumsum()
    total = abc["TotalSum"].sum()
    abc["Revenue_Share_Pct"] = 100 * abc["CumulativeRevenue"] / total

    abc["ABC_Class"] = pd.cut(
        abc["Revenue_Share_Pct"], bins=[0, 80, 95, 100], labels=["A", "B", "C"]
    )

    return abc
