## Dimension-linking helpers

Use these commands when you map fact-table columns to their dimension tables.

### Fact tables (context)

Preview the raw or DB-ready fact data and pull official metadata with the updated tables skill:

```bash
python .claude/skills/tables/scripts/tables.py view FOLK1A --rows 15
python .claude/skills/tables/scripts/tables.py view FOLK1A --db-format   # processed layout
python .claude/skills/tables/scripts/tables.py info FOLK1A               # XML metadata
```

All fact tables ultimately land in Postgres under the `fact` schema with lower-case/ASCII column names and coded values.

### Dimension tables

The CLI in this folder exposes the dimension-specific actions:

```bash
python varro/data/fact_col_to_dim_table/create_dimension_links.py view nuts --rows 12
python varro/data/fact_col_to_dim_table/create_dimension_links.py view nuts --db-format
python varro/data/fact_col_to_dim_table/create_dimension_links.py list
python varro/data/fact_col_to_dim_table/create_dimension_links.py describe nuts
```

`view` shows the `KODE | NIVEAU | TITEL` columns (optionally normalized to the DB schema), `list` enumerates every mapping table, and `describe` prints the trimmed `table_info_da.md`.

### Save links

Persist the mapping you discover as JSON:

```bash
python varro/data/fact_col_to_dim_table/create_dimension_links.py save-links FOLK1A \
  --dimension-links '[{"OMRÅDE": "nuts"}]'
```

Or load from a local file:

```bash
python varro/data/fact_col_to_dim_table/create_dimension_links.py save-links FOLK1A \
  --dimension-links "$(cat links.json)"
```

Files are written to `/mnt/HC_Volume_103849439/dimension_links/{TABLE_ID}.json`. Keys must match the fact column names (pre-processing), and values must match the dimension folder name (`nuts`, `db`, …).

### Validate a link

Check whether every value in a fact column exists in the dimension’s `KODE` column:

```bash
python varro/data/fact_col_to_dim_table/create_dimension_links.py check-links FOLK1A \
  --dim-table-id nuts \
  --fact-col OMRÅDE
```

Success prints a confirmation message; otherwise you get the missing codes (a lone `0` is treated as a placeholder and ignored). The checker loads `/statbank_tables/{FACT}.parquet` and `/mapping_tables/{DIM}/table_da.parquet`, so make sure those files exist before running it.

### Paths & conventions

- Facts: `/mnt/HC_Volume_103849439/statbank_tables/{TABLE_ID}.parquet`
- Dimensions: `/mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}/table_da.parquet`
- Dimension metadata: `/mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}/table_info_{da|en}.md`
- Dimension links JSON: `/mnt/HC_Volume_103849439/dimension_links/{TABLE_ID}.json`

Dimension previews only show `KODE | NIVEAU | TITEL`, and `KODE` is always the join key you should validate against.
