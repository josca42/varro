# docs_template — Documentation Structure

`mnt/docs_template/` contains all generated documentation used by the AI agent to understand and query Danmarks Statistik data.

## Directory Layout

```
docs_template/
├── subjects/          # Subject-level overviews (what tables exist in a topic)
│   ├── {root}/
│   │   ├── {mid}/
│   │   │   ├── {leaf}.md        # One file per leaf subject
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── fact/              # Per-table documentation for fact tables
│   ├── {root}/
│   │   ├── {mid}/
│   │   │   ├── {leaf}/
│   │   │   │   ├── {table_id}.md
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── ...
│   └── ...
├── dim/               # Per-table documentation for dimension tables
└── dashboards/        # Saved dashboard definitions
```

## Subject Hierarchy (3 levels)

Tables are organized into a tree with ~9 roots, ~50 mids, and ~230 leaves:

```
root (e.g. arbejde_og_indkomst)
└── mid (e.g. indkomst_og_løn)
    └── leaf (e.g. løn) → contains fact tables (lon10, lon20, ...)
```

## subjects/

Each leaf subject is a single markdown file at `subjects/{root}/{mid}/{leaf}.md`.

Contains an overview of all fact tables in that subject: linked dimension tables, table IDs, descriptions, columns, and time ranges. Used by `subject_overview()` to help the agent discover which tables are relevant for a topic.

Example: `subjects/arbejde_og_indkomst/indkomst_og_løn/løn.md`

## fact/

Each fact table has its own markdown file at `fact/{root}/{mid}/{leaf}/{table_id}.md`.

Contains detailed documentation for one table: description, measure unit, all columns with their valid values or dimension table links, and time range. Used by `table_docs()` when the agent needs column-level detail before writing SQL.

Example: `fact/arbejde_og_indkomst/indkomst_og_løn/løn/lon10.md`

## dim/

Dimension table docs (one file per dimension table). Same format as fact table docs but describes the hierarchy levels, kode/niveau/titel structure, and example values.