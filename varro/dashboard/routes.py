"""dashboard.routes

FastHTML routes for dashboards with on-demand loading.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

from fasthtml.common import APIRouter, Div, Response
from sqlalchemy.engine import Engine

from varro.dashboard.loader import Dashboard, load_dashboard
from varro.dashboard.executor import (
    clear_query_cache,
    execute_options_query,
    execute_output,
)
from varro.dashboard.components import (
    render_shell,
    render_metric_card,
    render_table,
    render_figure,
)
from varro.dashboard.filters import Filter, SelectFilter
from ui.app.layout import AppShell

# TODO: remove the sess.get("user_id", 1) and use the user_id from the session directly. With no default value.

# Module-level configuration
_dashboards_root: Path | None = None
_engine: Engine | None = None


@dataclass
class CachedDashboard:
    dashboard: Dashboard
    mtimes: tuple[float, ...]


_cache: dict[tuple[int, str], CachedDashboard] = {}

ar = APIRouter()


def configure(dashboards_root: Path | str, engine: Engine) -> None:
    """Configure dashboard routes with dashboards root and database engine."""
    global _dashboards_root, _engine, _cache
    _dashboards_root = Path(dashboards_root)
    _engine = engine
    _cache = {}


def mount_dashboard_routes(app, dashboards_root: Path | str, engine: Engine) -> None:
    """Configure and mount dashboard routes on the app."""
    configure(dashboards_root, engine)
    ar.to_app(app)


def _dashboards_dir(user_id: int) -> Path | None:
    if _dashboards_root is None:
        return None
    return _dashboards_root / "user" / str(user_id) / "dashboards"


def list_dashboards(user_id: int) -> list[str]:
    path = _dashboards_dir(user_id)
    if path is None or not path.exists():
        return []
    slugs = []
    for folder in sorted(path.iterdir()):
        if folder.is_dir() and (folder / "dashboard.md").exists():
            slugs.append(folder.name)
    return slugs


def get_mtimes(folder: Path) -> tuple[float, ...]:
    queries_dir = folder / "queries"
    files = [folder / "dashboard.md", folder / "outputs.py"]
    if queries_dir.exists() and queries_dir.is_dir():
        files.extend(sorted(queries_dir.glob("*.sql")))
    return tuple(f.stat().st_mtime for f in files)


def get_dashboard(name: str, user_id: int) -> Dashboard | None:
    """Load a dashboard on-demand with caching."""
    dashboards_dir = _dashboards_dir(user_id)
    if dashboards_dir is None:
        return None
    path = dashboards_dir / name
    if not (path / "dashboard.md").exists():
        return None

    cache_key = (user_id, name)
    mtimes = get_mtimes(path)
    cached = _cache.get(cache_key)
    if cached and cached.mtimes == mtimes:
        return cached.dashboard

    clear_query_cache()
    dash = load_dashboard(path)
    _cache[cache_key] = CachedDashboard(dashboard=dash, mtimes=mtimes)
    return dash


def parse_filters_from_request(
    req: Any,
    filters: list[Filter],
) -> dict[str, Any]:
    """Parse filter values from request query params.

    Applies defaults for missing values.
    """
    values = {}
    for f in filters:
        values.update(f.parse_query_params(req.query_params))
    return values


def build_filter_url(
    dash_name: str,
    values: dict[str, Any],
    filters: list[Filter],
) -> str:
    """Build URL with filter params, omitting defaults."""
    params: dict[str, str] = {}

    for f in filters:
        params.update(f.url_params(values))

    base = f"/dashboard/{dash_name}"
    if params:
        return f"{base}?{urlencode(params)}"
    return base


@ar("/dashboard/{name}", methods=["GET"])
def dashboard_shell(name: str, req, sess):
    user_id = sess.get("user_id", 1)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)

    options: dict[str, list[str]] = {}
    for f in dash.filters:
        if isinstance(f, SelectFilter) and f.options_query:
            options[f.name] = execute_options_query(dash, f, _engine)

    content = Div(
        render_shell(dash, filters, options),
    )

    if req.headers.get("HX-Request"):
        return content

    chat = None
    if chat_id := sess.get("chat_id"):
        chat = req.state.chats.get(chat_id, with_turns=True)
    return AppShell(chat, content)


@ar("/dashboard/{name}/_/filters", methods=["GET"])
def filter_sync(name: str, req, sess):
    user_id = sess.get("user_id", 1)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)
    url = build_filter_url(name, filters, dash.filters)

    return Response(
        "",
        headers={
            "HX-Replace-Url": url,
            "HX-Trigger": '{"filtersChanged": {}}',
        },
    )


@ar("/dashboard/{name}/_/figure/{output_name}", methods=["GET"])
def render_figure_endpoint(name: str, output_name: str, req, sess):
    user_id = sess.get("user_id", 1)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)

    try:
        result = execute_output(dash, output_name, filters, _engine)
        return render_figure(result)
    except Exception:
        return Div("Error loading chart", cls="text-error text-center p-4")


@ar("/dashboard/{name}/_/table/{output_name}", methods=["GET"])
def render_table_endpoint(name: str, output_name: str, req, sess):
    user_id = sess.get("user_id", 1)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)

    try:
        result = execute_output(dash, output_name, filters, _engine)
        return render_table(result)
    except Exception:
        return Div("Error loading table", cls="text-error text-center p-4")


@ar("/dashboard/{name}/_/metric/{output_name}", methods=["GET"])
def render_metric_endpoint(name: str, output_name: str, req, sess):
    user_id = sess.get("user_id", 1)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)

    try:
        result = execute_output(dash, output_name, filters, _engine)
        return render_metric_card(result)
    except Exception:
        return Div("Error loading metric", cls="text-error text-center p-4")
