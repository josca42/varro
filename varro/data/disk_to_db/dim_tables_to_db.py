from pathlib import Path
import pandas as pd
from varro.data.disk_to_db.create_db_table import emit_and_apply_dimension
from varro.data.disk_to_db.process_tables import process_dim_table
from varro.db.db import dst_owner_engine
from sqlalchemy import inspect
from varro.config import DATA_DIR

DIMENSIONS_DIR = DATA_DIR / "mapping_tables"
insp = inspect(dst_owner_engine)

for folder in DIMENSIONS_DIR.iterdir():
    print(folder.stem)
    if insp.has_table(folder.stem, schema="dim"):
        print(f"Table {folder.stem} already exists")
        continue

    df = pd.read_parquet(folder / "table_da.parquet")

    if folder.stem == "db":
        df = df[df["NIVEAU"] != 1].copy()  # Drop basic string level

    df = process_dim_table(df)

    kode_isna = df["kode"].isna()
    if kode_isna.sum() > 0:
        print(f"Dropping {kode_isna.sum()} rows with missing kode")
        df = df[~kode_isna].copy()

    # TODO: Add dimension links
    emit_and_apply_dimension(df, folder.stem)
