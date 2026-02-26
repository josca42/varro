# Plan: Include DB07 section-level codes (A-U) in dim.db

## Context & Discovery

### How we found this

During a playground exploration session (chat 19), we tested question 6 from the test plan: *"Sammenlign sygefravær på tværs af brancher og køn. Hvilke brancher har størst kønsforskelle?"* (Compare sickness absence across industries and gender. Which industries have the largest gender differences?)

The agent used `fact.fra022` which has an `erhverv` column linking to `dim.db` (the DB07 industry classification). The `erhverv` column contains letter codes like `A`, `B`, `C`... representing DB07 section-level industries (the most useful aggregation for high-level analysis).

**The agent wasted 10 of 17 steps** (steps 4-13) discovering and debugging why these letter codes don't join to `dim.db`:

1. Tried `JOIN dim.db ON erhverv=kode::text WHERE niveau=2` — got 10 granular sub-industries, not the 19 sections
2. Explored dim.db structure, found only numeric codes at niveaux 2-5
3. Discovered fact table contains letter codes (A-S) alongside numeric codes
4. Tried to join letter codes to dim.db — failed (kode is INTEGER, no level 1 exists)
5. Fell back to `WHERE erhverv ~ '^[A-Z]$'` regex
6. **Hardcoded all 19 DB07 section names in a CTE** to get readable labels

The final output quality was excellent, but the trajectory was terrible — 8+ wasted steps on a data gap that shouldn't exist.

### Root cause

In `varro/data/disk_to_db/dim_tables_to_db.py:20-21`:

```python
if folder.stem == "db":
    df = df[df["NIVEAU"] != 1].copy()  # Drop basic string level
```

NIVEAU 1 is explicitly filtered out before loading dim.db. This was done to enable integer conversion of the kode column in `process_kode_col()` — letter codes like 'A' can't become integers, so they were dropped entirely.

### What the raw data looks like

The raw parquet (`data/dst/mapping_tables/db/table_da.parquet`) contains a full DB07 hierarchy with 5 levels:

| SEKVENS | KODE   | NIVEAU | TITEL                                         |
|---------|--------|--------|-----------------------------------------------|
| 1       | A      | 1      | Landbrug, jagt, skovbrug og fiskeri           |
| 2       | 01     | 2      | Plante- og husdyravl, jagt og serviceydelser  |
| 3       | 01.1   | 3      | Dyrkning af etårige afgrøder                  |
| ...     | 01.11  | 4      | Dyrkning af korn, bælgfrugter...              |
| ...     | 011100 | 5      | Dyrkning af korn, bælgfrugter...              |

- NIVEAU 1: 21 letter codes A-U (sections) — **dropped**
- NIVEAU 2: 88 zero-padded 2-digit codes ('01'-'99')
- NIVEAU 3: 272 dotted codes ('01.1', '01.2', ...)
- NIVEAU 4: 615 dotted codes ('01.11', '01.12', ...)
- NIVEAU 5: 736 six-digit codes ('011100', '011200', ...)

### Current state in the database

- dim.db has INTEGER kode column with only niveaux 2-5 (1711 rows)
- No NIVEAU 1 exists at all
- fra022 has values: `['1', '2', '3', ..., '11', 'A', 'B', ..., 'S', 'TOT', 'X']`
- After fix: 29 of 32 values match (vs 10 of 32 currently)

### Scope of impact

~134 fact tables have columns (`erhverv`, `branche`, `branche07`) linking to dim.db. Checked examples:
- `hfudd16`: 8,459,294 rows with letter codes
- `ligehb11`: 480 rows with letter codes
- `aku420a`: 51 rows with letter codes
- `affald`: 0 (uses only numeric codes — unaffected)

This is the single highest-impact data gap found in trajectory analysis.

### Existing `process_kode_col` behavior

In `process_tables.py:38-50`, `process_kode_col()`:
1. Tries to convert all kode values to integers by stripping dots and casting
2. If conversion fails (letter codes present), **falls back to keeping text**
3. The NIVEAU 1 filter in `dim_tables_to_db.py` exists specifically to prevent this fallback for dim.db

So if we keep NIVEAU 1, the integer conversion will fail on 'A', and `process_kode_col` will fall back to text — which is exactly what we want, as long as we pre-normalize the numeric codes (strip dots, remove leading zeros).

---

## Implementation

### Step 1: Replace NIVEAU 1 filter with db-specific normalization

**File**: `varro/data/disk_to_db/dim_tables_to_db.py` (lines 20-21)

Replace:
```python
if folder.stem == "db":
    df = df[df["NIVEAU"] != 1].copy()  # Drop basic string level
```

