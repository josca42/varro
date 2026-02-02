# Markdown Dashboard Framework Specification

## Overview

A framework for creating data dashboards using extended Markdown, with SQL queries for data, Python functions for outputs (charts, tables, metrics), and FastHTML + HTMX for rendering. Designed for AI authorship—minimal syntax, clear conventions, predictable behavior.

## Architecture

```
dashboards/
├── sales/
│   ├── queries/         # Folder with SQL queries (one file per query)
│   │   ├── regions.sql
│   │   ├── monthly_revenue.sql
│   │   └── top_products.sql
│   ├── outputs.py       # @output functions returning figures, tables, metrics
│   └── dashboard.md     # Layout and component references
├── inventory/
│   ├── queries/
│   │   └── ...
│   ├── outputs.py
│   └── dashboard.md
```

Dashboards are loaded from a configured directory. In this repo the app mounts dashboards from `example_dashboard_folder/` in `app/main.py`. Each subfolder containing `dashboard.md` becomes a route at `/dash/{folder_name}`. **All three items are required** (`queries/` folder, `outputs.py`, `dashboard.md`)—missing items cause an error.

Database connection is global, configured in `db.py`. **PostgreSQL is assumed.**

The framework lives in `varro/dashboard/` and is mounted by the main app.

---

## 1. queries/ folder

SQL queries organized as individual files in a `queries/` folder.

### Structure

```
queries/
├── regions.sql           # Query name: "regions"
├── monthly_revenue.sql   # Query name: "monthly_revenue"
└── top_products.sql      # Query name: "top_products"
```

### Rules

- Each `.sql` file contains a single query
- Filename (without extension) becomes the query name
- Single SELECT statement (CTEs allowed, multi-statement not allowed)
- Filter parameters use `:param_name` syntax
- Use `(:param IS NULL OR column = :param)` pattern for optional filters
- Queries referenced by `options="query:..."` in markdown are **options queries** (run at shell time)
- All other queries are **data queries** (run when outputs lazy-load)
- **Param extraction uses regex** (`r':(\w+)'`) to discover parameters
- **Only params found in the query are bound**; unused filter values are not passed
- **Orphan params** (params in SQL not matching any filter) receive NULL silently

### Example

**queries/regions.sql**
```sql
SELECT DISTINCT region FROM sales ORDER BY region;
```

**queries/monthly_revenue.sql**
```sql
SELECT
    date_trunc('month', date) as month,
    sum(revenue) as revenue
FROM sales
WHERE (:region IS NULL OR region = :region)
  AND (:period_from IS NULL OR date >= :period_from)
  AND (:period_to IS NULL OR date <= :period_to)
GROUP BY 1
ORDER BY 1;
```

**queries/top_products.sql**
```sql
SELECT
    product_name,
    sum(revenue) as revenue,
    count(*) as orders
FROM sales
WHERE (:region IS NULL OR region = :region)
  AND (:period_from IS NULL OR date >= :period_from)
  AND (:period_to IS NULL OR date <= :period_to)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
```

---

## 2. outputs.py

Python functions decorated with `@output` that return figures, tables, or metrics.

### Decorator

```python
from dashboard import output, Metric
import plotly.express as px

@output
def revenue_trend(monthly_revenue, filters):
    return px.line(monthly_revenue, x="month", y="revenue", title="Revenue Trend")
```

**`@output` is a simple marker** with no configuration arguments. Function name must **exactly match** the `name` attribute in `<fig />`, `<df />`, or `<metric />` tags.

### Dependency Injection

- Parameter names matching query names receive the query result as a pandas DataFrame
- `filters` is a special parameter containing **all** current filter values as a dict (full access)
- Framework inspects function signature and injects matching data
- **Empty query results** are passed as empty DataFrames (with correct columns); the function handles empty cases
- Functions **must always return a valid type**; returning None is not supported

### Return Types

Three return types are supported:

| Return Type | Rendered As | Markdown Tag |
|-------------|-------------|--------------|
| `pd.DataFrame` | DaisyUI table | `<df />` |
| `plotly.graph_objects.Figure` | Plotly chart | `<fig />` |
| `Metric` | Metric card | `<metric />` |

### Metric Model

