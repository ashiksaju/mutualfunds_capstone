import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df.drop_duplicates()

df = df[df["nav"] > 0]

df.to_csv("data/processed/nav_history_clean.csv", index=False)

print("Cleaning completed!")
print("Rows:", len(df))