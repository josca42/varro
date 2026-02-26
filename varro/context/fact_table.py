import pickle
import json
from varro.config import DST_DIMENSION_LINKS_DIR, DST_METADATA_DIR
from varro.data.utils import (
    HEADER_VARS,
    normalize_column_name,
)
from varro.db.db import dst_owner_engine

TABLES_INFO_DIR = DST_METADATA_DIR / "tables_info_raw_da"
SKIP_VALUE_MAP_COLUMNS = {"tid"}
DIM_LINKS_DIR = DST_DIMENSION_LINKS_DIR
NUMERIC_DTYPES = {"integer", "smallint", "bigint", "double precision", "numeric", "real"}
TEXT_DTYPE_TOKENS = ("character", "text")


def get_distinct_values(table: str, columns: list[str]) -> dict[str, set]:
    if not columns:
        return {}

    values = {}
    with dst_owner_engine.connect() as conn:
        for col in columns:
            res = conn.exec_driver_sql(f"SELECT DISTINCT {col} FROM fact.{table}")
            values[col] = {v for v in res.scalars().all() if v is not None}
    return values


def get_dtype_family(dtype: str | None) -> str:
    dtype = (dtype or "").lower()
    if any(token in dtype for token in TEXT_DTYPE_TOKENS):
        return "text"
    if dtype in NUMERIC_DTYPES:
        return "numeric"
    return "other"


def get_join_expression(
    column: str,
    fact_dtype: str | None,
    dim_dtype: str | None,
    fact_alias: str | None = None,
    dim_alias: str | None = None,
) -> str:
    fact_column = f"{fact_alias}.{column}" if fact_alias else column
    dim_column = f"{dim_alias}.kode" if dim_alias else "kode"
    fact_family = get_dtype_family(fact_dtype)
    dim_family = get_dtype_family(dim_dtype)

    if fact_family == dim_family:
        return f"{fact_column}={dim_column}"
    if fact_family == "text":
        return f"{fact_column}={dim_column}::text"
    if dim_family == "text":
        return f"{fact_column}::text={dim_column}"
    return f"{fact_column}::text={dim_column}::text"


def get_niveau_levels(
    table: str, column: str, dim_table: str, join_expression: str
) -> list[int]:
    query = f"""
    SELECT DISTINCT n.niveau
    FROM fact.{table} f
    JOIN dim.{dim_table} n ON {join_expression}
    """

    with dst_owner_engine.connect() as conn:
        levels = sorted(conn.exec_driver_sql(query).scalars())
    return levels



def get_tid_range(table: str) -> tuple:
    column_dtypes = get_column_dtypes(table)
    tid_type = column_dtypes.get("tid", "")

    if "range" in tid_type.lower():
        query = f"""
        SELECT min(lower(tid)) AS min_tid, max(upper(tid)) AS max_tid
        FROM fact.{table}
        """
    else:
        query = f"""
        SELECT min(tid) AS min_tid, max(tid) AS max_tid
        FROM fact.{table}
        """

    with dst_owner_engine.connect() as conn:
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

    with dst_owner_engine.connect() as conn:
        rows = conn.exec_driver_sql(query).all()
    return {row.column_name: row.data_type for row in rows}


