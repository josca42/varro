import networkx as nx
from varro.config import DATA_DIR

G = nx.read_gml(DATA_DIR / "metadata" / "subjects_graph_da.gml")
SUBJECTS_OVERVIEW_DIR = DATA_DIR / "metadata" / "subjects_overview"


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
    with open(DATA_DIR / "metadata" / "subjects_overview.md", "w") as f:
        f.write(create_subjects_overview_md(path, tables))


def create_subjects_overview_md(path: list[str], tables: list[str]) -> str:
    return "\n".join([f"- {table}" for table in tables])


dump_subjects_overview_md([], ["folk1a"])
