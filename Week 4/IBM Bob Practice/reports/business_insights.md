# Business Insights Report
## Retail Sales Analysis – 500 Transactions (2024)

> **Data source:** `data/processed/sales_cleaned.csv`  
> **Period covered:** 1 January 2024 – 31 December 2024  
> **All values are calculated directly from the cleaned dataset. No values have been estimated or fabricated.**

---

## 1. Executive Summary

The retail operation recorded **500 transactions** across 2024, generating **₹1,31,71,997 in net sales** from **2,746 units** sold across **10 cities**, **8 product categories**, and **40 distinct products**.

| Metric | Value |
|---|---|
| Total Gross Sales | ₹1,51,23,011 |
| Total Discount Given | ₹19,51,014 |
| **Total Net Sales** | **₹1,31,71,997** |
| Overall Effective Discount Rate | 12.90% |
| Total Units Sold | 2,746 |
| Number of Transactions | 500 |
| Mean Order Value | ₹26,344 |
| Median Order Value | ₹3,838 |
| Unique Customer IDs | 184 |

**Notable observation:** The mean order value (₹26,344) is nearly 7× the median (₹3,838). This large gap indicates that a small number of very high-value Electronics transactions are pulling the mean upward. The median is the more representative figure for a typical transaction.

---

## 2. Sales Performance

### 2.1 Annual Revenue

Total net sales of **₹1.32 crore** were generated from 500 transactions over 12 months. The overall effective discount rate was **12.90%** (₹19.51 L discounted from ₹1.51 crore in gross sales).

### 2.2 Monthly Trends

| Month | Net Sales (₹) | Units Sold | Observation |
|---|---|---|---|
| January | 18,87,219 | 190 | Highest revenue month |
| February | 13,96,419 | 201 | Second strongest month |
| March | 6,50,929 | 274 | Large unit volume, lower revenue → more low-value items sold |
| April | 14,55,930 | 206 | Strong recovery |
| May | 13,22,480 | 238 | Moderate |
| June | 10,98,914 | 174 | Decline begins |
| July | 8,73,460 | 226 | Mid-year low |
| August | 5,11,923 | 257 | Lowest revenue; highest mid-year unit volume |
| September | 6,74,675 | 238 | Partial recovery |
| October | 8,59,817 | 313 | Highest unit volume month of the year |
| November | 6,35,410 | 185 | Weak revenue relative to Oct |
| December | 18,04,821 | 244 | Second highest revenue; year-end peak |

**Observations:**
- **January and December** are the two highest-revenue months, together accounting for ₹36.9 L (28.0% of annual net sales).
- **August** is the weakest revenue month (₹5.12 L), despite selling 257 units — the second-highest unit count for any month outside October.
- **March and August** share a pattern: high unit volumes paired with below-average revenue, suggesting these months skew toward lower-priced product categories (Groceries, Books, Beauty).
- There is no monotonic seasonal trend; revenue fluctuates significantly month-to-month.

> ⚠️ **Limitation:** With 500 transactions across 12 months (~42 per month on average), monthly figures are based on relatively small samples. Directional patterns are observable but should not be treated as statistically robust seasonal trends without additional data.

---

## 3. Customer Insights

### 3.1 Customer Base

| Metric | Value |
|---|---|
| Unique Customer IDs in dataset | 184 |
| Single-purchase customers | 44 (23.9% of unique customers) |
| Repeat customers (2+ transactions) | 140 (76.1% of unique customers) |
| Customers with 5+ transactions | 22 |
| Max transactions by one customer | 7 |

**Observation:** 76.1% of the 184 unique Customer IDs made more than one purchase during the year. However, the 500 transactions spread across 184 unique IDs means average transactions per customer is 2.7. The dataset contains repeat buyers, not just one-off purchasers.

> Note: Customer names are not guaranteed unique identifiers — `Customer_ID` is the definitive field. Top-customer rankings are by `Customer_Name` as displayed in the EDA; results should be re-confirmed against `Customer_ID` in a production system.

