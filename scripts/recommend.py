import pandas as pd


performance = pd.read_csv(
    "data/processed/sharpe_ratio.csv"
)

fund_master = pd.read_csv(
    "data/processed/01_fund_master_clean.csv"
)


recommendation_data = performance.merge(
    fund_master[
        [
            "amfi_code",
            "scheme_name",
            "risk_category",
            "fund_house"
        ]
    ],
    on="amfi_code",
    how="left"
)




risk = input(
    "Enter Risk Appetite (Low / Moderate / High): "
).strip().lower()


filtered = recommendation_data[
    recommendation_data["risk_category"].str.lower() == risk
]


if filtered.empty:
    print("\nNo funds found for this risk category.")
    print("\nAvailable Risk Categories are:")
    print(recommendation_data["risk_category"].unique())
    exit()


top3 = (
    filtered
    .sort_values(
        by="sharpe_ratio",
        ascending=False
    )
    .head(3)
)

print("\n========== TOP 3 RECOMMENDED FUNDS ==========\n")

print(
    top3[
        [
            "scheme_name",
            "fund_house",
            "risk_category",
            "sharpe_ratio"
        ]
    ].to_string(index=False)
)