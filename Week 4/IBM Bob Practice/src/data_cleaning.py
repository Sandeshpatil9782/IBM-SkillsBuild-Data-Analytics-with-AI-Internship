"""
data_cleaning.py
================
Retail Sales Analysis – 500 Transactions
-----------------------------------------
Reads  : data/raw/sales_500.csv
Writes : data/processed/sales_cleaned.csv

Cleaning decisions are based solely on the findings recorded in
reports/data_quality_report.md.  Because the data-quality assessment
reported ZERO issues, no rows are expected to be removed.  The script
still applies every check so that it remains correct if the raw file is
ever regenerated with real-world (potentially dirty) data.

Steps performed:
  1. Load raw CSV
  2. Remove fully duplicate rows
  3. Drop rows with duplicate Transaction_ID (keep first occurrence)
  4. Cast columns to correct data types
  5. Parse and validate Transaction_Date
  6. Validate Quantity    (must be >= 1)
  7. Validate Unit_Price  (must be >  0)
  8. Validate Discount_Percentage (must be 0 – 30)
  9. Recalculate Gross_Sales, Discount_Amount, Net_Sales from source columns
 10. Drop rows that still contain missing values after all fixes
 11. Save cleaned dataset
 12. Print cleaning summary
"""

import os
import numpy as np
import pandas as pd

# ── Paths ─────────────────────────────────────────────────────────────────────
RAW_PATH     = os.path.join("data", "raw",       "sales_500.csv")
CLEANED_PATH = os.path.join("data", "processed", "sales_cleaned.csv")

# ── 1. Load raw CSV ───────────────────────────────────────────────────────────
df_raw = pd.read_csv(RAW_PATH)
original_row_count = len(df_raw)

print("=" * 60)
print("RETAIL SALES – DATA CLEANING SCRIPT")
print("=" * 60)
print(f"\n[1] Raw dataset loaded : {original_row_count} rows, {df_raw.shape[1]} columns")

# Work on a copy so the raw DataFrame is never mutated.
df = df_raw.copy()

# Running tally of rows removed at each step.
removed = {}

# ── 2. Remove fully duplicate rows ────────────────────────────────────────────
# A fully duplicate row is one where every column value is identical to
# another row.  These offer no additional information and must be dropped.
n_before = len(df)
df = df.drop_duplicates()
removed["fully_duplicate_rows"] = n_before - len(df)
print(f"[2] Fully duplicate rows removed : {removed['fully_duplicate_rows']}")

# ── 3. Duplicate Transaction_ID ───────────────────────────────────────────────
# Transaction_ID is the primary key.  If the same ID appears more than once
# (without being a full duplicate), we keep the first occurrence and drop the
# rest.  The first occurrence is assumed to be the authoritative record.
n_before = len(df)
df = df.drop_duplicates(subset="Transaction_ID", keep="first")
removed["duplicate_txn_id"] = n_before - len(df)
print(f"[3] Duplicate Transaction_ID rows removed : {removed['duplicate_txn_id']}")

# ── 4. Cast columns to correct data types ─────────────────────────────────────
# All columns arrive as strings when read from CSV.
# We cast each column to its intended type; coerce=True turns un-parseable
# values into NaN so we can handle them explicitly in later steps.

