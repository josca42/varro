from pathlib import Path
import pandas as pd
from sqlalchemy import inspect

from varro.config import DATA_DIR
from varro.data.disk_to_db.create_db_table import emit_and_apply_fact
from varro.data.disk_to_db.process_tables import process_fact_table
from varro.db.db import engine

FACTS_DIR = DATA_DIR / "statbank_tables"
insp = inspect(engine)


def create_fact_table(table_id: str, fp: Path):
    df = pd.read_parquet(fp)
    df = process_fact_table(df)
    emit_and_apply_fact(df, table_id.lower())


for fp in FACTS_DIR.iterdir():
    table_id = fp.stem

    if insp.has_table(table_id.lower(), schema="fact"):
        print(f"Table {table_id} already exists")
        continue

    create_fact_table(table_id, fp)
    print(f"Table {table_id} processed successfully")
