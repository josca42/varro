# Data + Context Pipeline

## High-level pipeline

1. Pull metadata and table data from DST/StatBank.
2. Normalize/process raw dataframes.
3. Load fact and dimension tables into Postgres.
4. Generate documentation/context artifacts used by the agent.
5. Generate or maintain fact->dimension link JSON files.

## Data ingestion (`varro/data/`)

### StatBank to disk

- `statbank_to_disk/get_table_info.py`
  - fetches table ids and table metadata from StatBank API.
- `statbank_to_disk/copy_tables_statbank.py`
  - downloads bulk table data, optionally partitions by time for very large tables.
- `statbank_to_disk/create_subjects_graph.py`
  - builds subject hierarchy graph (`subjects_graph.gml`).
- `statbank_to_disk/get_cat_tables_and_descriptions.py`
  - pulls external classification table docs + CSV/parquet artifacts.

### Transform and load to DB

- `disk_to_db/process_tables.py`
  - column normalization, `tid` parsing, range handling, numeric cleanup.
- `disk_to_db/create_db_table.py`
  - infers Postgres column types and emits/applies DDL + COPY load.
- `disk_to_db/fact_tables_to_db.py`
  - loads processed fact tables into schema `fact`.
- `disk_to_db/dim_tables_to_db.py`
  - loads processed dimension tables into schema `dim`.

### Fact->dimension linking workflow

- `fact_col_to_dim_table/dimension_links_cli.py`
  - inspect dimension tables and save/check dimension link JSON.
- `fact_col_to_dim_table/create_dimension_links.py`
  - automation/orchestration script for generating links.

## Context generation (`varro/context/`)

- `subjects.py`
  - builds subject markdown files and table docs structure.
- `fact_table.py`
  - builds fact table docs and column value mappings from metadata + DB checks.
- `dim_table.py`
  - copies/summarizes dimension docs and dumps unique dim values parquet.
- `tools.py`
  - `generate_hierarchy` — compact format (roots + mids only, no leaves). Injected into prompt. Agent discovers leaves via filesystem browsing.
- `utils.py`
  - fact-column normalization and fuzzy matching for lookup.

## Runtime dependency from app/agent perspective

At runtime, chat agent behavior expects:

- populated Postgres schemas (`fact`, `dim`),
- docs under `context/subjects/...`, `context/fact/...`, `context/dim/...`, and `context/geo/...`,
- column value parquet files under `context/column_values/...`,
- dimension links under `data/dst/dimension_links/...`.

Without these artifacts, many analysis tools/prompts lose grounding.

## Config anchors

`varro/config.py` centralizes key paths from `.env`:

- `DATA_DIR`
- `CONTEXT_DIR`
- docs paths (`SUBJECTS_DIR`, `FACTS_DIR`, `DIMS_DIR`)
- `COLUMN_VALUES_DIR`
- `DIM_TABLE_DESCR_DIR`
- `DST_METADATA_DIR`
- `DST_MAPPING_TABLES_DIR`
- `DST_STATBANK_TABLES_DIR`
- `DST_DIMENSION_LINKS_DIR`

## Path learnings (2026-02-21)

- Canonical `.env` values are relative to project root:
  - `DATA_DIR=data`
  - `CONTEXT_DIR=context`
- `varro/config.py` resolves relative `.env` paths via `PROJECT_ROOT`.
- DST artifacts should be treated as a single subtree under `data/dst/`:
  - `metadata/`
  - `mapping_tables/`
  - `statbank_tables/`
  - `dimension_links/`
  - `dim_table_descr/`
- Agent/runtime docs live under `context/` and should not be mixed with DST raw data paths.
- `varro/playground/cli.py` status output path uses `data/chat/...` (singular `chat`, not `chats`).
- Current targeted test caveat: `tests/agent/test_filesystem_sandbox.py` expects `varro.agent.workspace.DOCS_DIR`, which is not present in current workspace module.

## Dim hierarchy learnings (2026-02-23)

- Raw mapping tables in `data/dst/mapping_tables/*/table_da.parquet` include `SEKVENS`, `KODE`, `NIVEAU`, `TITEL`.
- `SEKVENS` is a hierarchy-friendly traversal order; parent-child links can be derived with a simple level stack.
- Dim ingest now derives `parent_kode` for all dimensions in `process_dim_table()` before DB load.
- Dimension DDL now creates `kode,niveau,titel,parent_kode` and indexes both `niveau` and `parent_kode`.
- Dimension DDL no longer emits table/column `COMMENT` SQL statements.
- `varro/context/dim_table.py` now exports `(kode, niveau, titel, parent_kode)` to `context/column_values/{dim}.parquet`.
- Existing DBs can be backfilled by dropping `dim.*` tables and rerunning `varro/data/disk_to_db/dim_tables_to_db.py`.
- `dim_tables_to_db.py` still drops `db` niveau 1 rows; that leaves niveau 2 rows in `dim.db` with `parent_kode = NULL` by design.
- For dimensions with duplicate `kode` across levels (for example `db`, `nr_branche`), `parent_kode` alone can be ambiguous; add `parent_niveau` if strict unambiguous self-joins are needed.

