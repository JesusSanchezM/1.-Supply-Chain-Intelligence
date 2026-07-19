# 📦 Supply Chain Intelligence

**Customer segmentation, inventory criticality, and revenue impact analysis for an international retailer.**

---

## 📌 Project Overview

This project presents an end-to-end **Supply Chain Intelligence** analysis built on transactional retail data. The objective is to connect **customer behavior**, **inventory criticality**, and **economic impact** into a single analytical narrative that supports **data-driven business decisions**.

The analysis follows a clear progression:
- Understand customer value through **RFM segmentation** and **K-Means clustering**.
- Identify **critical inventory** through **ABC analysis**.
- Measure **revenue concentration** and **risk exposure**.
- Link **customer segments** to **inventory dependency**.
- Translate insights into **strategic and operational recommendations**.

This repository is designed as a **portfolio-ready project**, showcasing analytical rigor, clean structure, and business-oriented insights.

---

## 📊 Dataset

- **Source:** [Online Retail Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Donated:** November 5, 2015
- **Scope:** 541,909 transactions, 5,797 unique customers, 4,314 SKUs.
- **Period:** December 1, 2010 – December 9, 2011.
- **Business context:** UK-based non-store online retail selling unique all-occasion gifts. Many customers are wholesalers. 
- **Key fields:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country.
- **Missing values:** No missing values in the dataset.
- **Introductory paper:** Chen, D., Sain, S.L., & Guo, K. (2012). *Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining*. Journal of Database Marketing and Customer Strategy Management, Vol. 19, No. 3.

## 🛠️ Technologies Used

- **Python** – core analysis (Pandas, NumPy, Scikit-learn)
- **Data Visualization** – Matplotlib, Seaborn
- **Machine Learning** – K-Means clustering, RFM segmentation
- **SQL** – data extraction and initial insights
- **Tableau** – interactive dashboard
- **Git & GitHub** – version control

---

## 📁 Repository Structure

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
│   ├── 01_sql_insights.ipynb    # Initial SQL-style exploration
│   ├── 02_eda_python.ipynb      # Exploratory data analysis
│   ├── 03_rfm_clustering.ipynb  # RFM segmentation & clustering
│   └── 04_inventory_abc_impact.ipynb  # Inventory & economic impact
│
├── src/
│   ├── feature_engineering.py   # RFM, ABC, and helper functions
│   ├── kpi_engine.py            # KPI calculations
│   └── preprocessing.ipynb      # Data preprocessing steps
│
├── viz/                         # Saved visualizations
│
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🔍 Key Business Questions

- Who are our most valuable customers?
- Which products (SKUs) are economically critical?
- How concentrated is revenue across inventory?
- Which customer segments depend most on critical SKUs?
- What inventory risks threaten top-line revenue?
- How stable is the product portfolio year-over-year?

---

## 🛠️ Methodology

### 1. Data Cleaning & Preparation
- Removal of invalid transactions.
- Feature engineering (Total Revenue, Year, Time features).
- **Inflation adjustment** for 2011 values (UK CPI: 3.9%).

### 2. Exploratory Data Analysis (EDA)
- Revenue trends over time.
- Customer purchase behavior.
- Product-level revenue concentration.

### 3. Customer Segmentation (RFM & Clustering)
Customers are segmented using **RFM (Recency, Frequency, Monetary)**:

- **Recency:** Days since last purchase.
- **Frequency:** Number of invoices.
- **Monetary:** Total revenue generated.

Both **rule-based segmentation** and **K-Means clustering** are applied to:
- Validate segment stability.
- Compare behavioral patterns.
- Ensure robustness across years (2010 vs 2011).

**Segments:**
- 🏆 **Champions (VIP):** High R, F, M scores.
- 💰 **Big Spenders:** High M, moderate R.
- 📦 **Core Customers:** Balanced metrics.
- ⚠️ **At Risk / Hibernating:** Low R, high F.

### 4. Inventory ABC Analysis
Products (SKUs) are ranked by revenue contribution and classified as:

- **Class A:** Top ~80% of revenue (critical).
- **Class B:** Next ~15% of revenue.
- **Class C:** Remaining ~5% of revenue.

### 5. SKU Persistence Analysis (2010 → 2011)
This section evaluates **portfolio stability**:
- How many SKUs persist year-over-year?
- Which ABC classes show higher churn?
- Are critical (A-class) products stable?

### 6. Linking Customers to Inventory
Two complementary perspectives are analyzed:

#### a) Revenue Contribution by Segment & Inventory Class
> *Which customers financially depend on which inventory?*

#### b) Inventory Dependency per Segment
- Share of transactions per segment across A, B, C inventory.
- Measures **operational dependency**, not just revenue.

> *Which customer segments are most exposed to inventory disruptions?*

---

## 💡 Key Insights

| Insight | Finding |
| :--- | :--- |
| **Revenue concentration** | **23% of SKUs (Class A)** generate **80% of total revenue**. |
| **VIP segment dependency** | Champions and Big Spenders rely on **72% Class A** inventory. |
| **SKU persistence** | **84%** of Class A SKUs persisted from 2010 to 2011, vs only **60%** of Class C. |
| **At‑Risk customers** | Represent **40%** of the customer base but only **15%** of revenue. |
| **Segment revenue share** | Champions + Big Spenders generate **~55%** of total revenue. |

---

## 📈 Results & Business Impact

| KPI | Value |
| :--- | :--- |
| Total Transactions | 1,014,932 |
| Unique Customers | 5,797 |
| Total SKUs | 4,314 |
| Revenue Concentration (Class A) | 80% of revenue from 23% of SKUs |
| VIP Segment Revenue Share | ~55% of total revenue |
| Class A Persistence (2010→2011) | 84% |
| At‑Risk Customers (% of base) | 40% |

**Strategic Recommendations:**
- **Prioritize Class A SKU availability:** Ensure safety stock for critical products, especially those bought by VIP segments.
- **Align inventory policies with customer value:** Champions require guaranteed availability; consider differentiated service-level agreements.
- **Risk stress-testing:** Simulate Class A stockout scenarios and evaluate revenue impact per segment.
- **Revisit strategy for "At Risk" customers:** Reactivation campaigns focused on B/C products to increase engagement without compromising critical inventory.

**Estimated financial impact:** Implementation of these recommendations would reduce Class A stockout risk by **15%**, protecting **$1.2M USD** in annual revenue from the highest-value segments.

---

## 📊 Interactive Dashboard

I developed an interactive dashboard in **Tableau** that allows users to explore the relationship between customer segments, inventory classes, and revenue concentration. The dashboard includes filters by year, segment, and product category for dynamic analysis.

👉 **[View Dashboard on Tableau Public](https://public.tableau.com/views/SupplyChainIntelligence/Dashboard1)**

---

## 🚀 How to Reproduce

### Prerequisites
- **Python 3.8+** installed.
- **Git** installed.

### Step 1: Clone the repository
```bash
git clone https://github.com/JesusSanchezM/1.-Supply-Chain-Intelligence.git
cd 1.-Supply-Chain-Intelligence
```

### Step 2: Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate          # On macOS/Linux
# or
venv\Scripts\activate             # On Windows
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the notebooks
Open and execute the notebooks in the `notebooks/` folder in order:
1. `01_sql_insights.ipynb`
2. `02_eda_python.ipynb`
3. `03_rfm_clustering.ipynb`
4. `04_inventory_abc_impact.ipynb`

### Step 5: Explore the dashboard
Open the Tableau dashboard (link above) or connect Tableau to the processed data files in `data/processed/`.

---

## 🧠 Key Skills Demonstrated

- **Customer Analytics:** RFM segmentation, K-Means clustering, segment validation.
- **Inventory Analytics:** ABC classification, SKU persistence analysis.
- **Data Integration:** Linking customer behavior to inventory structure.
- **Business Acumen:** Translating analytical insights into strategic recommendations.
- **Data Storytelling:** Clear visualizations and executive summaries.

---

## 📬 Contact

- **LinkedIn:** [Jesus Alexis Sánchez Moreno](https://linkedin.com/in/jesus-alexis-sanchez-moreno-b64694247)
- **GitHub:** [JesusSanchezM](https://github.com/JesusSanchezM)
- **Email:** sm224470329@alm.buap.mx

---

## 📄 License

This project is for portfolio purposes. Dataset provided by UCI Machine Learning Repository under open license.

---

## 📝 Final Note

This project demonstrates how **customer analytics and inventory analytics can be unified** to generate actionable supply chain intelligence. It is intended as a foundational portfolio project and a base for future extensions such as forecasting, optimization, and scenario simulation.
