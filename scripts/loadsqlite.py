import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent

engine = create_engine(f"sqlite:///{PROJECT_DIR / 'bluestock_mf.db'}")

processed = PROJECT_DIR / "data" / "processed"

nav = pd.read_csv(processed / "nav_history_clean.csv")
transactions = pd.read_csv(processed / "investor_transactions_clean.csv")
performance = pd.read_csv(processed / "scheme_performance_clean.csv")

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All tables loaded successfully!")
print("NAV rows:", len(nav))
print("Transactions rows:", len(transactions))
print("Performance rows:", len(performance))