def get_raw_value_mappings(table: str):
    table_info = load_table_info(table)
    variables = table_info_variables_by_column(table_info)
    mappings = get_value_mappings(
        table=table, dim_columns=set(), variables=variables, skip_columns=set()
    )
    return mappings


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

    fact_dtypes = get_column_dtypes(table, schema="fact")
    dim_dtypes: dict[str, dict[str, str]] = {}
    dim_tables_linked = []
    dim_columns = set(dim_links.keys())
    mappings = get_value_mappings(table=table, dim_columns=dim_columns, variables=variables)
    for col, values in mappings.items():
        info["dimensions"][col] = {"values": values}

    for col, link_info in dim_links.items():
        dim_table = link_info["dimension"]
        if dim_table not in dim_dtypes:
            dim_dtypes[dim_table] = get_column_dtypes(dim_table, schema="dim")
        join_expression = get_join_expression(
            column=col,
            fact_dtype=fact_dtypes.get(col),
            dim_dtype=dim_dtypes[dim_table].get("kode"),
        )
        sql_join_expression = get_join_expression(
            column=col,
            fact_dtype=fact_dtypes.get(col),
            dim_dtype=dim_dtypes[dim_table].get("kode"),
            fact_alias="f",
            dim_alias="n",
        )
        info["dimensions"][col] = {
            "dimension_table": dim_table,
            "join": join_expression,
            "join_override": link_info.get("join_override"),
            "match_type": link_info["match_type"],
            "note": link_info.get("note"),
            "levels": get_niveau_levels(table, col, dim_table, sql_join_expression),
        }
        dim_tables_linked.append(dim_table)

    if "tid" in variables:
        min_tid, max_tid = get_tid_range(table)
        info["dimensions"]["tid"] = {
            "range": {"min": str(min_tid), "max": str(max_tid)}
        }

    return info, dim_tables_linked


def get_value_mappings(
    table: str,
    dim_columns: set[str],
    variables: dict[str, dict],
    skip_columns: set[str] = SKIP_VALUE_MAP_COLUMNS,
) -> dict[str, list[dict[str, str]]]:
    if skip_columns:
        skip_columns = skip_columns | dim_columns
    columns = [col for col in variables if col not in skip_columns]
    column_dtypes = get_column_dtypes(table)
    mappings = {}
    for col in columns:
        dtype = column_dtypes.get(col)
        values = []
        try:
            for value in variables[col]["values"]:
                if dtype in {"integer", "smallint", "bigint"}:
                    id_value = int(value["id"])
                elif dtype in {"double precision", "numeric", "real"}:
                    id_value = float(value["id"])
                else:
                    id_value = value["id"]
                values.append({"id": id_value, "text": value["text"]})
        except (ValueError, TypeError):
            values = variables[col]["values"]
        if values:
            mappings[col] = values

    return mappings


def load_table_info(table: str) -> dict:
    with open(TABLES_INFO_DIR / f"{table.upper()}.pkl", "rb") as f:
        return pickle.load(f)


def load_dim_links(table: str) -> dict[str, dict]:
    with open(DIM_LINKS_DIR / f"{table.upper()}.json", "r") as f:
        dim_links = json.load(f)
    return {
        normalize_column_name(link["column"]): {
            "dimension": link["dimension"],
            "match_type": link.get("match_type", "exact"),
            "note": link.get("note"),
            "join_override": link.get("join_override"),
        }
        for link in dim_links
    }


def table_info_variables_by_column(table_info: dict) -> dict[str, dict]:
    return {normalize_column_name(v["id"]): v for v in table_info["variables"]}


def format_fact_table_info(table_info: dict) -> str:
    dimensions = table_info.get("dimensions", {})
    table_columns = table_info.get("columns", [])
    column_details = []

    for column in table_columns:
        if column == "tid":
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
            join_expr = dimension.get("join_override") or dimension.get("join", f"{column}=kode")
            join_str = f"join dim.{dimension['dimension_table']} on {join_expr}"
            match_type = dimension.get("match_type", "exact")
            note = dimension.get("note")
            if match_type == "approx":
                if note:
                    join_str += f" [approx: {note}]"
                else:
                    join_str += " [approx]"
            levels = dimension.get("levels")
            details = [join_str]
            if levels:
                details.append(f"levels {levels}")
            column_lines.append(f"- {column}: {'; '.join(details)}")
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

    dim_tables_in_doc = sorted({
        dim.get("dimension_table")
        for dim in dimensions.values()
        if dim.get("dimension_table")
    })
    if dim_tables_in_doc:
        lines.append(f"dim docs: {', '.join(f'/dim/{dt}.md' for dt in dim_tables_in_doc)}")

    return "\n".join(lines)


def create_fact_tables_str_repr(tables: list[str] | str, overview: bool = False) -> str:
    if isinstance(tables, str):
        tables = [tables]
    func = format_fact_table_overview if overview else format_fact_table_info
    return "\n".join([func(get_fact_table_info(table)[0]) for table in tables])