## Dimension join audit tooling (2026-02-26)

- `scripts/audit_dim_joins.py`: Typer CLI to audit fact↔dim joins. Commands: `audit-table`, `audit-subject`, `update-link`, `regen-docs`.
- `.claude/skills/audit-dim-joins/SKILL.md`: Skill for AI analyst to review fact tables by subject, investigate joins with psql, and append free-form `notes:` to fact docs with query guidance, ColumnValues tips, and join gotchas.
- `scripts/gen_dim_docs.py` now looks up the actual fact column name from dimension_links JSON (via `get_fact_column_for_dim`) instead of using the dim table name as the fact column in SQL examples.
- `varro/context/subjects.py`: Fact doc regeneration now preserves any existing `notes:` section appended by the audit analyst. The `extract_notes()` function reads back everything from `notes:` onward before overwriting.

## Chat-15 context updates (2026-02-24)

- `varro/context/fact_table.py` now derives join expressions from actual fact/dim key dtypes and renders them in fact docs (for example `overtraed=kode::text`).
- Fact docs now include observed level-1 coverage per dim-linked column (`level-1 values [...]`) in both detailed fact readmes and subject table summaries.
- Level-1 coverage extraction now walks dim parent links when available, so lower-level fact codes still resolve to top-level categories.
- `varro/context/subjects.py` now adds a `<coverage notes>` block when leaf-subject table coverage differs, or when all tables share a subset that is smaller than the dimension's full level-1 universe.

## StatBank incremental sync + Prefect (2026-02-24)

- `varro/data/statbank_to_disk/copy_tables_statbank.py` was rewritten from one-shot full copy to incremental sync.
- Canonical fact storage is now partitioned parquet files per table and period:
  - `data/dst/statbank_tables/{TABLE_ID}/{urlquoted_tid}.parquet`
- Sync control files are under `data/dst/statbank_tables/_sync/`:
  - `state.json` tracks table-level sync state (`last_seen_updated`, `last_sync_at`, `frequency`, `bootstrap_complete`, `last_status`, `last_error`, `last_run_id`) and global poll state.
  - `runs/{run_id}.json` stores run manifests with catalog snapshot, per-table outcomes, changed tids, and summary counts.
  - `frequency_overrides.json` optionally overrides inferred per-table frequency.
- Incremental eligibility:
  - global catalog poll uses `/v1/tables?lang=da` with a weekly gate,
  - changed tables are detected by `updated`,
  - table metadata is refreshed via `/v1/tableinfo` and cached back to `tables_info_raw_da/{table}.pkl`.
- Frequency is inferred from `Tid` codes (yearly/quarterly/monthly/weekly/daily/half-yearly/other) and drives rolling refresh windows for revision handling.
- `periods_to_fetch = new_periods ∪ trailing_refresh_periods`; source-deleted periods are ignored.
- Full historical bootstrap is used for unseen tables.
- DST API pacing is now built into `copy_tables_statbank.py`:
  - `statbank_request()` wraps all DST HTTP calls (`tables`, `tableinfo`, `data`),
  - sleeps after each call using `DST_API_SLEEP_SECONDS` (env, default `120`, `0` disables).
- One-time migration utility added for legacy file layouts:
  - `varro/data/statbank_to_disk/migrate_legacy_statbank_layout.py`
  - migrates legacy `table.parquet` and `table/partition_i.parquet` files into canonical `table/{Tid}.parquet`,
  - optional `--archive-legacy` move to `data/dst/statbank_tables/initial_copy/`,
  - bootstraps `_sync/state.json` from canonical files and writes a `legacy_migration_bootstrap` run manifest.
- New DB delta loader: `varro/data/disk_to_db/fact_tables_incremental_to_db.py`.
  - Reads changed tids from a run manifest.
  - For existing `fact.{table}` tables: loads changed partitions, processes with `process_fact_table`, deletes target rows by `tid`, inserts refreshed rows.
  - Writes `db_apply` results back into the same run manifest.
- Prefect orchestration:
  - `varro/data/statbank_to_disk/prefect_flows.py` defines `weekly_statbank_sync_flow`.
  - Flow now orchestrates table sync as explicit Prefect tasks:
    - `fetch_catalog_task` once,
    - `sync_table_task` per table with `task_run_name=sync-{table_id}`,
    - sequential execution inside the flow (no parallel fan-out),
    - optional `max_tables` parameter for staged runs.
  - `varro/data/statbank_to_disk/deploy_prefect.py` registers deployment `weekly-statbank-sync` on cron `0 22 * * 0` in `UTC` using a process work pool (default `process`, override via `PREFECT_WORK_POOL`).

## StatBank incremental sync live experiment (2026-02-26)

- Ran a constrained live sync experiment against DST API and local Prefect API:
  - Prefect API health: `http://127.0.0.1:4200/api/health` -> `200 true`.
  - Experiment run root: `/tmp/statbank_sync_experiment_20260226T124346Z`.
  - Run id: `exp-20260226T124546Z`.
  - Single table: `AUF02`.
  - Enforced conservative pacing in run script: `sleep(120)` after each DST API call.
