---
name: tables
description: Explore Danmarks Statistik’s subject hierarchy and related tables
---

# Tables CLI

This CLI lets you explore Danmarks Statistik’s subject hierarchy and related tables from.

Run cli from project root in order to use python venv

```bash
python .claude/skills/tables/scripts/tables.py  
```

## Browsing subjects

```bash
python .claude/skills/tables/scripts/tables.py          # children of the root subject (DST)
python .claude/skills/tables/scripts/tables.py browse   # same as above
python .claude/skills/tables/scripts/tables.py browse "Borgere"
```

### Slash paths

Use slash-separated names to jump multiple levels in one command:

```bash
python .claude/skills/tables/scripts/tables.py browse "Borgere/Befolkning/Befolkningstal"
```

Each segment matches the description, label, or raw node id of a child under the previous segment.

### Depth control

`--depth` controls how many layers of descendants to show. `-1` means “all descendants”.

```bash
python .claude/skills/tables/scripts/tables.py browse "Borgere" --depth 2
python .claude/skills/tables/scripts/tables.py browse "Borgere/Befolkning" --depth -1
```

Indented children are subject nodes; when a leaf is reached, its tables print with descriptions.

### Breadcrumbs

`--parents` (or `--no-parents` to suppress) prints the resolved path from the root before the listing:

```bash
python .claude/skills/tables/scripts/tables.py browse "Befolkningstal" --parents
```

## Table metadata

Use `tables-info` to output XML metadata for one or more table IDs:

```bash
python .claude/skills/tables/scripts/tables.py tables-info FOLK1A FOLK1AM
```
