from pathlib import Path
import pandas as pd
from typing import Literal


FACTS_DIR = Path("/mnt/HC_Volume_103849439/statbank_tables")
DIMENSIONS_DIR = Path("/mnt/HC_Volume_103849439/mapping_tables")


def look_at_table(
    table_id: str,
    table_type: Literal["fact", "dimension"],
    lang: Literal["da", "en"] = "da",
) -> str:
    if table_type == "fact":
        df = pd.read_parquet(FACTS_DIR / f"{table_id}.parquet")
    elif table_type == "dimension":
        df = pd.read_parquet(DIMENSIONS_DIR / table_id / f"table_{lang}.parquet")
    else:
        raise ValueError(f"Invalid table type: {table_type}")
    return df_preview(df, name=table_id)


def read_dimension_description(table_id: str) -> pd.DataFrame:
    with open(DIMENSIONS_DIR / table_id / "table_info_da.md", "r") as f:
        return f.read()


def df_preview(df: pd.DataFrame, max_rows: int = 10, name: str = "df") -> str:
    """Generate DataFrame preview."""
    if df.index.name:
        df = df.reset_index()
    n_rows = min(max_rows, len(df))
    csv_string = df.head(n_rows).to_csv(
        sep="|",
        index=False,
        float_format="%.3f",
        na_rep="N/A",
    )
    if n_rows == len(df):
        return csv_string
    else:
        return f"{name}.head({n_rows})\n" + csv_string
