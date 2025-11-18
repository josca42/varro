from pathlib import Path
import pandas as pd
from varro.data.disk_to_db.create_db_table import emit_and_apply_fact
from varro.data.disk_to_db.process_tables import (
    process_fact_table,
    normalize_column_names,
)
from varro.db import engine
from sqlalchemy import inspect
from varro.config import DATA_DIR
import json

FACTS_DIR = DATA_DIR / "statbank_tables"
DIM_LINKS_DIR = DATA_DIR / "dimension_links"
DIM_LINKS_TABLE_IDS = set(fp.stem for fp in DIM_LINKS_DIR.glob("*.json"))
insp = inspect(engine)


def create_fact_col_to_dim_mapping(threshold: float = 0.80):
    # Load dimension links into df
    df_dims = []
    for fp in DIM_LINKS_DIR.glob("*.json"):
        dim_list = []
        dim_links = json.load(fp.open("r"))

        for link in dim_links:
            for k, v in link.items():
                dim_list.append({"fact_col": k, "dim_table": v})

        df_dim = pd.DataFrame(dim_list)
        df_dim["fact_table"] = fp.stem
        df_dims.append(df_dim)

    df_dims = pd.concat(df_dims)

    # Check for likely mis-mappings and remap
    top = df_dims.groupby("fact_col")["dim_table"].transform(
        lambda s: s.value_counts().idxmax()
    )
    share = df_dims.groupby("fact_col")["dim_table"].transform(
        lambda s: s.value_counts(normalize=True).max()
    )

    df_dims.loc[share >= threshold, "dim_table"] = top[share >= threshold]

    # Create mapping table
    fact_cols_with_single_dim = (
        df_dims.groupby("fact_col")["dim_table"]
        .nunique()
        .pipe(lambda s: s[s == 1])
        .index
    )
    df_dims = df_dims[df_dims["fact_col"].isin(fact_cols_with_single_dim)]
    db_10_bool = (df_dims["dim_table"] == "db") & df_dims["fact_col"].str.endswith("10")
    df_dims.loc[db_10_bool, "dim_table"] = "db_10"
    fact_col_to_dim_table = {
        row["fact_col"]: row["dim_table"] for _, row in df_dims.iterrows()
    }
    return fact_col_to_dim_table


fact_col_to_dim_table = create_fact_col_to_dim_mapping()

for fp in FACTS_DIR.iterdir():
    # if fp.stem != "HISB7":
    #     continue

    table_id = fp.stem
    # table_id = "ISBU02"
    if table_id not in DIM_LINKS_TABLE_IDS:
        print(f"Table {table_id} has no dimension links")
        continue

    if insp.has_table(table_id.lower(), schema="fact"):
        print(f"Table {table_id} already exists")
        continue

    with open(DIM_LINKS_DIR / f"{table_id}.json", "r") as f:
        dim_links = json.load(f)

    if dim_links:
        dim_links_dict = {}
        for dim_link in dim_links:
            for fact_col, dim_table in dim_link.items():
                if fact_col in fact_col_to_dim_table:
                    dim_table = fact_col_to_dim_table[fact_col]

                fact_col = (
                    fact_col.lower()
                    .replace("å", "a")
                    .replace("ø", "o")
                    .replace("æ", "ae")
                )
                dim_links_dict[fact_col] = dim_table
    else:
        dim_links_dict = None

    try:
        df = pd.read_parquet(fp)
        df = process_fact_table(df)
        emit_and_apply_fact(df, table_id.lower(), dim_links_dict)

        print(f"Table {table_id} processed successfully")
    except Exception as e:
        print(f"Error processing table {table_id}: {e}")
        continue
