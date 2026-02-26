"""dashboard.executor

Execute SQL queries and call @output functions.
"""

from __future__ import annotations

from datetime import date
import hashlib
import inspect
import json
from typing import Any

import pandas as pd
from sqlalchemy import text, bindparam, String, Date, Boolean
from sqlalchemy.engine import Engine

from varro.dashboard.loader import Dashboard, extract_params
from varro.dashboard.models import Metric
from varro.dashboard.filters import SelectFilter

_query_cache: dict[tuple[str, str], pd.DataFrame] = {}
SelectOption = tuple[str, str]


def _normalize_date_columns(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.select_dtypes(include=["object"]).columns:
        non_null = df[col].dropna()
        if non_null.empty:
            continue
        if non_null.map(lambda value: isinstance(value, date)).all():
            df[col] = pd.to_datetime(df[col])
    return df


def _infer_param_type(name: str, value: Any = None):
    """Infer SQLAlchemy type from parameter name."""
    if isinstance(value, bool):
        return Boolean
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
    param_types: dict[str, Any] = {}
    for param in params_needed:
        value = filters.get(param)
        bound[param] = None if value == "all" or value is None else value
        param_types[param] = _infer_param_type(param, bound[param])

    # Create typed bindparams for NULL handling
    stmt = text(query)
    for param in params_needed:
        stmt = stmt.bindparams(bindparam(param, type_=param_types[param]))

    with engine.connect() as conn:
        df = pd.read_sql(stmt, conn, params=bound)
    return _normalize_date_columns(df)


def execute_query_cached(
    query: str, filters: dict[str, Any], engine: Engine
) -> pd.DataFrame:
    """Execute a SQL query with a simple cache keyed by query + filters."""
    query_hash = hashlib.md5(query.encode()).hexdigest()
    filters_key = json.dumps(filters, sort_keys=True, default=str)
    key = (query_hash, filters_key)

    cached = _query_cache.get(key)
    if cached is not None:
        return cached.copy()

    df = execute_query(query, filters, engine)
    _query_cache[key] = df
    return df.copy()


def clear_query_cache() -> None:
    _query_cache.clear()


def execute_options_query(
    dash: Dashboard, f: SelectFilter, engine: Engine
) -> list[SelectOption]:
    """Execute an options query for a select filter.

    Returns (value, label) pairs.
    """
    if not f.options_query:
        return []
    query = dash.queries[f.options_query]

    options: list[SelectOption] = []
    with engine.connect() as conn:
        for row in conn.execute(text(query)):
            if len(row) < 1:
                continue
            value = "" if row[0] is None else str(row[0])
            label = value if len(row) < 2 or row[1] is None else str(row[1])
            options.append((value, label))
    return options


def execute_output(
    dash: Dashboard,
    output_name: str,
    filters: dict[str, Any],
    engine: Engine,
) -> Any:
    """Execute an @output function.

    Returns the output function result.
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
            kwargs[param] = execute_query_cached(
                dash.queries[param], filters, engine
            )
    return fn(**kwargs)
