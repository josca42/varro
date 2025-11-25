import networkx as nx
from varro.config import DATA_DIR
from pathlib import Path
from varro.context.fact_table import (
    get_fact_table_info,
    format_fact_table_info,
    format_fact_table_overview,
    get_raw_value_mappings,
)
import pandas as pd

G = nx.read_gml(DATA_DIR / "metadata" / "subjects_graph_da.gml")
SUBJECTS_DATA_DIR = Path.home() / "subjects"


def walk(node: int, path: list[str]) -> None:
    data = G.nodes[node]
    # extend the path with this node's description
    path = path + [data["description"]]

    # children in a directed graph
    children = list(G.successors(node))

    # leaf with tables -> call your function
    if not children and data.get("tables"):
        create_subject_data(path, data["tables"])

    # DFS into children
    for child in children:
        walk(child, path)


def create_subject_data(path: list[str], tables: list[str]):
    subject_dir = SUBJECTS_DATA_DIR.joinpath(*path)
    subject_dir.mkdir(parents=True, exist_ok=True)

    subject_overview_md = create_subject_overview_md(tables)
    dump_markdown_to_file(subject_dir / "subjects_overview.md", subject_overview_md)

    tables_dir = subject_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    for table in tables:
        table_id = table.lower()
        table_overview_md = create_table_overview_md(table_id)
        dump_markdown_to_file(tables_dir / f"{table_id}.md", table_overview_md)

        table_dir = tables_dir / table_id
        table_dir.mkdir(parents=True, exist_ok=True)
        dump_unique_col_vals_and_titles_to_csv(table_dir, table_id)


def create_subject_overview_md(tables: list[str]):
    table_infos = []
    for table in tables:
        table_info = get_fact_table_info(table.lower())
        table_infos.append(format_fact_table_info(table_info))
    return "\n".join(table_infos)


def create_table_overview_md(table: str):
    table_info = get_fact_table_info(table)
    return format_fact_table_overview(table_info)


def dump_unique_col_vals_and_titles_to_csv(table_dir: Path, table: str):
    table_info = get_raw_value_mappings(table)
    for col, values in table_info.items():
        pd.DataFrame(values).to_csv(table_dir / f"{col}.csv", sep="|", index=False)


def dump_markdown_to_file(path: Path, markdown: str):
    with open(path, "w") as f:
        f.write(markdown)
