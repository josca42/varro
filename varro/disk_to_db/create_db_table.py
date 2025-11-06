import re
from datetime import date, datetime
import numpy as np
import pandas as pd

# --------- Type inference helpers ---------

_RANGE_RE = re.compile(r"^\s*\[\s*-?\d+\s*,\s*(-?\d+)?\s*\)\s*$")


def choose_int_type(vmin: int, vmax: int) -> str:
    if -32768 <= vmin <= 32767 and -32768 <= vmax <= 32767:
        return "smallint"
    if -2147483648 <= vmin <= 2147483647 and -2147483648 <= vmax <= 2147483647:
        return "integer"
    return "bigint"


def looks_like_range_text(s: str) -> bool:
    return bool(_RANGE_RE.match(s))


def infer_pg_type(colname: str, s: pd.Series) -> str:
    non_null = s.dropna()
    if non_null.empty:
        return "text"

    if pd.api.types.is_bool_dtype(s):
        return "boolean"

    if pd.api.types.is_integer_dtype(s):
        vmin = int(non_null.min())
        vmax = int(non_null.max())
        return choose_int_type(vmin, vmax)

    if pd.api.types.is_float_dtype(s):
        return "double precision"

    if pd.api.types.is_datetime64_any_dtype(s):
        return "timestamp without time zone"

    vals = non_null.values

    # Pure date (not datetime) carried in object dtype
    if all(isinstance(x, date) and not isinstance(x, datetime) for x in vals):
        return "date"

    if any(isinstance(x, datetime) for x in vals):
        return "timestamp without time zone"

    # ALDER as textual int4range, e.g. "[0,5)"
    if colname == "alder" and all(looks_like_range_text(str(x)) for x in vals):
        return "int4range"

    # Objects that are actually ints
    if all(isinstance(x, (np.integer, int)) for x in vals):
        vmin = int(np.min(vals))
        vmax = int(np.max(vals))
        return choose_int_type(vmin, vmax)

    # Default: size by observed max string length
    maxlen = int(max(len(str(x)) for x in vals))
    return f"varchar({maxlen})"


# --------- Name & SQL helpers ---------


def fq_name(schema: str | None, table: str) -> str:
    return (schema + "." if schema else "") + table


def idx_name(schema: str | None, table: str, col: str, prefix: str) -> str:
    base = "_".join([p for p in [prefix, schema, table, col] if p])
    base = re.sub(r"[^a-z0-9_]+", "_", base.lower())
    return base[:63]  # safe for Postgres


def parse_dim_ref(ref: str) -> tuple[str | None, str]:
    if "." in ref:
        sch, tbl = ref.split(".", 1)
        return (sch or None), tbl
    return None, ref


