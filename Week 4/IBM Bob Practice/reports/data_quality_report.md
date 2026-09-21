# Data Quality Report
## Dataset: `data/raw/sales_500.csv`
### Project: Retail Sales Analysis – 500 Transactions

---

| | |
|---|---|
| **Report Date** | 2024 (post-generation assessment) |
| **Dataset** | `data/raw/sales_500.csv` |
| **Total Rows** | 500 |
| **Total Columns** | 16 |
| **Raw Dataset Modified?** | No — read-only assessment |

---

## Executive Summary

The dataset passed **all 11 data-quality checks** with zero issues found.  
The raw file is clean and ready for the data-cleaning / processing stage.

| Check | Status | Affected Rows |
|---|---|---|
| Missing values | ✅ Pass | 0 |
| Duplicate rows (full) | ✅ Pass | 0 |
| Duplicate Transaction_ID | ✅ Pass | 0 |
| Incorrect data types | ✅ Pass | 0 |
| Invalid dates (format) | ✅ Pass | 0 |
| Dates out of range | ✅ Pass | 0 |
| Quantity ≤ 0 | ✅ Pass | 0 |
| Unit_Price ≤ 0 | ✅ Pass | 0 |
| Discount_Percentage outside 0–30 | ✅ Pass | 0 |
| Gross_Sales calculation error | ✅ Pass | 0 |
| Discount_Amount calculation error | ✅ Pass | 0 |
| Net_Sales calculation error | ✅ Pass | 0 |

---

## Detailed Check Results

---

### Check 1 — Missing Values

| Column | Missing Count | Status |
|---|---|---|
| Transaction_ID | 0 | ✅ Pass |
| Transaction_Date | 0 | ✅ Pass |
| Customer_ID | 0 | ✅ Pass |
| Customer_Name | 0 | ✅ Pass |
| Gender | 0 | ✅ Pass |
| Age | 0 | ✅ Pass |
| City | 0 | ✅ Pass |
| Product_Category | 0 | ✅ Pass |
| Product | 0 | ✅ Pass |
| Quantity | 0 | ✅ Pass |
| Unit_Price | 0 | ✅ Pass |
| Discount_Percentage | 0 | ✅ Pass |
| Payment_Method | 0 | ✅ Pass |
| Gross_Sales | 0 | ✅ Pass |
| Discount_Amount | 0 | ✅ Pass |
| Net_Sales | 0 | ✅ Pass |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 2 — Duplicate Rows (Full Row Match)

| Finding | Value |
|---|---|
| Fully duplicate rows | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 3 — Duplicate Transaction_ID

| Finding | Value |
|---|---|
| Duplicate Transaction_IDs | 0 |
| Unique Transaction_IDs | 500 |

**Affected Rows:** 0  
**Recommended Action:** None required. All 500 Transaction_IDs are unique.

---

### Check 4 — Incorrect Data Types

Expected types checked against every value in the column:

| Column | Expected Type | Non-conforming Values |
|---|---|---|
| Age | Integer | 0 |
| Quantity | Integer | 0 |
| Unit_Price | Float | 0 |
| Discount_Percentage | Float | 0 |
| Gross_Sales | Float | 0 |
| Discount_Amount | Float | 0 |
| Net_Sales | Float | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required. When loading into a tool (pandas, SQL), cast columns as follows:

| Column | Recommended Cast |
|---|---|
| Transaction_Date | `datetime` / `DATE` |
| Age, Quantity | `int` / `INTEGER` |
| Unit_Price, Discount_Percentage, Gross_Sales, Discount_Amount, Net_Sales | `float` / `DECIMAL` |
| All other columns | `str` / `VARCHAR` |

---

### Check 5 — Invalid / Out-of-Range Dates

| Finding | Value |
|---|---|
| Dates that failed `YYYY-MM-DD` parse | 0 |
| Dates outside 2024-01-01 to 2024-12-31 | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 6 — Quantity ≤ 0

| Finding | Value |
|---|---|
| Rows with Quantity ≤ 0 | 0 |
| Valid range observed | 1 – 10 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 7 — Unit_Price ≤ 0

| Finding | Value |
|---|---|
| Rows with Unit_Price ≤ 0 | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 8 — Discount_Percentage Outside 0–30 %

| Finding | Value |
|---|---|
| Rows with Discount_Percentage < 0 | 0 |
| Rows with Discount_Percentage > 30 | 0 |
| Valid range observed | 0.00 % – 30.00 % |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 9 — Gross_Sales Calculation

**Formula verified:** `Gross_Sales = ROUND(Quantity × Unit_Price, 2)`

| Finding | Value |
|---|---|
| Rows where stored value ≠ recalculated value (tolerance 0.01) | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 10 — Discount_Amount Calculation

**Formula verified:** `Discount_Amount = ROUND(Gross_Sales × Discount_Percentage / 100, 2)`

| Finding | Value |
|---|---|
| Rows where stored value ≠ recalculated value (tolerance 0.01) | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

### Check 11 — Net_Sales Calculation

**Formula verified:** `Net_Sales = ROUND(Gross_Sales − Discount_Amount, 2)`

| Finding | Value |
|---|---|
| Rows where stored value ≠ recalculated value (tolerance 0.01) | 0 |

**Affected Rows:** 0  
**Recommended Action:** None required.

---

## Additional Observations (Informational)

These are not data-quality issues — they are factual observations about the dataset's content distribution.

| Item | Observation |
|---|---|
| Gender distribution | Male: 249 (49.8 %), Female: 251 (50.2 %) — well balanced |
| Payment methods | 6 methods, evenly distributed (81–87 rows each) |
| Age range | 18 – 65 (all within expected bounds) |
| Cities | 10 distinct cities |
| Product categories | 8 distinct categories |
| Products | 40 distinct products |
| Date coverage | Full year 2024 (Jan – Dec) |

---

## Conclusion

> **The dataset is clean.** No corrective action is required on the raw file before proceeding to the data-cleaning and processing stage.  
> The recommended next step is to copy the raw file to `data/processed/`, apply appropriate data-type casting, and proceed with exploratory data analysis.

---

*Report generated by automated PowerShell quality checks. Raw dataset was not modified.*