### 3.2 Gender

| Gender | Net Sales (₹) | Share | Transactions | Avg Order Value (₹) | Total Units |
|---|---|---|---|---|---|
| Female | 66,39,631 | 50.41% | 251 | 26,453 | 1,359 |
| Male | 65,32,366 | 49.59% | 249 | 26,234 | 1,387 |

**Observation:** Sales are nearly equally split between Female (50.4%) and Male (49.6%) customers. Average order values are also almost identical (₹26,453 vs ₹26,234 — a difference of <1%). No material gender-based purchase behaviour difference is observable in this dataset.

### 3.3 Age Distribution

| Age Band | Net Sales (₹) | Transactions |
|---|---|---|
| 18–25 | 32,47,797 | 71 |
| 26–35 | 18,70,403 | 109 |
| 36–45 | 36,94,861 | 112 |
| 46–55 | 27,94,213 | 113 |
| 56–65 | 15,64,723 | 95 |

**Observations:**
- The **36–45 age band** generates the highest net sales (₹36.9 L) and ties for highest transaction count (112).
- The **18–25 age band** generates the second-highest net sales (₹32.5 L) from only 71 transactions — implying a notably higher average order value per transaction for this group.
  - Calculated avg: ₹32,47,797 ÷ 71 = **₹45,744 per transaction** vs overall mean of ₹26,344.
- The **26–35 age band** has the most transactions (109) but the lowest net sales (₹18.7 L) — the lowest average order value of any group (₹17,160), suggesting this group purchases more lower-value items.

> ⚠️ These patterns are observational. They reflect what is in the 500-transaction dataset and should not be generalised without larger sample validation.

### 3.4 Top 10 Customers by Net Sales

| Rank | Customer Name | Net Sales (₹) | Transactions |
|---|---|---|---|
| 1 | Vivaan Shah | 7,00,025 | 1 |
| 2 | Anjali Mehta | 5,83,268 | 1 |
| 3 | Anjali Srivastava | 5,40,980 | 1 |
| 4 | Deepak Tiwari | 5,26,979 | 3 |
| 5 | Vihaan Rao | 4,87,968 | 1 |
| 6 | Priya Patel | 4,82,985 | 1 |
| 7 | Amit Bose | 4,51,789 | 1 |
| 8 | Pooja Pandey | 3,99,097 | 2 |
| 9 | Sai Joshi | 3,54,899 | 2 |
| 10 | Suresh Yadav | 3,52,095 | 1 |

**Observation:** Seven of the top 10 customers reached their ranking via a **single transaction**. This strongly suggests their high spend is driven by one high-value Electronics purchase (e.g., a Laptop at ₹45,000–₹95,000 × multiple units), not by sustained purchasing loyalty. **Deepak Tiwari** (rank 4, 3 transactions) is the most consistent high-value buyer in this group.

---

## 4. Product Insights

### 4.1 Category Performance

| Category | Net Sales (₹) | Share | Transactions | Units Sold | Avg Order Value (₹) |
|---|---|---|---|---|---|
| Electronics | 1,09,95,490 | 83.48% | 74 | 421 | 1,48,588 |
| Sports | 5,26,621 | 4.00% | 67 | 373 | 7,860 |
| Clothing | 4,32,932 | 3.29% | 49 | 261 | 8,835 |
| Home & Kitchen | 4,32,726 | 3.29% | 59 | 311 | 7,334 |
| Toys | 3,24,656 | 2.46% | 68 | 328 | 4,774 |
| Beauty | 2,38,725 | 1.81% | 58 | 338 | 4,116 |
| Groceries | 1,16,884 | 0.89% | 78 | 439 | 1,499 |
| Books | 1,03,963 | 0.79% | 47 | 275 | 2,212 |

