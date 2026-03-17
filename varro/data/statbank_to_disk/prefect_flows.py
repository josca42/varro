from prefect import flow, get_run_logger, task

from varro.data.disk_to_db.fact_tables_incremental_to_db import apply_table_delta, table_exists_in_db
from varro.data.statbank_to_disk import copy_tables_statbank as sync


@task(name="fetch-catalog", retries=3, retry_delay_seconds=[30, 120, 300])
def fetch_catalog_task() -> list[dict]:
    return sync.fetch_catalog()


@task(
    name="sync-table",
    task_run_name="sync-{table_id}",
    retries=2,
    retry_delay_seconds=[30, 120],
)
def sync_and_apply_table_task(table_id: str, catalog_updated: str, state_entry: dict) -> dict:
    if state_entry.get("updated") == catalog_updated:
        return {"status": "skipped", "reason": "unchanged"}

    info = sync.fetch_table_info(table_id)
    sync.save_table_info(table_id, info)
    remote_tids = sync.get_tid_values(info)
    overrides = sync.load_frequency_overrides()
    frequency = sync.resolve_frequency(table_id, remote_tids, overrides)
    local_tids = sync.list_local_tids(table_id)
    periods = sync.pick_periods_to_fetch(remote_tids, local_tids, frequency)

    if not periods:
        return {"status": "skipped", "reason": "no_periods", "frequency": frequency}

    rows_written = 0
    files_written = 0
    per_call = sync.max_tid_values_per_call(info, remote_tids)
    for batch in sync.chunk(periods, per_call):
        df = sync.copy_table_batch(table_id, info, batch)
        batch_rows, batch_files = sync.write_batch_partitions(table_id, batch, df)
        rows_written += batch_rows
        files_written += batch_files

    db_result = None
    if table_exists_in_db(table_id):
        db_result = apply_table_delta(table_id, periods)

    return {
        "status": "synced",
        "frequency": frequency,
        "periods_fetched": len(periods),
        "rows_written": rows_written,
        "files_written": files_written,
        "bootstrap": len(local_tids) == 0,
        "db_apply": db_result,
    }


@flow(name="monthly-statbank-sync")
def monthly_sync_flow(max_tables: int | None = None) -> dict:
    logger = get_run_logger()
    sync.ensure_dirs()

    catalog = fetch_catalog_task()
    if max_tables is not None:
        catalog = catalog[:max_tables]

    state = sync.load_state()
    results = {}
    total = len(catalog)

    for idx, row in enumerate(catalog, start=1):
        table_id = row["id"]
        catalog_updated = row.get("updated")
        state_entry = state.get(table_id, {})

        logger.info("table %s (%s/%s)", table_id, idx, total)
        try:
            result = sync_and_apply_table_task(table_id, catalog_updated, state_entry)
        except Exception as exc:
            logger.error("table %s failed: %s", table_id, exc)
            result = {"status": "failed", "error": str(exc)}

        results[table_id] = result
        if result["status"] == "synced":
            state[table_id] = {
                "updated": catalog_updated,
                "frequency": result["frequency"],
            }

    sync.save_state(state)

    synced = sum(1 for r in results.values() if r["status"] == "synced")
    skipped = sum(1 for r in results.values() if r["status"] == "skipped")
    failed = sum(1 for r in results.values() if r["status"] == "failed")
    logger.info("done: %s synced, %s skipped, %s failed", synced, skipped, failed)

    return {
        "tables_total": total,
        "tables_synced": synced,
        "tables_skipped": skipped,
        "tables_failed": failed,
        "tables": results,
    }


if __name__ == "__main__":
    monthly_sync_flow()
