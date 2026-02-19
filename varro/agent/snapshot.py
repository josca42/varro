from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import json
import os
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit

import pandas as pd
import plotly.graph_objects as go
from sqlalchemy.engine import Engine

from varro.agent.images import SNAPSHOT_MAX_PIXELS, save_png
from varro.agent.playwright_render import url_to_png
from varro.agent.utils import plotly_figure_to_png
from varro.agent.workspace import user_workspace_root
from varro.dashboard.executor import clear_query_cache, execute_output
from varro.dashboard.loader import Dashboard, load_dashboard
from varro.dashboard.models import Metric
from varro.db.db import dst_read_engine as default_engine

DEFAULT_APP_BASE_URL = os.getenv("VARRO_APP_BASE_URL", "http://127.0.0.1:5001")
DASHBOARD_READY_SELECTOR = "[data-slot='dashboard-shell']"
PLOTLY_READY_SELECTOR = ".plotly-graph-div .main-svg, .plotly-graph-div canvas"


@dataclass(frozen=True)
class SnapshotResult:
    url: str
    folder: Path


def canonical_query_folder(query: str) -> str:
    params = [(k, v) for k, v in parse_qsl(query, keep_blank_values=True) if k]
    if not params:
        return "_"
    params.sort(key=lambda item: (item[0], item[1]))
    return urlencode(params, doseq=True)


def parse_dashboard_url(url: str) -> tuple[str, str]:
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        raise ValueError("url must be app-relative and start with '/'")
    if not parsed.path.startswith("/"):
        raise ValueError("url must start with '/'")

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) != 2 or parts[0] != "dashboard" or not parts[1]:
        raise ValueError("url must match /dashboard/{slug}")

    return parts[1], parsed.query


def parse_dashboard_filters(dash: Dashboard, query: str) -> dict[str, Any]:
    query_params = dict(parse_qsl(query, keep_blank_values=True))
    values: dict[str, Any] = {}
    for filter_def in dash.filters:
        values.update(filter_def.parse_query_params(query_params))
    return values


def _serialize_metric(value: Any) -> Any:
    if isinstance(value, Metric):
        return value.model_dump(mode="json")
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "item"):
        return value.item()
    return str(value)


def _absolute_app_url(url: str, app_base_url: str | None = None) -> str:
    base = (app_base_url or DEFAULT_APP_BASE_URL).rstrip("/") + "/"
    return urljoin(base, url.lstrip("/"))


async def render_dashboard_url_to_png(url: str) -> bytes:
    return await url_to_png(
        url,
        wait_selector=DASHBOARD_READY_SELECTOR,
        plotly_wait_selector=PLOTLY_READY_SELECTOR,
        full_page=True,
    )


async def snapshot_dashboard_url(
    user_id: int,
    url: str,
    *,
    app_base_url: str | None = None,
    db_engine: Engine = default_engine,
    max_pixels: int = SNAPSHOT_MAX_PIXELS,
) -> SnapshotResult:
    target_url = (url or "").strip()
    if not target_url:
        raise ValueError("url is required")

    slug, query = parse_dashboard_url(target_url)

    workspace_root = user_workspace_root(user_id)
    dashboard_dir = workspace_root / "dashboard" / slug
    if not dashboard_dir.exists():
        raise ValueError(f"dashboard not found: {slug}")

    dash = load_dashboard(dashboard_dir)
    filters = parse_dashboard_filters(dash, query)
    snapshot_dir = dashboard_dir / "snapshots" / canonical_query_folder(query)
    snapshot_dir.mkdir(parents=True, exist_ok=True)

    dashboard_png = await render_dashboard_url_to_png(
        _absolute_app_url(target_url, app_base_url=app_base_url)
    )
    save_png(snapshot_dir / "dashboard.png", dashboard_png, max_pixels=max_pixels)

    (snapshot_dir / f"{date.today().isoformat()}.date").touch()

    clear_query_cache()
    metrics: dict[str, Any] = {}
    for output_name in sorted(dash.outputs):
        result = execute_output(dash, output_name, filters, db_engine)
        if isinstance(result, go.Figure):
            figure_png = await plotly_figure_to_png(result, max_pixels=max_pixels)
            save_png(
                snapshot_dir / "figures" / f"{output_name}.png",
                figure_png,
                max_pixels=max_pixels,
            )
            continue
        if isinstance(result, pd.DataFrame):
            table_path = snapshot_dir / "tables" / f"{output_name}.parquet"
            table_path.parent.mkdir(parents=True, exist_ok=True)
            result.to_parquet(table_path, index=False)
            continue
        metrics[output_name] = _serialize_metric(result)

    (snapshot_dir / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, sort_keys=True, indent=2),
        encoding="utf-8",
    )

    return SnapshotResult(url=target_url, folder=snapshot_dir)
