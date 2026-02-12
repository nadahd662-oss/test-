import pandas as pd
df = pd.read_csv("data1.csv")

#REMOVE A NA VALUE
'''
df = df.dropna(subset=["quantite", "categorie"])

print(df.to_string())
print("Missing Values are well treated")
'''

#REPLACING A NA VALUE
'''
df = df.fillna({"quantite": "None"})

print(df.to_string())
'''

#FIX INCONSIITENT VALUE
'''
df["categorie"] = df["categorie"].replace({"Accessoires": "Accessory"})


print("DATA WELL TREATED !")

print(df.to_string())
'''

#REMOVE DUPLICATES
df = df.drop_duplicates()

df = df.dropna(subset=["quantite", "categorie"])
print("Missing Values are well treated")



print(df.to_string())


