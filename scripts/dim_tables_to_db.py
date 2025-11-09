from pathlib import Path
import pandas as pd
from varro.disk_to_db.create_db_table import emit_and_apply_dimension
from varro.disk_to_db.process_tables import process_dim_table
from varro.db import engine
from sqlalchemy import inspect

DIMENSIONS_DIR = Path("/mnt/HC_Volume_103849439/statbank_tables")
insp = inspect(engine)

for dir in DIMENSIONS_DIR.iterdir():
    print(dir.stem)
    if insp.has_table(dir.stem, schema="dim"):
        print(f"Table {dir.stem} already exists")
        continue

    df = pd.read_parquet(dir / "table_da.parquet")
    df = process_dim_table(df)

    kode_isna = df["kode"].isna()
    if kode_isna.sum() > 0:
        print(f"Dropping {kode_isna.sum()} rows with missing kode")
        df = df[~kode_isna].copy()

    # TODO: Add dimension links
    emit_and_apply_dimension(df, dir.stem, dimension_links=...)
