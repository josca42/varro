# Dashboard Framework

Markdown-driven dashboards with HTMX lazy loading.

For detailed specs see: agent/specs/dashboard_spec.md
Always consult the specs before making updates to dashboard functionality

## Architecture

```
dashboard.md  →  parser.py  →  AST  →  components.py  →  FastHTML
queries/      →  loader.py  →  dict[name, sql]    (filename = query name)
outputs.py    →  loader.py  →  dict[name, callable]
```

## Flow

1. `mount_dashboards(app, engine, "dashboards/")` scans folders
2. Each folder needs: `queries/` folder, `outputs.py`, `dashboard.md`
3. `GET /dash/{name}` renders shell with placeholder cards
4. Placeholders lazy-load via `hx_trigger="load, filtersChanged from:body"`
5. Filter changes → `/_/filters` → `HX-Replace-Url` + `HX-Trigger: filtersChanged`

## Modules

| File | Purpose |
|------|---------|
| `models.py` | `Metric` pydantic model, `@output` marker decorator |
| `parser.py` | Stack-based parser for `:::` containers and `<tag />` components |
| `loader.py` | Load folder, load queries from `queries/` folder |
| `executor.py` | Inject query results into `@output` functions by param name |
| `routes.py` | `/dash/{name}`, `/_/filters`, `/_/{type}/{output}` |
| `components.py` | Render AST to FastHTML, format metrics |

## Syntax

```markdown
::: filters
<filter-select name="region" options="query:regions" default="all" />
<filter-date name="period" />
:::

::: grid cols=2
<metric name="total_revenue" />
:::

::: tabs
::: tab name="Chart"
<fig name="trend" />
:::
:::
```

## Output Functions

```python
@output
def total_revenue(monthly_revenue, filters):  # monthly_revenue = query result
    return Metric(value=df["revenue"].sum(), label="Revenue", format="currency")

@output
def trend(monthly_revenue, filters):
    return px.line(monthly_revenue, x="month", y="revenue")  # Plotly figure
```

Return types: `Metric`, `pd.DataFrame` (table), or Plotly figure.

## Query Binding

- Params extracted via `:param_name` regex
- `filters["region"]` bound to `:region` if query uses it
- `"all"` values converted to `None` for `IS NULL OR` patterns

# UI

The dashboard should always import UI components from the ui library. If a new component is needed then it is added to the ui library and then imported from there.
