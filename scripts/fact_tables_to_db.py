from pathlib import Path
import pandas as pd
from varro.disk_to_db.create_db_table import emit_and_apply_fact
from varro.disk_to_db.process_tables import process_fact_table
from varro.db import engine
from sqlalchemy import inspect


FACTS_DIR = Path("/mnt/HC_Volume_103849439/statbank_tables")
insp = inspect(engine)

for fp in FACTS_DIR.iterdir():
    table_id = fp.stem
    if insp.has_table(table_id, schema="fact"):
        print(f"Table {table_id} already exists")
        continue

    df = pd.read_parquet(fp)
    df = process_fact_table(df)
    emit_and_apply_fact(df, table_id)
