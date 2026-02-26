from __future__ import annotations

import pandas as pd
from types import SimpleNamespace

from varro.dashboard.executor import execute_options_query, execute_output, execute_query
from varro.dashboard.filters import SelectFilter
from varro.dashboard.loader import extract_params, load_dashboard
from varro.dashboard.models import Metric


def test_extract_params_ignores_postgres_cast_syntax() -> None:
    query = """
    SELECT f.alder::int AS age
    FROM fact.folk1a f
    WHERE (:region IS NULL OR f.region = :region)
      AND (:period_from IS NULL OR f.tid >= :period_from)
    """
    assert extract_params(query) == {"region", "period_from"}


def test_execute_output_injects_queries_and_filters(dashboard_env) -> None:
    dash = load_dashboard(dashboard_env.dashboard_path)

    result = execute_output(
        dash,
        "total_population",
        {
            "region": "North",
            "period_from": "2024-04-01",
            "period_to": None,
            "include_estimate": False,
            "unused": "ignored",
        },
        dashboard_env.engine,
    )

    assert isinstance(result, Metric)
    assert result.value == 225
    assert result.label == "Total Population"


def test_execute_query_normalizes_date_columns(dashboard_env) -> None:
    dash = load_dashboard(dashboard_env.dashboard_path)

    result = execute_query(
        dash.queries["population_trend"],
        {},
        dashboard_env.engine,
    )

    assert pd.api.types.is_datetime64_any_dtype(result["period"])


def test_execute_options_query_handles_single_column(dashboard_env) -> None:
    dash = SimpleNamespace(
        queries={"regions": "SELECT 'North' AS region UNION ALL SELECT 'South' AS region"}
    )
    filter_def = SelectFilter(
        type="select",
        name="region",
        default="all",
        options_query="regions",
    )
    result = execute_options_query(dash, filter_def, dashboard_env.engine)
    assert result == [("North", "North"), ("South", "South")]


def test_execute_options_query_handles_value_and_label_columns(dashboard_env) -> None:
    dash = SimpleNamespace(
        queries={
            "regions": (
                "SELECT '84' AS kode, 'Region Hovedstaden' AS titel "
                "UNION ALL "
                "SELECT '85' AS kode, 'Region Sjælland' AS titel"
            )
        }
    )
    filter_def = SelectFilter(
        type="select",
        name="region",
        default="all",
        options_query="regions",
    )
    result = execute_options_query(dash, filter_def, dashboard_env.engine)
    assert result == [
        ("84", "Region Hovedstaden"),
        ("85", "Region Sjælland"),
    ]
