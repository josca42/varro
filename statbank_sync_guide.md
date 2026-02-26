# StatBank Incremental Sync Guide

This document describes the current incremental sync setup for StatBank data, how to run it, how to debug it, and where to extend it.

## Scope

The sync setup has three parts:

1. Pull table update metadata and data from StatBank.
2. Persist canonical fact data on disk as partitioned parquet files by `Tid`.
3. Apply changed `Tid` partitions into existing `fact.*` Postgres tables.

The orchestration layer is Prefect.

## Key Code References

- Sync engine: `varro/data/statbank_to_disk/copy_tables_statbank.py`
- Prefect flow: `varro/data/statbank_to_disk/prefect_flows.py`
- Prefect deployment bootstrap: `varro/data/statbank_to_disk/deploy_prefect.py`
- DB delta apply: `varro/data/disk_to_db/fact_tables_incremental_to_db.py`
- Fact transformation before DB load: `varro/data/disk_to_db/process_tables.py`
- Shared DB COPY helpers: `varro/data/disk_to_db/create_db_table.py`
- Path config anchors: `varro/config.py`
- Tests: `tests/data/test_statbank_incremental_sync.py`, `tests/data/test_fact_tables_incremental_to_db.py`

## Disk Layout

Canonical facts are partitioned by table + `Tid`:

- `data/dst/statbank_tables/<TABLE_ID>/<urlquoted_tid>.parquet`

Sync control artifacts:

- `data/dst/statbank_tables/_sync/state.json`
- `data/dst/statbank_tables/_sync/runs/<run_id>.json`
- `data/dst/statbank_tables/_sync/frequency_overrides.json` (optional)

Metadata cache refreshed for changed tables:

- `data/dst/metadata/tables_info_raw_da/<TABLE_ID>.pkl`

## End-to-End Flow

### 1. Entry point

`run_sync_cycle(force_catalog_poll: bool = False, run_id: str | None = None)` in `copy_tables_statbank.py` is the primary sync entry point.

### 2. Weekly catalog poll gate

- Catalog source: `GET https://api.statbank.dk/v1/tables?lang=da`
- Poll is skipped unless:
  - `force_catalog_poll=True`, or
  - `last_catalog_poll_at` is at least 7 days old.

If gate blocks the poll, a run manifest is still written with status `skipped`.

### 3. Per-table eligibility

For each table in catalog:

- If table has local partitions and `state.tables[table_id].last_seen_updated == catalog.updated`:
  - table is `skipped` (`unchanged_updated`).
- Otherwise table is synced.
- Bootstrap mode is used when no partition files exist for table.

### 4. Metadata refresh + frequency inference

For syncing tables:

- Fetch `tableinfo` from `GET /v1/tableinfo`.
- Persist pickle to `tables_info_raw_da/<TABLE_ID>.pkl`.
- Extract remote `Tid` values.
- Infer frequency from `Tid` pattern unless overridden in `frequency_overrides.json`.

Supported inferred frequencies:

- yearly: `^\d{4}$`
- quarterly: `^\d{4}K[1-4]$`
- monthly: `^\d{4}M\d{2}$`
- weekly: `^\d{4}U\d{2}$`
- daily: `^\d{4}M\d{2}D\d{2}$`
- half-yearly: `^\d{4}H[12]$`
- other: fallback

### 5. Period selection

- `new_periods = remote_tids - local_tids`
- `refresh_periods = trailing window(remote_tids, window_size_for_frequency)`
- non-bootstrap fetch set: `new_periods ∪ refresh_periods`
- bootstrap fetch set: all remote tids

Default refresh window sizes:

- daily: 14
- weekly: 12
- monthly: 18
- quarterly: 8
- half-yearly: 6
- yearly: 4
- other: 2

### 6. Data fetch + partition writes

- Data endpoint: `POST https://api.statbank.dk/v1/data`
- Request format: `BULK`, `valuePresentation=Code`
- All non-`Tid` dimensions use `"*"`; `Tid` is restricted to selected period batch.
- Batch size is derived from estimated rows/time period and `MAX_ROWS_PER_CALL`.
- Returned dataframe is split by `Tid` and each `Tid` is written to one parquet file.
- Writes are atomic (temp file + rename).

### 7. Run manifest + state updates

`run_sync_cycle` always writes:

- mutable state (`state.json`)
- immutable run record (`runs/<run_id>.json`)

Per-table failures are captured and do not stop the cycle.

## `state.json` Contract

Global keys:

- `last_catalog_poll_at`
- `last_run_id`
- `tables`

Per-table keys:

- `last_seen_updated`
- `last_sync_at`
- `frequency`
- `bootstrap_complete`
- `last_status`
- `last_error`
- `last_run_id`

## Run Manifest Contract

`runs/<run_id>.json` includes:

