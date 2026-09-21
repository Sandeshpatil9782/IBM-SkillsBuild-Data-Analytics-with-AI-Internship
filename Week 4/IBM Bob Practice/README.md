# Retail Sales Analysis – 500 Transactions

A beginner-level data analytics portfolio project that simulates a real-world retail sales scenario.
The project covers the full data analytics workflow: data generation → quality assessment → cleaning → exploratory analysis → business insights.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Business Problem](#2-business-problem)
3. [Objectives](#3-objectives)
4. [Dataset Description](#4-dataset-description)
5. [Data Cleaning](#5-data-cleaning)
6. [Exploratory Data Analysis](#6-exploratory-data-analysis)
7. [SQL Analysis](#7-sql-analysis)
8. [Key Business Insights](#8-key-business-insights)
9. [Tools and Technologies](#9-tools-and-technologies)
10. [Project Structure](#10-project-structure)
11. [How to Run the Project](#11-how-to-run-the-project)
12. [Future Improvements](#12-future-improvements)

---

## 1. Project Overview

| | |
|---|---|
| **Project Type** | Data Analytics – End-to-End Pipeline |
| **Level** | Beginner / Junior Portfolio |
| **Dataset** | Synthetic – 500 retail sales transactions |
| **Period** | Full calendar year 2024 (Jan – Dec) |
| **Total Net Revenue Analysed** | ₹1,31,71,997 |
| **Tools** | Python · Pandas · NumPy · Matplotlib · SQL |

This project demonstrates a complete data analytics workflow applied to a retail sales dataset.
It was built as a portfolio project to practise data wrangling, exploratory data analysis, and deriving business observations from structured data.

> **Note:** The dataset is fully synthetic and was generated programmatically for educational purposes.
> No real customer or business data is involved.

---

## 2. Business Problem

A retail company wants to understand its sales performance across a full year.
Specifically, the business needs answers to the following questions:

- Which months, cities, and product categories drive the most revenue?
- Which products are the top and bottom performers?
- How are customers distributed by age and gender, and does either segment spend more?
- Which payment methods are preferred, and do they differ in average order value?
- Does the discount percentage offered on a transaction have a measurable effect on the revenue generated?

---

## 3. Objectives

- [x] Generate a realistic synthetic sales dataset with 500 transactions and 16 columns
- [x] Perform a structured data quality assessment across all 11 quality dimensions
- [x] Clean and type-cast the dataset; recalculate all derived financial columns
- [x] Conduct exploratory data analysis across 13 analytical dimensions
- [x] Produce visualisations for each analysis area
- [x] Derive business observations grounded strictly in the data
- [ ] Write SQL queries to replicate and extend the EDA findings *(in progress)*

---

## 4. Dataset Description

**File:** `data/raw/sales_500.csv`  
**Rows:** 500 | **Columns:** 16 | **No missing values**

### Columns

| Column | Type | Description |
|---|---|---|
| `Transaction_ID` | String | Unique transaction identifier (e.g. TXN12080) |
| `Transaction_Date` | Date | Date of transaction (YYYY-MM-DD, range: 2024-01-01 to 2024-12-31) |
| `Customer_ID` | String | Customer identifier – repeat customers share the same ID |
| `Customer_Name` | String | Full name of the customer |
| `Gender` | String | Male / Female |
| `Age` | Integer | Customer age at time of purchase (18–65) |
| `City` | String | City where the purchase was made (10 cities) |
| `Product_Category` | String | High-level product group (8 categories) |
| `Product` | String | Specific product purchased (40 distinct products) |
| `Quantity` | Integer | Units purchased per transaction (1–10) |
| `Unit_Price` | Float | Price per unit in ₹ |
| `Discount_Percentage` | Float | Discount applied to the transaction (0%–30%) |
| `Payment_Method` | String | Mode of payment (6 methods) |
| `Gross_Sales` | Float | **Derived:** Quantity × Unit_Price |
| `Discount_Amount` | Float | **Derived:** Gross_Sales × Discount_Percentage / 100 |
| `Net_Sales` | Float | **Derived:** Gross_Sales − Discount_Amount |

### Dataset Coverage

| Dimension | Values |
|---|---|
| Cities | Mumbai, Delhi, Bangalore, Chennai, Hyderabad, Kolkata, Pune, Ahmedabad, Jaipur, Surat |
| Product Categories | Electronics, Clothing, Groceries, Home & Kitchen, Sports, Beauty, Books, Toys |
| Payment Methods | Credit Card, Debit Card, UPI, Cash, Net Banking, Wallet |
| Unique Customer IDs | 184 |

---

## 5. Data Cleaning

**Script:** `src/data_cleaning.py`  
**Output:** `data/processed/sales_cleaned.csv`  
**Report:** `reports/data_quality_report.md`

### Data Quality Assessment Results

All 12 quality checks passed with zero issues on the raw dataset:

| Check | Result |
|---|---|
| Missing values (all 16 columns) | ✅ 0 missing values |
| Fully duplicate rows | ✅ 0 duplicates |
| Duplicate Transaction_ID | ✅ All 500 IDs unique |
| Non-numeric values in numeric columns | ✅ 0 type errors |
| Invalid date format | ✅ All dates parse as YYYY-MM-DD |
| Dates outside 2024 range | ✅ All dates within Jan–Dec 2024 |
| Quantity ≤ 0 | ✅ 0 invalid quantities |
| Unit_Price ≤ 0 | ✅ 0 invalid prices |
| Discount_Percentage outside 0–30% | ✅ 0 violations |
| Gross_Sales calculation error | ✅ 0 mismatches |
| Discount_Amount calculation error | ✅ 0 mismatches |
| Net_Sales calculation error | ✅ 0 mismatches |

### Cleaning Steps Applied

Even with a clean dataset, the script applies all steps defensively so it remains correct if rerun on real-world data:

1. Drop fully duplicate rows
2. Drop duplicate `Transaction_ID` (keep first occurrence)
3. Cast all columns to their correct Python/Pandas types (`int64`, `float64`, `datetime64`)
4. Parse and validate `Transaction_Date`; flag out-of-range dates as `NaT`
5. Invalidate `Quantity < 1`, `Unit_Price ≤ 0`, and `Discount_Percentage` outside 0–30 → `NaN`
6. **Recalculate** `Gross_Sales`, `Discount_Amount`, and `Net_Sales` from source columns to guarantee consistency
7. Drop any rows with remaining `NaN` values

**Cleaning result:** 500 rows in → 500 rows out. No data was removed.

---

## 6. Exploratory Data Analysis

**Notebook:** `notebooks/01_sales_eda.ipynb`  
**Charts:** `reports/` (10 PNG files)

### Analyses Performed

| # | Analysis | Chart Type |
|---|---|---|
| 1 | KPI Summary (Total Net Sales, Quantity, Transactions, Avg Order Value) | Tile cards |
| 2 | Monthly Net Sales trend | Bar + line overlay |
| 3 | Sales by City | Horizontal bar |
| 4 | Sales by Product Category | Bar + donut pie |
| 5 | Sales by Product (all 40) | Horizontal bar |
| 6 | Sales by Gender | Grouped bar |
| 7 | Sales by Payment Method | Horizontal bar + donut pie |
| 8 | Top 10 Products by Net Sales | Bar chart |
| 9 | Top 10 Customers by Net Sales | Horizontal bar |
| 10 | Discount Percentage vs Net Sales | Scatter + regression + band average |

### Top-Level Results

| KPI | Value |
|---|---|
| Total Gross Sales | ₹1,51,23,011 |
| Total Discount Given | ₹19,51,014 |
| **Total Net Sales** | **₹1,31,71,997** |
| Overall Effective Discount Rate | 12.90% |
| Total Units Sold | 2,746 |
| Mean Order Value | ₹26,344 |
| Median Order Value | ₹3,838 |

---

## 7. SQL Analysis

**Folder:** `sql/`

> SQL analysis is planned as the next phase of this project.
> Queries will replicate the EDA findings using SQL and extend the analysis with window functions, ranking, and segmentation.

Planned queries include:
- Monthly revenue aggregation with `GROUP BY` and `ORDER BY`
- City and category ranking using `RANK()` / `DENSE_RANK()`
- Customer segmentation by total spend and transaction count
- Payment method performance comparison
- Discount band analysis using `CASE WHEN`

---

## 8. Key Business Insights

All findings below are observations drawn directly from the 500-transaction dataset.
No causal claims are made unless directly supported by the data.

| # | Finding | Supporting Metric |
|---|---|---|
| 1 | **Electronics dominates revenue** | 83.5% of net sales from 14.8% of transactions |
| 2 | **Laptop is the single highest-revenue product** | ₹56.9 L — 43.2% of total net sales; 16 transactions |
| 3 | **Mean order value is heavily skewed** | Mean ₹26,344 vs Median ₹3,838 — driven by high-ticket Electronics |
| 4 | **January and December are peak revenue months** | Together = 28.0% of annual net sales |
| 5 | **August is the lowest-revenue month despite above-average unit sales** | ₹5.12 L revenue; 257 units sold |
| 6 | **Top 5 cities generate 69% of net sales** | Delhi · Kolkata · Chennai · Hyderabad · Mumbai |
| 7 | **Gender split is nearly equal** | Female 50.4% · Male 49.6% of net sales |
| 8 | **Wallet users have the highest average order value** | ₹39,296 vs overall mean ₹26,344 |
| 9 | **Discount level has no meaningful linear relationship with order value** | Pearson r = −0.094 |
| 10 | **76.1% of unique customers made repeat purchases** | 140 of 184 unique Customer IDs |

Full analysis available in [`reports/business_insights.md`](reports/business_insights.md).

---

## 9. Tools and Technologies

| Tool / Library | Version | Purpose |
|---|---|---|
| Python | 3.13 | Core language |
| Pandas | 2.2.3 | Data loading, manipulation, aggregation |
| NumPy | 2.1.3 | Numerical operations, correlation |
| Matplotlib | 3.x | All visualisations |
| Jupyter Notebook | 7.x | Interactive analysis environment |
| PowerShell | 5.1 | Dataset generation, data quality checks |
| Git | — | Version control |

---

## 10. Project Structure

```
Retail-Sales-Analysis/
│
├── data/
│   ├── raw/
│   │   └── sales_500.csv               # Original synthetic dataset (do not modify)
│   └── processed/
│       └── sales_cleaned.csv           # Type-cast, validated, recalculated dataset
│
├── notebooks/
│   └── 01_sales_eda.ipynb              # Full EDA notebook (13 analyses, 10 charts)
│
├── reports/
│   ├── data_quality_report.md          # 12-point quality assessment results
│   ├── business_insights.md            # Observations and further investigation areas
│   ├── 01_kpi_tiles.png
│   ├── 02_monthly_sales.png
│   ├── 03_sales_by_city.png
│   ├── 04_sales_by_category.png
│   ├── 05_sales_by_product.png
│   ├── 06_sales_by_gender.png
│   ├── 07_sales_by_payment.png
│   ├── 08_top10_products.png
│   ├── 09_top10_customers.png
│   └── 10_discount_vs_net_sales.png
│
├── sql/
│   └── (SQL queries – planned)
│
├── src/
│   └── data_cleaning.py                # Reusable cleaning pipeline script
│
├── generate_dataset.py                 # One-time dataset generation script
├── requirements.txt                    # Python dependencies
└── README.md
```

---

## 11. How to Run the Project

### Prerequisites

- Python 3.9 or higher
- pip

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/your-username/retail-sales-analysis.git
cd retail-sales-analysis

# 2. Install dependencies
pip install -r requirements.txt
```

### Run the Data Cleaning Script

```bash
python src/data_cleaning.py
```

This reads `data/raw/sales_500.csv`, applies all cleaning and validation steps,
recalculates the three derived columns, and writes `data/processed/sales_cleaned.csv`.

### Open the EDA Notebook

```bash
jupyter notebook notebooks/01_sales_eda.ipynb
```

Run all cells from top to bottom. Charts are saved automatically to `reports/`.

### Regenerate the Dataset (optional)

```bash
python generate_dataset.py
```

Regenerates `data/raw/sales_500.csv` using a fixed random seed (`seed=42`),
producing the same 500 rows each time.

### Dependencies

```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
jupyter>=1.0.0
notebook>=7.0.0
openpyxl>=3.1.0
```

---

## 12. Future Improvements

The following extensions are planned or would be natural next steps for this project:

| Area | Description |
|---|---|
| **SQL Analysis** | Recreate all EDA aggregations in SQL; add window function queries (ranking, running totals, period-over-period comparison) |
| **Dashboard** | Build an interactive dashboard using Power BI or Tableau to present the key charts in a single view |
| **Statistical Testing** | Apply hypothesis tests (e.g. t-test on gender order values, ANOVA on age groups) to determine whether observed differences are statistically significant |
| **Customer Segmentation** | Use RFM (Recency, Frequency, Monetary) analysis to segment the 184 unique customers |
| **Larger Dataset** | Scale to 5,000–50,000 transactions to validate whether the observed patterns hold at a larger sample size |
| **Time Series Forecasting** | Fit a basic forecasting model to the monthly revenue series to project the next quarter |
| **Real Data** | Apply the same pipeline to a real public retail dataset (e.g. from Kaggle) to practise on messy, real-world data |

---

## Acknowledgements

- Dataset is fully synthetic, generated using Python's `random` module with a fixed seed for reproducibility.
- Project structure and workflow inspired by standard data analytics portfolio practices.

---

*Built as a beginner-level portfolio project to demonstrate end-to-end data analytics skills.*
*All analysis results are calculated from the dataset — no values have been estimated or fabricated.*
