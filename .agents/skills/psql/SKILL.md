---
name: psql
description: Query the fact/dim schemas in Postgres using psql
---

# psql CLI

psql is already connected to the correct database, when used in the shell. Connection info have been stored in environment variables so it automatically connects.


<database_schema>
Data is stored in PostgreSQL with two schemas:
- **dim.{table_id}** — Dimension tables (hierarchical groupings)
- **fact.{table_id}** — Fact tables (measurements and statistics)

### Dimension Tables
Store hierarchical groupings (regions, industries, education levels, etc.) with exactly 3 columns:

| Column | Description |
|--------|-------------|
| kode | Unique identifier (join key) |
| niveau | Hierarchy level (1 = most aggregated, higher = finer detail) |
| titel | Human-readable label |

Example hierarchy: niveau=1 "Regioner" → niveau=2 "Landsdele" → niveau=3 individual municipalities.

### Fact Tables
Contain statistical measurements with these column patterns:
- **indhold** — The measure/value (always present)
- **tid** — Time period (usually present)
- **Dimension columns** — Either:
  - Linked to dim table: `branche` → `JOIN dim.branche ON branche=kode`
  - Inline categorical: `køn` with values `['M', 'K']` (no join needed)

### Join Pattern
```sql
SELECT f.indhold, d.titel
FROM fact.{table_id} f
JOIN dim.{dim_table} d ON f.{column} = d.kode
```
</database_schema>
