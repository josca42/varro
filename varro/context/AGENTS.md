# Context Generation

Generates README.md documentation for Denmark Statistics tables.

## Modules

| File | Purpose |
|------|---------|
| `dim_table.py` | Create README.md for dimension tables from dst.dk docs + table values |
| `fact_table.py` | Create README.md for fact tables from DST API metadata |
| `subjects.py` | Create README.md for subject hierarchy with linked fact tables |
| `tools.py` | Agent tools for accessing context |
| `utils.py` | Utility functions (fuzzy matching) |
