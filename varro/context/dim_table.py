import shutil
import pandas as pd
from varro.db.db import dst_owner_engine
from varro.config import COLUMN_VALUES_DIR, DIMS_DIR, DIM_TABLE_DESCR_DIR


def get_long_dim_descr_md(dim_tables: set[str]):
    return "\n".join(
        [
            open(DIM_TABLE_DESCR_DIR / f"{dim_table}.md").read()
            for dim_table in dim_tables
        ]
    )


def get_short_dim_descrs_md(dim_tables: set[str]):
    return "\n".join(_format_short_dim(dt) for dt in dim_tables)


def _format_short_dim(dim_table: str) -> str:
    lines = open(DIM_TABLE_DESCR_DIR / f"{dim_table}_short.md").read().strip().splitlines()
    # skip header line and blank line, first body line is description, rest is niveaux
    body = [l for l in lines[1:] if l.strip()]
    description = body[0] if body else ""
    niveaux = "\n".join(body[1:])
    parts = [f"id: {dim_table}", f"description: {description}"]
    if niveaux:
        parts.append(niveaux)
    return f"<table>\n{chr(10).join(parts)}\n</table>"


def copy_dim_table_docs():
    source_dir = DIM_TABLE_DESCR_DIR
    dest_dir = DIMS_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)
    for md_file in source_dir.glob("*.md"):
        if "_short" not in md_file.stem:
            shutil.copy2(md_file, dest_dir / md_file.name)


def dump_dim_table_unique_values():
    """
    For each dimension table markdown file in dims,
    create a folder and store unique (kode, niveau, titel, parent_kode) combinations as parquet.
    """
    for md_file in DIMS_DIR.glob("*.md"):
        table_name = md_file.stem
        dump_dim_table_values_to_parquet(table_name)


def dump_dim_table_values_to_parquet(table_name: str):
    """
    Query unique (kode, niveau, titel, parent_kode) combinations from dim.{table_name}
    and save to parquet file.
    """
    query = f"""
    SELECT DISTINCT kode, niveau, titel, parent_kode
    FROM dim.{table_name}
    ORDER BY niveau, kode, parent_kode
    """

    with dst_owner_engine.connect() as conn:
        df = pd.read_sql_query(query, conn)

    output_file = COLUMN_VALUES_DIR / f"{table_name}.parquet"
    df.to_parquet(output_file, index=False)
    print(f"Saved {len(df)} rows to {output_file}")


prompt_dim_table_descr = """Go through all the tables in schema dim. Each table has columns: kode, niveau, titel, parent_kode. These are dimension tables in a star schema. Each dimension table defines a hierarchical grouping where niveau is the hierarchy level (1 = most aggregated, higher = finer detail). parent_kode links each row to its direct parent and is NULL at the root level (niveau 1).

For each dimension table you can find a source description in data/dst/mapping_tables/{table_id}/table_info_da.md

For each table, create two markdown files:

### Full doc: data/dst/dim_table_descr/{table_id}.md

Structure (follow this template exactly):

1. **Title line**: `# {Descriptive name} ({table_id})`
2. **Description**: 1-2 sentences about what the classification covers and its context (standard, origin).
3. **Struktur table**: Niveau | Beskrivelse | Antal kategorier
4. **Niveau 1 table**: All codes and titles at the top level. For tables with few niveau 2 categories (<15), also show niveau 2.
5. **Hierarki-eksempel** (for tables with >1 niveau): Show 3-4 example rows as a table with columns: kode | niveau | titel | parent_kode. Pick one branch that shows a path from root to leaf so the reader can see how parent_kode chains work. Query the actual data to get real examples.
6. **Brug section**: Two SQL examples:
   - Basic join: `SELECT f.indhold, d.titel FROM fact.<tabel> f JOIN dim.{table_id} d ON f.{col} = d.kode WHERE d.niveau = 1`
   - **Aggregation via parent_kode** (only for tables with >1 niveau): Show how to go from the finest level to the coarsest by chaining parent_kode joins. For a 3-level table:
     ```sql
     SELECT r.titel, SUM(f.indhold)
     FROM fact.<tabel> f
     JOIN dim.{table_id} detail ON f.{col} = detail.kode AND detail.niveau = 3
     JOIN dim.{table_id} mid ON mid.kode = detail.parent_kode AND mid.niveau = 2
     JOIN dim.{table_id} top ON top.kode = mid.parent_kode AND top.niveau = 1
     GROUP BY r.titel
     ```
     Adjust the number of joins to match the actual number of levels. This is the most important SQL pattern — it's how analysts aggregate fine-grained fact data to higher levels.
7. **Cross-references**: If related dim tables exist (e.g. ddu_udd vs ddu_audd), note the relationship briefly.

### Short doc: data/dst/dim_table_descr/{table_id}_short.md

Format (keep to ~5-8 lines):
```
# {Descriptive name} ({table_id})

{One sentence description}

- **Niveau 1:** {Label} ({count}, fx {2-3 example titles})
- **Niveau 2:** {Label} ({count})
...
- **parent_kode:** peger på direkte forældreniveau (NULL for topniveau). Brug parent_kode-joins til at aggregere fra lavere til højere niveau.
```

### Important notes
- Use the psql skill to query dim schema tables and get real data for examples.
- All docs should be in Danish.
- If you start reaching context window limits, note which tables are done and stop."""

if __name__ == "__main__":
    copy_dim_table_docs()
    dump_dim_table_unique_values()
