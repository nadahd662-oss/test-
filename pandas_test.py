#SERIES
'''
import pandas as pd
data = [100, 102, 104, 200, 202]

series = pd.Series(data, index =["a", "b", "c", "d", "e"])

print(series[series < 200])
'''
##EXERCICE:
'''
import pandas as pd

calories = {"D1": 1750, "D2": 2100, "D3": 1700}
series = pd.Series(calories)
#series.loc["D3"] += 500
print(series)
'''
#DF
'''
import pandas as pd
data = {"Name": ["BOB", "EVE", "JOHN"],
        "Age": [25, 21, 55]}
df = pd.DataFrame(data, index=["student 1", "student 2", "student 3" ])
#print(df.ilock[0])
#print(df.loc["student 1"])
### Add a new column:
#df["hobbies"] = ["football", "swimming", "driving"]
### Add a new row:
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "hobby": "reading"}],
index=["students 4"])
df = pd.concat([df, new_row])

print(df)
'''
#IMPORTING:
# SELECTION:
'''
import pandas as pd

df = pd.read_csv("data.csv")
'''
###selecting by column
'''
#print(df["product_name"])
'''

###selecting by row/s 
'''
import pandas as pd
df = pd.read_csv("data.csv", index_col="product_name")

product = input("Enter a product name: ")
try:
    print(df.loc[product])

except KeyError:
    print(f"{product} not found !")
'''

###FILTERING
'''
import pandas as pd
df = pd.read_csv("data.csv")
p = df[df["price"] < 10]
print(p)
'''

### AGGREGATION
import pandas as pd

df = pd.read_csv("data.csv")



 