```python
from pydantic import BaseModel

class Metric(BaseModel):
    value: float | int | str
    label: str
    format: str = "number"  # "number", "currency", "percent"
    change: float | None = None
    change_label: str | None = None
```

**Formatting rules:**
- `currency`: Fixed format as `kr.` (e.g., `1.2M kr.`)
- `number`: Abbreviated with K/M/B suffixes (e.g., `1.2M`)
- `percent`: Percentage with % suffix
- `change`: **Always manually calculated** by the @output function

### Example outputs.py

```python
from dashboard import output, Metric
import plotly.express as px
import plotly.graph_objects as go

@output
def total_revenue(monthly_revenue, filters):
    current = monthly_revenue["revenue"].sum()
    return Metric(
        value=current,
        label="Total Revenue",
        format="currency",
        change=0.12,
        change_label="vs last period"
    )

@output
def revenue_trend(monthly_revenue, filters):
    return px.line(
        monthly_revenue,
        x="month",
        y="revenue",
        title="Monthly Revenue"
    )

@output
def top_products_table(top_products, filters):
    # Return DataFrame directly for table rendering
    return top_products

@output
def revenue_breakdown(monthly_revenue, filters):
    # Inline pandas transform allowed
    df = monthly_revenue.copy()
    df["pct_of_total"] = df["revenue"] / df["revenue"].sum() * 100
    return df
```

---

## 3. dashboard.md

Extended Markdown with containers and component tags. **Full markdown is supported**—headers, paragraphs, lists, links, etc. render normally between components.

### Markdown Structure

```markdown
# Dashboard Title

::: filters
<filter-select name="region" label="Region" options="query:regions" default="all" />
<filter-date name="period" label="Period" default="all" />
:::

::: grid cols=2
<metric name="total_revenue" />
<metric name="total_orders" />
:::

::: tabs
::: tab name="Overview"
::: grid cols=2
<fig name="revenue_trend" />
<fig name="orders_by_category" />
:::
:::
::: tab name="Details"
<df name="top_products_table" />
:::
:::

Some markdown commentary here.

<fig name="detailed_chart" />
```

**Title handling:** H1 renders as regular markdown. No dashboard title.

---

## 4. Container Syntax

Containers use `:::` fence syntax (Docusaurus/VuePress style). **Parsed using the stack parser in `dashboard/parser.py`.**

### Available Containers

| Container | Attributes | Description |
|-----------|------------|-------------|
| `filters` | none | Wraps filter components in a form |
| `grid` | `cols` (default: 2) | CSS grid layout |
| `tabs` | none | Tab container (Alpine.js controlled) |
| `tab` | `name` | Individual tab panel |

### Nesting

Maximum one level of nesting is supported. Primary use case: grid inside tab. **Container closing is stack-based**—`:::` always closes the most recently opened container (like HTML tags).

```markdown
::: tabs
::: tab name="Charts"
::: grid cols=2
<fig name="chart1" />
<fig name="chart2" />
:::
:::
:::
```

### Container Details

**filters**
```markdown
::: filters
<filter-select ... />
<filter-date ... />
:::
```
- Renders as `<form id="filters">`
- All output placeholders use `hx-include="#filters"`
- Filter changes trigger URL update and `filtersChanged` event
- **Styling delegated to ui library** (request filter component from ui/)

**grid**
```markdown
::: grid cols=3
content
:::
```
- Renders as Tailwind CSS grid: `<div class="grid grid-cols-{cols} gap-4">`
- `cols` attribute sets column count (default: 2)
- **Fixed columns**—not responsive (always N columns regardless of screen size)

**tabs / tab**
```markdown
::: tabs
::: tab name="Overview"
content
:::
::: tab name="Details"
content
:::
:::
```
- Tab switching is client-side only via Alpine.js
- Tab state is NOT persisted in URL
- **First tab shown by default**
- `name` attribute is both the identifier and display label (**literal, no transformation**)

---

## 5. Component Tag Syntax

Component tags use self-closing HTML-style tags (e.g. `<fig name="..." />`).

### Available Tags

