"""Test dashboard query parsing and execution."""

from pathlib import Path
from varro.dashboard.loader import parse_queries, extract_params, load_dashboard
from varro.dashboard.executor import execute_query
from varro.db.db import engine


def test_extract_params_ignores_cast():
    """Verify :: cast syntax is not matched."""
    query = "SELECT * FROM t WHERE x = :param::date"
    params = extract_params(query)
    assert params == {"param"}
    assert "date" not in params


def test_parse_queries():
    """Verify query parsing from SQL file."""
    sql = Path("example_dashboard_folder/sales/queries.sql").read_text()
    queries = parse_queries(sql)
    assert "regions" in queries
    assert "population_trend" in queries
    assert "population_by_region" in queries
    assert "age_distribution" in queries


def test_population_trend_params():
    """Verify correct params extracted from population_trend query."""
    sql = Path("example_dashboard_folder/sales/queries.sql").read_text()
    queries = parse_queries(sql)
    params = extract_params(queries["population_trend"])
    assert params == {"region", "period_from", "period_to"}
    assert "date" not in params  # from ::date cast


def test_execute_queries():
    """Test queries execute successfully."""
    dash = load_dashboard(Path("example_dashboard_folder/sales"))

    # Test regions query (no params)
    df = execute_query(dash.queries["regions"], {}, engine)
    assert len(df) == 5  # 5 Danish regions

    # Test population_trend with no filters
    df = execute_query(dash.queries["population_trend"], {}, engine)
    assert not df.empty
    assert "quarter" in df.columns
    assert "population" in df.columns


if __name__ == "__main__":
    test_extract_params_ignores_cast()
    print("✓ extract_params ignores :: cast")

    test_parse_queries()
    print("✓ parse_queries works")

    test_population_trend_params()
    print("✓ population_trend params correct")

    test_execute_queries()
    print("✓ queries execute successfully")

    print("\nAll tests passed!")
