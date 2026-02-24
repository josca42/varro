import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4
from urllib.parse import quote

import pandas as pd
import psycopg
from sqlalchemy import inspect

from varro.config import DST_STATBANK_TABLES_DIR
from varro.data.disk_to_db.create_db_table import copy_df_via_copy, fq_name, quote_ident
from varro.data.disk_to_db.process_tables import process_fact_table
from varro.db.db import POSTGRES_DST, dst_owner_engine

SYNC_DIR = DST_STATBANK_TABLES_DIR / "_sync"
RUNS_DIR = SYNC_DIR / "runs"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_utc(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def run_manifest_path(run_id: str) -> Path:
    return RUNS_DIR / f"{run_id}.json"


def latest_run_manifest_path() -> Path:
    runs = sorted(RUNS_DIR.glob("*.json"))
    if not runs:
        raise FileNotFoundError("No run manifests found")
    return runs[-1]


def write_json_atomic(fp: Path, data: dict) -> None:
    fp.parent.mkdir(parents=True, exist_ok=True)
    tmp = fp.parent / f"{fp.name}.{uuid4().hex}.tmp"
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    tmp.replace(fp)


def partition_fp(table_id: str, tid: str) -> Path:
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


def apply_table_delta(table_id: str, changed_tids: list[str], df: pd.DataFrame) -> dict:
    table = table_id.lower()
    temp_table = f"_tmp_sync_{table}_{uuid4().hex[:8]}"
    processed = process_fact_table(df)

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
                (changed_tids,),
            )
            deleted_rows = cur.rowcount
            inserted_rows = 0
            if not processed.empty:
                cur.execute(
                    f"INSERT INTO {fq_name('fact', table)} SELECT * FROM {quote_ident(temp_table)};"
                )
                inserted_rows = cur.rowcount

    return {
        "table": table_id,
        "status": "applied",
        "changed_tids": changed_tids,
        "deleted_rows": deleted_rows,
        "inserted_rows": inserted_rows,
    }


def apply_incremental_run(run_id: str) -> dict:
    manifest_fp = run_manifest_path(run_id)
    if not manifest_fp.exists():
        raise FileNotFoundError(f"Run manifest not found: {manifest_fp}")

    manifest = json.loads(manifest_fp.read_text())
    run_id = manifest["run_id"]
    inspector = inspect(dst_owner_engine)
    db_apply = {
        "run_id": run_id,
        "started_at": iso_utc(now_utc()),
        "finished_at": None,
        "status": "running",
        "tables": {},
        "summary": {},
    }

    changed_tables = {
        table_id: table_result.get("changed_tids", [])
        for table_id, table_result in manifest.get("tables", {}).items()
        if table_result.get("changed_tids")
    }

    for table_id, changed_tids in changed_tables.items():
        table = table_id.lower()
        if not inspector.has_table(table, schema="fact"):
            db_apply["tables"][table_id] = {
                "table": table_id,
                "status": "skipped",
                "reason": "missing_fact_table",
                "changed_tids": changed_tids,
            }
            continue

        try:
            df, missing_tids = load_partitions(table_id, changed_tids)
            if df.empty and len(df.columns) == 0:
                db_apply["tables"][table_id] = {
                    "table": table_id,
                    "status": "failed",
                    "reason": "missing_partition_files",
                    "missing_tids": missing_tids,
                    "changed_tids": changed_tids,
                }
                continue

            result = apply_table_delta(table_id, changed_tids, df)
            if missing_tids:
                result["missing_tids"] = missing_tids
            db_apply["tables"][table_id] = result
        except Exception as exc:
            db_apply["tables"][table_id] = {
                "table": table_id,
                "status": "failed",
                "changed_tids": changed_tids,
                "error": str(exc),
            }

    results = list(db_apply["tables"].values())
    applied = sum(1 for result in results if result["status"] == "applied")
    skipped = sum(1 for result in results if result["status"] == "skipped")
    failed = sum(1 for result in results if result["status"] == "failed")
    db_apply["summary"] = {
        "tables_total": len(results),
        "tables_applied": applied,
        "tables_skipped": skipped,
        "tables_failed": failed,
    }
    db_apply["status"] = "partial_failure" if failed else "success"
    db_apply["finished_at"] = iso_utc(now_utc())

    manifest["db_apply"] = db_apply
    write_json_atomic(manifest_fp, manifest)
    return db_apply


if __name__ == "__main__":
    latest_manifest = json.loads(latest_run_manifest_path().read_text())
    apply_incremental_run(latest_manifest["run_id"])
