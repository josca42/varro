"""Backfill partitions that exist on disk but are missing from the database."""

import argparse
import sys

import pandas as pd
import psycopg

from varro.config import DST_STATBANK_TABLES_DIR
from varro.data.disk_to_db.create_db_table import emit_and_apply_fact, fq_name
from varro.data.disk_to_db.fact_tables_incremental_to_db import (
    apply_table_delta,
    load_partitions,
    normalize_changed_tids,
    table_exists_in_db,
)
from varro.data.disk_to_db.process_tables import process_fact_table
from varro.data.statbank_to_disk.copy_tables_statbank import list_local_tids
from varro.db.db import POSTGRES_DST


def get_db_tids(table_id: str) -> set[str]:
    table = table_id.lower()
    with psycopg.connect(POSTGRES_DST) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT DISTINCT tid::text FROM {fq_name('fact', table)}")
            return {row[0] for row in cur.fetchall()}


def find_missing_tids(table_id: str) -> list[str]:
    disk_tids = list_local_tids(table_id)
    if not disk_tids:
        return []
    db_tids = get_db_tids(table_id)
    normalized_to_raw = dict(zip(normalize_changed_tids(disk_tids), disk_tids))
    return [raw for norm, raw in normalized_to_raw.items() if norm not in db_tids]


def create_table_from_disk(table_id: str):
    disk_tids = list_local_tids(table_id)
    df, _ = load_partitions(table_id, disk_tids)
    if df.empty:
        print(f"  no data on disk, skipping")
        return
    processed = process_fact_table(df)
    emit_and_apply_fact(processed, table_id.lower())
    print(f"  created fact.{table_id.lower()} with {len(processed)} rows")


def backfill_table(table_id: str, missing_tids: list[str]):
    result = apply_table_delta(table_id, missing_tids)
    print(f"  loaded {len(missing_tids)} tids: +{result.get('inserted_rows', 0)} rows")


SKIP_DIRS = {"_sync", "initial_copy"}


def list_table_dirs() -> list[str]:
    return sorted(
        d.name
        for d in DST_STATBANK_TABLES_DIR.iterdir()
        if d.is_dir() and d.name not in SKIP_DIRS
    )


def run(table_id: str | None = None, dry_run: bool = False):
    table_ids = [table_id] if table_id else list_table_dirs()
    total = len(table_ids)

    failed = []
    for idx, tid in enumerate(table_ids, 1):
        try:
            exists = table_exists_in_db(tid)

            if not exists:
                disk_tids = list_local_tids(tid)
                if not disk_tids:
                    continue
                print(f"[{idx}/{total}] {tid}: NEW table ({len(disk_tids)} tids on disk)")
                if not dry_run:
                    create_table_from_disk(tid)
            else:
                missing = find_missing_tids(tid)
                if not missing:
                    continue
                print(f"[{idx}/{total}] {tid}: {len(missing)} missing tids")
                if not dry_run:
                    backfill_table(tid, missing)
        except Exception as e:
            print(f"  ERROR: {e}")
            failed.append(tid)

    if failed:
        print(f"\nFailed tables ({len(failed)}): {', '.join(failed)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backfill missing partitions from disk to DB")
    parser.add_argument("--table", help="Process single table instead of all")
    parser.add_argument("--dry-run", action="store_true", help="Just print what would be loaded")
    args = parser.parse_args()
    run(table_id=args.table, dry_run=args.dry_run)