**Observations:**
- **Electronics commands 83.48% of net sales** from only 74 transactions (14.8% of all transactions). This is entirely driven by unit price — Electronics items range from ₹1,500 (Earphones) to ₹95,000 (Laptop).
- **Groceries generates the most unit volume** (439 units from 78 transactions — avg 5.6 units/transaction) but only ₹1.17 L in net sales because of very low unit prices (₹80–₹600).
- The **bottom 7 categories combined** account for only 16.52% of net revenue, despite making up 85.2% of transactions.

### 4.2 Top 10 Products by Net Sales

| Rank | Product | Net Sales (₹) | Transactions | Units Sold |
|---|---|---|---|---|
| 1 | Laptop | 56,90,035 | 16 | 100 |
| 2 | Smartphone | 24,65,054 | 15 | 81 |
| 3 | Tablet | 19,43,913 | 18 | 94 |
| 4 | Smartwatch | 6,23,460 | 10 | 60 |
| 5 | Earphones | 2,73,029 | 15 | 86 |
| 6 | Cricket Bat | 2,24,630 | 16 | 98 |
| 7 | Mixer Grinder | 2,12,522 | 18 | 92 |
| 8 | Dumbbells | 1,55,424 | 19 | 100 |
| 9 | Remote Car | 1,33,613 | 18 | 79 |
| 10 | Jacket | 1,30,932 | 13 | 50 |

**Observations:**
- **Laptop alone accounts for ₹56.9 L — 43.2% of total net sales** — from just 16 transactions.
- **Dumbbells and Cricket Bat** each sold 98–100 units with 16–19 transactions, indicating consistent multi-unit purchases in Sports.
- **Cricket Bat** is the only non-Electronics product in the top 6 by net sales.

### 4.3 Bottom 5 Products by Net Sales

| Product | Net Sales (₹) | Transactions | Units Sold |
|---|---|---|---|
| Sugar (5 kg) | 13,777 | 16 | 75 |
| Fiction Novel | 11,864 | 8 | 36 |
| Water Bottle | 9,583 | 8 | 31 |
| Comic Book | 9,483 | 7 | 38 |
| Pulses (1 kg) | 7,744 | 15 | 82 |

**Observation:** The five lowest-revenue products are all from Groceries or Books — categories with inherently low unit prices (₹80–₹600). Low net sales for these products do not necessarily indicate poor demand; they reflect the nature of the product price point.

---

## 5. Geographic Insights

### 5.1 Net Sales by City

| Rank | City | Net Sales (₹) | Share | Transactions | Avg Order Value (₹) |
|---|---|---|---|---|---|
| 1 | Delhi | 20,01,959 | 15.20% | 46 | 43,521 |
| 2 | Kolkata | 19,22,362 | 14.59% | 47 | 40,901 |
| 3 | Chennai | 18,60,444 | 14.12% | 44 | 42,283 |
| 4 | Hyderabad | 17,42,886 | 13.23% | 63 | 27,665 |
| 5 | Mumbai | 15,60,443 | 11.85% | 50 | 31,209 |
| 6 | Jaipur | 11,54,689 | 8.77% | 62 | 18,624 |
| 7 | Pune | 10,50,957 | 7.98% | 46 | 22,847 |
| 8 | Surat | 9,65,380 | 7.33% | 55 | 17,552 |
| 9 | Bangalore | 5,14,686 | 3.91% | 44 | 11,697 |
| 10 | Ahmedabad | 3,98,192 | 3.02% | 43 | 9,260 |

**Observations:**
- The **top 5 cities** (Delhi, Kolkata, Chennai, Hyderabad, Mumbai) account for **69.0%** of net sales.
- **Delhi, Chennai, and Kolkata** have similarly high average order values (₹40,901–₹43,521) despite similar transaction counts (44–47), suggesting these cities have a higher proportion of Electronics purchases.
- **Hyderabad** has the most transactions (63) but a lower average order value (₹27,665), indicating a more diverse or lower-value purchase mix.
- **Ahmedabad and Bangalore** are the weakest cities — both by total net sales and by average order value (₹9,260 and ₹11,697 respectively). This could reflect fewer high-value transactions rather than low transaction counts (both have 43–44 transactions).

