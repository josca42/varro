import networkx as nx
from varro.config import DATA_DIR
from pathlib import Path

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
        create_tables_overview_md(path, data["tables"])

    # DFS into children
    for child in children:
        walk(child, path)


def dump_subjects_overview_md(path: list[str], tables: list[str]):
    SUBJECTS_DATA_DIR / path / "subjects_overview.md"
    with open(path, "w") as f:
        f.write(create_subjects_overview_md(path, tables))
