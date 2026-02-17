---
name: Dashboard Creation
description: Create, edit, and iterate on data dashboards. Use when the user wants a persistent visual analysis with charts, tables, metrics, and filters — saved as files at /dashboard/{name}/.
---

# Dashboard Creation

Create dashboards at `/dashboard/{name}/` with three required files:

```
dashboard/{name}/
├── queries/         # One .sql file per query
│   ├── regions.sql
│   └── trend.sql
├── outputs.py       # @output functions → Metric, DataFrame, or Plotly figure
└── dashboard.md     # Layout with containers and component tags
```

## queries/*.sql

One file per query. Filename (without extension) = query name.

Use `:param` for filter binding. The framework extracts params via regex — only params found in the query are bound, others get NULL.

For optional filters, use the `IS NULL OR` pattern:

```sql
SELECT
    tid, indhold as population
FROM fact.folk1a
WHERE kon = 'TOT'
  AND (:region IS NULL OR omrade = :region)
  AND (:period_from IS NULL OR tid >= :period_from)
  AND (:period_to IS NULL OR tid <= :period_to)
ORDER BY tid
```

Avoid `::` PostgreSQL casts in the same position as `:param` — the regex uses negative lookbehind to distinguish them, but keep casts away from param names to be safe.

Queries referenced by `options="query:..."` in a filter tag are **options queries** — run at page load to populate dropdowns. All others are **data queries** — run when outputs lazy-load.

## outputs.py

Functions decorated with `@output` that produce dashboard content. The names `output`, `Metric`, `px`, `go`, and `pd` are pre-injected — no imports needed for these, though explicit imports also work.

```python
@output
def population_trend(trend, filters):
    return px.line(trend, x="tid", y="population", title="Population Over Time")

@output
def total_population(trend, filters):
    current = trend["population"].iloc[-1]
    return Metric(value=current, label="Total Population", format="number")

@output
def region_table(by_region, filters):
    return by_region
```

**Dependency injection:** parameter names matching a query name receive that query's result as a DataFrame. The `filters` parameter receives all current filter values as a dict.

**Return types:**

| Return type | Rendered as | Markdown tag |
|---|---|---|
| Plotly `Figure` | Interactive chart | `<fig />` |
| `pd.DataFrame` | DaisyUI table | `<df />` |
| `Metric` | Metric card | `<metric />` |

**Metric model:**

```python
Metric(
    value=1234567,           # float, int, or str
    label="Total Revenue",
    format="number",         # "number" (K/M/B), "currency" (kr.), "percent" (%)
    change=0.12,             # optional, manually calculated
    change_label="vs last year",
)
```

## dashboard.md

Extended markdown with `:::` container syntax and self-closing component tags. Regular markdown (headers, paragraphs, lists) renders normally between components.

### Containers

| Container | Attributes | Purpose |
|---|---|---|
| `filters` | — | Wraps filter components in a form |
| `grid` | `cols` (default: 2) | CSS grid layout |
| `tabs` | — | Tab container |
| `tab` | `name` | Individual tab panel |

Nesting: one level supported (e.g. grid inside tab). `:::` always closes the most recently opened container.

### Component tags

**Output tags** — reference an `@output` function by exact name:

```markdown
<fig name="trend_chart" />
<df name="detail_table" />
<metric name="total_count" />
```

**Filter tags:**

```markdown
<filter-select name="region" label="Region" options="query:regions" default="all" />
<filter-date name="period" label="Period" default="all" />
<filter-date name="period" label="Period" default_from="2020-01-01" default_to="2025-12-31" />
<filter-checkbox name="include_pending" label="Include Pending" default=false />
```

- `filter-select`: `options="query:{query_name}"` references a single-column query. `default="all"` means no filter (NULL in SQL).
- `filter-date`: produces `{name}_from` and `{name}_to` params. `default="all"` = no date filter. Can set `default_from`/`default_to` independently.
- `filter-checkbox`: `default=true` or `default=false`. URL format: `?name=true` or `?name=false`.

### Example dashboard.md

```markdown
# Det Danske Boligmarked

::: grid cols=4
<metric name="total_boliger" />
<metric name="andel_parcelhuse" />
<metric name="andel_etageboliger" />
<metric name="prisindeks_seneste" />
:::

::: tabs

::: tab name="Boligbestand"
Udvikling i boligbestanden over tid.
<fig name="boligbestand_chart" />
<df name="boligbestand_tabel" />
:::

::: tab name="Prisudvikling"
Prisindeks for forskellige ejendomstyper (2015=100).
<fig name="prisindeks_chart" />
<df name="prisudvikling_tabel" />
:::

::: tab name="Salgsaktivitet"
<fig name="salg_antal_chart" />
<fig name="salg_priser_chart" />
:::

:::
```

## Workflow

1. **Explore data** — use SQL to understand available tables, columns, and values
2. **Write queries** — one `.sql` per query in `queries/`. Use `:param` and `IS NULL OR` for optional filters
3. **Write outputs.py** — one `@output` function per visual element. Match function names to the tags you'll use in the markdown
4. **Write dashboard.md** — arrange components with containers. Add markdown commentary to explain the data
5. **Navigate to the dashboard** — use `UpdateUrl(path="/dashboard/{name}")` to open it in the app
6. **Snapshot and inspect** — use `Snapshot()` (no arguments needed when already viewing the dashboard) to materialize outputs to disk
7. **Iterate** — read snapshot files to check results, fix issues, re-snapshot

## Snapshot

Use the `Snapshot` tool to capture the current dashboard state to disk. When already viewing a dashboard, call with no arguments:

```
Snapshot()
```

Or specify a URL with filters:

```
Snapshot(url="/dashboard/boligmarked?region=Hovedstaden")
```

Outputs are written to `/dashboard/{name}/snapshots/{query}/`:
- `dashboard.png` — full page screenshot
- `figures/{output_name}.png` — each chart as PNG
- `tables/{output_name}.parquet` — each table as parquet
- `metrics.json` — all metrics as JSON

Inspect results with `Read` on the png and json files, or check parquet files to verify data.
