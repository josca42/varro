from __future__ import annotations

from urllib.parse import parse_qs, urlparse

from varro.dashboard.routes import _content_hash


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
        "/dashboard/does-not-exist",
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 404


def test_dashboard_code_editor_fragment_renders(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/code",
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert f'hx-put="{dashboard_env.base_url}/code"' in response.text
    assert 'name="content"' in response.text
    assert "dashboard.md" in response.text
    assert "outputs.py" in response.text
    assert "queries/regions.sql" in response.text
    assert 'name="file"' in response.text


def test_dashboard_code_editor_can_load_outputs_file(dashboard_env) -> None:
    response = dashboard_env.client.get(
        f"{dashboard_env.base_url}/code",
        params={"file": "outputs.py"},
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert 'value="outputs.py"' in response.text
    assert "def total_population" in response.text


def test_dashboard_code_put_updates_selected_file(dashboard_env) -> None:
    outputs_file = dashboard_env.dashboard_path / "outputs.py"
    original = outputs_file.read_text(encoding="utf-8")
    updated_content = original.replace("Total Population", "Total Population Updated")
    payload = {
        "file": "outputs.py",
        "file_hash": _content_hash(original),
        "content": updated_content,
    }

    response = dashboard_env.client.put(
        f"{dashboard_env.base_url}/code",
        data=payload,
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200

    updated = outputs_file.read_text(encoding="utf-8")
    assert "Total Population Updated" in updated


def test_dashboard_code_put_detects_hash_conflict(dashboard_env) -> None:
    dashboard_md = dashboard_env.dashboard_path / "dashboard.md"
    original = dashboard_md.read_text(encoding="utf-8")
    external_change = original + "\nExternal change\n"
    dashboard_md.write_text(external_change, encoding="utf-8")

    payload = {
        "file": "dashboard.md",
        "file_hash": _content_hash(original),
        "content": original,
    }

    response = dashboard_env.client.put(
        f"{dashboard_env.base_url}/code",
        data=payload,
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert 'name="content"' in response.text
    assert dashboard_md.read_text(encoding="utf-8") == external_change
