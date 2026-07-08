import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

raw_data = PROJECT_DIR / "data" / "raw"
processed_data = PROJECT_DIR / "data" / "processed"

df = pd.read_csv(raw_data / "02_nav_history.csv")

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(["amfi_code", "date"])

df["nav"] = df.groupby("amfi_code")["nav"].ffill()

df = df.drop_duplicates()

df = df[df["nav"] > 0]

df.to_csv(processed_data / "nav_history_clean.csv", index=False)

print("NAV cleaning completed!")
print("Rows:", len(df))