| Tag | Attributes | Description |
|-----|------------|-------------|
| `fig` | `name` | Plotly chart placeholder |
| `df` | `name` | DataFrame table placeholder |
| `metric` | `name` | Metric card placeholder |
| `filter-select` | `name`, `label`, `options`, `default` | Dropdown filter |
| `filter-date` | `name`, `label`, `default` or `default_from`/`default_to` | Date range filter |
| `filter-checkbox` | `name`, `label`, `default` | Boolean filter |

### Output Tags (fig, df, metric)

```markdown
<fig name="revenue_trend" />
<df name="top_products" />
<metric name="total_revenue" />
```

- `name` references a function in `outputs.py` (**exact match required**)
- Renders as a card with spinner, content lazy-loads via HTMX
- All use same HTMX pattern: `hx-get`, `hx-include="#filters"`, `hx-trigger="load, filtersChanged from:body"`
- **Placeholder styling delegated to ui library**

### Filter Tags

**filter-select**
```markdown
<filter-select name="region" label="Region" options="query:regions" default="all" />
```
- `name`: URL parameter name and SQL parameter name
- `label`: Display label
- `options`: `query:{query_name}` references a query returning **single column** (same value for display and submission)
- `default`: Default value; `"all"` is magic value meaning no filter (NULL in SQL)
- **Empty options queries render an empty dropdown**

**filter-date**
```markdown
<filter-date name="period" label="Period" default="all" />
<filter-date name="period" label="Period" default_from="2025-01-01" default_to="2025-12-31" />
```
- `name`: Base name; produces `{name}_from` and `{name}_to` URL/SQL parameters
- `label`: Display label
- `default="all"`: Both from/to are NULL (no date filter)
- `default_from`/`default_to`: Explicit default dates
- **Independent bounds**—setting just 'from' (open-ended) or just 'to' (historical cutoff) is valid
- **Date picker UI delegated to ui library**

**filter-checkbox**
```markdown
<filter-checkbox name="include_pending" label="Include Pending" default=false />
```
- `name`: URL parameter name and SQL parameter name
- `label`: Display label
- `default`: `true` or `false`
- **URL format: explicit** `?include_pending=true` or `?include_pending=false`

---

## 6. URL State Management

### Principles

- URL is the source of truth for filter state
- Default values are omitted from URL (clean URLs)
- Tab state is NOT in URL (client-side only)
- URLs are shareable, bookmarkable, back-button-friendly

### URL Structure

```
/dash/sales?region=east&period_from=2025-01-01&period_to=2025-12-31
```

### Parameter Mapping

| Filter Type | URL Parameters |
|-------------|----------------|
| filter-select | `?{name}={value}` |
| filter-date | `?{name}_from={date}&{name}_to={date}` (independent) |
| filter-checkbox | `?{name}=true` or `?{name}=false` |

### Defaults

- `default="all"` → parameter omitted from URL → NULL passed to SQL
- Explicit defaults → parameter omitted from URL when value equals default
- Server-side code always applies defaults when parameter is missing

---

## 7. HTMX Flow

### Filter Change Handling

**Debounce at source:** Filter form uses longer debounce (500ms+) to reduce rapid-fire requests when users click through options quickly. No request cancellation—debounce prevents the issue.

### Initial Page Load

```
Browser                          Server
   │                                │
   │  GET /dash/sales?region=east   │
   │  ─────────────────────────────>│
   │                                │
   │                                │  1. Parse dashboard.md
   │                                │  2. Execute options queries (fresh, no cache)
   │                                │  3. Render shell with:
   │                                │     - Populated filter form
   │                                │     - Placeholder cards with spinners
   │  <html> (AppShell)             │
   │  <─────────────────────────────│
   │                                │
   │  GET /dash/sales/_/figure/     │
   │      revenue_trend             │
   │      (hx-include sends filters)│
   │  ─────────────────────────────>│
   │                                │  4. Execute required data queries
   │                                │  5. Call @output function
   │                                │  6. Render fig/df/metric
   │  <plotly html>                 │
   │  <─────────────────────────────│
   │                                │
   │  (parallel requests for other  │
   │   figures/tables/metrics)      │
```

### Filter Change

