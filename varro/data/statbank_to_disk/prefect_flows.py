from prefect import flow, get_run_logger, task

from varro.data.disk_to_db.fact_tables_incremental_to_db import apply_incremental_run
from varro.data.statbank_to_disk import copy_tables_statbank as sync


@task(name="statbank-fetch-catalog", retries=3, retry_delay_seconds=[30, 120, 300])
def fetch_catalog_task() -> list[dict]:
    return sync.fetch_catalog()


@task(
    name="statbank-sync-table",
    task_run_name="sync-{table_id}",
    retries=3,
    retry_delay_seconds=[30, 120, 300],
)
def sync_table_task(table_id: str, catalog_updated: str, run_id: str) -> dict:
    return sync.sync_table(table_id=table_id, catalog_updated=catalog_updated, run_id=run_id)


@task(name="fact-db-apply", retries=1, retry_delay_seconds=60)
def apply_incremental_run_task(run_id: str) -> dict:
    return apply_incremental_run(run_id)


def no_changed_tids_result(run_id: str) -> dict:
    return {
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


def update_failed_table_state(table_id: str, catalog_updated: str, run_id: str, error: str) -> None:
    state = sync.load_state()
    previous = state["tables"].get(table_id, {})
    frequency = previous.get("frequency", "other")
    state["tables"][table_id] = sync.build_table_state(
        previous,
        catalog_updated=catalog_updated,
        frequency=frequency,
        run_id=run_id,
        now=sync.now_utc(),
        status="failed",
        error=error,
    )
    state["last_run_id"] = run_id
    sync.save_state(state)


@flow(name="weekly-statbank-sync")
def weekly_statbank_sync_flow(force_catalog_poll: bool = False, max_tables: int | None = None) -> dict:
    logger = get_run_logger()
    sync.ensure_dirs()
    started = sync.now_utc()
    run_id = sync.make_run_id(started)
    state = sync.load_state()
    manifest = {
        "run_id": run_id,
        "started_at": sync.iso_utc(started),
        "finished_at": None,
        "force_catalog_poll": force_catalog_poll,
        "status": "running",
        "catalog": {},
        "tables": {},
        "summary": {},
    }

    try:
        if not sync.should_poll_catalog(state, started, force_catalog_poll):
            manifest["status"] = "skipped"
            manifest["catalog"] = {
                "polled": False,
                "reason": "weekly_gate",
                "last_catalog_poll_at": state.get("last_catalog_poll_at"),
            }
            manifest["summary"] = {
                "tables_total": 0,
                "tables_synced": 0,
                "tables_skipped": 0,
                "tables_failed": 0,
                "tables_with_changed_tids": 0,
            }
            db_apply = no_changed_tids_result(run_id)
            manifest["db_apply"] = db_apply
            return {"sync": manifest, "db_apply": db_apply}

        catalog = fetch_catalog_task()
        if max_tables is not None:
            catalog = catalog[:max_tables]

        polled_at = sync.iso_utc(sync.now_utc())
        state["last_catalog_poll_at"] = polled_at
        state["last_run_id"] = run_id
        sync.save_state(state)
        manifest["catalog"] = {
            "polled": True,
            "table_count": len(catalog),
            "polled_at": polled_at,
        }

        total = len(catalog)
        for idx, row in enumerate(catalog, start=1):
            table_id = row["id"]
            catalog_updated = row.get("updated")
            logger.info("sync table %s (%s/%s)", table_id, idx, total)
            try:
                result = sync_table_task(
                    table_id=table_id,
                    catalog_updated=catalog_updated,
                    run_id=run_id,
                )
            except Exception as exc:
                result = {
                    "status": "failed",
                    "catalog_updated": catalog_updated,
                    "error": str(exc),
                    "changed_tids": [],
                }
                update_failed_table_state(
                    table_id=table_id,
                    catalog_updated=catalog_updated,
                    run_id=run_id,
                    error=str(exc),
                )
            manifest["tables"][table_id] = result

        table_results = list(manifest["tables"].values())
        synced = sum(1 for result in table_results if result["status"] == "synced")
        skipped = sum(1 for result in table_results if result["status"] == "skipped")
        failed = sum(1 for result in table_results if result["status"] == "failed")
        changed = sum(1 for result in table_results if result.get("changed_tids"))
        manifest["summary"] = {
            "tables_total": len(table_results),
            "tables_synced": synced,
            "tables_skipped": skipped,
            "tables_failed": failed,
            "tables_with_changed_tids": changed,
        }
        manifest["status"] = "partial_failure" if failed else "success"

        if changed > 0:
            db_apply = apply_incremental_run_task(run_id)
        else:
            db_apply = no_changed_tids_result(run_id)
        manifest["db_apply"] = db_apply

        logger.info(
            "run_id=%s sync_status=%s db_status=%s",
            run_id,
            manifest.get("status"),
            db_apply.get("status"),
        )
        return {"sync": manifest, "db_apply": db_apply}
    except Exception as exc:
        manifest["status"] = "failed"
        manifest["error"] = str(exc)
        raise
    finally:
        manifest["finished_at"] = sync.iso_utc(sync.now_utc())
        state = sync.load_state()
        state["last_run_id"] = run_id
        sync.write_run_manifest(run_id, manifest)
        sync.save_state(state)


if __name__ == "__main__":
    weekly_statbank_sync_flow()