> ⚠️ Transaction counts per city range from 43 to 63 (relatively balanced by design), so city-level revenue differences are largely driven by order value mix, not transaction volume.

---

## 6. Payment Behavior

### 6.1 Payment Method Analysis

| Payment Method | Net Sales (₹) | Share | Transactions | Avg Order Value (₹) |
|---|---|---|---|---|
| Wallet | 31,82,988 | 24.16% | 81 | 39,296 |
| Net Banking | 26,23,691 | 19.92% | 81 | 32,391 |
| Cash | 23,84,755 | 18.10% | 83 | 28,732 |
| UPI | 21,08,483 | 16.01% | 85 | 24,806 |
| Credit Card | 17,18,727 | 13.05% | 87 | 19,755 |
| Debit Card | 11,53,352 | 8.76% | 83 | 13,896 |

**Observations:**
- **Wallet** generates the highest net sales (₹31.8 L, 24.2%) and has the highest average order value (₹39,296), despite having the same transaction count as Net Banking (81 each).
- **Transaction counts are broadly even across all six methods** (81–87 transactions), meaning the revenue differences arise entirely from **average order value**, not from usage frequency.
- **Credit Card and Debit Card** have the two lowest average order values (₹19,755 and ₹13,896). This is an observation about the data; no causal claim about payment method preference is made.
- **Debit Card** is the lowest-revenue method (₹11.5 L, 8.8%) despite having 83 transactions — the lowest average order value of all methods (₹13,896).

---

## 7. Discount Analysis

### 7.1 Overall Discount Statistics

| Metric | Value |
|---|---|
| Min Discount | 0.00% |
| Max Discount | 29.92% |
| Mean Discount | 14.73% |
| Median Discount | 14.56% |
| Std Deviation | 8.90% |
| 25th Percentile | 7.22% |
| 75th Percentile | 22.88% |
| Total Discount Given | ₹19,51,014 |
| Effective Overall Discount Rate | 12.90% |

The mean (14.73%) and median (14.56%) discount are very close, indicating discounts are fairly uniformly distributed across the dataset — consistent with the random generation method.

### 7.2 Discount by Category

| Category | Avg Discount % |
|---|---|
| Beauty | 15.62% |
| Home & Kitchen | 15.39% |
| Sports | 15.21% |
| Groceries | 15.08% |
| Toys | 14.81% |
| Clothing | 14.03% |
| Electronics | 13.88% |
| Books | 13.45% |

**Observation:** Average discount rates across categories are all between 13.45% and 15.62% — a narrow 2.2 percentage-point spread. No category has a structurally higher or lower discount rate in this dataset.

### 7.3 Discount–Revenue Relationship

| Metric | Value |
|---|---|
| Pearson r (Discount % vs Net Sales) | −0.0943 |

A Pearson correlation of **−0.094** is very close to zero, indicating **no meaningful linear relationship** between the discount percentage applied to a transaction and the net sales value of that transaction.

**What this means:** In this dataset, order value is determined primarily by the product being purchased (category and unit price) and quantity — not by how large a discount was given. A customer buying a laptop at a 2% discount generates far more revenue than a customer buying rice at a 28% discount.

> ⚠️ **Correlation ≠ causation.** This result does not mean that changing discount policy would have no effect on sales behaviour. It means that, in the observed transaction data, the discount level and the order value vary independently of each other.

---

## 8. Key Findings

The following findings are **direct observations** from the cleaned 500-transaction dataset.

