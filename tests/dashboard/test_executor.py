from __future__ import annotations

from varro.dashboard.executor import execute_output
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
