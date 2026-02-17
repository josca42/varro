"""dashboard.routes

FastHTML routes for dashboards with on-demand loading.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

from fasthtml.common import APIRouter, A, Button, Div, Form, Input, Response, Textarea
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
from varro.db import crud
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
    return _dashboards_root / "user" / str(user_id) / "dashboard"


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


def _dashboard_dir(name: str, user_id: int) -> Path | None:
    dashboards_dir = _dashboards_dir(user_id)
    if dashboards_dir is None:
        return None
    folder = dashboards_dir / name
    if not (folder / "dashboard.md").exists():
        return None
    return folder


def _dashboard_code_files(folder: Path) -> list[str]:
    files: list[str] = []
    if (folder / "dashboard.md").exists():
        files.append("dashboard.md")
    if (folder / "outputs.py").exists():
        files.append("outputs.py")
    queries_dir = folder / "queries"
    if queries_dir.exists() and queries_dir.is_dir():
        for path in sorted(queries_dir.glob("*.sql")):
            files.append(f"queries/{path.name}")
    return files


def _resolve_dashboard_code_file(
    folder: Path, files: list[str], file_name: str
) -> Path | None:
    if file_name not in files:
        return None
    path = (folder / file_name).resolve()
    try:
        path.relative_to(folder.resolve())
    except ValueError:
        return None
    if not path.exists() or not path.is_file():
        return None
    return path


def _shell_or_fragment(req, sess, content):
    if req.headers.get("HX-Request"):
        return content

    chat = None
    chats = getattr(req.state, "chats", None)
    if chats and (chat_id := sess.get("chat_id")):
        chat = chats.get(chat_id, with_turns=True)
    db_user = crud.user.get(sess.get("user_id"))
    return AppShell(
        chat,
        content,
        user_name=db_user.name if db_user else None,
        user_email=db_user.email if db_user else None,
    )


def _content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _render_dashboard_code_editor(
    name: str,
    files: list[str],
    selected_file: str,
    content: str,
):
    tabs = [
        A(
            file_name,
            href=f"/dashboard/{name}/code?{urlencode({'file': file_name})}",
            cls="tab tab-active" if file_name == selected_file else "tab",
            hx_get=f"/dashboard/{name}/code?{urlencode({'file': file_name})}",
            hx_target="#content-panel",
            hx_swap="innerHTML",
            hx_push_url="true",
        )
        for file_name in files
    ]

    return Div(
        Div(*tabs, cls="tabs tabs-box"),
        Form(
            Input(type="hidden", name="file_hash", value=_content_hash(content)),
            Input(type="hidden", name="file", value=selected_file),
            Textarea(
                content,
                name="content",
                cls="textarea textarea-bordered w-full font-mono text-sm min-h-[28rem]",
            ),
            Div(
                Button("Save", type="submit", cls="btn btn-primary"),
                A(
                    "View dashboard",
                    href=f"/dashboard/{name}",
                    cls="btn btn-ghost",
                    hx_get=f"/dashboard/{name}",
                    hx_target="#content-panel",
                    hx_swap="innerHTML",
                    hx_push_url="true",
                ),
                cls="flex items-center gap-2",
            ),
            hx_put=f"/dashboard/{name}/code",
            hx_target="#content-panel",
            hx_swap="innerHTML",
            cls="space-y-4",
        ),
        cls="p-6 space-y-4",
        data_slot="dashboard-code-page",
    )


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

    return _shell_or_fragment(req, sess, content)


@ar("/dashboard/{name}/code", methods=["GET"])
def dashboard_code(name: str, req, sess):
    user_id = sess.get("user_id", 1)
    folder = _dashboard_dir(name, user_id=user_id)
    if folder is None:
        return Response("Dashboard not found", status_code=404)

    files = _dashboard_code_files(folder)
    if not files:
        return Response("Dashboard source files not found", status_code=404)

    selected_file = req.query_params.get("file", "dashboard.md")
    if selected_file not in files:
        selected_file = files[0]
    path = _resolve_dashboard_code_file(folder, files, selected_file)
    if path is None:
        return Response("File not found", status_code=404)

    content = _render_dashboard_code_editor(
        name,
        files,
        selected_file,
        path.read_text(encoding="utf-8"),
    )
    return _shell_or_fragment(req, sess, content)


@ar("/dashboard/{name}/code", methods=["PUT"])
async def dashboard_code_save(name: str, req, sess):
    user_id = sess.get("user_id", 1)
    folder = _dashboard_dir(name, user_id=user_id)
    if folder is None:
        return Response("Dashboard not found", status_code=404)

    files = _dashboard_code_files(folder)
    if not files:
        return Response("Dashboard source files not found", status_code=404)

    form = await req.form()
    selected_file = str(form.get("file", "dashboard.md"))
    if selected_file not in files:
        selected_file = files[0]
    path = _resolve_dashboard_code_file(folder, files, selected_file)
    if path is None:
        return Response("File not found", status_code=404)

    current_content = path.read_text(encoding="utf-8")
    form_hash = str(form.get("file_hash", ""))
    next_content = str(form.get("content", "")).replace("\r\n", "\n")

    if form_hash != _content_hash(current_content):
        content = _render_dashboard_code_editor(
            name, files, selected_file, current_content
        )
        return _shell_or_fragment(req, sess, content)

    path.write_text(next_content, encoding="utf-8")
    _cache.pop((user_id, name), None)
    clear_query_cache()

    content = _render_dashboard_code_editor(name, files, selected_file, next_content)
    return _shell_or_fragment(req, sess, content)


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
