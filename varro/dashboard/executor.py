"""dashboard.executor

Execute SQL queries and call @output functions.
"""

from __future__ import annotations

import inspect
from typing import Any, Literal

import pandas as pd
from sqlalchemy import text, bindparam, String, Date
from sqlalchemy.engine import Engine

from .loader import Dashboard, extract_params
from .models import Metric


OutputType = Literal["figure", "table", "metric"]


def _infer_param_type(name: str):
    """Infer SQLAlchemy type from parameter name."""
    if "date" in name or "from" in name or "to" in name:
        return Date
    return String


def execute_query(query: str, filters: dict[str, Any], engine: Engine) -> pd.DataFrame:
    """Execute a SQL query with filter parameters.

    Only binds parameters that exist in the query.
    'all' values are converted to None (for IS NULL pattern).
    Uses typed bindparams so PostgreSQL can handle NULL values.
    """
    params_needed = extract_params(query)

    # Build params dict, converting 'all' to None
    bound: dict[str, Any] = {}
    for param in params_needed:
        value = filters.get(param)
        bound[param] = None if value == "all" or value is None else value

    # Create typed bindparams for NULL handling
    stmt = text(query)
    for param in params_needed:
        stmt = stmt.bindparams(bindparam(param, type_=_infer_param_type(param)))

    with engine.connect() as conn:
        return pd.read_sql(stmt, conn, params=bound)


def execute_options_query(
    dash: Dashboard, filter_def: Any, engine: Engine
) -> list[str]:
    """Execute an options query for a select filter.

    Returns a list of option values from the first column.
    """
    options_attr = filter_def.attrs.get("options", "")
    if not options_attr.startswith("query:"):
        return []

    query_name = options_attr[6:]  # Remove "query:" prefix
    if query_name not in dash.queries:
        return []

    query = dash.queries[query_name]
    # Options queries don't receive filter params
    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)

    if df.empty:
        return []

    # Return first column values as strings
    return df.iloc[:, 0].astype(str).tolist()


def detect_output_type(result: Any) -> OutputType:
    """Detect the type of an output result."""
    if isinstance(result, pd.DataFrame):
        return "table"
    if isinstance(result, Metric):
        return "metric"
    if hasattr(result, "to_html"):  # Plotly figure
        return "figure"
    raise ValueError(f"Unknown output type: {type(result)}")


def execute_output(
    dash: Dashboard,
    output_name: str,
    filters: dict[str, Any],
    engine: Engine,
) -> tuple[OutputType, Any]:
    """Execute an @output function.

    Returns (type, result).
    """
    if output_name not in dash.outputs:
        raise ValueError(f"Unknown output: {output_name}")

    fn = dash.outputs[output_name]
    sig = inspect.signature(fn)

    # Build kwargs by matching param names
    kwargs: dict[str, Any] = {}
    for param in sig.parameters:
        if param == "filters":
            kwargs["filters"] = filters
        elif param in dash.queries:
            kwargs[param] = execute_query(dash.queries[param], filters, engine)

    result = fn(**kwargs)
    return detect_output_type(result), result


__all__ = [
    "OutputType",
    "execute_query",
    "execute_options_query",
    "execute_output",
    "detect_output_type",
]
