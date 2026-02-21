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
python varro/data/fact_col_to_dim_table/dimension_links_cli.py view nuts --rows 12
python varro/data/fact_col_to_dim_table/dimension_links_cli.py view nuts --db-format
python varro/data/fact_col_to_dim_table/dimension_links_cli.py list
python varro/data/fact_col_to_dim_table/dimension_links_cli.py describe nuts
```

`view` shows the `KODE | NIVEAU | TITEL` columns (optionally normalized to the DB schema), `list` enumerates every mapping table, and `describe` prints the trimmed `table_info_da.md`.

### Save links

Persist the mapping you discover as JSON:

```bash
python varro/data/fact_col_to_dim_table/dimension_links_cli.py save-links FOLK1A \
  --dimension-links '[{"column": "OMRÅDE", "dimension": "nuts", "match_type": "exact"}]'
```

Or load from a local file:

```bash
python varro/data/fact_col_to_dim_table/dimension_links_cli.py save-links FOLK1A \
  --dimension-links "$(cat links.json)"
```

Files are written to `data/dst/dimension_links/{TABLE_ID}.json`. Each link object must include:

- `column`: fact column name (pre-processing)
- `dimension`: dimension folder name (`nuts`, `db`, …)
- `match_type`: `"exact"` if codes align and can be enforced as a foreign key, otherwise `"approx"` for a soft/semantic link
- optional `note` for clarifying any quirks

### Validate a link

Check whether every value in a fact column exists in the dimension’s `KODE` column:

```bash
python varro/data/fact_col_to_dim_table/dimension_links_cli.py check-links FOLK1A \
  --dim-table-id nuts \
  --fact-col OMRÅDE
```

Success prints a confirmation message; otherwise you get the missing codes (a lone `0` is treated as a placeholder and ignored). If real differences show up, save the link anyway but set `"match_type": "approx"`. The checker loads `data/dst/statbank_tables/{FACT}.parquet` and `data/dst/mapping_tables/{DIM}/table_da.parquet`, so make sure those files exist before running it.

### Paths & conventions

- Facts: `data/dst/statbank_tables/{TABLE_ID}.parquet`
- Dimensions: `data/dst/mapping_tables/{DIM_ID}/table_da.parquet`
- Dimension metadata: `data/dst/mapping_tables/{DIM_ID}/table_info_da.md`
- Dimension links JSON: `data/dst/dimension_links/{TABLE_ID}.json`

Dimension previews only show `KODE | NIVEAU | TITEL`, and `KODE` is always the join key you should validate against.
