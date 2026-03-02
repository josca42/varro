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


def test_dashboard_shell_select_options_use_value_and_label(dashboard_env) -> None:
    response = dashboard_env.client.get(
        dashboard_env.base_url,
        params={"region": "North"},
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert 'value="North"' in response.text
    assert "Label North" in response.text
    assert 'value="South"' in response.text
    assert "Label South" in response.text


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


def test_publish_creates_public_dashboard_with_source_files_only(dashboard_env) -> None:
    source_dir = dashboard_env.dashboard_path
    (source_dir / "notes.md").write_text("Note", encoding="utf-8")
    (source_dir / "extra.txt").write_text("ignore", encoding="utf-8")
    snapshots_dir = source_dir / "snapshots"
    snapshots_dir.mkdir()
    (snapshots_dir / "x.txt").write_text("ignore", encoding="utf-8")

    response = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200

    public_dir = dashboard_env.public_dashboard_dir(dashboard_env.user_id)
    assert (public_dir / "dashboard.md").exists()
    assert (public_dir / "outputs.py").exists()
    assert (public_dir / "queries" / "regions.sql").exists()
    assert (public_dir / "notes.md").exists()
    assert not (public_dir / "extra.txt").exists()
    assert not (public_dir / "snapshots").exists()


def test_publish_overwrites_public_dashboard_and_removes_stale_files(dashboard_env) -> None:
    first = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert first.status_code == 200

    public_dir = dashboard_env.public_dashboard_dir(dashboard_env.user_id)
    stale_file = public_dir / "stale.txt"
    stale_file.write_text("stale", encoding="utf-8")

    outputs_file = dashboard_env.dashboard_path / "outputs.py"
    updated = outputs_file.read_text(encoding="utf-8").replace(
        "Total Population", "Total Population Updated"
    )
    outputs_file.write_text(updated, encoding="utf-8")

    second = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert second.status_code == 200
    assert not stale_file.exists()
    assert "Total Population Updated" in (public_dir / "outputs.py").read_text(
        encoding="utf-8"
    )


def test_public_dashboard_shell_uses_public_lazy_load_routes(dashboard_env) -> None:
    publish = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert publish.status_code == 200

    response = dashboard_env.client.get(
        dashboard_env.public_base_url,
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert f'hx-get="{dashboard_env.public_base_url}/_/filters"' in response.text
    assert f'{dashboard_env.public_base_url}/_/metric/total_population' in response.text
    assert (
        f'{dashboard_env.public_base_url}/_/figure/population_trend_chart'
        in response.text
    )
    assert f'{dashboard_env.public_base_url}/_/table/region_table' in response.text


def test_public_dashboard_is_accessible_while_logged_out(dashboard_env) -> None:
    publish = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert publish.status_code == 200
    dashboard_env.client.get("/__test/logout")

    response = dashboard_env.client.get(
        dashboard_env.public_base_url,
        headers={"HX-Request": "true"},
    )
    assert response.status_code == 200
    assert 'id="filters"' in response.text


def test_context_action_endpoint_returns_publish_update_and_edit(dashboard_env) -> None:
    publish_action = dashboard_env.client.get(
        "/public/_/context-action",
        params={"url": dashboard_env.base_url},
    )
    assert publish_action.status_code == 200
    assert "Publish" in publish_action.text

    published = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert published.status_code == 200

    update_action = dashboard_env.client.get(
        "/public/_/context-action",
        params={"url": dashboard_env.base_url},
    )
    assert update_action.status_code == 200
    assert "Update" in update_action.text

    edit_action = dashboard_env.client.get(
        "/public/_/context-action",
        params={"url": dashboard_env.public_base_url},
    )
    assert edit_action.status_code == 200
    assert "Edit" in edit_action.text
    assert f'href="{dashboard_env.public_base_url}/fork"' in edit_action.text

    empty_action = dashboard_env.client.get(
        "/public/_/context-action",
        params={"url": "/app"},
    )
    assert empty_action.status_code == 200
    assert empty_action.text == ""


def test_logged_in_public_fork_copies_dashboard_and_redirects(dashboard_env) -> None:
    published = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert published.status_code == 200

    dashboard_env.client.get("/__test/login/2")
    response = dashboard_env.client.get(
        f"{dashboard_env.public_base_url}/fork",
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == f"/dashboard/{dashboard_env.dashboard_name}"

    fork_dir = dashboard_env.dashboard_dir(2)
    assert (fork_dir / "dashboard.md").exists()
    assert (fork_dir / "outputs.py").exists()
    assert (fork_dir / "queries" / "regions.sql").exists()


def test_public_fork_uses_incremented_suffix_on_name_collisions(dashboard_env) -> None:
    published = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert published.status_code == 200

    dashboard_env.client.get("/__test/login/2")
    dashboard_env.dashboard_dir(2, dashboard_env.dashboard_name).mkdir(parents=True)
    dashboard_env.dashboard_dir(2, f"{dashboard_env.dashboard_name}-fork").mkdir(
        parents=True
    )

    response = dashboard_env.client.get(
        f"{dashboard_env.public_base_url}/fork",
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert (
        response.headers["location"]
        == f"/dashboard/{dashboard_env.dashboard_name}-fork-2"
    )
    assert dashboard_env.dashboard_dir(2, f"{dashboard_env.dashboard_name}-fork-2").exists()


def test_logged_out_public_fork_redirects_to_login_with_next(dashboard_env) -> None:
    published = dashboard_env.client.post(
        f"{dashboard_env.base_url}/publish",
        headers={"HX-Request": "true"},
    )
    assert published.status_code == 200
    dashboard_env.client.get("/__test/logout")

    response = dashboard_env.client.get(
        f"{dashboard_env.public_base_url}/fork",
        follow_redirects=False,
    )
    assert response.status_code == 303
    parsed = urlparse(response.headers["location"])
    assert parsed.path == "/login"
    assert parse_qs(parsed.query)["next"] == [f"{dashboard_env.public_base_url}/fork"]
