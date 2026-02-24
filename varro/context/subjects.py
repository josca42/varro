import networkx as nx
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
    dump_markdown_to_file(subject_file, subject_readme)

    fact_leaf_dir = FACTS_DIR.joinpath(*subject_path)
    fact_leaf_dir.mkdir(parents=True, exist_ok=True)

    for table in tables:
        table_id = table.lower()
        if not insp.has_table(table_id, schema="fact"):
            print(f"Table {table_id} not found in database")
            continue

        table_overview_md = create_table_readme(table_id)
        dump_markdown_to_file(
            fact_leaf_dir / f"{table_id}.md", table_overview_md
        )
        dump_unique_col_vals_and_titles_to_parquet(table_id)


def get_coverage_notes(table_infos: list[dict]) -> list[str]:
    coverage: dict[str, dict[str, tuple[str, ...]]] = {}
    for table_info in table_infos:
        table_id = table_info["id"]
        for dim in table_info.get("dimensions", {}).values():
            dim_table = dim.get("dimension_table")
            level_1_values = dim.get("level_1_values")
            if not dim_table or level_1_values is None:
                continue
            coverage.setdefault(dim_table, {})[table_id] = tuple(level_1_values)

    notes = []
    for dim_table, table_sets in sorted(coverage.items()):
        if len(table_sets) < 2:
            continue
        full_level_1_values = get_dim_level_1_values(dim_table)
        grouped: dict[tuple[str, ...], list[str]] = {}
        for table_id, values in table_sets.items():
            grouped.setdefault(values, []).append(table_id)
        matches_full_coverage = all(values == full_level_1_values for values in table_sets.values())
        if len(grouped) < 2 and matches_full_coverage:
            continue

        parts = []
        for values in sorted(grouped):
            tables = ", ".join(sorted(grouped[values]))
            labels = ", ".join(values) if values else "none"
            parts.append(f"{tables}=[{labels}]")
        if full_level_1_values:
            full_labels = ", ".join(full_level_1_values)
            notes.append(
                f"- {dim_table}: full level-1 [{full_labels}]; tables {'; '.join(parts)}"
            )
        else:
            notes.append(f"- {dim_table}: level-1 coverage differs: {'; '.join(parts)}")
    return notes


def get_dim_level_1_values(dim_table: str) -> tuple[str, ...]:
    query = f"""
    SELECT DISTINCT titel
    FROM dim.{dim_table}
    WHERE niveau = 1
    ORDER BY titel
    """
    with dst_owner_engine.connect() as conn:
        return tuple(value for value in conn.exec_driver_sql(query).scalars() if value)


def create_subject_readme(tables: list[str]):
    table_infos, table_descriptions, dim_tables = [], [], set()
    for table in tables:
        table_id = table.lower()
        if not insp.has_table(table_id, schema="fact"):
            print(f"Skipping {table_id} (not in database)")
            continue

        table_info, dim_tables_linked = get_fact_table_info(table_id)
        table_infos.append(table_info)
        table_descriptions.append(format_fact_table_info(table_info))
        dim_tables.update(dim_tables_linked)

    dim_tables_descr = get_short_dim_descrs_md(dim_tables)
    fact_tables_descr = "\n".join(table_descriptions)
    coverage_notes = get_coverage_notes(table_infos)

    sections = [
        f"""<dim tables>
{dim_tables_descr}
</dim tables>
<fact tables>
{fact_tables_descr}
</fact tables>"""
    ]
    if coverage_notes:
        sections.append(
            "<coverage notes>\n"
            + "\n".join(coverage_notes)
            + "\n</coverage notes>"
        )
    return "\n".join(sections)


def create_table_readme(table: str):
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
