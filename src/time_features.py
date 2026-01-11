import pandas as pd


def add_time_features(df, date_col="InvoiceDate"):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Day"] = df[date_col].dt.day
    df["Hour"] = df[date_col].dt.hour

    df["DayOfWeek"] = df[date_col].dt.dayofweek
    df["DayName"] = df[date_col].dt.day_name()
    df["IsWeekend"] = (df["DayOfWeek"] >= 5).astype(int)

    df["IsMonthStart"] = df[date_col].dt.is_month_start.astype(int)
    df["IsMonthEnd"] = df[date_col].dt.is_month_end.astype(int)

    df["DayPart"] = pd.cut(
        df["Hour"],
        bins=[0, 6, 12, 18, 24],
        labels=["Early Morning", "Morning", "Afternoon", "Evening"],
        right=False,
    )
    return df
