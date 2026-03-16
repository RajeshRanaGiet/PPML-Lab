import pandas as pd
df_csv = pd.read_csv("sample.csv")
print("DataFrame from csv :", df_csv)
df_json = pd.read_json("sample.json")
print("\n DataFrame from JSON :\n", df_json)