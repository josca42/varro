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
- Caches query results in-process by `(query_hash, filters_json)`.

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
- `GET /dashboard/{name}/_/filters`:
  - returns empty body with:
    - `HX-Replace-Url`
    - `HX-Trigger: {"filtersChanged": {}}`
- `GET /dashboard/{name}/_/figure/{output}`
- `GET /dashboard/{name}/_/table/{output}`
- `GET /dashboard/{name}/_/metric/{output}`

Dashboards are cached by file mtimes (`dashboard.md`, `outputs.py`, all query files).
Dashboards are discovered per-user from `DATA_DIR/user/{user_id}/dashboards/{slug}`.

## Example dashboard

- path: `mnt/user/1/dashboards/sales/`
- includes filters + metrics + tabs + figure/table outputs.

## Test coverage

- `tests/dashboard/test_parser_loader.py`
- `tests/dashboard/test_executor.py`
- `tests/dashboard/test_routes.py`
- `tests/dashboard/conftest.py`
