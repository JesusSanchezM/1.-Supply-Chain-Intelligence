# 📦 Supply Chain Intelligence: Retail Analytics & Customer Segmentation

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange.svg)
![EDA](https://img.shields.io/badge/Analysis-RFM_Segmentation-green.svg)

## 🎯 Project Overview
This project focuses on transforming raw transactional data from a UK-based online retailer into actionable business intelligence. By leveraging **SQL for data engineering** and **Python for advanced EDA**, I implemented a comprehensive analytics pipeline to optimize supply chain operations and customer retention strategies.

## 🛠️ Tech Stack
* **Data Engineering:** SQLite, Python (Pandas).
* **Visualization:** Seaborn, Matplotlib.
* **Frameworks:** RFM (Recency, Frequency, Monetary) Analysis.
* **Environment:** Virtualenv, Git/GitHub.

## 📊 Key Data Pipeline
1.  **Ingestion & Cleansing:** Handling a 1M+ record dataset, removing outliers (1st & 99th percentiles), and segregating cancellations to maintain data integrity.
2.  **SQL KPI Engine:** Automated extraction of Revenue Growth, Product Velocity, and Geographical Market Share.
3.  **Customer Intelligence:** Implementation of an RFM Model to segment the customer base into actionable tiers (Champions, Loyal, At Risk, Lost).
4.  **Logistics Insight:** Cross-referencing cancellation patterns with customer churn to identify service failures.

## 📈 Strategic Insights Found
* **Seasonality:** Identified peak operational hours (10:00 - 15:00) and mid-week surges, allowing for optimized warehouse labor allocation.
* **Pareto Effect:** 20% of SKUs generate 80% of revenue; implemented ABC analysis for inventory prioritization.
* **Churn Correlation:** High-value customers (Champions) manage a higher volume of returns, requiring a specialized reverse logistics stream to maintain loyalty.

## 📁 Project Structure
```text
├── data/
│   ├── raw/            # Original Excel files
│   └── processed/      # Cleaned CSVs and SQLite Database
├── notebooks/
│   ├── 01_sql_insights.ipynb    # SQL-driven KPI analysis
│   └── 02_eda_python.ipynb     # RFM and Behavioral EDA
├── src/
│   ├── preprocessing.py         # Data cleansing scripts
│   └── kpi_engine.py           # SQL query automation
├── viz/                        # Exported charts for reports
└── README.md
