import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

raw_data = PROJECT_DIR / "data" / "raw"
processed_data = PROJECT_DIR / "data" / "processed"

df = pd.read_csv(raw_data / "08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]

df = df[df["transaction_type"].isin(valid_types)]

df = df[df["amount_inr"] > 0]

print("Unique KYC Status Values:")
print(df["kyc_status"].unique())

df = df.drop_duplicates()

df.to_csv(
    processed_data / "investor_transactions_clean.csv",
    index=False
)

print("\nTransaction cleaning completed!")
print("Rows:", len(df))