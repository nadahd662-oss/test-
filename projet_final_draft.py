#------------------
# STEP 1 
#------------------
import pandas as pd

# Load Excel file
file_path = "C:/Users/ADMIN/Desktop/ventes.xlsx"
df = pd.read_excel(file_path)

print("Dataset loaded successfully")
print(df.head())

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nColumns standardized:")
print(df.columns.tolist())

# Create full datetime column (date + hour combined)
df["datetime_reglement"] = pd.to_datetime(df["date_règlement"].astype(str) + " " + df["heure_règlement"].astype(str), errors="coerce") # Feature engineering
#print(df["datetime_reglement"])

# Extract time features
df["year"] = df["datetime_reglement"].dt.year
df["month"] = df["datetime_reglement"].dt.month
df["week"] = df["datetime_reglement"].dt.isocalendar().week
df["day_name"] = df["datetime_reglement"].dt.day_name()
df["hour"] = df["datetime_reglement"].dt.hour

print("Datetime features created")

# Convert financial columns to numeric
financial_cols = ["montant_rgl", "montant_rst", "solde_cpp"]

for col in financial_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Handle missing values
df[financial_cols] = df[financial_cols].fillna(0)
df["client"] = df["client"].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates()

print("\nData cleaning completed")

##---------------------
#STEP 2
##---------------------
# Daily revenue
daily_revenue = df.groupby(df["datetime_reglement"].dt.date)["montant_rgl"].sum()

# Weekly revenue
weekly_revenue = df.groupby("week")["montant_rgl"].sum()

# Monthly revenue
monthly_revenue = df.groupby("month")["montant_rgl"].sum()

print("\nDaily Revenue:")
print(daily_revenue.head())

print("\nWeekly Revenue:")
print(weekly_revenue.head())

print("\nMonthly Revenue:")
print(monthly_revenue.head())

# Best & worst month
best_month = monthly_revenue.idxmax()
worst_month = monthly_revenue.idxmin()

print(f"\nBest month: {best_month}")
print(f"Worst month: {worst_month}")

# Daily average card balance
daily_balance_avg = df.groupby(df["datetime_reglement"].dt.date)["solde_cpp"].mean()

print("\nDaily average prepaid card balance:")
print(daily_balance_avg.head())

##--------------------
# STEP 3
##--------------------

# Top spending clients
top_clients = df.groupby("id_client").agg({"montant_rgl": ["sum", "mean"],"solde_cpp": "mean"})

top_clients.columns = ["total_spent", "average_transaction", "average_balance"]

top_10 = top_clients.sort_values(by="total_spent", ascending=False).head(10)

print("\nTop 10 Premium Clients:")
print(top_10)

# Clients with unpaid amounts
unpaid = df[df["montant_rst"] > 0]

debt_clients = unpaid.groupby("id_client")["montant_rst"].sum().sort_values(ascending=False)

print("\nClients with unpaid balances:")
print(debt_clients)

#-----------------
##STEP 4
#------------------

# Revenue per restaurant
restaurant_perf = df.groupby("restaurant").agg({"montant_rgl": "sum","id_operation": "count"}).sort_values(by="montant_rgl", ascending=False)

restaurant_perf.columns = ["total_revenue", "transaction_count"]

print("\nRestaurant performance:")
print(restaurant_perf)

# Peak hour
peak_hour = df.groupby("hour")["id_operation"].count()

print("\nPeak hour:", peak_hour.idxmax())
print(peak_hour)

#-----------------
## STEP 5
#-----------------
Q1 = df["montant_rgl"].quantile(0.25)
Q3 = df["montant_rgl"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies = df[(df["montant_rgl"] < lower_bound) | (df["montant_rgl"] > upper_bound)]     #filtering

print("\nNumber of anomalies:", len(anomalies))

#-------------------
## STEP 6
#-------------------

cashier_perf = df.groupby("id_user").agg({"montant_rgl": "sum","id_operation": "count"})

cashier_perf.columns = ["total_processed", "transaction_count"]

print("\nCashier Performance:")
print(cashier_perf.sort_values(by="total_processed", ascending=False))

#--------------------
## STEP 7
#--------------------

correlation = df["solde_cpp"].corr(df["montant_rgl"])

print("\nCorrelation between balance and spending:")
print(correlation)

#--------------------
## STEP 8
#--------------------

print("\n=========== FINAL REPORT ===========")

print(f"Total Revenue: {df['montant_rgl'].sum():.2f}")
print(f"Average Balance: {df['solde_cpp'].mean():.2f}")
print(f"Peak Hour: {peak_hour.idxmax()}")
print(f"Total Anomalies: {len(anomalies)}")

print("\nTop Restaurants:")
print(restaurant_perf.head(5))

## STEP 9

fichier = "clean_data.xlsx"
df.to_excel(fichier, index=False, engine="openpyxl")
print("======= New Data======",fichier) 





























































def clean_data(filepath):

    df = pd.read_excel(filepath)

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    df["datetime_reglement"] = pd.to_datetime(df["date_règlement"].astype(str) + " " + df["heure_règlement"].astype(str),errors="coerce")

    df["hour"] = df["datetime_reglement"].dt.hour

    df["montant_rgl"] = pd.to_numeric(df["montant_rgl"], errors="coerce").fillna(0)

    return df


def generate_report(filepath):

    df = clean_data(filepath)

    total_revenue = df["montant_rgl"].sum()

    print("\n===== AUTOMATED DAILY REPORT =====")
    print(f"Total Revenue: {total_revenue:.2f}")


generate_report("C:/Users/ADMIN/Desktop/ventes.xlsx")