from pathlib import Path

DIM_TABLE_DESCR_DIR = Path("/root/varro/agents/tasks/dim_table_descr")


def get_long_dim_descr_md(dim_tables: set[str]):
    return "\n".join(
        [
            open(DIM_TABLE_DESCR_DIR / f"{dim_table}.md").read()
            for dim_table in dim_tables
        ]
    )


def get_short_dim_descrs_md(dim_tables: set[str]):
    return "\n".join(
        [
            open(DIM_TABLE_DESCR_DIR / f"{dim_table}_short.md").read()
            for dim_table in dim_tables
        ]
    )


prompt_dim_table_descr = """Go through all the tables in schema dim . Each of the tables have a kode, niveau, titel column. Each table in the dim schema is a dimension table used in a star schema with fact tables and dimension tables. Each dimension table specify a hierachical grouping hierarchy, where niveau is the level of hierarchy. level 1 is the highest categories and then level 2 are sub categories to level categories and so on.
Kode is the id used for joining the dimension table to a fact table. Niveau is the levelof the hierarchy and titel is the descriptive label.
For each dimension table then you can find a markdown file with a short highlevel description of the table in /mnt/HC_Volume_103849439/mapping_tables/{table_id}/table_info_da.md

Can you through each of the tables in dim schema and for each table read the corresponding table description and then create a short/concise table description markdown that an new analyst unfamiliar with the dimension table can read to quickly get an overview of how to use the dim table. Put the markdown doc in /root/varro/agents/tasks/dim_table_descr/{table_id}.md also create a super short version that just tells what the table is and what different level signify and drop that to /root/varro/agents/tasks/dim_table_descr/{table_id}_short.md

Use sql skill to get dim schema tables. If you start reaching the limit of your context window then create an md file noting which tables you have created description md's for and then stop.

All the markdown docs describing the dimension tables should be in danish."""
