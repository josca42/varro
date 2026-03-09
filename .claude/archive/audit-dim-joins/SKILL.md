---
name: audit-dim-joins
description: >
  Review and annotate fact table documentation for the AI statistician.
  Use when given a subject .md file to audit, or when asked to: review dimension joins,
  improve fact/dim documentation, add query notes to fact tables, or investigate
  join mismatches between fact and dim tables.
---

# Fact Table Documentation Review

You are reviewing fact table docs so the AI statistician (Rigsstatistikeren) can query tables efficiently. You'll be given a subject .md file listing fact tables. Go through each table, investigate its dimension joins and column values, then add practical notes directly to the fact doc. After reviewing all tables, add notes to the subject doc about when to use which table.

## Database Schema

Data is in PostgreSQL with two schemas:

**dim.{table_id}** — Dimension tables with columns: `kode` (join key), `niveau` (hierarchy level, 1=most aggregated), `titel` (label), `parent_kode` (parent in hierarchy).

**fact.{table_id}** — Fact tables with: `indhold` (the measure), `tid` (time period), and dimension columns that either join to a dim table or have inline coded values.

## Docs Structure

- `context/subjects/{path}/{leaf}.md` — Subject overview listing fact tables with IDs, descriptions, columns, time ranges
- `context/fact/{path}/{leaf}/{table_id}.md` — Per-table doc with column details, dimension joins, value mappings
- `context/dim/{table_id}.md` — Dimension table hierarchy, structure, SQL examples

The fact docs are what the AI statistician reads before writing SQL. Your notes go at the bottom of each fact doc.

## ColumnValues Tool

The AI statistician has a `ColumnValues(table, column, fuzzy_match_str?, n?, for_table?)` tool that returns unique values from precomputed parquet files in `context/column_values/`.

- For **dim tables**: `ColumnValues("nuts", "titel")` returns kode/niveau/titel. Use `for_table="folk1a"` to filter to only codes present in that fact table.
- For **fact tables**: `ColumnValues("folk1a", "kon")` returns the id/text value mapping for that column.
- `fuzzy_match_str` does fuzzy search: `ColumnValues("nuts", "titel", fuzzy_match_str="København")`.

When writing notes, think about what ColumnValues calls the statistician would need. If you discover that `for_table` filtering is essential for a particular dim join (because the dim has 500 codes but the fact table only uses 50), note that.

## Workflow

You'll receive a subject .md path. For each fact table in that subject:

1. **Read the fact doc** — `context/fact/.../{table_id}.md`
2. **Run the audit CLI** — `uv run python scripts/audit_dim_joins.py audit-table {table_id}` to get match rates and unmatched codes for dimension joins
3. **Investigate with psql** — For dimension-linked columns, use `$psql` to:
   - Test the join and see what matches/doesn't match
   - Check which hierarchy levels are in the fact table
   - Look at unmatched codes to understand if they're aggregates, use different coding, etc.
   - Try a sample query or two that the statistician would likely write
4. **Check ColumnValues** — Look at `context/column_values/{table_id}/` to see what the statistician's ColumnValues tool would return for each column. Note if any column's values are confusing or if `for_table` filtering is particularly important. This step is most valuable when a dim table has many codes (100+) and `for_table` filtering significantly reduces the set. For small dims (5-15 codes), the audit CLI and psql already cover this.
5. **Write fact doc notes** — Append a `notes:` section to the fact doc with practical guidance

If a table has no dimension links and simple inline values, it may not need notes — use your judgement. However, many tables without dim links still have tricky columns worth noting:

- **Measurement selector columns** — columns like `enhed` (unit), `saeson` (seasonal adjustment), or `arbejdstid` (measurement type) where every dimension combination is repeated for each selector value. Failing to filter these silently doubles/triples counts. These are the highest-priority notes for non-dim tables.
- **Independent category columns** — columns like `atyp` (type of atypical work: evening/night/Saturday/Sunday) where values are not mutually exclusive for a person. Summing across them is wrong. Note this clearly.
- **Rate vs. count semantics** — percentage tables (BFK/LPCT/EFK) where the values are independent rates that should never be summed.