```
Browser                          Server
   │                                │
   │  (user changes region filter)  │
   │  (debounce 500ms)              │
   │                                │
   │  GET /dash/sales/_/filters     │
   │      ?region=west              │
   │  ─────────────────────────────>│
   │                                │
   │  Response headers:             │
   │  HX-Replace-Url: /dash/sales?region=west
   │  HX-Trigger: {"filtersChanged":{}}
   │  <─────────────────────────────│
   │                                │
   │  (filtersChanged event fires)  │
   │  (all placeholders reload)     │
   │                                │
   │  GET /dash/sales/_/figure/...  │
   │      (with new filters)        │
   │  ─────────────────────────────>│
```

### HTMX Attributes on Placeholders

```html
<div class="card">
  <div
    hx-get="/dash/sales/_/figure/revenue_trend"
    hx-include="#filters"
    hx-trigger="load, filtersChanged from:body"
    hx-swap="innerHTML"
  >
    <span class="loading loading-spinner"></span>
  </div>
</div>
```

**Reload feedback uses HTMX defaults** (loading class).

### Filter Form Attributes

```html
<form id="filters"
      hx-get="/dash/sales/_/filters"
      hx-trigger="change delay:500ms"
      hx-swap="none">
  <!-- filter inputs -->
</form>
```

---

## 8. Endpoints

| Endpoint | Purpose |
|----------|---------|
| `GET /dash/{name}` | Dashboard shell (filters + placeholders); returns fragment for HTMX requests |
| `GET /dash/{name}/_/filters` | Filter sync (updates URL, triggers reload) |
| `GET /dash/{name}/_/figure/{output_name}` | Render Plotly figure |
| `GET /dash/{name}/_/table/{output_name}` | Render DataFrame table |
| `GET /dash/{name}/_/metric/{output_name}` | Render metric card |

All `/_/figure`, `/_/table`, `/_/metric` endpoints:
- Receive filter values as query parameters
- Execute required SQL queries (introspect query for params, only bind those found)
- Call the `@output` function
- Return rendered HTML fragment

**No dashboard index page** at `/dash/` for v1.

## 9. App Integration

- `/dash/{name}` is dual-mode: full AppShell for normal requests, content fragment for HTMX swaps.
- Dashboards are wrapped with `ContentNavbar` (title + quick links) in `varro/dashboard/routes.py`.

---

## 10. Rendering

### Figures (Plotly)

- Plotly JS loaded once in app headers: `Script(src="https://cdn.plot.ly/plotly-{version}.min.js")`
- Figure endpoint returns: `fig.to_html(include_plotlyjs=False, full_html=False)`
- Wrapped in `NotStr()` so FastHTML doesn't escape
- **Plotly defaults for sizing and theming**—no framework intervention

### Tables (DataFrames)

- Rendered using DaisyUI table component (NOT `df.to_html()`)
- Wrapped in `<div class="overflow-x-auto">` for horizontal scroll
- Table component from ui/ library
- **Column order from DataFrame** (author controls via pandas)
- **Raw column names** (no formatting/transformation)
- **Raw values** (no number formatting—author formats in pandas)

### Metrics

- Rendered as DaisyUI card using ui/ library components
- Shows: label, formatted value, optional change indicator
- **Change colors and styling delegated to ui library**
- Currency: `kr.` suffix
- Numbers: Abbreviated (K, M, B)

### Placeholders

- All placeholders render as card with centered spinner
- Card component from ui/ library
- Spinner: `<span class="loading loading-spinner"></span>`
- **Height and styling delegated to ui library**

---

## 10. Error Handling

**For v1, keep it simple—let things fail naturally.**

- @output exceptions: Show generic "Error loading data" message (production-safe)
- No timeout on @output functions
- No startup validation of output references
- Missing dashboard files cause error at startup
- **Full error handling deferred to later versions**

---

## 11. Database

### Connection Pattern

Simple synchronous connections per request:

```python
from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine(DATABASE_URL)

def execute_query(query: str, params: dict) -> pd.DataFrame:
    with engine.connect() as conn:
        return pd.read_sql(text(query), conn, params=params)
```

### Rules

- **Sync only**—no async database drivers
- **PostgreSQL assumed**
- **Independent connections per HTMX request** (no shared transactions)
- **Options queries re-fetch on every page load** (no caching)
- **Per-output query execution** (same query may run multiple times for different outputs)

