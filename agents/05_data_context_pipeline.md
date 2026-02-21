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
