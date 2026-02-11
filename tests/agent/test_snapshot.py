from __future__ import annotations

import asyncio
import importlib
import io
import json
from datetime import date
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
import plotly.graph_objects as go
import pytest
from PIL import Image

from varro.dashboard.models import Metric


def _png_bytes(width: int, height: int) -> bytes:
    image = Image.new("RGBA", (width, height), color=(30, 90, 150, 255))
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


@pytest.fixture
def assistant_module(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    import logfire

    monkeypatch.setattr(logfire, "configure", lambda **kwargs: None)
    monkeypatch.setattr(logfire, "instrument_pydantic_ai", lambda: None)

    utils = importlib.import_module("varro.agent.utils")
    monkeypatch.setattr(utils, "get_dim_tables", lambda: ())

    assistant = importlib.import_module("varro.agent.assistant")
    return importlib.reload(assistant)


def test_canonical_query_folder_empty_query_maps_to_underscore() -> None:
    snapshot = importlib.import_module("varro.agent.snapshot")
    assert snapshot.canonical_query_folder("") == "_"


def test_canonical_query_folder_sorts_query_params() -> None:
    snapshot = importlib.import_module("varro.agent.snapshot")
    assert snapshot.canonical_query_folder("b=2&a=1&a=0") == "a=0&a=1&b=2"


def test_snapshot_tool_uses_current_url_when_url_is_omitted(
    assistant_module, monkeypatch
) -> None:
    calls = []
    snapshot_model = importlib.import_module("varro.agent.snapshot")

    async def fake_snapshot_dashboard_url(user_id: int, url: str):
        calls.append((user_id, url))
        return snapshot_model.SnapshotResult(url=url, folder=Path("/tmp/snapshots"))

    monkeypatch.setattr(
        assistant_module,
        "snapshot_dashboard_url",
        fake_snapshot_dashboard_url,
    )
    ctx = SimpleNamespace(
        deps=SimpleNamespace(
            user_id=7,
            request_current_url=lambda: "/dashboard/sales?region=North",
        )
    )

    result = asyncio.run(assistant_module.Snapshot(ctx))

    assert result == "/dashboard/sales?region=North"
    assert calls == [(7, "/dashboard/sales?region=North")]


def test_snapshot_tool_uses_explicit_url_over_current_url(
    assistant_module, monkeypatch
) -> None:
    calls = []
    snapshot_model = importlib.import_module("varro.agent.snapshot")

    async def fake_snapshot_dashboard_url(user_id: int, url: str):
        calls.append((user_id, url))
        return snapshot_model.SnapshotResult(url=url, folder=Path("/tmp/snapshots"))

    monkeypatch.setattr(
        assistant_module,
        "snapshot_dashboard_url",
        fake_snapshot_dashboard_url,
    )
    ctx = SimpleNamespace(
        deps=SimpleNamespace(
            user_id=7,
            request_current_url=lambda: "/dashboard/sales?region=North",
        )
    )

    result = asyncio.run(assistant_module.Snapshot(ctx, url="/dashboard/sales?region=South"))

    assert result == "/dashboard/sales?region=South"
    assert calls == [(7, "/dashboard/sales?region=South")]


def test_snapshot_dashboard_writes_expected_artifacts(tmp_path: Path, monkeypatch) -> None:
    workspace = importlib.import_module("varro.agent.workspace")
    snapshot = importlib.import_module("varro.agent.snapshot")

    data_dir = tmp_path / "data"
    dashboard_dir = data_dir / "user" / "1" / "dashboard" / "sales"
    dashboard_dir.mkdir(parents=True)

    monkeypatch.setattr(workspace, "DATA_DIR", data_dir)
    monkeypatch.setattr(workspace, "DOCS_DIR", data_dir / "docs_template")

    fake_dashboard = SimpleNamespace(
        filters=[],
        outputs={
            "line_plot": object(),
            "summary_table": object(),
            "total_metric": object(),
            "note": object(),
        },
    )

    def fake_load_dashboard(folder: Path):
        assert folder == dashboard_dir
        return fake_dashboard

    def fake_execute_output(dash, output_name: str, filters, engine):
        if output_name == "line_plot":
            return go.Figure(data=[go.Scatter(x=[1, 2], y=[1, 3])])
        if output_name == "summary_table":
            return pd.DataFrame({"value": [2, 3]})
        if output_name == "total_metric":
            return Metric(value=5, label="Total")
        if output_name == "note":
            return "saved"
        raise AssertionError(output_name)

    async def fake_dashboard_png(url: str):
        assert url.startswith("http://127.0.0.1:5001/dashboard/sales?")
        return _png_bytes(2200, 1200)

    async def fake_plotly_png(fig: go.Figure, *, max_pixels: int):
        assert max_pixels == snapshot.SNAPSHOT_MAX_PIXELS
        return _png_bytes(2400, 1000)

    monkeypatch.setattr(snapshot, "load_dashboard", fake_load_dashboard)
    monkeypatch.setattr(snapshot, "execute_output", fake_execute_output)
    monkeypatch.setattr(snapshot, "render_dashboard_url_to_png", fake_dashboard_png)
    monkeypatch.setattr(snapshot, "plotly_figure_to_png", fake_plotly_png)

    result = asyncio.run(
        snapshot.snapshot_dashboard_url(
            1,
            "/dashboard/sales?b=2&a=1",
            db_engine=None,
        )
    )

    snapshot_dir = dashboard_dir / "snapshots" / "a=1&b=2"
    assert result.url == "/dashboard/sales?b=2&a=1"
    assert result.folder == snapshot_dir
    assert not (snapshot_dir / "context.url").exists()
    assert (snapshot_dir / f"{date.today().isoformat()}.date").exists()
    assert (snapshot_dir / "dashboard.png").exists()
    assert (snapshot_dir / "figures" / "line_plot.png").exists()
    assert (snapshot_dir / "tables" / "summary_table.parquet").exists()
    assert (snapshot_dir / "metrics.json").exists()

    with Image.open(snapshot_dir / "dashboard.png") as dashboard_png:
        assert dashboard_png.width * dashboard_png.height <= snapshot.SNAPSHOT_MAX_PIXELS
    with Image.open(snapshot_dir / "figures" / "line_plot.png") as figure_png:
        assert figure_png.width * figure_png.height <= snapshot.SNAPSHOT_MAX_PIXELS

    metrics = json.loads((snapshot_dir / "metrics.json").read_text(encoding="utf-8"))
    assert metrics == {
        "note": "saved",
        "total_metric": {
            "change": None,
            "change_label": None,
            "format": "number",
            "label": "Total",
            "value": 5,
        },
    }

    table_df = pd.read_parquet(snapshot_dir / "tables" / "summary_table.parquet")
    assert list(table_df.columns) == ["value"]
    assert table_df["value"].tolist() == [2, 3]
