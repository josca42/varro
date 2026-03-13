# Dashboard Framework

## Scope

Dashboard system is implemented in `varro/dashboard/` and mounted by `app/main.py`.

A dashboard folder requires:

- `dashboard.md`
- `outputs.py`
- `queries/*.sql` (at least one)

## Loader (`loader.py`)

- `load_queries(folder)` reads all `queries/*.sql` by stem name.
- `load_outputs(outputs.py)` uses `exec` with injected symbols (`output`, `Metric`, `px`, `go`, `pd`).
- `load_outputs(outputs.py)` wraps injected `gpd.read_parquet` so absolute `/geo/...` paths resolve to `varro.config.GEO_DIR` outside bwrap too; plain `pd` remains unwrapped.
- `load_dashboard(folder)` validates files, parses markdown AST, extracts filters, validates select options queries.

## Parser (`parser.py`)

AST node types:

- `ContainerNode` (`::: filters`, `::: grid`, `::: tabs`, `::: tab`)
- `ComponentNode` (`<fig />`, `<df />`, `<metric />`, filter tags)
- `MarkdownNode`

Important details:

- stack-based `:::` closing,
- inline component scanning in markdown lines,
- filters in `::: filters` become typed filter definitions.

## Filters (`filters.py`)

Supported filters:

- `SelectFilter`
- `DateRangeFilter`
- `CheckboxFilter`

Each filter defines:

- request param parsing (`parse_query_params`)
- URL serialization without defaults (`url_params`)

## Executor (`executor.py`)

- Extracts SQL params with regex that ignores Postgres casts (`(?<!:):(\w+)`).
- Binds only params present in query.
- Converts `"all"` and missing to `None`.
- infers param SQL types (`String`, `Date`, `Boolean`) for safe NULL binding.
- Normalizes object columns that contain Python `date` values to pandas `datetime64[ns]`.
- Caches query results in-process by `(query_hash, filters_json)`.
- Select options queries now support:
  - 1 column -> `(value, label)` becomes `(col1, col1)`,
  - 2+ columns -> `(value, label)` becomes `(col1, col2)`.

Output execution:

- matches `@output` function by name,
- injects `filters` dict and query dataframes by function signature param names.

## Components (`components.py`)

- Renders AST to FastHTML.
- Filter container renders `<form id="filters">`.
- Figures/tables/metrics are lazy placeholders with:
  - `hx_get="/dashboard/{name}/_/{type}/{output}"`
  - `hx_include="#filters"`
  - `hx_trigger="load, filtersChanged from:body"`
- Tabs rendered with Alpine state `active`.

## Routes (`routes.py`)

- `GET /dashboard/{name}`:
  - HTMX request -> content fragment
  - full request -> wraps in `AppShell`
  - select filters receive `(value, label)` options; UI renders labels while submitting values.
- `POST /dashboard/{name}/publish`:
  - copies dashboard source files to `data/public/{user_id}/{name}`
  - upsert behavior (publish/update in one endpoint)
- `GET /dashboard/{name}/_/filters`:
  - returns empty body with:
    - `HX-Replace-Url`
    - `HX-Trigger: {"filtersChanged": {}}`
- `GET /dashboard/{name}/_/figure/{output}`
- `GET /dashboard/{name}/_/table/{output}`
- `GET /dashboard/{name}/_/metric/{output}`
- `GET /public/{owner_id}/{name}`:
  - renders published dashboard (anonymous-readable)
- `GET /public/{owner_id}/{name}/_/filters`
- `GET /public/{owner_id}/{name}/_/figure/{output}`
- `GET /public/{owner_id}/{name}/_/table/{output}`
- `GET /public/{owner_id}/{name}/_/metric/{output}`
- `GET /public/{owner_id}/{name}/fork`:
  - authenticated: copies published dashboard to viewer workspace and redirects to `/dashboard/{fork_slug}`
  - anonymous: redirects to `/login?next=/public/{owner_id}/{name}/fork`
- `GET /_internal/dashboard/{token}/{name}` and matching `/_/filters|figure|table|metric` endpoints:
  - used only by server-side snapshot rendering,
  - bypass normal session auth,
  - require a short-lived HMAC token tied to `{user_id, slug}`.
