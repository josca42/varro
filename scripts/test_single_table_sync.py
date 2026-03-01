"""Quick end-to-end incremental sync test for a single table."""

import json
import sys

from varro.data.disk_to_db.fact_tables_incremental_to_db import apply_incremental_run
from varro.data.statbank_to_disk import copy_tables_statbank as sync

TABLE_ID = sys.argv[1] if len(sys.argv) > 1 else "FOLK1A"


def main():
    sync.ensure_dirs()
    now = sync.now_utc()
    run_id = f"test-{sync.make_run_id(now)}"

    print(f"run_id: {run_id}")
    print(f"table:  {TABLE_ID}")
    print(f"api sleep: {sync.DST_API_SLEEP_SECONDS}s")
    print()

    print("Fetching catalog...")
    catalog = sync.fetch_catalog()
    entry = next((row for row in catalog if row["id"] == TABLE_ID), None)
    if not entry:
        sys.exit(f"Table {TABLE_ID} not found in catalog")

    catalog_updated = entry.get("updated")
    print(f"catalog updated: {catalog_updated}")
    print()

    print(f"Syncing {TABLE_ID}...")
    result = sync.sync_table(table_id=TABLE_ID, catalog_updated=catalog_updated, run_id=run_id)
    print(json.dumps(result, indent=2, default=str))
    print()

    manifest = {
        "run_id": run_id,
        "started_at": sync.iso_utc(now),
        "finished_at": sync.iso_utc(sync.now_utc()),
        "status": result["status"],
        "tables": {TABLE_ID: result},
        "summary": {"tables_total": 1, "tables_synced": int(result["status"] == "synced")},
    }

    changed_tids = result.get("changed_tids", [])
    if changed_tids:
        sync.write_run_manifest(run_id, manifest)
        print(f"Applying {len(changed_tids)} changed tids to DB...")
        db_result = apply_incremental_run(run_id)
        print(json.dumps(db_result, indent=2, default=str))
    else:
        sync.write_run_manifest(run_id, manifest)
        print("No changed tids — skipping DB apply")


if __name__ == "__main__":
    main()