- top-level run metadata (`run_id`, `started_at`, `finished_at`, `status`)
- catalog section (`polled`, `table_count`, `polled_at` or skip reason)
- per-table results in `tables`
- summary counters in `summary`
- optional `db_apply` section after DB delta apply

Per-table sync result fields usually include:

- `status`
- `catalog_updated`
- `bootstrap`
- `frequency`
- `new_periods`
- `refresh_periods`
- `changed_tids`
- `rows_written`
- `files_written`

## DB Delta Apply Flow

Entry point:

- `apply_incremental_run(run_id: str)` in `fact_tables_incremental_to_db.py`

Behavior:

1. Read sync manifest `runs/<run_id>.json`.
2. For each table with non-empty `changed_tids`:
   - Skip if `fact.<table>` does not exist.
   - Load only changed partition files.
   - Process with `process_fact_table`.
   - In one transaction:
     - create temp table from `fact.<table>` schema
     - COPY processed rows into temp table
     - `DELETE` target rows where `tid` in changed tids
     - INSERT rows from temp table into target
3. Persist `db_apply` report back into same run manifest.

## Prefect Orchestration

Flow:

- `weekly_statbank_sync_flow(force_catalog_poll=False)` in `prefect_flows.py`
- Task 1: `run_sync_cycle_task` (retries: 3)
- Task 2: `apply_incremental_run_task` (retries: 1), only when sync summary shows changed tids

Deployment bootstrap:

- `deploy_weekly_sync()` in `deploy_prefect.py`
- Deployment name: `weekly-statbank-sync`
- Schedule: Sunday 22:00 UTC (`cron: 0 22 * * 0`)
- Work pool default: `process` (override via `PREFECT_WORK_POOL` env)

## Operations Runbook

### One-off local sync run

```bash
uv run python varro/data/statbank_to_disk/copy_tables_statbank.py
```

### One-off DB delta apply from latest run

```bash
uv run python varro/data/disk_to_db/fact_tables_incremental_to_db.py
```

### Register/update Prefect deployment

```bash
uv run python varro/data/statbank_to_disk/deploy_prefect.py
```

### Run tests for sync setup

```bash
uv run pytest tests/data/test_statbank_incremental_sync.py tests/data/test_fact_tables_incremental_to_db.py
```

## Debugging Guide

### Symptom: No tables synced

Check:

- `state.json -> last_catalog_poll_at`
- latest run manifest `catalog.reason`

Likely reason:

- weekly poll gate skipped catalog call.

### Symptom: Table marked changed but no data files updated

Check manifest table result:

- `new_periods`
- `refresh_periods`
- `changed_tids`
- `rows_written`

Likely reasons:

- empty `changed_tids` after selection logic
- source returned no rows for some requested tids

### Symptom: Table fails in sync

Check manifest table result:

- `error`

Common causes:

- `tableinfo` error payload (`errorTypeCode`)
- response shape changed (missing `Tid`)
- transient network/API error

### Symptom: DB apply skipped table

Check `db_apply.tables[table].reason`:

- `missing_fact_table`: target table does not exist in schema `fact`.

### Symptom: DB apply failed table

Check:

- `db_apply.tables[table].error` or `reason`
- presence of expected partition files for `changed_tids`

Common causes:

- missing partition files
- DB schema mismatch with processed dataframe columns

## Extension Points

### Add a new frequency pattern

Edit in `copy_tables_statbank.py`:

- regex constants
- `infer_frequency`
- `REFRESH_WINDOWS`

### Tune fetch batch sizing

Edit:

- `MAX_ROWS_PER_CALL`
- `estimate_rows_per_time`
- `max_tid_values_per_call`

### Add hard deletion sync behavior

Current behavior ignores source-deleted periods. To change this:

- compare `local_tids - remote_tids`
- add explicit deletion handling for partition files and DB rows
- record deletion stats in run manifest

### Make DB apply stricter

Potential upgrades:

- verify `changed_tids` coverage before delete
- add row-count assertions per tid
- add dry-run mode that only reports planned deletes/inserts

### Add alerting/observability

Use Prefect state hooks or downstream log consumers keyed by:

- run status (`success`, `partial_failure`, `failed`)
- summary counters
- table-level error payloads

## Known Constraints

- Partitioning assumes every fact table has a usable `Tid` variable.
- DB apply assumes target `fact.*` table schema already exists.
- Sync and DB apply are resilient to per-table failures but not guaranteed all-or-nothing globally.
- Source-deleted periods are currently ignored by design.

## Quick Orientation for New Engineers

1. Read `copy_tables_statbank.py` top-to-bottom.
2. Run one forced sync cycle with a custom `run_id` from a Python shell.
3. Inspect `runs/<run_id>.json` and one table partition directory.
4. Run `apply_incremental_run(run_id)` and inspect `db_apply` section.
5. Run tests in `tests/data/` before modifying selection logic or state format.
