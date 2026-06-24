import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

nav = pd.read_csv("data/processed/nav_history_clean.csv")
transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/scheme_performance_clean.csv")

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All tables loaded successfully!")

print("NAV rows:", len(nav))
print("Transactions rows:", len(transactions))
print("Performance rows:", len(performance))