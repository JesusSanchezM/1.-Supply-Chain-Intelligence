# === IMPORTS ===
import sqlite3
import pandas as pd

# === GLOBAL CONFIGURATION ===
DATABASE_PATH = r"C:\Users\Jesus Sanchez\Desktop\ALEXIS\1. Pre-Trabajo\1. Supply Chain Intelligence\data\processed\retail_vault.db"


def get_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect(DATABASE_PATH)


# === SECTION 1: SALES TRENDS & GROWTH ===


def get_sales_per_year():
    """Calculates total revenue aggregated by the defined fiscal periods."""
    print("⏳ Querying yearly sales data...")
    connection = get_connection()
    query = """
    SELECT Period, SUM(Quantity * Price) AS TotalSales
    FROM transactions
    GROUP BY Period
    ORDER BY Period;
    """
    sales_df = pd.read_sql(query, connection)
    connection.close()
    print("✅ Yearly sales data retrieved successfully.")
    return sales_df


def get_sales_per_month():
    """Calculates monthly revenue to analyze temporal demand patterns."""
    print("⏳ Querying monthly revenue trends...")
    connection = get_connection()
    query = """
    SELECT strftime('%Y-%m', InvoiceDate) AS Month, 
           SUM(Quantity * Price) AS MonthlySales
    FROM transactions
    GROUP BY Month
    ORDER BY Month;
    """
    monthly_df = pd.read_sql(query, connection)
    connection.close()
    print("✅ Monthly trends retrieved.")
    return monthly_df


# === SECTION 2: PRODUCT PERFORMANCE & INVENTORY ===


def get_top_products_by_revenue(n=10):
    """Identifies the top N products generating the highest financial impact."""
    print(f"⏳ Extracting Top {n} products by revenue...")
    connection = get_connection()
    query = f"""
    SELECT Description, SUM(Quantity * Price) AS TotalRevenue
    FROM transactions
    WHERE StockCode NOT IN ('POST', 'D', 'M', 'BANK CHARGES', 'ADJUST', 'ADJUST2')
    GROUP BY StockCode
    ORDER BY TotalRevenue DESC
    LIMIT {n};
    """
    revenue_df = pd.read_sql(query, connection)
    connection.close()
    print("📊 Revenue-based product ranking complete.")
    return revenue_df


def get_top_products_by_quantity(n=10):
    """Identifies products with the highest inventory turnover (physical volume)."""
    print(f"⏳ Extracting Top {n} products by volume...")
    connection = get_connection()
    query = f"""
    SELECT Description, SUM(Quantity) AS TotalQuantity
    FROM transactions
    WHERE StockCode NOT IN ('POST', 'D', 'M', 'BANK CHARGES', 'ADJUST', 'ADJUST2')
    GROUP BY StockCode
    ORDER BY TotalQuantity DESC
    LIMIT {n};
    """
    quantity_df = pd.read_sql(query, connection)
    connection.close()
    print("📦 Inventory turnover ranking complete.")
    return quantity_df


def get_product_matrix_data(n=30):
    """
    Consolidates Revenue and Quantity metrics for strategic
    product positioning analysis.
    """
    print(f"⏳ Building strategic product matrix for top {n} items...")
    connection = get_connection()
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
    matrix_df = pd.read_sql(query, connection)
    connection.close()
    print("✅ Strategic matrix data ready.")
    return matrix_df


# === SECTION 3: GEOGRAPHICAL & CUSTOMER BEHAVIOR ===


def get_geo_analysis(exclude_uk=True):
    """
    Analyzes Market Share by Country.
    Focuses on international growth by filtering out the domestic market.
    """
    target_market = "International (Ex-UK)" if exclude_uk else "Full Global"
    print(f"⏳ Analyzing geographical distribution for {target_market}...")

    connection = get_connection()
    where_clause = "WHERE Country != 'United Kingdom'" if exclude_uk else ""

    query = f"""
    SELECT Country, 
           SUM(Quantity * Price) AS TotalRevenue,
           SUM(Quantity) AS TotalQuantity,
           COUNT(DISTINCT "Customer ID") AS UniqueCustomers
    FROM transactions
    {where_clause}
    GROUP BY Country
    ORDER BY TotalRevenue DESC;
    """
    geo_df = pd.read_sql(query, connection)
    connection.close()
    print(f"✅ Geographical analysis for {target_market} complete.")
    return geo_df


def get_customer_behavior_metrics():
    """Calculates average spend and order frequency per unique customer."""
    print("⏳ Calculating Customer Persona metrics...")
    connection = get_connection()
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
    behavior_df = pd.read_sql(query, connection)
    connection.close()
    print("👤 Customer behavior metrics consolidated.")
    return behavior_df


# === SECTION 4: LOGISTICS & OPERATIONAL EFFICIENCY ===


def get_logistics_units_per_order():
    """Analyzes the average cargo size dispatched per unique invoice."""
    print("⏳ Calculating logistics load per order...")
    connection = get_connection()
    query = """
    SELECT AVG(items_per_order) AS avg_units_per_order
    FROM (
        SELECT Invoice, SUM(Quantity) AS items_per_order
        FROM transactions
        GROUP BY Invoice
    );
    """
    logistics_df = pd.read_sql(query, connection)
    connection.close()
    print("📦 Operational efficiency metrics ready.")
    return logistics_df


def get_top_products_pricing_analysis(n=10):
    """Analyzes unit price correlation with revenue for top-performing SKUs."""
    print(f"⏳ Analyzing pricing strategy for top {n} SKUs...")
    connection = get_connection()
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
    pricing_df = pd.read_sql(query, connection)
    connection.close()
    print("✅ Pricing correlation analysis complete.")
    return pricing_df


# === SECTION 5: REVERSE LOGISTICS & CANCELLATIONS ===


def get_cancellation_summary_metrics():
    """Quantifies financial loss and volume caused by order cancellations."""
    print("⏳ Calculating reverse logistics impact...")
    connection = get_connection()
    query = """
    SELECT 
        COUNT(DISTINCT Invoice) AS total_cancelled_orders,
        SUM(ABS(Quantity)) AS total_cancelled_units,
        SUM(ABS(Quantity * Price)) AS potential_revenue_loss
    FROM cancellations;
    """
    summary_df = pd.read_sql(query, connection)
    connection.close()
    print("📊 Cancellation financial impact calculated.")
    return summary_df


def get_top_cancelled_products(n=10):
    """Identifies high-risk SKUs with the highest frequency of returns."""
    print(f"⏳ Identifying Top {n} high-risk products (cancellations)...")
    connection = get_connection()
    query = f"""
    SELECT 
        Description, 
        COUNT(*) AS cancellation_event_count, 
        SUM(ABS(Quantity)) AS total_units_cancelled
    FROM cancellations
    WHERE Description IS NOT NULL
    GROUP BY Description
    ORDER BY total_units_cancelled DESC
    LIMIT {n};
    """
    top_cancelled_df = pd.read_sql(query, connection)
    connection.close()
    print("⚠️ High-risk SKU identification complete.")
    return top_cancelled_df
