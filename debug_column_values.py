"""Debug script for ColumnValues flow with and without filtered DataFrames."""

import pandas as pd
from varro.config import COLUMN_VALUES_DIR, DST_DIMENSION_LINKS_DIR
from varro.context.utils import fuzzy_match
from varro.data.utils import df_preview, normalize_column_name
from varro.agent.assistant import filter_dimension_values_for_table

DIM_TABLES = ("overtraedtype",)
DIMENSION_LINKS_DIR = DST_DIMENSION_LINKS_DIR


def column_values(table, column, fuzzy_match_str=None, n=5, for_table=None):
    """Standalone replica of the ColumnValues tool for debugging."""
    table = table.strip().lower().replace("fact.", "").replace("dim.", "")
    for_table = for_table.strip().lower().replace("fact.", "").replace("dim.", "") if for_table else None

    if table in DIM_TABLES:
        df = pd.read_parquet(COLUMN_VALUES_DIR / f"{table}.parquet")
        print(f"  Loaded dim table '{table}': {len(df)} rows, index contiguous: {df.index.is_monotonic_increasing and df.index[0] == 0}")
        if for_table:
            df = filter_dimension_values_for_table(df, table, for_table)
            print(f"  After filter for '{for_table}': {len(df)} rows, index contiguous: {list(range(len(df))) == df.index.tolist()}")
        name = f"df_{table}_titel"
        schema = "dim"
    else:
        df = pd.read_parquet(COLUMN_VALUES_DIR / f"{table}/{column}.parquet")
        print(f"  Loaded fact column '{table}.{column}': {len(df)} rows")
        name = f"df_{table}_{column}"
        schema = "fact"

    if fuzzy_match_str:
        return fuzzy_match(fuzzy_match_str, df=df, limit=n, schema=schema, name=name)
    else:
        return df_preview(df, max_rows=n, name=name)


# --- Case 1: Dim table, no filter, no fuzzy ---
print("=" * 60)
print("CASE 1: ColumnValues(overtraedtype, titel)")
print("  No for_table, no fuzzy — plain preview of full dim table")
print("=" * 60)
print(column_values("overtraedtype", "titel", n=10))
print()

# --- Case 2: Dim table, filtered by for_table, no fuzzy ---
print("=" * 60)
print("CASE 2: ColumnValues(overtraedtype, titel, for_table=straf10)")
print("  Filtered to codes present in straf10, no fuzzy")
print("=" * 60)
print(column_values("overtraedtype", "titel", for_table="straf10", n=10))
print()

# --- Case 3: Dim table, filtered by for_table, WITH fuzzy (the crash case) ---
print("=" * 60)
print("CASE 3: ColumnValues(overtraedtype, titel, fuzzy='seksual', for_table=straf10)")
print("  Filtered + fuzzy — this was the crash before the .iloc→.loc fix")
print("=" * 60)
print(column_values("overtraedtype", "titel", fuzzy_match_str="seksual", for_table="straf10", n=5))
print()

# --- Case 4: Dim table, no filter, WITH fuzzy ---
print("=" * 60)
print("CASE 4: ColumnValues(overtraedtype, titel, fuzzy='seksual')")
print("  Unfiltered + fuzzy — always worked (contiguous index)")
print("=" * 60)
print(column_values("overtraedtype", "titel", fuzzy_match_str="seksual", n=5))
print()

# --- Case 5: Fact table column values (no dim filtering path) ---
print("=" * 60)
print("CASE 5: ColumnValues(straf10, overtraed)")
print("  Fact table path — reads per-column parquet, no dim filtering")
print("=" * 60)
print(column_values("straf10", "overtraed", n=10))
print()

# --- Case 6: Fact table column values WITH fuzzy ---
print("=" * 60)
print("CASE 6: ColumnValues(straf10, overtraed, fuzzy='vold')")
print("  Fact table + fuzzy")
print("=" * 60)
print(column_values("straf10", "overtraed", fuzzy_match_str="vold", n=5))
