import sqlite3
import pandas as pd


def get_connection():
    return sqlite3.connect(
        r"C:\Users\Jesus Sanchez\Desktop\ALEXIS\1. Pre-Trabajo\1. Supply Chain Intelligence\data\processed\retail_vault.db"
    )


# --- SECCIÓN 1: VENTAS TOTALES Y CRECIMIENTO ---


def get_sales_per_year():
    """Calcula las ventas totales agrupadas por el periodo (hojas de Excel)."""
    conn = get_connection()
    query = """
    SELECT Period, SUM(Quantity * Price) AS TotalSales
    FROM transactions
    GROUP BY Period
    ORDER BY Period;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_sales_per_month():
    """Calcula las ventas mensuales para analizar la tendencia temporal."""
    conn = get_connection()
    query = """
    SELECT strftime('%Y-%m', InvoiceDate) AS Month, 
           SUM(Quantity * Price) AS MonthlySales
    FROM transactions
    GROUP BY Month
    ORDER BY Month;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# --- SECCIÓN 2: PRODUCTOS E INVENTARIO ---


def get_top_products_by_revenue(n=10):
    """KPI 3: Los 10 productos que generan más ingresos."""
    conn = get_connection()
    query = f"""
    SELECT Description, SUM(Quantity * Price) AS TotalRevenue
    FROM transactions
    WHERE StockCode NOT IN ('POST', 'D', 'M', 'BANK CHARGES', 'ADJUST', 'ADJUST2')
    GROUP BY StockCode
    ORDER BY TotalRevenue DESC
    LIMIT {n};
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_top_products_by_quantity(n=10):
    """KPI 4: Los 10 productos con mayor rotación física (Volumen)."""
    conn = get_connection()
    query = f"""
    SELECT Description, SUM(Quantity) AS TotalQuantity
    FROM transactions
    WHERE StockCode NOT IN ('POST', 'D', 'M', 'BANK CHARGES', 'ADJUST', 'ADJUST2')
    GROUP BY StockCode
    ORDER BY TotalQuantity DESC
    LIMIT {n};
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_product_matrix_data(n=30):
    """
    Combines Revenue and Quantity metrics for top products to create
    a strategic performance matrix.
    """
    conn = get_connection()
    query = f"""
    SELECT 
        Description, 
        SUM(Quantity * Price) AS TotalRevenue, 
        SUM(Quantity) AS TotalQuantity
    FROM transactions
    WHERE StockCode NOT IN ('POST', 'D', 'M', 'BANK CHARGES', 'ADJUST', 'ADJUST2')
    GROUP BY StockCode
    ORDER BY TotalRevenue DESC
    LIMIT {n};
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# --- SECCIÓN 3: COMPORTAMIENTO GEOGRÁFICO Y CLIENTES ---


def get_geo_analysis():
    """KPI 6: Análisis de ingresos y volumen por país."""
    conn = get_connection()
    query = """
    SELECT Country, 
           SUM(Quantity * Price) AS TotalRevenue,
           SUM(Quantity) AS TotalQuantity
    FROM transactions
    GROUP BY Country
    ORDER BY TotalRevenue DESC;
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_customer_behavior_metrics():
    """KPI 8: Gasto promedio y frecuencia de órdenes por cliente."""
    conn = get_connection()
    # Calculamos métricas promedio a nivel de cliente
    query = """
    SELECT 
        AVG(customer_revenue) AS avg_spend_per_customer,
        AVG(order_count) AS avg_orders_per_customer
    FROM (
        SELECT "Customer ID", 
               SUM(Quantity * Price) AS customer_revenue,
               COUNT(DISTINCT Invoice) AS order_count
        FROM transactions
        WHERE "Customer ID" IS NOT NULL
        GROUP BY "Customer ID"
    );
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# --- SECCIÓN 4: LOGÍSTICA Y PEDIDOS ---


def get_logistics_units_per_order():
    """KPI 9: Promedio de unidades físicas que se mueven por cada pedido."""
    conn = get_connection()
    query = """
    SELECT AVG(items_per_order) AS avg_units_per_order
    FROM (
        SELECT Invoice, SUM(Quantity) AS items_per_order
        FROM transactions
        GROUP BY Invoice
    );
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def get_top_products_pricing_analysis(n=10):
    """KPI 10: Precio unitario y relevancia de los productos más vendidos."""
    conn = get_connection()
    # Obtenemos el precio promedio de cada producto top para ver su posicionamiento
    query = f"""
    SELECT Description, 
           AVG(Price) AS UnitPrice,
           SUM(Quantity * Price) AS TotalRevenue
    FROM transactions
    WHERE StockCode NOT IN ('POST', 'D', 'M', 'BANK CHARGES', 'ADJUST', 'ADJUST2')
    GROUP BY StockCode
    ORDER BY TotalRevenue DESC
    LIMIT {n};
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df
