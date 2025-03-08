"""from results csv remove duplicates or where p1 > p2 and export to results_sorted.csv"""


import pandas  as pd


df = pd.read_csv(r"results.csv")

print(df.head())
print(len(df))


df2 = df.drop_duplicates()
df2 = df2.sort_values(by=["k", "p1"])
df2 = df2[df2["p1"] < df2["p2"]]
print(len(df2))
print(df2.head())

df2.to_csv("results_sorted.csv", index=False)