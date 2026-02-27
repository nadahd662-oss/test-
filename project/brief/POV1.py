
#DATA INGESTION AND CLEANING

# ======================
# DATA CLEANING
# ======================

import pandas as pd
#file_path =  (r"C:\Users\ADMIN\Desktop\python\project\brief\store.csv")
df = pd.read_csv("store.csv")
print(f"COLUMNS ARE: {df.columns}")
print(df.shape)
print(df.describe())
print(df.info())
print(df.head())
print(f"Duplicates found: {df.duplicated().sum()}")
print(f" Missing values:\n{df.isnull().sum()}")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True) 
df["ship_date"] = pd.to_datetime(df["ship_date"], dayfirst=True)
print(df.info())
df = df.drop_duplicates()
print(df.columns)
df["postal_code"] = df["postal_code"].fillna(0)

# ======================
# FEATURE ENGINEERING
# ======================

df["shipping_delay"] = (df["ship_date"] - df["order_date"]).dt.days
df["order_year"] = df["order_date"].dt.year
df["order_month"] = df["order_date"].dt.month
df['quarter'] = df['order_date'].dt.quarter

# ======================
# KPIs CALCULATION
# ======================
### TOTAL REVENUE
TR = df["sales"].sum()
average_sales = df["sales"].mean()
print(f" The Total Revenue is: {TR:,.2f}")
print(f"The Average total: {average_sales:,.2f}")

# Profit simulated using assumed 20% margin (dataset does not include cost data)
df["profit"] = df["sales"] * 0.20
TP = df["sales"] 
### AVERAGE MARGIN %
#average_margin = (TP / TR) * 100 

#print(f"The Total Profit: {TP:,.2f}")
#print(f"Total Profit:    ${TP:,.2f}")
#print(f"The Average Margin: {average_margin:2f}%")
### SALES BY REGION
sales_by_region = df.groupby("region")["sales"].sum()
### SALES BY CATEGORY
sales_by_category = df.groupby("category")["sales"].sum()
### TOP 10 PRODUCTS
top_10 = df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)
print(f"\nSALES BY REGION: ")

print(sales_by_region) 
print(f"\nSALES BY CATEGORY: ")
print(sales_by_category)
print(f"TOP 10 PRODUCTS: {top_10}")

### MONTHLY GROWTH
df["month_period"] = df["order_date"].dt.to_period("M")
monthly_sales = df.groupby("month_period")["sales"].sum()
monthly_sales = monthly_sales.sort_index()
growth = monthly_sales.pct_change() * 100
growth = growth.fillna(0)
growth_report = pd.DataFrame({'Revenue': monthly_sales,'Growth %': growth})

print(growth_report.round(2))


negative_sales = (df["sales"] < 0).sum()
negative_profit = (df["profit" < 0]).sum()


