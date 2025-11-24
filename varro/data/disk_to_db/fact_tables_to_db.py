from pathlib import Path
from dataclasses import dataclass
import json
import subprocess
from typing import Iterable, Iterator, Tuple

import pandas as pd
from psycopg.errors import ForeignKeyViolation
from sqlalchemy import inspect

from varro.config import DATA_DIR
from varro.data.disk_to_db.create_db_table import emit_and_apply_fact
from varro.data.disk_to_db.process_tables import process_fact_table
from varro.db import crud
from varro.db.db import engine

FACTS_DIR = DATA_DIR / "statbank_tables"
DIM_LINKS_DIR = DATA_DIR / "dimension_links"
DIM_LINKS_TABLE_IDS = set(fp.stem for fp in DIM_LINKS_DIR.glob("*.json"))
FK_FILTER_RULES_PATH = Path(__file__).resolve().parent / "fk_filter_rules.json"
insp = inspect(engine)

MATCH_TYPE_EXACT = "exact"
MATCH_TYPE_APPROX = "approx"
VALID_MATCH_TYPES = {MATCH_TYPE_EXACT, MATCH_TYPE_APPROX}


def normalize_fact_col_name(name: str) -> str:
    return name.lower().replace("å", "a").replace("ø", "o").replace("æ", "ae")


def iter_dimension_links(records: Iterable[dict]) -> Iterator[Tuple[str, str, str]]:
    for entry in records or []:
        if not isinstance(entry, dict):
            raise TypeError("Dimension link entries must be objects")
        fact_col = entry["column"]
        dim_table = entry["dimension"]
        match_type = entry.get("match_type", MATCH_TYPE_EXACT)
        if not isinstance(match_type, str):
            match_type = MATCH_TYPE_EXACT
        match_type = match_type.lower()
        if match_type not in VALID_MATCH_TYPES:
            match_type = MATCH_TYPE_APPROX
        yield fact_col, dim_table, match_type


def load_filter_rules() -> list[dict]:
    if not FK_FILTER_RULES_PATH.exists():
        return []
    return json.loads(FK_FILTER_RULES_PATH.read_text())


def apply_filter_rules(
    df: pd.DataFrame,
    table_id: str,
    dimension_links: dict[str, str] | None,
    rules: list[dict],
) -> pd.DataFrame:
    if not rules or not dimension_links:
        return df
    for rule in rules:
        fact_column = normalize_fact_col_name(rule["fact_column"])
        dimension_table = rule["dimension_table"].strip().lower()
        drop_values = rule.get("drop_values") or []
        if fact_column not in df.columns:
            continue
        if dimension_links.get(fact_column) != dimension_table:
            continue
        if not drop_values:
            continue
        series = df[fact_column]
        mask = series.isin(drop_values)
        str_values = {str(v) for v in drop_values}
        mask = mask | series.astype(str).isin(str_values)
        removed = int(mask.sum())
        if removed:
            df = df.loc[~mask].copy()
            print(
                f"Applied FK filter for {table_id}.{fact_column} "
                f"(dimension {dimension_table}); removed {removed} rows"
            )
    return df


def create_fact_col_to_dim_mapping(threshold: float = 0.80):
    # Load dimension links into df
    df_dims = []
    for fp in DIM_LINKS_DIR.glob("*.json"):
        dim_list = []
        dim_links = json.load(fp.open("r"))

        for fact_col, dim_table, _ in iter_dimension_links(dim_links):
            dim_list.append({"fact_col": fact_col, "dim_table": dim_table})

        if not dim_list:
            continue
        df_dim = pd.DataFrame(dim_list)
        df_dim["fact_table"] = fp.stem
        df_dims.append(df_dim)

    if not df_dims:
        return {}

    df_dims = pd.concat(df_dims, ignore_index=True)

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


def create_fact_table(
    table_id: str, fp: Path, dim_links_dict: dict[str, str], soft_link_cols: set[str]
):
    filter_rules = load_filter_rules()
    df = pd.read_parquet(fp)
    df = process_fact_table(df)
    df = apply_filter_rules(
        df=df,
        table_id=table_id,
        dimension_links=dim_links_dict,
        rules=filter_rules,
    )
    emit_and_apply_fact(
        df,
        table_id.lower(),
        dimension_links=dim_links_dict,
        soft_dimension_columns=soft_link_cols,
    )


fact_col_to_dim_table = create_fact_col_to_dim_mapping()

for fp in FACTS_DIR.iterdir():
    table_id = fp.stem

    if table_id not in DIM_LINKS_TABLE_IDS:
        # print(f"Table {table_id} has no dimension links")
        continue

    if insp.has_table(table_id.lower(), schema="fact"):
        print(f"Table {table_id} already exists")
        continue

    with open(DIM_LINKS_DIR / f"{table_id}.json", "r") as f:
        dim_links = json.load(f)

    dim_entries = list(iter_dimension_links(dim_links))
    if dim_entries:
        dim_links_dict = {}
        soft_link_cols = set()
        for fact_col, dim_table, match_type in dim_entries:
            if fact_col in fact_col_to_dim_table:
                dim_table = fact_col_to_dim_table[fact_col]

            normalized_col = normalize_fact_col_name(fact_col)
            dim_links_dict[normalized_col] = dim_table
            if match_type != MATCH_TYPE_EXACT:
                soft_link_cols.add(normalized_col)
    else:
        dim_links_dict = None
        soft_link_cols = None

    # Try creating the fact table with both exact and approx links
    create_fact_table(table_id, fp, dim_links_dict, soft_link_cols=None)
    print(f"Table {table_id} processed successfully")