- `GET /public/_/context-action?url=...`:
  - returns navbar action fragment (`Publish`, `Update`, `Edit`, or empty)

Dashboards are cached by file mtimes (`dashboard.md`, `outputs.py`, all query files) with cache keys scoped by `private/public`.
Dashboards are discovered per-user from `data/user/{user_id}/dashboard/{slug}`.
Published dashboards are stored in `data/public/{owner_id}/{slug}`.

## Publish and fork filesystem helpers (`public_fs.py`)

- `public_dashboard_dir(data_root, owner_id, slug)`
- `copy_dashboard_source(src, dst)` copies only:
  - `dashboard.md`
  - `outputs.py`
  - `queries/*.sql`
  - optional `notes.md`
- destination directory is replaced on publish/update (stale files removed)
- `next_fork_slug(private_dashboards_dir, base_slug)` picks:
  - `{slug}`
  - `{slug}-fork`
  - `{slug}-fork-2`
  - ...

## Example dashboard

- path: `data/user/1/dashboard/sales/`
- includes filters + metrics + tabs + figure/table outputs.

## Test coverage

- `tests/dashboard/test_parser_loader.py`
- `tests/dashboard/test_executor.py`
- `tests/dashboard/test_routes.py`
- `tests/dashboard/conftest.py`

## Source editing constraints (2026-02-09)

- `parse_dashboard_md` is render-oriented, not round-trip safe for rewriting `dashboard.md`:
  - it strips markdown buffers before building `MarkdownNode` (`text.strip()` in `parser.py`),
  - whitespace and exact original formatting are not preserved.
- For file-over-app editing with protected dashboard syntax, use raw-source segmentation instead of AST re-serialization:
  - lock custom syntax segments (`:::` container lines and component tag lines),
  - expose only markdown segments as editable fields,
  - reconstruct file by interleaving edited markdown with original locked segments.
- Add optimistic concurrency guard for saves:
  - include a file hash/etag in the edit form,
  - reject save if current file hash changed since editor load.

### Implemented dashboard source editor (2026-02-09)

- New routes in `varro/dashboard/routes.py`:
  - `GET /dashboard/{name}/code`
  - `PUT /dashboard/{name}/code`
- Editor behavior:
  - code mode exposes raw source files in tabs:
    - `dashboard.md`
    - `outputs.py`
    - `queries/*.sql` (sorted)
  - selected file is edited in a single textarea,
  - all syntax is editable (standard markdown + custom dashboard syntax).
  - no inline syntax highlighting in editor; textarea is used for simple editable flow.
- Save safeguards:
  - file hash mismatch returns editor with conflict notice and latest file content,
  - successful save clears dashboard cache entry for `(user_id, dashboard_name)`.

## Dashboard validation flow (2026-03-04)

- Validation core is `varro/dashboard/verify.py`.
- `validate_dashboard_url(...)` executes all `queries/*.sql` and all `@output` functions for a dashboard URL and returns a structured result (`queries`, `outputs`, `warnings`, `query_errors`, `output_errors`).
- Empty-result severity rule is URL-aware:
  - unfiltered/default filters: empty query/output is blocking (`*_errors`),
  - filtered URLs: empty query/output is warning-only.
- `ValidateDashboard(url?)` in `varro/agent/assistant.py` runs full validation with `strict_structure=True` and:
  - returns `VALIDATION_RESULT {json}` on pass/warnings,
  - raises `ModelRetry` on blocking failures.
- `Write`/`Edit` in `varro/agent/assistant.py` call `run_validation_after_write(...)` only for:
  - `/dashboard/{slug}/queries/*.sql` -> execute that single SQL (`validate_single_query`),
  - `/dashboard/{slug}/outputs.py` -> syntax compile only (`validate_outputs_syntax`),
  - `/dashboard/{slug}/dashboard.md` -> lightweight structure warnings (`validate_dashboard_structure`).
- Write-time validation never raises `ModelRetry`; it appends plain text status/warnings to the tool result.
- Snapshot remains separate (`Snapshot` does not auto-validate).
