name: sql
description: Query the fact/dim schemas in Postgres from any shell
---

# sql CLI

`sql` is a thin wrapper around `psql` that already knows the warehouse DSN. Use it when you are done exploring tables via the `subjects`/`tables` skills and want to slice the loaded tables inside Postgres.

The loaders in `varro/data/disk_to_db/*` create:

- `fact.<table_id>`: processed denmark statistics fact tables (lower-case, ASCII-safe columns, `tid` parsed to dates/quarters).
- `dim.<dimension_id>`: dimension tables with the standard `kode`, `niveau`, `titel` columns. 

## Quick start

```bash
sql "\conninfo"                                   # confirm DSN
sql "\dn"                                         # list schemas (fact, dim, public)
sql "\d+ fact.folk1a"                             # describe table, comments include dim links
sql "SET search_path TO fact, dim, public; SELECT * FROM folk1a LIMIT 5;"
```

## Run ad-hoc analysis

```bash
# Fact slice
sql "SELECT tid, omrade, indhold FROM fact.folk1a WHERE kon = 1 ORDER BY tid DESC LIMIT 10;"

# Join to dimension labels (dimension tables always expose kode/niveau/titel)
sql <<'SQL'
SELECT f.tid, n.titel AS omrade, f.indhold
FROM fact.folk1a AS f
JOIN dim.nuts AS n ON f.omrade = n.kode
WHERE f.kon = 1 AND n.niveau = 2
ORDER BY f.tid DESC, n.titel
LIMIT 20;
SQL
```

Tips:

- The ingest scripts build indexes on every non-measure column, so filters on foreign keys (e.g., `omrade`, `tid`) are cheap.

## Exporting results

```bash
sql --csv -c "SELECT * FROM fact.folk1a LIMIT 100" > folk1a_sample.csv
sql -A -F $'\t' -c "SELECT kode, titel FROM dim.nuts LIMIT 20" > nuts.tsv
```

Exit codes bubble up from `psql`, so failed queries stop scripts immediately (`ON_ERROR_STOP=1`). Output respects `psql` defaults: tabular for interactive use, unaligned/no headers when piped. Use `\?` inside `sql` for the full list of meta-commands.***
