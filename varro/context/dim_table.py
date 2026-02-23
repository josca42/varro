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


prompt_dim_table_descr = """Go through all the tables in schema dim . Each of the tables have a kode, niveau, titel, parent_kode column. Each table in the dim schema is a dimension table used in a star schema with fact tables and dimension tables. Each dimension table specify a hierachical grouping hierarchy, where niveau is the level of hierarchy. level 1 is the highest categories and then level 2 are sub categories to level categories and so on.
Kode is the id used for joining the dimension table to a fact table. Niveau is the level of the hierarchy and titel is the descriptive label. parent_kode links each row to its direct parent in the hierarchy and is null at the root level.
For each dimension table then you can find a markdown file with a short highlevel description of the table in data/dst/mapping_tables/{table_id}/table_info_da.md

Can you go through each of the tables in dim schema and for each table read the corresponding table description and then create a short/concise table description markdown that an new analyst unfamiliar with the dimension table can read to quickly get an overview of how to use the dim table. Put the markdown doc in data/dst/dim_table_descr/{table_id}.md also create a super short version that just tells what the table is and what different level signify and dump that to data/dst/dim_table_descr/{table_id}_short.md

Use the psql skill to get dim schema tables. If you start reaching the limit of your context window then create an md file noting which tables you have created description md's for and then stop.

All the markdown docs describing the dimension tables should be in danish."""

if __name__ == "__main__":
    copy_dim_table_docs()
    dump_dim_table_unique_values()
