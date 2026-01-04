import pandas as pd


def add_time_features(df, date_col="InvoiceDate"):
    """
    Transforma la columna de fecha en variables categóricas y numéricas
    para capturar estacionalidad y ciclos de consumo.
    """
    # Asegurar que sea tipo datetime
    df[date_col] = pd.to_datetime(df[date_col])

    # --- Estacionalidad Básica ---
    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["Day"] = df[date_col].dt.day
    df["Hour"] = df[date_col].dt.hour

    # --- Comportamiento Semanal ---
    # 0 = Lunes, 6 = Domingo
    df["DayOfWeek"] = df[date_col].dt.dayofweek
    df["IsWeekend"] = df["DayOfWeek"].apply(lambda x: 1 if x >= 5 else 0)

    # --- Ciclos de Nómina (Económicos) ---
    # ¿Es inicio de mes o fin de mes? (Impacto en liquidez del consumidor)
    df["IsMonthStart"] = df[date_col].dt.is_month_start.astype(int)
    df["IsMonthEnd"] = df[date_col].dt.is_month_end.astype(int)

    # --- Segmentos del Día (Logística) ---
    # Ayuda a planificar turnos en el almacén
    df["DayPart"] = pd.cut(
        df["Hour"],
        bins=[0, 6, 12, 18, 24],
        labels=["Madrugada", "Mañana", "Tarde", "Noche"],
        right=False,
    )

    return df
