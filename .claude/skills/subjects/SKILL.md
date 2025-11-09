---
name: subjects
description: Explore Danmarks Statistik’s subject hierarchy and related tables
---

# subjects CLI

This CLI lets you explore Danmarks Statistik’s subject hierarchy and related tables. Only fact tables are included in the subject hierarchy

```bash
python scripts/subjects.py  
```

## Browsing subjects

```bash
python scripts/subjects.py          # children of the root subject (DST)
python scripts/subjects.py browse   # same as above
python scripts/subjects.py browse "Borgere"
```

### Slash paths

Use slash-separated names to jump multiple levels in one command:

```bash
python scripts/subjects.py browse "Borgere/Befolkning/Befolkningstal"
```

Each segment matches the description, label, or raw node id of a child under the previous segment.

### Depth control

`--depth` controls how many layers of descendants to show. `-1` means “all descendants”.

```bash
python scripts/subjects.py browse "Borgere" --depth 2
python scripts/subjects.py browse "Borgere/Befolkning" --depth -1
```

Indented children are subject nodes; when a leaf is reached, its subjects print with descriptions.

### Breadcrumbs

`--parents` (or `--no-parents` to suppress) prints the resolved path from the root before the listing:

```bash
python scripts/subjects.py browse "Befolkningstal" --parents
```

## Table metadata

Use `tables-info` to output XML metadata for one or more table IDs.

```bash
python scripts/subjects.py tables-info FOLK1A FOLK1AM
```

Use `--verbose` og `-v` to get all metadata for a table id as json. Much more verbose. Usually prefer not to use. Only works with a single table id

```bash
python scripts/subjects.py tables-info FOLK1A -v
```