---
name: tables
description: Preview StatBank fact/dimension Parquet tables and read dimension descriptions
---

# tables CLI

Small utilities for inspecting cloned StatBank data:

- **preview** a fact or dimension parquet (first *n* rows)
- **schema** to list columns and dtypes
- **describe** to print the markdown description for a dimension
- **path** to show which parquet path will be used


```bash
python scripts/tables.py --help
````

## Commands

### Preview rows

```bash
# Fact table
python scripts/tables.py preview FOLK1A --type fact --rows 15
python scripts/tables.py preview amt_kom --type dimension --rows 12
```

### Show schema (columns & dtypes)

```bash
python scripts/tables.py schema FOLK1A --type fact
python scripts/tables.py schema amt_kom --type dimension --lang da
```

### Dimension description

```bash
# Prints table_info_da.md with first & last line removed
python scripts/tables.py describe amt_kom
```

### Show underlying parquet path

```bash
python scripts/tables.py path FOLK1A --type fact
python scripts/tables.py path amt_kom --type dimension --lang da
```

### List all dimension tables

```bash
python scripts/tables.py list
```

## Notes

* Facts are loaded from:

  ```
  /mnt/HC_Volume_103849439/statbank_tables/{TABLE_ID}.parquet
  ```

* Dimensions are loaded from:

  ```
  /mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}/table_{da|en}.parquet
  /mnt/HC_Volume_103849439/mapping_tables/{DIM_ID}/table_info_{da|en}.md
  ```

* Previews are pipe-separated (`|`) for copy-paste friendly output.