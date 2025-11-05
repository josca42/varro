---
name: sql
description: Interact with postgres database. Execute queries using bash terminal.
---

# `sql` — quick usage

Run Postgres from any Bash shell/script.

## Basics

```bash
sql "SELECT now();"                # one-liner
sql -f schema.sql                  # execute file
cat query.sql | sql                # pipe
sql <<'SQL'                        # here-doc
BEGIN; CREATE TABLE t(id int); COMMIT;
SQL
```

## Switch database/profile

```bash
PGSERVICE=analytics sql "SELECT version();"
# (Default profile is used if PGSERVICE is unset.)
```

## Introspection & sanity checks

```bash
sql "\conninfo"                    # what am I connected to?
sql "\dt public.*"                 # list tables
sql "\d+ public.my_table"          # describe table
```

## Output modes

```bash
# Human (TTY): pretty table with headers (default)
# Script (pipes): headerless, unaligned (default)
sql --csv -c "SELECT * FROM my_table LIMIT 5"      > out.csv   # CSV
sql -A -t -F $'\t' -c "SELECT * FROM my_table"     > out.tsv   # TSV
```

## Import / export data

```bash
sql -c "\copy public.my_table FROM 'in.csv'  csv header"       # import
sql -c "\copy (SELECT * FROM public.my_table) TO 'out.csv' csv header"  # export
```

## Variables & transactions

```bash
sql -v n=10 -c "SELECT generate_series(1,:n);"
sql <<'SQL'
BEGIN;
-- your statements
COMMIT;
SQL
```

## Behavior

* Exits non-zero on first SQL error (`ON_ERROR_STOP=1`).
* No pager; suitable for cron/systemd/CI.