---

## 12. Execution Flow

### Dashboard Load

1. Load dashboard folder (`queries/` folder, `outputs.py`, `dashboard.md`)—error if missing
2. Load queries from `queries/` folder → dict of named query strings (filename = query name)
3. Import `outputs.py` → dict of `@output` functions with their dependencies
4. Parse `dashboard.md` (stack parser):
   - Extract filter definitions (including `options="query:..."` references)
   - Build component tree (stack-based container closing)
5. Execute options queries (no filter params, always fresh)
6. Render shell HTML with populated filters and placeholders

### Output Render (fig/df/metric request)

1. Parse filter params from request
2. Look up `@output` function by name (exact match)
3. Inspect function signature for required queries
4. For each query: extract params via regex, bind only found params, execute
5. Call function with query results (as DataFrames) + all filter values
6. Detect return type (`isinstance` checks)
7. Render appropriate HTML fragment

---

## 13. Complete Example

### dashboards/sales/queries/regions.sql

```sql
SELECT DISTINCT region FROM sales ORDER BY region;
```

### dashboards/sales/queries/monthly_revenue.sql

```sql
SELECT
    date_trunc('month', date) as month,
    sum(revenue) as revenue
FROM sales
WHERE (:region IS NULL OR region = :region)
  AND (:period_from IS NULL OR date >= :period_from)
  AND (:period_to IS NULL OR date <= :period_to)
GROUP BY 1
ORDER BY 1;
```

### dashboards/sales/queries/top_products.sql

```sql
SELECT
    product_name,
    sum(revenue) as revenue,
    count(*) as orders
FROM sales
WHERE (:region IS NULL OR region = :region)
  AND (:period_from IS NULL OR date >= :period_from)
  AND (:period_to IS NULL OR date <= :period_to)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
```

### dashboards/sales/outputs.py

```python
from dashboard import output, Metric
import plotly.express as px

@output
def total_revenue(monthly_revenue, filters):
    total = monthly_revenue["revenue"].sum()
    return Metric(
        value=total,
        label="Total Revenue",
        format="currency"
    )

@output
def revenue_trend(monthly_revenue, filters):
    return px.line(
        monthly_revenue,
        x="month",
        y="revenue",
        title="Monthly Revenue"
    )

@output
def top_products_table(top_products, filters):
    return top_products
```

### dashboards/sales/dashboard.md

```markdown
# Sales Dashboard

::: filters
<filter-select name="region" label="Region" options="query:regions" default="all" />
<filter-date name="period" label="Period" default="all" />
:::

::: grid cols=2
<metric name="total_revenue" />
:::

::: tabs
::: tab name="Trend"
<fig name="revenue_trend" />
:::
::: tab name="Products"
<df name="top_products_table" />
:::
:::
```

---

## 14. Implementation Modules

| Module | Responsibility |
|--------|----------------|
| `dashboard/loader.py` | Load dashboard folder, load queries from queries/ folder, import outputs.py |
| `dashboard/parser.py` | Stack parser for `:::` containers and `<tag />` components |
| `dashboard/executor.py` | Execute queries, call @output functions, detect return types |
| `dashboard/routes.py` | FastHTML routes for shell, filters, figure/table/metric endpoints |
| `dashboard/models.py` | Pydantic models (`Metric`), `@output` decorator |
| `dashboard/components.py` | UI components for rendering (delegates to ui/ library) |

---

## 15. UI Library Dependencies

The following components are needed from the ui/ library:

- **Filter form container** (styling for ::: filters)
- **Date picker** (for filter-date)
- **Metric card** (with change indicator styling)
- **Table** (DaisyUI table rendering)
- **Placeholder card** (with spinner, appropriate heights)
- **Tabs** (Alpine.js tab component)

---

## 16. Future Considerations (Not in v1)

- Verbose error handling (dev mode with tracebacks)
- Query result caching
- Dashboard index page (`/dash/`)
- Collapse container
- Variable interpolation (`{{ filters.region }}`)
- Multi-database support
- Refresh intervals
- Search filter with debouncing
- Slider filter
- Hot reload for development
- CLI scaffolding
- Async database support
- Request cancellation for rapid filter changes
