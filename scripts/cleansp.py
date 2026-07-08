import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

raw_data = PROJECT_DIR / "data" / "raw"
processed_data = PROJECT_DIR / "data" / "processed"

df = pd.read_csv(raw_data / "07_scheme_performance.csv")

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Missing values after numeric conversion:")
print(df[numeric_cols].isnull().sum())

df = df.dropna(subset=numeric_cols)

anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(len(anomalies))

anomalies.to_csv(
    processed_data / "performance_anomalies.csv",
    index=False
)

df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

df = df.drop_duplicates()

df.to_csv(
    processed_data / "scheme_performance_clean.csv",
    index=False
)

print("\nScheme Performance cleaning completed!")
print("Rows:", len(df))