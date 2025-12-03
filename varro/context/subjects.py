import networkx as nx
from varro.config import DATA_DIR
from pathlib import Path
from varro.context.fact_table import (
    get_fact_table_info,
    format_fact_table_info,
    format_fact_table_overview,
    get_raw_value_mappings,
)
from varro.context.dim_table import get_short_dim_descrs_md
import pandas as pd
from typing import Callable
from varro.db.db import engine
from sqlalchemy import inspect
from varro.config import COLUMN_VALUES_DIR

G = nx.read_gml(DATA_DIR / "metadata" / "subjects_graph_da.gml")
SUBJECTS_DATA_DIR = Path.home() / "varro" / "docs" / "fact_tables"
insp = inspect(engine)


def create_subjects_data():
    walk("0", [], create_subject_data)


def walk(node: int, path: list[str], apply_function: Callable) -> None:
    data = G.nodes[node]
    # extend the path with this node's description
    path = path + [data["description"].lower().replace(" ", "_")]

    # children in a directed graph
    children = list(G.successors(node))

    # leaf with tables -> call your function
    if not children and data.get("tables"):
        apply_function(path, data["tables"])

    # DFS into children
    for child in children:
        walk(child, path, apply_function)


def create_subject_data(path: list[str], tables: list[str]):
    subject_dir = SUBJECTS_DATA_DIR.joinpath(*[x for x in path if x != "dst"])
    subject_dir.mkdir(parents=True, exist_ok=True)

    subject_overview_md = create_subject_overview_md(tables)
    dump_markdown_to_file(subject_dir / "subject_overview.md", subject_overview_md)

    tables_dir = subject_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    for table in tables:
        table_id = table.lower()
        if not insp.has_table(table_id, schema="fact"):
            print(f"Table {table_id} not found in database")
            continue

        table_overview_md = create_table_overview_md(table_id)
        dump_markdown_to_file(tables_dir / f"{table_id}.md", table_overview_md)

        table_dir = tables_dir / table_id
        table_dir.mkdir(parents=True, exist_ok=True)
        dump_unique_col_vals_and_titles_to_parquet(table_id)


def create_subject_overview_md(tables: list[str]):
    table_infos, dim_tables = [], set()
    for table in tables:
        table_id = table.lower()
        if not insp.has_table(table_id, schema="fact"):
            print(f"Skipping {table_id} (not in database)")
            continue

        table_info, dim_tables_linked = get_fact_table_info(table_id)
        table_infos.append(format_fact_table_info(table_info))
        dim_tables.update(dim_tables_linked)

    dim_tables_descr = get_short_dim_descrs_md(dim_tables)
    fact_tables_descr = "\n".join(table_infos)
    return f"""<dim tables>
{dim_tables_descr}
</dim tables>
<fact tables>
{fact_tables_descr}
</fact tables>"""


def create_table_overview_md(table: str):
    table_info, _ = get_fact_table_info(table)
    return format_fact_table_overview(table_info)


def dump_unique_col_vals_and_titles_to_parquet(table: str):
    table_info = get_raw_value_mappings(table)
    table_dir = COLUMN_VALUES_DIR / table
    table_dir.mkdir(parents=True, exist_ok=True)
    for col, values in table_info.items():
        pd.DataFrame(values).to_parquet(table_dir / f"{col}.parquet")


def dump_markdown_to_file(path: Path, markdown: str):
    with open(path, "w") as f:
        f.write(markdown)


if __name__ == "__main__":
    create_subjects_data()
