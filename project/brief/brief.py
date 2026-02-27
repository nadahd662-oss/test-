# ============================================
# 1️ IMPORT LIBRARIES
# ============================================

import pandas as pd
import numpy as np

# ============================================
# 2️ LOAD THE DATA (INGESTION)
# ============================================

#file_path = r"C:\Users\ADMIN\Desktop\python\project\SAS\brief\store.csv"
df = pd.read_csv("store.csv")

print("First 5 rows:")
print(df.head())

print("\nData Information:")
print(df.info())

print("\nDataset Shape:")
print(df.shape)


# ============================================
# 3️ DATA CLEANING
# ============================================

# --- Standardize column names ---
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")

# --- Convert dates to datetime ---
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)
df["ship_date"] = pd.to_datetime(df["ship_date"], dayfirst=True)

# --- Check missing values ---
print("\nMissing Values:")
print(df.isnull().sum())

# --- Handle missing postal codes ---
df["postal_code"] = df["postal_code"].fillna(0)

# --- Remove duplicates ---
df = df.drop_duplicates()

print("\nAfter Cleaning:")
print(df.info())


# ============================================
# 4️ FEATURE ENGINEERING (TRANSFORMATION)
# ============================================

# --- Create shipping delay (in days) ---
df["shipping_delay"] = (df["ship_date"] - df["order_date"]).dt.days

# --- Extract year and month ---
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month

# --- Create year_month column for growth analysis ---
df["year_month"] = df["order_date"].dt.to_period("M")

# ---- Basic Statistics ----
print("\n===== DESCRIPTIVE STATISTICS =====")
print(df.describe())


# ---- Detect negative or impossible values ----
print("\n===== NEGATIVE VALUES CHECK =====")
print("Negative Sales:", (df["sales"] < 0).sum())

# ---- Outlier Detection using IQR ----
Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df["sales"] < lower_bound) | (df["sales"] > upper_bound)]

print("\n===== OUTLIERS DETECTED (SALES) =====")
print("Number of outliers:", outliers.shape[0])


# flag them instead of removing
df["is_sales_outlier"] = np.where((df["sales"] < lower_bound) | (df["sales"] > upper_bound),1,0)


# ============================================
# 5️ KPIs FOR COMMERCIAL DIRECTOR
# ============================================

# --- Total Revenue ---
total_revenue = df["sales"].sum()

# --- Average Sale ---
average_sale = df["sales"].mean()

print(f"\nTotal Revenue: {total_revenue:,.2f}")
print(f"Average Sale: {average_sale:,.2f}")

# --- Sales by Category ---
sales_by_category = df.groupby("category")["sales"].sum()

# --- Sales by Region ---
sales_by_region = df.groupby("region")["sales"].sum()

# --- Sales by Segment ---
sales_by_segment = df.groupby("segment")["sales"].sum()

# --- Top 10 Products ---
top_10_products = (df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10))

print("\nSales by Category:")
print(sales_by_category)

print("\nSales by Region:")
print(sales_by_region)

print("\nSales by Segment:")
print(sales_by_segment)

print("\nTop 10 Products:")
print(top_10_products)

# --- Monthly Growth ---
monthly_sales = df.groupby("year_month")["sales"].sum()
monthly_growth = monthly_sales.pct_change() * 100

print("\nMonthly Sales:")
print(monthly_sales)

print("\nMonthly Growth (%):")
print(monthly_growth)

# ============================================
# 7️ EXPORT CLEAN DATASET
# ============================================

df.to_csv("superstore_clean.csv", index=False)

print("\nClean dataset exported successfully!")