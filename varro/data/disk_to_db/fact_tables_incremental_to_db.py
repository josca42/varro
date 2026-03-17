from urllib.parse import quote

import pandas as pd
import psycopg
from sqlalchemy import inspect

from varro.config import DST_STATBANK_TABLES_DIR
from varro.data.disk_to_db.create_db_table import copy_df_via_copy, fq_name, quote_ident
from varro.data.disk_to_db.process_tables import process_fact_table
from varro.db.db import POSTGRES_DST, dst_owner_engine

from uuid import uuid4


def partition_fp(table_id: str, tid: str):
    encoded = quote(tid, safe="")
    return DST_STATBANK_TABLES_DIR / table_id / f"{encoded}.parquet"


def load_partitions(table_id: str, tids: list[str]) -> tuple[pd.DataFrame, list[str]]:
    missing = []
    dfs = []
    for tid in tids:
        fp = partition_fp(table_id, tid)
        if not fp.exists():
            missing.append(tid)
            continue
        dfs.append(pd.read_parquet(fp))

    if not dfs:
        return pd.DataFrame(), missing
    return pd.concat(dfs, ignore_index=True), missing


def normalize_changed_tids(changed_tids: list[str]) -> list[str]:
    if not changed_tids:
        return []
    normalized = process_fact_table(
        pd.DataFrame({"Tid": changed_tids, "INDHOLD": [0] * len(changed_tids)})
    )["tid"].astype(str)
    return list(dict.fromkeys(normalized.tolist()))


def table_exists_in_db(table_id: str) -> bool:
    inspector = inspect(dst_owner_engine)
    return inspector.has_table(table_id.lower(), schema="fact")


def apply_table_delta(table_id: str, changed_tids: list[str]) -> dict:
    table = table_id.lower()
    df, missing_tids = load_partitions(table_id, changed_tids)

    if df.empty and len(df.columns) == 0:
        return {
            "table": table_id,
            "status": "skipped",
            "reason": "no_partition_data",
            "missing_tids": missing_tids,
        }

    temp_table = f"_tmp_sync_{table}_{uuid4().hex[:8]}"
    processed = process_fact_table(df)
    delete_tids = normalize_changed_tids(changed_tids)

    with psycopg.connect(POSTGRES_DST) as conn:
        with conn.cursor() as cur:
            cur.execute(
                f"CREATE TEMP TABLE {quote_ident(temp_table)} AS TABLE {fq_name('fact', table)} WITH NO DATA;"
            )

        if not processed.empty:
            copy_df_via_copy(conn, processed, temp_table, schema=None)

        with conn.cursor() as cur:
            cur.execute(
                f"DELETE FROM {fq_name('fact', table)} AS tgt USING (SELECT UNNEST(%s::text[]) AS tid) AS src WHERE tgt.tid::text = src.tid;",
                (delete_tids,),
            )
            deleted_rows = cur.rowcount
            inserted_rows = 0
            if not processed.empty:
                cur.execute(
                    f"INSERT INTO {fq_name('fact', table)} SELECT * FROM {quote_ident(temp_table)};"
                )
                inserted_rows = cur.rowcount

    result = {
        "table": table_id,
        "status": "applied",
        "changed_tids": changed_tids,
        "deleted_rows": deleted_rows,
        "inserted_rows": inserted_rows,
    }
    if missing_tids:
        result["missing_tids"] = missing_tids
    return result
