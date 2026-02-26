import networkx as nx
from pathlib import Path
from varro.context.fact_table import (
    get_fact_table_info,
    format_fact_table_info,
    format_fact_table_overview,
    get_raw_value_mappings,
)
import pandas as pd
from typing import Callable
from varro.db.db import dst_owner_engine
from sqlalchemy import inspect
from varro.config import COLUMN_VALUES_DIR, FACTS_DIR, SUBJECTS_DIR, DST_METADATA_DIR

G = nx.read_gml(DST_METADATA_DIR / "subjects_graph_da.gml")
insp = inspect(dst_owner_engine)


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
    subject_path = [x for x in path if x != "dst"]
    if not subject_path:
        return

    subject_file = SUBJECTS_DIR.joinpath(
        *subject_path[:-1], f"{subject_path[-1]}.md"
    )
    subject_file.parent.mkdir(parents=True, exist_ok=True)

    subject_readme = create_subject_readme(tables)
    existing_notes = extract_notes(subject_file)
    if existing_notes:
        subject_readme += "\n" + existing_notes
    dump_markdown_to_file(subject_file, subject_readme)

    fact_leaf_dir = FACTS_DIR.joinpath(*subject_path)
    fact_leaf_dir.mkdir(parents=True, exist_ok=True)

    for table in tables:
        table_id = table.lower()
        if not insp.has_table(table_id, schema="fact"):
            print(f"Table {table_id} not found in database")
            continue

        table_overview_md = create_table_readme(table_id)
        fact_file = fact_leaf_dir / f"{table_id}.md"
        existing_notes = extract_notes(fact_file)
        if existing_notes:
            table_overview_md += "\n" + existing_notes
        dump_markdown_to_file(fact_file, table_overview_md)
        dump_unique_col_vals_and_titles_to_parquet(table_id)



def create_subject_readme(tables: list[str]):
    table_descriptions = []
    for table in tables:
        table_id = table.lower()
        if not insp.has_table(table_id, schema="fact"):
            print(f"Skipping {table_id} (not in database)")
            continue

        table_info, _ = get_fact_table_info(table_id)
        table_descriptions.append(format_fact_table_info(table_info))

    fact_tables_descr = "\n".join(table_descriptions)
    return f"<fact tables>\n{fact_tables_descr}\n</fact tables>"


def create_table_readme(table: str):
    table_info, _ = get_fact_table_info(table)
    return format_fact_table_overview(table_info)


def dump_unique_col_vals_and_titles_to_parquet(table: str):
    table_info = get_raw_value_mappings(table)
    table_dir = COLUMN_VALUES_DIR / table
    table_dir.mkdir(parents=True, exist_ok=True)
    for col, values in table_info.items():
        pd.DataFrame(values).to_parquet(table_dir / f"{col}.parquet")


NOTES_MARKER = "notes:"


def extract_notes(path: Path) -> str | None:
    if not path.exists():
        return None
    content = path.read_text()
    idx = content.find(NOTES_MARKER)
    if idx == -1:
        return None
    return content[idx:]


def dump_markdown_to_file(path: Path, markdown: str):
    with open(path, "w") as f:
        f.write(markdown)


if __name__ == "__main__":
    create_subjects_data()
    # copy_dim_table_docs()
    # dump_dim_table_unique_values()
