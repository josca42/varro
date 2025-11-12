from pathlib import Path
import pandas as pd
from varro.disk_to_db.create_db_table import emit_and_apply_dimension
from varro.disk_to_db.process_tables import process_dim_table
from varro.db import engine
from sqlalchemy import inspect
from varro.config import DATA_DIR

DIMENSIONS_DIR = DATA_DIR / "mapping_tables"
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
    emit_and_apply_dimension(df, dir.stem)


def db_codes_preprocessing(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["niveau"] != 1].copy()
    return df
