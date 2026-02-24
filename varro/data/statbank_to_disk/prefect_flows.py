from prefect import flow, get_run_logger, task

from varro.data.disk_to_db.fact_tables_incremental_to_db import apply_incremental_run
from varro.data.statbank_to_disk.copy_tables_statbank import run_sync_cycle


@task(name="statbank-sync", retries=3, retry_delay_seconds=[30, 120, 300])
def run_sync_cycle_task(force_catalog_poll: bool = False) -> dict:
    return run_sync_cycle(force_catalog_poll=force_catalog_poll)


@task(name="fact-db-apply", retries=1, retry_delay_seconds=60)
def apply_incremental_run_task(run_id: str) -> dict:
    return apply_incremental_run(run_id)


@flow(name="weekly-statbank-sync")
def weekly_statbank_sync_flow(force_catalog_poll: bool = False) -> dict:
    logger = get_run_logger()
    sync_result = run_sync_cycle_task(force_catalog_poll=force_catalog_poll)
    run_id = sync_result["run_id"]
    changed = sync_result.get("summary", {}).get("tables_with_changed_tids", 0)

    if changed > 0:
        db_apply = apply_incremental_run_task(run_id)
    else:
        db_apply = {
            "run_id": run_id,
            "status": "skipped",
            "reason": "no_changed_tids",
            "summary": {
                "tables_total": 0,
                "tables_applied": 0,
                "tables_skipped": 0,
                "tables_failed": 0,
            },
        }

    logger.info(
        "run_id=%s sync_status=%s db_status=%s",
        run_id,
        sync_result.get("status"),
        db_apply.get("status"),
    )
    return {"sync": sync_result, "db_apply": db_apply}


if __name__ == "__main__":
    weekly_statbank_sync_flow()
