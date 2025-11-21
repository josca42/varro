import pickle
import json
from varro.config import DATA_DIR
from varro.data.utils import (
    HEADER_VARS,
    create_table_info_dict,
    normalize_column_name,
)
from varro.db.db import engine

TABLES_INFO_DIR = DATA_DIR / "metadata" / "tables_info_raw_da"
SKIP_VALUE_MAP_COLUMNS = {"tid", "alder"}
DIM_LINKS_DIR = DATA_DIR / "dimension_links"


def get_distinct_values(table: str, columns: list[str]) -> dict[str, set]:
    if not columns:
        return {}

    values = {}
    with engine.connect() as conn:
        for col in columns:
            res = conn.exec_driver_sql(f"SELECT DISTINCT {col} FROM fact.{table}")
            values[col] = {v for v in res.scalars().all() if v is not None}
    return values


def get_niveau_levels(table: str, column: str, dim_table: str) -> list[int]:
    query = f"""
    SELECT DISTINCT n.niveau
    FROM fact.{table} f
    JOIN dim.{dim_table} n ON f.{column}::text = n.kode::text
    """

    with engine.connect() as conn:
        levels = sorted(conn.exec_driver_sql(query).scalars())
    return levels


def get_tid_range(table: str) -> tuple:
    query = f"""
    SELECT min(tid) AS min_tid, max(tid) AS max_tid
    FROM fact.{table}
    """

    with engine.connect() as conn:
        min_tid, max_tid = conn.exec_driver_sql(query).one()
    return min_tid, max_tid


def get_column_dtypes(table: str, schema: str = "fact"):
    query = f"""
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_schema = '{schema}'
      AND table_name   = '{table}'
    ORDER BY ordinal_position
    """

    with engine.connect() as conn:
        rows = conn.exec_driver_sql(query).all()
    return {row.column_name: row.data_type for row in rows}


def get_fact_table_info(table: str, raw: bool = False) -> dict:
    table_info = load_table_info(table)
    if raw:
        return table_info

    table_info["id"] = table_info["id"].lower()
    dim_links = load_dim_links(table)
    variables = table_info_variables_by_column(table_info)

    info = {key: table_info[key] for key in HEADER_VARS}
    info["columns"] = list(variables.keys())
    info["dimensions"] = {}

    mappings = get_value_mappings(table=table, dim_links=dim_links, variables=variables)
    for col, values in mappings.items():
        info["dimensions"][col] = {"values": values}

    for col, dim_table in dim_links.items():
        info["dimensions"][col] = {
            "dimension_table": dim_table,
            "levels": get_niveau_levels(table, col, dim_table),
        }

    if "tid" in variables:
        min_tid, max_tid = get_tid_range(table)
        info["dimensions"]["tid"] = {
            "range": {"min": str(min_tid), "max": str(max_tid)}
        }

    return info


def get_value_mappings(
    table: str,
    dim_links: dict[str, str],
    variables: dict[str, dict],
) -> dict[str, list[dict[str, str]]]:
    skip_columns = SKIP_VALUE_MAP_COLUMNS | set(dim_links)
    columns = [col for col in variables if col not in skip_columns]
    present_values = get_distinct_values(table, columns)
    mappings = {}
    for col in columns:
        present_ids = {str(v) for v in present_values.get(col, set())}
        if not present_ids:
            continue

        values = [
            {"id": value["id"], "text": value["text"]}
            for value in variables[col]["values"]
            if str(value["id"]) in present_ids
        ]
        if values:
            mappings[col] = values

    return mappings


def load_table_info(table: str) -> dict:
    with open(TABLES_INFO_DIR / f"{table.upper()}.pkl", "rb") as f:
        return pickle.load(f)


def load_dim_links(table: str) -> dict[str, str]:
    with open(DIM_LINKS_DIR / f"{table.upper()}.json", "r") as f:
        dim_links = json.load(f)
    return {
        normalize_column_name(link["column"]): link["dimension"] for link in dim_links
    }


def table_info_variables_by_column(table_info: dict) -> dict[str, dict]:
    return {normalize_column_name(v["id"]): v for v in table_info["variables"]}


def format_fact_table_info(table_info: dict) -> str:
    dimensions = table_info.get("dimensions", {})
    table_columns = table_info.get("columns", [])
    column_details = []

    for column in table_columns:
        dimension = dimensions.get(column, {})
        dim_table = dimension.get("dimension_table")
        levels = dimension.get("levels")

        if dim_table:
            suffix = f" ({dim_table} lvl {levels})" if levels else f" ({dim_table})"
            column_details.append(f"{column}{suffix}")
        elif column == "tid":
            column_details.append("tid (time)")
        else:
            column_details.append(column)

    unit = table_info.get("unit")
    if unit:
        column_details.append(f"indhold (unit {unit})")

    lines = [
        f"id: {table_info.get('id', '')}",
        f"description: {table_info.get('description', '')}",
        f"columns: {', '.join(column_details)}",
    ]

    if "tid" in table_columns:
        tid_range = dimensions.get("tid", {}).get("range")
        if tid_range:
            lines.append(
                f"tid range: {tid_range.get('min', '')} to {tid_range.get('max', '')}"
            )

    table_str = "\n".join(lines)
    return f"<table>\n{table_str}\n</table>"


def format_fact_table_overview(table_info: dict) -> str:
    dimensions = table_info.get("dimensions", {})
    columns = table_info.get("columns", [])
    lines = [f"table: fact.{table_info.get('id', '')}"]

    description = table_info.get("description")
    if description:
        lines.append(f"description: {description}")

    unit = table_info.get("unit")
    if unit:
        lines.append(f"measure: indhold (unit {unit})")

    column_lines = []
    for column in columns:
        dimension = dimensions.get(column, {})

        if "dimension_table" in dimension:
            levels = dimension.get("levels")
            level_text = f"; levels {levels}" if levels else ""
            column_lines.append(
                f"- {column}: join dim.{dimension['dimension_table']} on {column}=kode{level_text}"
            )
        elif "values" in dimension:
            if len(dimension["values"]) > 20:
                pairs = ", ".join(
                    f"{v.get('id', '')}={v.get('text', '')}"
                    for v in dimension["values"][:5]
                )
                pairs += " ... " + ", ".join(
                    f"{v.get('id', '')}={v.get('text', '')}"
                    for v in dimension["values"][-5:]
                )
            else:
                pairs = ", ".join(
                    f"{v.get('id', '')}={v.get('text', '')}"
                    for v in dimension["values"]
                )
            column_lines.append(f"- {column}: values [{pairs}]")
        elif column == "tid":
            range_info = dimension.get("range")
            if range_info:
                column_lines.append(
                    f"- {column}: date range {range_info.get('min', '')} to {range_info.get('max', '')}"
                )
            else:
                column_lines.append(f"- {column}")
        else:
            column_lines.append(f"- {column}")

    if column_lines:
        lines.append("columns:")
        lines.extend(column_lines)

    return "\n".join(lines)


def create_fact_tables_str_repr(tables: list[str] | str, overview: bool = False) -> str:
    if isinstance(tables, str):
        tables = [tables]
    func = format_fact_table_overview if overview else format_fact_table_info
    return "\n".join([func(get_fact_table_info(table)) for table in tables])
