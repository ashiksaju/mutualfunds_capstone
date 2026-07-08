import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

raw_data = PROJECT_DIR / "data" / "raw"
processed_data = PROJECT_DIR / "data" / "processed"

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    df = pd.read_csv(raw_data / file)

    df = df.drop_duplicates()

    df = df.dropna(how="all")

    print(f"\n{file}")
    print("Missing Values:")
    print(df.isnull().sum())

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in numeric_cols:
        negative_count = (df[col] < 0).sum()

        if negative_count > 0:
            print(f"Anomaly: {negative_count} negative values found in {col}")

    output_file = file.replace(".csv", "_clean.csv")

    df.to_csv(
        processed_data / output_file,
        index=False
    )

    print(f"Saved {output_file}")

print("\nRemaining datasets cleaned successfully!")