import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("Columns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\n=== UNIQUE FUND HOUSES ===")
print(df["fund_house"].unique())

print("\n=== UNIQUE CATEGORIES ===")
print(df["category"].unique())

print("\n=== UNIQUE SUB-CATEGORIES ===")
print(df["sub_category"].unique())

print("\n=== UNIQUE RISK GRADES ===")
print(df["risk_category"].unique())