After reviewing all tables in the subject:

6. **Write subject doc notes** — Append a `notes:` section to the subject .md file with guidance on when to use which table. The subject doc lists all fact tables — the statistician reads it first to pick a table. Your notes help them choose without reading every individual fact doc.

## What to Note in Fact Docs

Write notes that help the AI statistician go from "I need data about X" to correct SQL in as few steps as possible. Think about:

- **How to query this table** — If the table has 5 dimension columns and you need to filter all of them to avoid overcounting, say so. If `indhold` means different things depending on another column (like `enhed`), explain.
- **Dimension join gotchas** — If the join column uses a different coding scheme, if only certain hierarchy levels are present, if there are aggregate codes mixed in that aren't in the dim table.
- **Multiple hierarchy levels** — If a join column contains codes at niveaus 3 and 4, note that the statistician should filter `WHERE d.niveau = 3` or similar to avoid double-counting across hierarchy levels.
- **ColumnValues tips** — If `ColumnValues("dim_table", "titel", for_table="this_table")` is the fastest way to see what's available, or if fuzzy matching on titel is better than browsing kode values.

## What to Note in Subject Docs

After reviewing all fact tables, append `notes:` to the subject .md. This is the first doc the statistician reads when exploring a topic, so the notes should help them pick the right table:

- **Which table for which question** — If one table has regional breakdown and another doesn't, or one goes back to 1901 but another only to 2008, note that.
- **Overlapping tables** — If multiple tables cover the same data at different granularities (e.g. folk1a quarterly vs folk1am monthly vs befolk1 annual), explain the trade-offs.
- **Naming conventions** — DST tables often encode time granularity in their suffix (e.g. k=quarterly, a=annual, m=monthly). If you spot a pattern like this, document it — it helps the statistician pick the right table without reading every doc.
- **Common pitfalls** — If most tables in the subject share a gotcha (e.g. all need overcounting filters), mention it once here rather than repeating in every fact doc.

## Notes Format

Append to fact doc and subject doc files using Edit. Free-form, no rigid structure — just useful notes.

Fact doc example:
```
notes:
- omrade joins dim.nuts. Use ColumnValues("nuts", "titel", for_table="folk1a") to see the 104 regions available. niveau 1 = 5 regioner, niveau 3 = 99 kommuner. Filter d.niveau to pick your granularity.
- This table has 5 dimension columns (omrade, kon, alder, civilstand, tid). To get a simple population count, filter all non-target dimensions to their total: kon='TOT', alder='IALT', civilstand='TOT'. Forgetting any one of these inflates the sum.
- alder has 126 individual ages (0-125) plus IALT. For age groups, aggregate in SQL with CASE expressions — there's no age-group dimension.
```

Subject doc example (appended after `</fact tables>`):
```
notes:
- For current population by region/age/gender: use folk1a (quarterly, from 2008) or folk1am (monthly, from 2021). folk1a also has civilstand.
- For long historical series: befolk1 goes back to 1971 (with civilstand) or befolk2 back to 1901 (without). Neither has regional breakdown.
- ft has the longest series (1769) but only summariske tal by hovedlandsdele — very coarse.
- For population by geography below kommune level: by1/by2 (byområder), postnr1/postnr2 (postnumre), sogn1 (sogne).
- All population tables that have kon, alder, or civilstand include total rows (TOT/IALT). Always filter these to avoid overcounting.
```

## Helper CLI

```bash
# Diagnostic report for a table's dimension joins
uv run python scripts/audit_dim_joins.py audit-table <table_id>

# Audit all tables in a subject
uv run python scripts/audit_dim_joins.py audit-subject <subject_path>

# Update dimension_links JSON (for fixing join_override or match_type)
uv run python scripts/audit_dim_joins.py update-link <TABLE_ID> <COLUMN> --note "..." [--override "..."]
```
