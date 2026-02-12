import pandas as pd
df = pd.read_csv("data1.csv")
print("THE 5 FIRST LINES ARE: ")
print(df.head())

print("Number of columns: ")
print(df.columns.tolist)

print("Types of data")
print(df.info())
