import argparse
import json
import shutil
from pathlib import Path
from urllib.parse import unquote

import pandas as pd

from varro.data.statbank_to_disk import copy_tables_statbank as sync

INITIAL_COPY_DIR = "initial_copy"


def parse_args():
    parser = argparse.ArgumentParser(
        description="One-time migration from legacy StatBank parquet layout to per-Tid partitions and state bootstrap."
    )
    parser.add_argument(
        "--table",
        action="append",
        default=None,
        help="Only process specific table id(s). Can be repeated.",
    )
    parser.add_argument(
        "--archive-legacy",
        action="store_true",
        help="Move migrated legacy files to statbank_tables/initial_copy/.",
    )
    parser.add_argument(
        "--overwrite-canonical",
        action="store_true",
        help="Overwrite existing canonical Tid parquet files.",
    )
    parser.add_argument(
        "--no-catalog",
        action="store_true",
        help="Skip catalog fetch and bootstrap state without catalog updated timestamps.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan only. Do not write partitions, manifests, or state.",
    )
    return parser.parse_args()


def should_include_table(table_id, only_tables):
    if not only_tables:
        return True
    return table_id.upper() in only_tables


def iter_legacy_sources(base_dir, only_tables):
    for fp in sorted(base_dir.glob("*.parquet")):
        table_id = fp.stem.upper()
        if should_include_table(table_id, only_tables):
            yield table_id, fp

    for table_dir in sorted(base_dir.iterdir()):
        if not table_dir.is_dir():
            continue
        if table_dir.name in {"_sync", INITIAL_COPY_DIR}:
            continue
        table_id = table_dir.name.upper()
        if not should_include_table(table_id, only_tables):
            continue
        for fp in sorted(table_dir.glob("partition_*.parquet")):
            yield table_id, fp


def find_tid_column(df):
    for col in df.columns:
        if str(col).lower() == "tid":
            return str(col)
    raise RuntimeError("Missing Tid column")


def canonical_tids_for_table(table_id):
    table_folder = sync.table_dir(table_id)
    if not table_folder.exists():
        return []
    tids = []
    for fp in table_folder.glob("*.parquet"):
        if fp.name.startswith("partition_"):
            continue
        tids.append(unquote(fp.stem))
    return sorted(set(tids))


def migrate_source_file(table_id, source_fp, overwrite_canonical, dry_run):
    df = pd.read_parquet(source_fp)
    tid_col = find_tid_column(df)
    rows_total = len(df)
    written = 0
    skipped = 0
    tids_seen = []
    for tid, group in df.groupby(tid_col, sort=False):
        tid_str = str(tid)
        tids_seen.append(tid_str)
        target_fp = sync.tid_to_partition_fp(table_id, tid_str)
        if target_fp.exists() and not overwrite_canonical:
            skipped += 1
            continue
        if not dry_run:
            sync.write_parquet_atomic(group, target_fp)
        written += 1

    return {
        "source": str(source_fp),
        "rows_total": rows_total,
        "tids_total": len(set(tids_seen)),
        "tids": sorted(set(tids_seen)),
        "files_written": written,
        "files_skipped_existing": skipped,
    }


def archive_source_file(base_dir, source_fp, dry_run):
    rel = source_fp.relative_to(base_dir)
    dst = base_dir / INITIAL_COPY_DIR / rel
    if dry_run:
        return str(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(source_fp), str(dst))
    return str(dst)


def build_bootstrap_state(state, run_id, catalog_by_table, planned_tids_by_table=None):
    now = sync.now_utc()
    overrides = sync.load_frequency_overrides()
    table_reports = {}
    table_ids = set()
    for table_dir in sorted(sync.FACT_TABLES_DIR.iterdir()):
        if table_dir.is_dir() and table_dir.name not in {"_sync", INITIAL_COPY_DIR}:
            table_ids.add(table_dir.name.upper())
    if planned_tids_by_table:
        table_ids.update(planned_tids_by_table)

    for table_id in sorted(table_ids):
        tids = canonical_tids_for_table(table_id)
        if planned_tids_by_table and table_id in planned_tids_by_table:
            tids = sorted(set(tids) | set(planned_tids_by_table[table_id]))
        if not tids:
            continue

        previous = state["tables"].get(table_id, {})
        frequency = sync.resolve_frequency(table_id, tids, overrides)
        catalog_updated = catalog_by_table.get(table_id)
        if catalog_updated is None:
            catalog_updated = previous.get("last_seen_updated")
        next_state = sync.build_table_state(
            previous,
            catalog_updated=catalog_updated,
            frequency=frequency,
            run_id=run_id,
            now=now,
            status="bootstrapped",
            error=None,
        )
        state["tables"][table_id] = next_state
        table_reports[table_id] = {
            "status": "bootstrapped",
            "frequency": frequency,
            "canonical_tid_count": len(tids),
            "catalog_updated": catalog_updated,
            "changed_tids": [],
        }

    state["last_run_id"] = run_id
    if catalog_by_table:
        state["last_catalog_poll_at"] = sync.iso_utc(now)
    return table_reports


def build_manifest(run_id, started_at, catalog, migration_sources, tables):
    finished_at = sync.iso_utc(sync.now_utc())
    failed = sum(1 for source in migration_sources if source["status"] == "failed")
    status = "partial_failure" if failed else "success"
    return {
        "run_id": run_id,
        "started_at": started_at,
        "finished_at": finished_at,
        "status": status,
        "type": "legacy_migration_bootstrap",
        "catalog": catalog,
        "migration_sources": migration_sources,
        "tables": tables,
        "summary": {
            "sources_total": len(migration_sources),
            "sources_failed": failed,
            "tables_bootstrapped": len(tables),
        },
    }


def main():
    args = parse_args()
    only_tables = {value.upper() for value in (args.table or [])}
    if not args.dry_run:
        sync.ensure_dirs()

    run_id = f"bootstrap-{sync.make_run_id(sync.now_utc())}"
    started_at = sync.iso_utc(sync.now_utc())
    catalog_by_table = {}
    catalog_info = {"polled": False}
    if not args.no_catalog:
        catalog = sync.fetch_catalog()
        catalog_by_table = {row["id"].upper(): row.get("updated") for row in catalog}
        catalog_info = {
            "polled": True,
            "table_count": len(catalog),
            "polled_at": sync.iso_utc(sync.now_utc()),
        }

    migration_sources = []
    planned_tids_by_table = {}
    for table_id, source_fp in iter_legacy_sources(sync.FACT_TABLES_DIR, only_tables):
        source_report = {
            "table_id": table_id,
            "status": "migrated",
            "source": str(source_fp),
        }
        try:
            source_report.update(
                migrate_source_file(
                    table_id,
                    source_fp,
                    overwrite_canonical=args.overwrite_canonical,
                    dry_run=args.dry_run,
                )
            )
            source_tids = source_report.pop("tids", [])
            planned_tids_by_table.setdefault(table_id, set()).update(source_tids)
            if args.archive_legacy:
                source_report["archived_to"] = archive_source_file(
                    sync.FACT_TABLES_DIR, source_fp, dry_run=args.dry_run
                )
        except Exception as exc:
            source_report["status"] = "failed"
            source_report["error"] = str(exc)
        migration_sources.append(source_report)

    state = sync.load_state()
    table_reports = build_bootstrap_state(
        state,
        run_id,
        catalog_by_table,
        planned_tids_by_table=planned_tids_by_table,
    )
    manifest = build_manifest(run_id, started_at, catalog_info, migration_sources, table_reports)

    if not args.dry_run:
        sync.write_run_manifest(run_id, manifest)
        sync.save_state(state)

    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
