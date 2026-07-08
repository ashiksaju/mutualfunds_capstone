import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")

csv_files = list(RAW_DIR.glob("*.csv"))

if not csv_files:
    print("No CSV files found!")

for file in csv_files:
    print("=" * 50)
    print("File:", file.name)

    df = pd.read_csv(file)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())