- Sync outcome:
  - `run_sync_cycle(force_catalog_poll=True)` completed with `status=success` for 1 table.
  - `changed_tids`: `2025M03..2025M06`.
  - `rows_written=526,781`, `files_written=4`.
- Found and fixed a DB delta bug:
  - `changed_tids` in manifest are code strings (for example `2025M03`), but `process_fact_table()` converts monthly/quarterly/half-year `tid` to date values (for example `2025-03-01`) before insert.
  - Delete step used raw `changed_tids`, which can miss existing rows and cause duplicate inserts.
  - Fix in `varro/data/disk_to_db/fact_tables_incremental_to_db.py`:
    - new `normalize_changed_tids()` reuses `process_fact_table()` conversion logic on tid codes.
    - `apply_table_delta()` now deletes using normalized tid values.
  - Regression tests added in `tests/data/test_fact_tables_incremental_to_db.py` for monthly tid normalization and deduplication.
- Re-applied DB delta for the same run after the fix:
  - `deleted_rows=662,754`, `inserted_rows=526,781`.
  - Verified `fact.auf02` counts for `2025-03-01..2025-06-01` now exactly match inserted partition totals.

## Staged legacy migration run (2026-02-26)

- Executed real staged migration with archive enabled:
  - `uv run python varro/data/statbank_to_disk/migrate_legacy_statbank_layout.py --table INST15 --table STRAF47 --table UDDAKT35 --archive-legacy`
  - run id: `bootstrap-20260226T133603Z`.
- Outcome:
  - status `success`, `sources_total=29`, `tables_bootstrapped=3`.
  - canonical per-`Tid` files now exist in:
    - `data/dst/statbank_tables/INST15/` (20 yearly tids)
    - `data/dst/statbank_tables/STRAF47/` (18 yearly tids)
    - `data/dst/statbank_tables/UDDAKT35/` (20 yearly tids)
  - migrated legacy source files were moved to:
    - `data/dst/statbank_tables/initial_copy/`
      (including both root `*.parquet` and `partition_*.parquet` files).
- State bootstrap confirmed:
  - `data/dst/statbank_tables/_sync/state.json` now has `last_status=bootstrapped`, `bootstrap_complete=true`, seeded `last_seen_updated` from catalog, and `last_run_id=bootstrap-20260226T133603Z` for the three staged tables.

## Full legacy migration run (2026-02-26)

- Executed full migration + archive:
  - `uv run python varro/data/statbank_to_disk/migrate_legacy_statbank_layout.py --archive-legacy`
  - run id: `bootstrap-20260226T134239Z`
  - manifest output captured in `/tmp/statbank_full_migration_20260226T134238Z.json`
  - run manifest persisted to `data/dst/statbank_tables/_sync/runs/bootstrap-20260226T134239Z.json`
- Summary:
  - `status=success`
  - `sources_total=2915`
  - `sources_failed=0`
  - `tables_bootstrapped=2201`
  - catalog was polled (`table_count=2238`)
- Post-run storage validation:
  - legacy root files remaining in `data/dst/statbank_tables/*.parquet`: `0`
  - legacy `partition_*.parquet` remaining outside `initial_copy`: `0`
  - archived legacy files under `data/dst/statbank_tables/initial_copy/`:
    - root files: `2197`
    - partition files: `747`
  - canonical `table/{Tid}.parquet` files present: `131184`
- State validation:
  - `_sync/state.json` now has `last_run_id=bootstrap-20260226T134239Z` and `table_states=2201`.
  - migrated tables with unchanged catalog `updated` now hit skip path (`reason=unchanged_updated`) without calling `tableinfo`.

## Prefect staged run validation (2026-02-27)

- Updated deployment bootstrap:
  - `varro/data/statbank_to_disk/deploy_prefect.py` now deploys with
    `weekly_statbank_sync_flow.from_source(...).deploy(...)`.
  - Added `PREFECT_API_URL` default: `http://127.0.0.1:4200/api` (env override still supported).
  - Deployment parameters now include `max_tables` default `None`.
- Registered deployment against local Prefect API:
  - `weekly-statbank-sync/weekly-statbank-sync` applied in work pool `process`.
- Executed staged deployment run to validate orchestration:
  - flow run id: `3164e195-f7d4-4378-8916-15198dcaeee7`
  - parameters: `force_catalog_poll=true`, `max_tables=5`
  - sync run id: `20260227T152411Z`
  - result: `status=success`, `tables_total=5`, `tables_skipped=5`, `tables_with_changed_tids=0`, `db_apply=skipped(no_changed_tids)`.
- Verified sequential table-task execution:
  - task order observed in logs and Prefect task runs:
    `sync-ABST1 -> sync-AED01 -> sync-AED012 -> sync-AED02 -> sync-AED021`
  - no overlap detected between table sync task start/end timestamps.
