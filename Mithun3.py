import pandas as pd
data = {
    "Name": ["Ram", "Vani"],
    "Age": [20,25 ]
}

df = pd.DataFrame(data)
print(df)
print("\n")


print(df.loc[0]) 