def sql_literal(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


# --------- Core builders ---------


def build_column_types(df: pd.DataFrame) -> dict[str, str]:
    return {col: infer_pg_type(col, df[col]) for col in df.columns}


def create_table_stmt(
    table: str,
    schema: str | None,
    col_types: dict[str, str],
    if_not_exists: bool = True,
    primary_key: str | None = None,
) -> str:
    cols = []
    for c in col_types:
        line = f"{c} {col_types[c]}"
        if primary_key and c == primary_key:
            line += " PRIMARY KEY"
        cols.append(line)
    ine = " IF NOT EXISTS" if if_not_exists else ""
    return (
        f"CREATE TABLE{ine} {fq_name(schema, table)} (\n  "
        + ",\n  ".join(cols)
        + "\n);"
    )


def create_indexes_stmts(
    table: str,
    schema: str | None,
    col_types: dict[str, str],
    exclude: tuple[str, ...] = ("indhold",),
) -> list[str]:
    stmts = []
    exclude_up = {e.lower() for e in exclude}
    for col, pgtype in col_types.items():
        if col.lower() in exclude_up:
            continue
        using = " USING gist" if pgtype == "int4range" else ""
        stmts.append(
            f"CREATE INDEX IF NOT EXISTS {idx_name(schema, table, col, 'idx')} "
            f"ON {fq_name(schema, table)}{using} ({col});"
        )
    return stmts


def create_dimension_links_stmts(
    table: str,
    schema: str | None,
    col_types: dict[str, str],
    dimension_links: dict[str, str] | None,
    add_comments: bool = True,
) -> tuple[list[str], list[str]]:
    if not dimension_links:
        return [], []
    fk_stmts, comment_stmts = [], []
    for col, ref in dimension_links.items():
        dim_schema, dim_table = parse_dim_ref(ref)
        dim_fq = fq_name(dim_schema, dim_table)
        # Skip FK if the source column is a range (cannot reference dim.kode)
        if col_types.get(col, "") == "int4range":
            if add_comments:
                txt = f"Range column; intended to map to {dim_fq} conceptually."
                comment_stmts.append(
                    f"COMMENT ON COLUMN {fq_name(schema, table)}.{col} IS {sql_literal(txt)};"
                )
            continue
        fkname = idx_name(schema, f"{table}_{col}_{dim_table}", "kode", "fk")
        fk_stmts.append(
            f"ALTER TABLE {fq_name(schema, table)} "
            f"ADD CONSTRAINT {fkname} FOREIGN KEY ({col}) "
            f"REFERENCES {dim_fq} (kode) DEFERRABLE INITIALLY DEFERRED NOT VALID;"
        )
        if add_comments:
            txt = f"Links to {dim_fq}(kode). Dimension columns: kode (key), niveau (1=top), titel (label)."
            comment_stmts.append(
                f"COMMENT ON COLUMN {fq_name(schema, table)}.{col} IS {sql_literal(txt)};"
            )
    return fk_stmts, comment_stmts


# --------- Public entry points ---------


def create_fact_table_sql(
    df: pd.DataFrame,
    table_name: str,
    schema: str | None = None,
    if_not_exists: bool = True,
    exclude_index_cols: tuple[str, ...] = ("indhold",),
    dimension_links: dict[str, str] | None = None,
    add_dimension_comments: bool = True,
) -> str:
    """
    Build SQL for a fact table:
      1) CREATE TABLE with inferred types
      2) CREATE INDEX on every column except those in exclude_index_cols
      3) Optional FOREIGN KEYs + COMMENTS for declared dimension links
    """
    col_types = build_column_types(df)
    stmts = [create_table_stmt(table_name, schema, col_types, if_not_exists)]
    stmts += create_indexes_stmts(table_name, schema, col_types, exclude_index_cols)
    fk_stmts, comment_stmts = create_dimension_links_stmts(
        table_name, schema, col_types, dimension_links, add_dimension_comments
    )
    stmts += fk_stmts + comment_stmts
    return "\n".join(stmts)


def create_dimension_table_sql(
    df: pd.DataFrame,
    table_name: str,
    schema: str | None = None,
    if_not_exists: bool = True,
    index_titel: bool = False,
) -> str:
    """
    Build SQL for a dimension table with structure: kode, niveau, titel.
    - Sets PRIMARY KEY (kode)
    - Adds index on niveau (and optional index on titel)
    - Adds helpful table/column comments
    """
    # Expect the three columns to exist; no try/except by design.
    assert {"kode", "niveau", "titel"}.issubset(df.columns)

    # Infer types just for these columns (uses same inference rules)
    kt = infer_pg_type("kode", df["kode"])
    nt = infer_pg_type("niveau", df["niveau"])
    tt = infer_pg_type("titel", df["titel"])

    col_types = {"kode": kt, "niveau": nt, "titel": tt}

    stmts = [
        create_table_stmt(
            table_name, schema, col_types, if_not_exists, primary_key="kode"
        )
    ]

    # indexes
    stmts.append(
        f"CREATE INDEX IF NOT EXISTS {idx_name(schema, table_name, 'niveau', 'idx')} "
        f"ON {fq_name(schema, table_name)} (niveau);"
    )
    if index_titel:
        stmts.append(
            f"CREATE INDEX IF NOT EXISTS {idx_name(schema, table_name, 'titel', 'idx')} "
            f"ON {fq_name(schema, table_name)} (titel);"
        )

    # comments
    stmts.append(
        f"COMMENT ON TABLE {fq_name(schema, table_name)} IS "
        f"{sql_literal('Static dimension: kode (key), niveau (hierarchy level), titel (label).')};"
    )
    stmts.append(
        f"COMMENT ON COLUMN {fq_name(schema, table_name)}.niveau IS "
        f"{sql_literal('1 = broadest level; higher numbers = deeper levels.')};"
    )
    return "\n".join(stmts)
