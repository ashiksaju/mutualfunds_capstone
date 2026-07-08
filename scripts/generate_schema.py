import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


db_path = BASE_DIR / "bluestock_mf.db"


sql_folder = BASE_DIR / "sql"
sql_folder.mkdir(exist_ok=True)

schema_file = sql_folder / "schema.sql"


conn = sqlite3.connect(db_path)


schema = "\n".join(conn.iterdump())


create_statements = []

for line in schema.splitlines():

    if (
        line.startswith("CREATE TABLE")
        or line.startswith("CREATE INDEX")
        or line.startswith("CREATE UNIQUE INDEX")
    ):
        create_statements.append(line + ";")

with open(schema_file, "w", encoding="utf-8") as f:

    f.write("-- Bluestock Mutual Fund Database Schema\n\n")

    for statement in create_statements:
        f.write(statement + "\n\n")

conn.close()

print("Schema exported successfully!")
print(schema_file)