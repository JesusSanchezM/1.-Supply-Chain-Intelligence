# 📦 Supply Chain Intelligence: Customer Segmentation, Inventory Risk & Revenue Impact

<div class='tableauPlaceholder' id='viz1768194095661' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;My&#47;Myseconddashboard_1&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='Myseconddashboard_1&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;My&#47;Myseconddashboard_1&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1768194095661');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='420px';vizElement.style.maxWidth='650px';vizElement.style.width='100%';vizElement.style.minHeight='587px';vizElement.style.maxHeight='887px';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>

## Project Overview

This project presents an end-to-end **Supply Chain Intelligence analysis** built on transactional retail data. The objective is to connect **customer behavior**, **inventory criticality**, and **economic impact** into a single analytical narrative that supports **data-driven business decisions**.

The analysis follows a clear progression:

* Understand customer value through **RFM segmentation**
* Identify **critical inventory (ABC analysis)**
* Measure **revenue concentration and risk exposure**
* Link **customer segments to inventory dependency**
* Translate insights into **strategic and operational recommendations**

This repository is designed as a **portfolio-ready project**, showcasing analytical rigor, clean structure, and business-oriented insights.

---

## Business Questions Addressed

* Who are our most valuable customers?
* Which products (SKUs) are economically critical?
* How concentrated is revenue across inventory?
* Which customer segments depend most on critical SKUs?
* What inventory risks threaten top-line revenue?
* How stable is the product portfolio year-over-year?

---

## Dataset

* **Source:** Online Retail transactional dataset
* **Time period:** 2010–2011
* **Granularity:** Invoice-level transactions
* **Key fields:** Customer ID, Invoice Date, SKU Description, Quantity, Price

(Brief dataset description or link here)

---

## Repository Structure

```
SUPPLY_CHAIN_INTELLIGENCE/
│
├── data/
│   ├── raw/                     # Raw input data
│   └── processed/               # Cleaned and feature-engineered data
│
├── models/                      # Trained models and scalers
│   ├── rfm_kmeans_model.pkl
│   ├── rfm_kmeans_2011.pkl
│   ├── rfm_scaler.pkl
│   └── rfm_scaler_2011.pkl
│
├── notebooks/
│   ├── 01_sql_insights.ipynb     # Initial SQL-style exploration
│   ├── 02_eda_python.ipynb       # Exploratory data analysis
│   ├── 03_rfm_clustering.ipynb   # RFM segmentation & clustering
│   └── 04_inventory_abc_impact.ipynb  # Inventory & economic impact analysis
│
├── src/
│   ├── feature_engineering.py   # RFM, ABC, and helper functions
│   ├── kpi_engine.py             # KPI calculations
│   └── preprocessing.ipynb      # Data preprocessing steps
│
├── viz/                          # (Optional) Saved visualizations
├── venv/                         # Virtual environment
│
├── LICENSE
├── requirements.txt
└── README.md
```

---

## Methodology & Analysis Flow

### 1. Data Cleaning & Preparation

* Removal of invalid transactions
* Feature engineering (Total Revenue, Year, Time features)
* Inflation adjustment for 2011 values

(Explain preprocessing decisions here)

---

### 2. Exploratory Data Analysis (EDA)

* Revenue trends over time
* Customer purchase behavior
* Product-level concentration

(Key EDA insights here)

---

### 3. Customer Segmentation (RFM & Clustering)

Customers are segmented using **RFM (Recency, Frequency, Monetary)** analysis:

* Recency: Days since last purchase
* Frequency: Number of invoices
* Monetary: Total revenue generated

Both **rule-based segmentation** and **K-Means clustering** are applied to:

* Validate segment stability
* Compare behavioral patterns
* Ensure robustness across years (2010 vs 2011)

(Segment definitions here)

(Insert RFM segment visualization here)

---

### 4. Inventory ABC Analysis

Products (SKUs) are ranked by revenue contribution and classified as:

* **Class A:** Top ~80% of revenue
* **Class B:** Next ~15%
* **Class C:** Remaining ~5%

This step identifies **economically critical inventory** and highlights revenue concentration risk.

(Insert ABC Pareto curve here)

---

### 5. SKU Persistence Analysis (2010 → 2011)

This section evaluates **portfolio stability**:

* How many SKUs persist year-over-year?
* Which ABC classes show higher churn?
* Are critical (A-class) products stable?

(Key persistence insights here)

---

### 6. Linking Customers to Inventory

This is the core intelligence layer of the project.

Two complementary perspectives are analyzed:

#### a) Revenue Contribution by Segment & Inventory Class

* How much revenue each customer segment generates
* Broken down by ABC inventory class

This answers:

> *Which customers financially depend on which inventory?*

(Insert revenue by segment & ABC table here)

(Insert stacked revenue bar chart here)

---

#### b) Inventory Dependency per Segment

* Share of transactions per segment across A, B, C inventory
* Measures **operational dependency**, not just revenue

This answers:

> *Which customer segments are most exposed to inventory disruptions?*

(Insert inventory dependency table here)

(Insert inventory dependency stacked bar chart here)

---

## Key Insights

(Insert consolidated insights here, for example:)

* Revenue is highly concentrated in a small subset of SKUs (Class A)
* Champions and Big Spenders generate the majority of revenue
* VIP segments show strong dependency on Class A inventory
* Core and At-Risk customers rely more on B/C products
* Loss of A-class SKUs poses a direct threat to top-line revenue

---

## Strategic Implications

(Insert business recommendations here)

* Prioritize availability of Class A SKUs
* Align safety stock policies with customer value
* Stress-test supply chain risk based on customer dependency
* Use segmentation to guide assortment and replenishment strategy

---

## Dashboard

(Tableau dashboard embedded or linked here)

👉 **(Insert Tableau dashboard link here)**

---

## Tools & Technologies

* Python (Pandas, NumPy, Scikit-learn)
* Data Visualization (Matplotlib, Seaborn)
* SQL-style analysis
* Tableau (Dashboarding)
* Git & GitHub

---

## How to Run This Project

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run notebooks in order (01 → 04)

---

## Author

**Jesús Sánchez**
Data Analyst | Supply Chain & Business Intelligence

Portfolio: [https://jesussanchezm.github.io/Jesus-s_portafolio/](https://jesussanchezm.github.io/Jesus-s_portafolio/)

---

## Final Note

This project demonstrates how **customer analytics and inventory analytics can be unified** to generate actionable supply chain intelligence. It is intended as a foundational portfolio project and a base for future extensions such as forecasting, optimization, and scenario simulation.

(Closing reflection or future work ideas here)