| # | Finding | Supporting Metric |
|---|---|---|
| 1 | **Electronics dominates revenue.** | 83.48% of net sales from 14.8% of transactions |
| 2 | **Laptop is the single most impactful product.** | 43.2% of net sales from 16 transactions |
| 3 | **Mean order value is heavily skewed.** | Mean ₹26,344 vs Median ₹3,838 — a 7× gap |
| 4 | **January and December are peak revenue months.** | Together = 28.0% of annual net sales |
| 5 | **August is the lowest-revenue month despite above-average unit volume.** | ₹5.12 L revenue, 257 units sold |
| 6 | **Top 5 cities account for 69% of net sales.** | Delhi + Kolkata + Chennai + Hyderabad + Mumbai |
| 7 | **Gender split is nearly equal in both transactions and revenue.** | 50.4% Female / 49.6% Male |
| 8 | **Wallet users have the highest average order value.** | ₹39,296 vs overall mean ₹26,344 |
| 9 | **Discount rate has no meaningful linear relationship with order value.** | r = −0.094 |
| 10 | **76.1% of unique customers made more than one purchase.** | 140 of 184 unique Customer IDs |
| 11 | **The 18–25 age band has the highest average spend per transaction.** | ₹45,744 vs overall mean ₹26,344 |
| 12 | **Bottom 7 categories combined = 16.5% of revenue from 85.2% of transactions.** | Non-Electronics categories |

---

## 9. Recommended Areas for Further Investigation

The following are **analytical questions** raised by the EDA findings. They are not business recommendations — they are directions for deeper investigation that the available data could support (or that would require additional data).

---

### 9.1 Investigate the August Revenue Dip

**Observation:** August has the second-highest unit volume (257) but the lowest revenue (₹5.12 L).  
**Question to investigate:** What product mix was sold in August? If August transactions concentrated heavily in Groceries, Beauty, and Books, the low revenue is explained by product mix alone, not by lower demand or fewer customers.  
**How to investigate:** Cross-tabulate August transactions by Product_Category and compare to the annual average.

---

### 9.2 Understand the High-Spend 18–25 Age Band

**Observation:** Customers aged 18–25 generated ₹32.5 L from only 71 transactions — an average of ₹45,744 per transaction, the highest of any age group.  
**Question to investigate:** Are 18–25-year-old customers disproportionately buying Electronics (specifically Laptops), or do they genuinely purchase higher quantities?  
**How to investigate:** Filter the dataset to Age 18–25 and examine Product_Category and Product distributions.

---

### 9.3 Wallet vs Other Payment Methods — Order Value Difference

**Observation:** Wallet transactions have an average order value of ₹39,296, which is 49% higher than the overall mean.  
**Question to investigate:** Is the higher Wallet average order value driven by the product mix of Wallet users (i.e., do Wallet users happen to buy more Electronics?), or is there something else?  
**How to investigate:** Cross-tabulate Payment_Method with Product_Category to see whether Wallet transactions are concentrated in Electronics.

---

### 9.4 City-Level Product Mix

**Observation:** Delhi, Chennai, and Kolkata have high average order values (₹40,000+), while Ahmedabad and Bangalore have low average order values (₹9,000–₹12,000).  
**Question to investigate:** Does the difference in city-level revenue reflect a different product mix across cities, or a different number of high-value customers?  
**How to investigate:** Break down net sales by City × Product_Category.

---

### 9.5 Discount Policy Effectiveness

**Observation:** The overall discount–revenue correlation is −0.094 (effectively zero). The average discount across all categories is between 13.45% and 15.62%.  
**Question to investigate:** Is the current uniform discount policy (random 0–30%) having any measurable effect on purchase behaviour, or is purchasing driven entirely by product need?  
**Note:** This dataset does not contain non-purchase data (e.g., browsing without buying), so measuring the effect of discounts on conversion is not possible with the current data alone.

---

### 9.6 Repeat Customer Value

**Observation:** 140 of 184 unique customers made repeat purchases. The maximum was 7 transactions from one customer.  
**Question to investigate:** Do repeat customers have a higher lifetime spend or higher average order value than single-purchase customers? Is there a segment of very high-value repeat buyers worth prioritising?  
**How to investigate:** Compute total and average spend per Customer_ID, segmented by number of transactions.

---

*Report generated from `data/processed/sales_cleaned.csv`. All values are computed metrics — no values have been estimated or fabricated. Insights are observational; causal claims have been explicitly avoided unless directly supported by the data.*