With db-specific kode normalization that keeps NIVEAU 1 and normalizes numeric codes to match fact table values:
```python
if folder.stem == "db":
    def normalize_db_kode(val):
        stripped = val.replace(".", "")
        try:
            return str(int(stripped))
        except ValueError:
            return val
    df["KODE"] = df["KODE"].map(normalize_db_kode)
```

**Why this works**: Normalizes BEFORE `process_dim_table()` runs. Then `process_kode_col()` tries `astype(int)`, fails on 'A', and falls back to keeping the already-normalized text values. No changes needed to `process_tables.py`.

**Why db-specific**: 5 other dim tables (`ddu_udd`, `kn`, `nr_branche`, `nst`, `landbrugslandsdele`) also have letter codes and their linked fact tables use raw values (not normalized). Only dim.db needs this treatment because its fact tables use stripped/zero-removed codes.

**What changes in dim.db**:
- kode column type: INTEGER -> VARCHAR (text)
- NIVEAU 1 rows added: 21 entries with letter codes A-U
- NIVEAU 2+ codes: same values as before but as text ('1', '2', ... instead of 1, 2, ...)
- parent_kode: NIVEAU 2 entries now correctly point to NIVEAU 1 parents (e.g., kode='1' -> parent_kode='A')
- PK stays composite (kode, niveau) since kode values collide across levels (NIVEAU 3 kode '11' from '01.1' collides with NIVEAU 2 kode '11')

### Step 2: Drop and recreate dim.db

```bash
PGPASSWORD=... psql -h localhost -U dstowner -d dst -c "DROP TABLE IF EXISTS dim.db CASCADE;"
uv run python -m varro.data.disk_to_db.dim_tables_to_db  # or run just the db portion
```

The script checks `if insp.has_table(...)` and skips existing tables, so we must drop first.

### Step 3: Regenerate derived artifacts

```bash
# Regenerate column_values parquet for ColumnValues tool
uv run python -c "from varro.context.dim_table import dump_dim_table_values_to_parquet; dump_dim_table_values_to_parquet('db')"

# Regenerate all subject READMEs and fact table READMEs
uv run python -m varro.context.subjects
```

The READMEs auto-adapt: `get_join_expression()` produces `erhverv=kode` (both text, no cast), `get_niveau_levels()` includes niveau 1, `get_level_1_values()` returns section names directly.

### Step 4: Regenerate dim.db description docs

The `db.md` and `db_short.md` files in `data/dst/dim_table_descr/` describe the dimension structure. They need updating to reflect the new NIVEAU 1 level. This uses the AI prompt in `dim_table.py:prompt_dim_table_descr` — can be done manually or deferred.

---

## Why this is safe

- **Only dim.db changes** — the normalization is db-specific, not in the generic `process_kode_col`. Other dim tables are untouched.
- **Existing `process_kode_col` fallback already handles text kode** — `create_db_table.py:make_dimension_plan` infers VARCHAR type, uses composite PK. Proven by 13 other dim tables that already use text kode.
- **Existing SQL still works** — `kode::text` casts (text->text) are no-ops in PostgreSQL. Agent-written queries adapt via regenerated READMEs.
- **Unmatched values are expected** — TOT, X in fact tables won't join. This is pre-existing and correctly flagged as `match_type: "approx"` in dimension links.

---

## Verification

1. After recreating dim.db:
   ```sql
   -- Verify NIVEAU 1 exists with letter codes
   SELECT kode, niveau, titel FROM dim.db WHERE niveau = 1 ORDER BY kode;
   -- Should show 21 rows: A through U

   -- Verify parent_kode hierarchy works
   SELECT d.kode, d.titel, d.parent_kode, p.titel as parent_titel
   FROM dim.db d JOIN dim.db p ON d.parent_kode = p.kode AND p.niveau = 1
   WHERE d.niveau = 2 LIMIT 5;

   -- Verify fra022 join works with letter codes
   SELECT d.titel, f.kon, f.indhold
   FROM fact.fra022 f JOIN dim.db d ON f.erhverv = d.kode
   WHERE d.niveau = 1 AND f.tid = '2023-01-01' AND f.fravaer1 = '10'
     AND f.sektor = '1000' AND f.fravaer = '1100' AND f.kon IN ('1','2')
   ORDER BY d.titel, f.kon;
   ```

2. Check regenerated fra022 README shows `levels [1, 2, 3]` instead of `[2, 3]`

3. Re-run playground question: "Sammenlign sygefravær på tværs af brancher og køn" — agent should reach data in ~3 SQL queries instead of 9
