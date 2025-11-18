# Dimension table (shows only KODE|NIVEAU|TITEL)
python scripts/tables.py view nuts --type dimension --lang da --rows 12


### List all dimension tables

```bash
python scripts/tables.py list
```

Prints a comma-separated list of dimension folder names under the mapping tables directory.

---

### Dimension description

```bash
# Prints table_info.md
python scripts/tables.py describe nuts



### Save dimension links

Store your fact→dimension mappings as JSON.
**Structure:** an array of one-key objects mapping `{FACT_COLUMN: DIMENSION_TABLE_ID}`

```json
[
  {"OMRÅDE": "nuts"}
]
```

**Inline example (quote carefully):**

```bash
python scripts/tables.py save-links FOLK1A \
  --dimension-links '[{"OMRÅDE": "nuts"}]'
```

**From a file:**

```bash
cat > links.json <<'JSON'
[
  {"OMRÅDE": "nuts"}
]
JSON

python scripts/tables.py save-links FOLK1A \
  --dimension-links "$(cat links.json)"
```

This writes:

```
/mnt/HC_Volume_103849439/dimension_links/FOLK1A.json
```

Notes:

* Keys/values must be valid JSON (double quotes). Wrap the whole JSON in single quotes in your shell.
* Column names are case-sensitive and must match the fact table exactly.
* `DIMENSION_TABLE_ID` should match the dimension’s folder/id (e.g., `nuts`, `db`).

---

### Check a single fact ↔ dimension mapping

Validate that all values in a fact column exist in a dimension’s key column:

```bash
python scripts/tables.py check-links FOLK1A \
  --dim-table-id nuts \
  --fact-col OMRÅDE
```

* Success prints:
  `Values in fact column OMRÅDE are in dimension table nuts`
* On mismatch: prints the set of missing values.

**Special case:** A lone `0` mismatch is treated as a placeholder and ignored.

> Under the hood, this compares `unique(df_fact[fact_col])` against `df_dim['kode']` (dimension file must expose a `KODE` column, which is normalized to `kode` before checking).

---

## Paths & Layout

**Facts**

```
/mnt/HC_Volume_103849439/statbank_tables/{TABLE_ID}.parquet
```

**Dimensions (used by `preview` / `describe`)**

```
/mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}/table_{da|en}.parquet
/mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}/table_info_{da|en}.md
```

**Dimension links (written by `save-links`)**

```
/mnt/HC_Volume_103849439/dimension_links/{TABLE_ID}.json
```

**Dimension (used by `check-links`)**

```
/mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}.parquet
```

The checker expects a flat `{DIM_ID}.parquet` exposing columns `KODE, NIVEAU, TITEL`. If your dimensions only exist as `.../{DIM_ID}/table_{lang}.parquet`, export a flat parquet (or adapt the path).

---

## Conventions

* Dimension previews show only `KODE | NIVEAU | TITEL`.
* `KODE` is treated as the join key for validations.