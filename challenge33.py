import pandas as pd
df = pd.read_csv("data1.csv")
product_A = df[(df["prix_unitaire"] >= 150 ) & (df["categorie"] == "Audio") ]   #filtring
print(product_A)