# Integer columns
for col in ["Age", "Quantity"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")  # nullable int

# Float columns
for col in ["Unit_Price", "Discount_Percentage", "Gross_Sales",
            "Discount_Amount", "Net_Sales"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# String columns – strip leading/trailing whitespace that may creep in from CSV
str_cols = ["Transaction_ID", "Customer_ID", "Customer_Name",
            "Gender", "City", "Product_Category", "Product", "Payment_Method"]
for col in str_cols:
    df[col] = df[col].astype(str).str.strip()

print(f"[4] Data types cast correctly")

# ── 5. Parse and validate Transaction_Date ────────────────────────────────────
# Convert the string column to a proper datetime object.
# Rows whose dates cannot be parsed are flagged (set to NaT) and will be
# removed in the missing-value step below.
# We also check that dates fall within the expected year 2024.
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"],
                                        format="%Y-%m-%d",
                                        errors="coerce")

# Mark out-of-range dates as NaT so they are treated as missing.
valid_start = pd.Timestamp("2024-01-01")
valid_end   = pd.Timestamp("2024-12-31")
out_of_range_mask = (
    df["Transaction_Date"].notna() &
    ((df["Transaction_Date"] < valid_start) | (df["Transaction_Date"] > valid_end))
)
df.loc[out_of_range_mask, "Transaction_Date"] = pd.NaT
print(f"[5] Transaction_Date parsed | out-of-range set to NaT : {out_of_range_mask.sum()}")

# ── 6. Validate Quantity (must be >= 1) ───────────────────────────────────────
# A quantity of 0 or below makes no business sense for a sales transaction.
# Invalid values are set to NaN so the row is removed in step 10.
# We do NOT silently replace them with an assumed value — that would invent data.
invalid_qty_mask = df["Quantity"].notna() & (df["Quantity"] < 1)
df.loc[invalid_qty_mask, "Quantity"] = np.nan
print(f"[6] Quantity < 1 set to NaN : {invalid_qty_mask.sum()}")

# ── 7. Validate Unit_Price (must be > 0) ──────────────────────────────────────
# A zero or negative price is not a valid sales price.
invalid_price_mask = df["Unit_Price"].notna() & (df["Unit_Price"] <= 0)
df.loc[invalid_price_mask, "Unit_Price"] = np.nan
print(f"[7] Unit_Price <= 0 set to NaN : {invalid_price_mask.sum()}")

# ── 8. Validate Discount_Percentage (0 – 30 %) ───────────────────────────────
# Business rule: discounts are between 0 % and 30 % inclusive.
# Values outside this range are set to NaN; the row is dropped in step 10.
# We do not clamp them to 0 or 30 because we cannot know the intended value.
invalid_disc_mask = (
    df["Discount_Percentage"].notna() &
    ((df["Discount_Percentage"] < 0) | (df["Discount_Percentage"] > 30))
)
df.loc[invalid_disc_mask, "Discount_Percentage"] = np.nan
print(f"[8] Discount_Percentage out of range set to NaN : {invalid_disc_mask.sum()}")

# ── 9. Recalculate derived columns from source columns ────────────────────────
# Gross_Sales, Discount_Amount, and Net_Sales are always recalculated from
# the (now validated) source columns.  This ensures internal consistency even
# if the original CSV contained stale or mismatched values.
#
# Formulae (rounded to 2 decimal places to match financial display):
#   Gross_Sales    = Quantity × Unit_Price
#   Discount_Amount = Gross_Sales × Discount_Percentage / 100
#   Net_Sales       = Gross_Sales − Discount_Amount

df["Gross_Sales"]     = (df["Quantity"] * df["Unit_Price"]).round(2)
df["Discount_Amount"] = (df["Gross_Sales"] * df["Discount_Percentage"] / 100).round(2)
df["Net_Sales"]       = (df["Gross_Sales"] - df["Discount_Amount"]).round(2)

print("[9] Gross_Sales, Discount_Amount, Net_Sales recalculated")

# ── 10. Drop rows with any remaining missing values ───────────────────────────
# At this point NaN marks data that could not be repaired without inventing
# values (bad dates, invalid quantities, prices, discounts, or un-parseable
# numerics).  Dropping these rows is the only defensible action.
n_before = len(df)
df = df.dropna()
removed["remaining_missing"] = n_before - len(df)
print(f"[10] Rows dropped due to remaining NaN : {removed['remaining_missing']}")

# ── 11. Reset index and save ──────────────────────────────────────────────────
df = df.reset_index(drop=True)

# Restore Transaction_Date to a plain YYYY-MM-DD string for portability.
df["Transaction_Date"] = df["Transaction_Date"].dt.strftime("%Y-%m-%d")

# Restore integer types (drop nullable Int64 → standard int) for clean CSV output
df["Age"]      = df["Age"].astype(int)
df["Quantity"] = df["Quantity"].astype(int)

os.makedirs(os.path.dirname(CLEANED_PATH), exist_ok=True)
df.to_csv(CLEANED_PATH, index=False)
print(f"[11] Cleaned dataset saved to : {CLEANED_PATH}")

# ── 12. Cleaning summary ──────────────────────────────────────────────────────
total_removed = original_row_count - len(df)

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)
print(f"  Original row count          : {original_row_count}")
print(f"  Fully duplicate rows removed: {removed['fully_duplicate_rows']}")
print(f"  Duplicate TXN_ID removed    : {removed['duplicate_txn_id']}")
print(f"  NaN-triggered removals      : {removed['remaining_missing']}")
print(f"  Total rows removed          : {total_removed}")
print(f"  Final row count             : {len(df)}")

print("\n  Remaining missing values per column:")
missing_counts = df.isnull().sum()
if missing_counts.sum() == 0:
    print("    None — 0 missing values across all columns")
else:
    for col, cnt in missing_counts[missing_counts > 0].items():
        print(f"    {col}: {cnt}")

print("\n  Remaining duplicate Transaction_IDs:")
dup_count = df["Transaction_ID"].duplicated().sum()
print(f"    {dup_count}")

print("\n  Remaining fully duplicate rows:")
full_dup_count = df.duplicated().sum()
print(f"    {full_dup_count}")

print("=" * 60)
print("Data cleaning complete.")
print("=" * 60)
