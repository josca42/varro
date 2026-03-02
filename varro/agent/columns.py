from __future__ import annotations

import json
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd
from pydantic_ai import ModelRetry

from varro.config import COLUMN_VALUES_DIR, DST_DIMENSION_LINKS_DIR
from varro.data.utils import normalize_column_name

DIMENSION_LINKS_DIR = DST_DIMENSION_LINKS_DIR


def normalize_table_name(table: str) -> str:
    return table.strip().lower().replace("fact.", "").replace("dim.", "")


def load_dimension_links(table: str) -> dict[str, str]:
    path = DIMENSION_LINKS_DIR / f"{table.upper()}.json"
    if not path.exists():
        return {}
    entries = json.loads(path.read_text())
    links = {}
    for entry in entries:
        links[normalize_column_name(entry["column"])] = entry["dimension"].strip().lower()
    return links


def get_fact_value_files(table: str) -> list[Path]:
    table_dir = COLUMN_VALUES_DIR / table
    if not table_dir.exists():
        raise ModelRetry(f"No column values directory found for fact table '{table}'.")
    files = sorted(table_dir.glob("*.parquet"))
    if not files:
        raise ModelRetry(f"No fact column values found for table '{table}'.")
    return files


# TODO: If no overlap then create an appropriate string representation with the report generated
# and then let the Agent decide the best action going forward.
def infer_fact_column_for_dim(df: pd.DataFrame, dim_table: str, for_table: str) -> str:
    value_files = get_fact_value_files(for_table)
    columns = [file.stem for file in value_files]

    prefix_matches = sorted(col for col in columns if dim_table.startswith(col))
    if len(prefix_matches) == 1:
        return prefix_matches[0]

    ranked_names = sorted(
        ((col, SequenceMatcher(None, col, dim_table).ratio()) for col in columns),
        key=lambda item: item[1],
        reverse=True,
    )
    if ranked_names and ranked_names[0][1] >= 0.7:
        return ranked_names[0][0]

    codes = {str(code) for code in df["kode"].dropna()}
    ranked_overlaps = []
    for file in value_files:
        values = pd.read_parquet(file)
        if "id" not in values:
            continue
        value_ids = {str(value) for value in values["id"].dropna()}
        overlap = len(value_ids & codes)
        overlap_ratio = overlap / len(value_ids) if value_ids else 0.0
        ranked_overlaps.append((file.stem, overlap, overlap_ratio))

    ranked_overlaps.sort(key=lambda item: (item[1], item[2]), reverse=True)
    if ranked_overlaps and ranked_overlaps[0][1] > 0:
        return ranked_overlaps[0][0]

    raise ModelRetry(
        f"Could not infer a fact column in '{for_table}' for dim table '{dim_table}'."
    )


# TODO: Again implement good messages to the agent here about, what is happening. It is important that the knows a filter has been applied and what the filter is. Primarily, due to error cases where case mismatch like "001" vs "1" etc.. And hence filter should not be applied blindly.
def filter_dimension_values_for_table(
    df: pd.DataFrame, dim_table: str, for_table: str
) -> pd.DataFrame:
    links = load_dimension_links(for_table)
    fact_columns = sorted(col for col, dim in links.items() if dim == dim_table)
    fact_column = (
        fact_columns[0]
        if fact_columns
        else infer_fact_column_for_dim(df, dim_table, for_table)
    )
    fact_values_path = COLUMN_VALUES_DIR / for_table / f"{fact_column}.parquet"
    if not fact_values_path.exists():
        raise ModelRetry(
            f"Missing column values for '{for_table}.{fact_column}' at '{fact_values_path}'."
        )

    fact_values = pd.read_parquet(fact_values_path)
    if "id" not in fact_values:
        raise ModelRetry(
            f"Column values file for '{for_table}.{fact_column}' must include an 'id' column."
        )
    codes = {str(code) for code in fact_values["id"].dropna()}
    return df[df["kode"].astype(str).isin(codes)]
