from __future__ import annotations

from urllib.parse import parse_qs, urlparse


def test_dashboard_shell_fragment_renders_filters_and_placeholders(dashboard_env) -> None:
    response = dashboard_env.client.get(
        dashboard_env.base_url,
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert 'id="filters"' in response.text
    assert f'hx-get="{dashboard_env.base_url}/_/filters"' in response.text
    assert 'hx-trigger="change delay:500ms"' in response.text
    assert f'{dashboard_env.base_url}/_/metric/total_population' in response.text
    assert f'{dashboard_env.base_url}/_/figure/population_trend_chart' in response.text
    assert f'{dashboard_env.base_url}/_/table/region_table' in response.text
    assert "North" in response.text
    assert "South" in response.text


def test_filter_sync_sets_replace_url_and_trigger(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/_/filters",
        params={
            "region": "North",
            "period_from": "2024-04-01",
            "include_estimate": "true",
        },
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert response.headers["HX-Trigger"] == '{"filtersChanged": {}}'

    parsed = urlparse(response.headers["HX-Replace-Url"])
    assert parsed.path == dashboard_env.base_url
    assert parse_qs(parsed.query) == {
        "region": ["North"],
        "period_from": ["2024-04-01"],
        "include_estimate": ["true"],
    }


def test_filter_sync_omits_default_values_from_url(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/_/filters",
        params={"include_estimate": "false"},
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert response.headers["HX-Replace-Url"] == dashboard_env.base_url


def test_metric_endpoint_renders_metric_fragment(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/_/metric/total_population",
        params={
            "region": "North",
            "period_to": "2024-04-01",
        },
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert "Total Population" in response.text
    assert "210" in response.text


def test_figure_endpoint_renders_plotly_fragment(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/_/figure/population_trend_chart",
        params={"region": "South"},
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert "plotly-graph-div" in response.text


def test_table_endpoint_renders_dataframe_fragment(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/_/table/region_table",
        params={"include_estimate": "true"},
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert "<table" in response.text
    assert "South" in response.text
    assert "265" in response.text
    assert "North" not in response.text


def test_unknown_dashboard_returns_404(dashboard_env) -> None:
    response = dashboard_env.client.get(
        "/dash/does-not-exist",
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 404
