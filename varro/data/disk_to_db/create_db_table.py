from __future__ import annotations
import io
import re
from datetime import date, datetime
from typing import NamedTuple
import numpy as np
import pandas as pd
import psycopg
from varro.db.db import POSTGRES_DST

# -------------------------- inference helpers --------------------------

_RANGE_RE = re.compile(r"^\s*\[\s*-?\d+\s*,\s*(-?\d+)?\s*\)\s*$")


def looks_like_range_text(s: str) -> bool:
    return bool(_RANGE_RE.match(s))


def choose_int_type(vmin: int, vmax: int) -> str:
    if -32768 <= vmin <= 32767 and -32768 <= vmax <= 32767:
        return "smallint"
    if -2147483648 <= vmin <= 2147483647 and -2147483648 <= vmax <= 2147483647:
        return "integer"
    return "bigint"


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

    if len(non_null) > 1000:
        vals_sample = non_null.sample(1000)
    else:
        vals_sample = non_null.values

    # object column containing dates?
    if all(isinstance(x, date) and not isinstance(x, datetime) for x in vals_sample):
        return "date"

    if any(isinstance(x, datetime) for x in vals_sample):
        return "timestamp without time zone"

    # ALDER as textual range -> int4range
    if colname in ["alder", "tid"] and all(
        looks_like_range_text(str(x)) for x in vals_sample
    ):
        return "int4range"

    # object that is all ints
    if all(isinstance(x, (np.integer, int)) for x in vals_sample):
        vmin = int(non_null.min())
        vmax = int(non_null.max())
        return choose_int_type(vmin, vmax)

    maxlen = int(non_null.str.len().max())
    return f"varchar({maxlen})"


# -------------------------- naming & sql helpers --------------------------


def quote_ident(ident: str) -> str:
    return '"' + ident.replace('"', '""') + '"'


def fq_name(schema: str | None, table: str) -> str:
    if schema:
        return f"{quote_ident(schema)}.{quote_ident(table)}"
    return quote_ident(table)


def idx_name(schema: str | None, table: str, col: str, prefix: str) -> str:
    base = "_".join([p for p in [prefix, schema, table, col] if p])
    base = re.sub(r"[^a-z0-9_]+", "_", base.lower())
    return base[:63]


def sql_literal(s: str) -> str:
    return "'" + s.replace("'", "''") + "'"


# -------------------------- core builders --------------------------


def build_column_types(df: pd.DataFrame) -> dict[str, str]:
    return {col: infer_pg_type(col, df[col]) for col in df.columns}


def create_table_stmt(
    table: str,
    schema: str | None,
    col_types: dict[str, str],
    if_not_exists: bool = True,
    primary_key: str | list[str] | None = None,
) -> str:
    cols = []
    for c in col_types:
        line = f"{quote_ident(c)} {col_types[c]}"
        if isinstance(primary_key, str) and c == primary_key:
            line += " PRIMARY KEY"
        cols.append(line)
    ine = " IF NOT EXISTS" if if_not_exists else ""
    create_table_stmt = (
        f"CREATE TABLE{ine} {fq_name(schema, table)} (\n  " + ",\n  ".join(cols)
    )
    if isinstance(primary_key, list):
        pk_cols = ", ".join(quote_ident(c) for c in primary_key)
        create_table_stmt += f",\n  PRIMARY KEY ({pk_cols})"

    return create_table_stmt + "\n);"


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
            f"ON {fq_name(schema, table)}{using} ({quote_ident(col)});"
        )
    return stmts


# -------------------------- public API: plans + runners --------------------------


class DDLPlan(NamedTuple):
    create_sql: str  # CREATE TABLE ...
    post_sql: str  # indexes + comments (joined)
    post_statements: list[str]


def make_fact_plan(
    df: pd.DataFrame,
    table_name: str,
) -> DDLPlan:
    schema, exclude_index_cols = "fact", ("indhold",)
    col_types = build_column_types(df)
    create_sql = create_table_stmt(table_name, schema, col_types, True)
    idxs = create_indexes_stmts(table_name, schema, col_types, exclude_index_cols)
    post_sql = "\n".join(idxs)
    return DDLPlan(create_sql, post_sql, idxs)


def make_dimension_plan(df: pd.DataFrame, table_name: str) -> DDLPlan:
    assert {"kode", "niveau", "titel"}.issubset(df.columns)
    kt = infer_pg_type("kode", df["kode"])
    nt = infer_pg_type("niveau", df["niveau"])
    tt = infer_pg_type("titel", df["titel"])
    col_types = {"kode": kt, "niveau": nt, "titel": tt}
    schema, if_not_exists = "dim", True

    is_kode_unique = df["kode"].value_counts().max() == 1
    primary_key = "kode" if is_kode_unique else ["kode", "niveau"]

    create_sql = create_table_stmt(
        table_name, schema, col_types, if_not_exists, primary_key=primary_key
    )
    idxs = [
        f"CREATE INDEX IF NOT EXISTS {idx_name(schema, table_name, 'niveau', 'idx')} "
        f"ON {fq_name(schema, table_name)} ({quote_ident('niveau')});"
    ]
    comments = [
        f"COMMENT ON TABLE {fq_name(schema, table_name)} IS "
        f"{sql_literal('Static dimension: kode (key), niveau (hierarchy level), titel (label).')};",
        f"COMMENT ON COLUMN {fq_name(schema, table_name)}.{quote_ident('niveau')} IS "
        f"{sql_literal('1 = broadest; higher numbers = deeper levels.')};",
    ]
    post_statements = idxs + comments
    post_sql = "\n".join(post_statements)
    return DDLPlan(create_sql, post_sql, post_statements)


# -------------------------- COPY loader + executor --------------------------


def copy_df_via_copy(
    conn: psycopg.Connection, df: pd.DataFrame, table: str, schema: str | None = None
) -> None:
    cols = [quote_ident(c) for c in df.columns]
    buf = io.StringIO()
    df.to_csv(buf, index=False, header=False, na_rep="\\N")
    buf.seek(0)
    copy_sql = f"COPY {fq_name(schema, table)} ({', '.join(cols)}) FROM STDIN WITH (FORMAT CSV, NULL '\\N');"
    with conn.cursor() as cur:
        with cur.copy(copy_sql) as cp:
            cp.write(buf.getvalue())


def execute_statements(conn: psycopg.Connection, statements: list[str]) -> None:
    if not statements:
        return
    with conn.cursor() as cur:
        for s in statements:
            cur.execute(s)


def create_insert_then_post(
    df: pd.DataFrame,
    plan: DDLPlan,
    table_name: str,
    schema: str | None,
) -> None:
    """
    1) CREATE TABLE
    2) COPY df
    3) run post statements (indexes, comments)
    """
    with psycopg.connect(POSTGRES_DST) as conn:
        with conn.cursor() as cur:
            cur.execute(plan.create_sql)
        copy_df_via_copy(conn, df, table_name, schema)
        execute_statements(conn, plan.post_statements)
        # connection context manager commits on success


# -------------------------- convenience wrapper --------------------------


def emit_and_apply_fact(
    df: pd.DataFrame,
    table_name: str,
) -> DDLPlan:
    plan = make_fact_plan(
        df=df,
        table_name=table_name,
    )
    create_insert_then_post(
        df=df,
        plan=plan,
        table_name=table_name,
        schema="fact",
    )
    return plan


def emit_and_apply_dimension(df: pd.DataFrame, table_name: str) -> DDLPlan:
    plan = make_dimension_plan(df, table_name)
    create_insert_then_post(
        df=df,
        plan=plan,
        table_name=table_name,
        schema="dim",
    )
    return plan
