"""dashboard.routes

FastHTML routes for dashboards with on-demand loading.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlencode, urlsplit

from fasthtml.common import (
    APIRouter,
    A,
    Button,
    Div,
    Form,
    H3,
    Input,
    P,
    RedirectResponse,
    Response,
    Textarea,
)
from sqlalchemy.engine import Engine

from varro.dashboard.loader import Dashboard, load_dashboard
from varro.dashboard.executor import (
    clear_query_cache,
    execute_options_query,
    execute_output,
    SelectOption,
)
from varro.dashboard.components import (
    render_shell,
    render_metric_card,
    render_table,
    render_figure,
)
from varro.dashboard.filters import Filter, SelectFilter
from varro.dashboard.public_fs import (
    copy_dashboard_source,
    has_public_dashboard,
    next_fork_slug,
    public_dashboard_dir,
)
from varro.db import crud
from ui.app.layout import AppShell

_dashboards_root: Path | None = None
_engine: Engine | None = None


@dataclass
class CachedDashboard:
    dashboard: Dashboard
    mtimes: tuple[float, ...]


_cache: dict[tuple[str, int, str], CachedDashboard] = {}

ar = APIRouter()


def configure(dashboards_root: Path | str, engine: Engine) -> None:
    global _dashboards_root, _engine, _cache
    _dashboards_root = Path(dashboards_root)
    _engine = engine
    _cache = {}


def mount_dashboard_routes(app, dashboards_root: Path | str, engine: Engine) -> None:
    configure(dashboards_root, engine)
    ar.to_app(app)


def _session_user_id(sess) -> int | None:
    auth = sess.get("auth")
    if auth is None:
        auth = sess.get("user_id")
    if auth is None:
        return None
    return int(auth)


def _private_dashboards_dir(user_id: int) -> Path | None:
    if _dashboards_root is None:
        return None
    return _dashboards_root / "user" / str(user_id) / "dashboard"


def _public_dashboards_dir(owner_id: int) -> Path | None:
    if _dashboards_root is None:
        return None
    return _dashboards_root / "public" / str(owner_id)


def _dashboard_mtimes(folder: Path) -> tuple[float, ...]:
    queries_dir = folder / "queries"
    files = [folder / "dashboard.md", folder / "outputs.py"]
    if queries_dir.exists() and queries_dir.is_dir():
        files.extend(sorted(queries_dir.glob("*.sql")))
    return tuple(f.stat().st_mtime for f in files)


def _load_cached_dashboard(
    scope: str,
    owner_id: int,
    name: str,
    folder: Path,
) -> Dashboard:
    cache_key = (scope, owner_id, name)
    mtimes = _dashboard_mtimes(folder)
    cached = _cache.get(cache_key)
    if cached and cached.mtimes == mtimes:
        return cached.dashboard

    clear_query_cache()
    dash = load_dashboard(folder)
    _cache[cache_key] = CachedDashboard(dashboard=dash, mtimes=mtimes)
    return dash


def list_dashboards(user_id: int) -> list[str]:
    path = _private_dashboards_dir(user_id)
    if path is None or not path.exists():
        return []
    slugs = []
    for folder in sorted(path.iterdir()):
        if folder.is_dir() and (folder / "dashboard.md").exists():
            slugs.append(folder.name)
    return slugs


def get_dashboard(name: str, user_id: int) -> Dashboard | None:
    dashboards_dir = _private_dashboards_dir(user_id)
    if dashboards_dir is None:
        return None
    folder = dashboards_dir / name
    if not (folder / "dashboard.md").exists():
        return None
    return _load_cached_dashboard("private", user_id, name, folder)


def get_public_dashboard(name: str, owner_id: int) -> Dashboard | None:
    dashboards_dir = _public_dashboards_dir(owner_id)
    if dashboards_dir is None:
        return None
    folder = dashboards_dir / name
    if not (folder / "dashboard.md").exists():
        return None
    return _load_cached_dashboard("public", owner_id, name, folder)


def _dashboard_dir(name: str, user_id: int) -> Path | None:
    dashboards_dir = _private_dashboards_dir(user_id)
    if dashboards_dir is None:
        return None
    folder = dashboards_dir / name
    if not (folder / "dashboard.md").exists():
        return None
    return folder


def _public_dashboard_source_dir(owner_id: int, name: str) -> Path | None:
    dashboards_dir = _public_dashboards_dir(owner_id)
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

    db_user = None
    if user_id := _session_user_id(sess):
        db_user = crud.user.get(user_id)

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
    values = {}
    for f in filters:
        values.update(f.parse_query_params(req.query_params))
    return values


def build_filter_url(
    base_path: str,
    values: dict[str, Any],
    filters: list[Filter],
) -> str:
    params: dict[str, str] = {}
    for f in filters:
        params.update(f.url_params(values))
    if params:
        return f"{base_path}?{urlencode(params)}"
    return base_path


def _dashboard_content(dash: Dashboard, req, base_path: str):
    filters = parse_filters_from_request(req, dash.filters)
    options: dict[str, list[SelectOption]] = {}
    for f in dash.filters:
        if isinstance(f, SelectFilter) and f.options_query:
            options[f.name] = execute_options_query(dash, f, _engine)
    return Div(render_shell(dash, filters, options, base_path=base_path))


def _render_output_fragment(dash: Dashboard, output_name: str, req, renderer):
    filters = parse_filters_from_request(req, dash.filters)
    try:
        result = execute_output(dash, output_name, filters, _engine)
        return renderer(result)
    except Exception:
        return None


def _match_private_dashboard_path(path: str) -> str | None:
    match = re.match(r"^/dashboard/([^/]+)$", path)
    if not match:
        return None
    return unquote(match.group(1))


def _match_public_dashboard_path(path: str) -> tuple[int, str] | None:
    match = re.match(r"^/public/([0-9]+)/([^/]+)$", path)
    if not match:
        return None
    return int(match.group(1)), unquote(match.group(2))


def _context_path(url: str) -> str:
    value = (url or "").strip()
    if not value:
        return ""
    parsed = urlsplit(value)
    if parsed.scheme or parsed.netloc:
        return ""
    return parsed.path


@ar("/public/_/context-action", methods=["GET"])
def navbar_context_action(url: str = "", sess=None):
    path = _context_path(url)
    if not path:
        return ""
    if path.endswith("/code"):
        return ""

    user_id = _session_user_id(sess) if sess else None
    private_slug = _match_private_dashboard_path(path)
    if private_slug:
        if user_id is None or _dashboards_root is None:
            return ""
        if _dashboard_dir(private_slug, user_id=user_id) is None:
            return ""

        label = "Opdater" if has_public_dashboard(_dashboards_root, user_id, private_slug) else "Publicer"
        return Form(
            Button(label, type="submit", cls="btn btn-primary btn-sm"),
            hx_post=f"/dashboard/{private_slug}/publish",
            hx_target="body",
            hx_swap="beforeend",
            **{
                "hx-on::after-request": "window.__varroRefreshNavbarContextAction && window.__varroRefreshNavbarContextAction()",
            },
        )

    public_match = _match_public_dashboard_path(path)
    if public_match:
        owner_id, slug = public_match
        if _public_dashboard_source_dir(owner_id, slug) is None:
            return ""
        return A("Rediger", href=f"/public/{owner_id}/{slug}/fork", cls="btn btn-primary btn-sm")

    return ""


@ar("/dashboard/{name}", methods=["GET"])
def dashboard_shell(name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)

    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _dashboard_content(dash, req, base_path=f"/dashboard/{name}")
    return _shell_or_fragment(req, sess, content)


@ar("/public/{owner_id}/{name}", methods=["GET"])
def public_dashboard_shell(owner_id: int, name: str, req, sess):
    dash = get_public_dashboard(name, owner_id=owner_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _dashboard_content(dash, req, base_path=f"/public/{owner_id}/{name}")
    return _shell_or_fragment(req, sess, content)


@ar("/dashboard/{name}/code", methods=["GET"])
def dashboard_code(name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)

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
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)

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
    _cache.pop(("private", user_id, name), None)
    clear_query_cache()

    content = _render_dashboard_code_editor(name, files, selected_file, next_content)
    return _shell_or_fragment(req, sess, content)


def _publish_modal(slug, user_id, is_update):
    path = f"/public/{user_id}/{slug}"
    url = f"https://varro.dk{path}"
    title = "Dashboard opdateret!" if is_update else "Dashboard publiceret!"
    return Div(
        Div(
            Div(cls="fixed inset-0 bg-black/30 z-40", **{"x-dialog:overlay": True}),
            Div(
                Div(
                    H3(title, cls="text-lg font-semibold", **{"x-dialog:title": True}),
                    P(A(url, href=path, target="_blank", cls="link link-primary break-all"), cls="py-2"),
                    Div(
                        Button("Kopier link", type="button", cls="btn btn-sm btn-outline",
                               **{"@click": f"navigator.clipboard.writeText('{url}')"}),
                        Button("Luk", type="button", cls="btn btn-sm btn-primary",
                               **{"@click": "$dialog.close()"}),
                        cls="flex gap-2 justify-end",
                    ),
                    cls="bg-base-100 rounded-xl p-6 shadow-lg w-full max-w-sm space-y-2",
                ),
                cls="fixed inset-0 z-50 flex items-center justify-center p-4",
                **{"x-dialog:panel": True},
            ),
            **{"x-dialog": True, "x-model": "open"},
        ),
        x_data="{ open: true }",
        **{"x-effect": "if (!open) $el.remove()"},
    )


@ar("/dashboard/{name}/publish", methods=["POST"])
def publish_dashboard(name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)
    if _dashboards_root is None:
        return Response("Dashboard root not configured", status_code=500)

    source_dir = _dashboard_dir(name, user_id=user_id)
    if source_dir is None:
        return Response("Dashboard not found", status_code=404)

    is_update = has_public_dashboard(_dashboards_root, user_id, name)
    destination_dir = public_dashboard_dir(_dashboards_root, user_id, name)
    copy_dashboard_source(source_dir, destination_dir)
    _cache.pop(("public", user_id, name), None)

    if req.headers.get("HX-Request"):
        return _publish_modal(name, user_id, is_update)
    return RedirectResponse(f"/dashboard/{name}", status_code=303)


@ar("/public/{owner_id}/{name}/fork", methods=["GET"])
def fork_public_dashboard(owner_id: int, name: str, sess):
    source_dir = _public_dashboard_source_dir(owner_id, name)
    if source_dir is None:
        return Response("Dashboard not found", status_code=404)

    user_id = _session_user_id(sess)
    if user_id is None:
        next_url = f"/public/{owner_id}/{name}/fork"
        return RedirectResponse(
            f"/login?{urlencode({'next': next_url})}",
            status_code=303,
        )

    private_dir = _private_dashboards_dir(user_id)
    if private_dir is None:
        return Response("Dashboard root not configured", status_code=500)
    private_dir.mkdir(parents=True, exist_ok=True)

    fork_slug = next_fork_slug(private_dir, name)
    destination_dir = private_dir / fork_slug
    copy_dashboard_source(source_dir, destination_dir)
    _cache.pop(("private", user_id, fork_slug), None)

    return RedirectResponse(f"/dashboard/{fork_slug}", status_code=303)


@ar("/dashboard/{name}/_/filters", methods=["GET"])
def filter_sync(name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)

    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)
    url = build_filter_url(f"/dashboard/{name}", filters, dash.filters)
    return Response(
        "",
        headers={
            "HX-Replace-Url": url,
            "HX-Trigger": '{"filtersChanged": {}}',
        },
    )


@ar("/public/{owner_id}/{name}/_/filters", methods=["GET"])
def public_filter_sync(owner_id: int, name: str, req):
    dash = get_public_dashboard(name, owner_id=owner_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    filters = parse_filters_from_request(req, dash.filters)
    url = build_filter_url(f"/public/{owner_id}/{name}", filters, dash.filters)
    return Response(
        "",
        headers={
            "HX-Replace-Url": url,
            "HX-Trigger": '{"filtersChanged": {}}',
        },
    )


@ar("/dashboard/{name}/_/figure/{output_name}", methods=["GET"])
def render_figure_endpoint(name: str, output_name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _render_output_fragment(dash, output_name, req, render_figure)
    if content is None:
        return Div("Error loading chart", cls="text-error text-center p-4")
    return content


@ar("/public/{owner_id}/{name}/_/figure/{output_name}", methods=["GET"])
def render_public_figure_endpoint(owner_id: int, name: str, output_name: str, req):
    dash = get_public_dashboard(name, owner_id=owner_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _render_output_fragment(dash, output_name, req, render_figure)
    if content is None:
        return Div("Error loading chart", cls="text-error text-center p-4")
    return content


@ar("/dashboard/{name}/_/table/{output_name}", methods=["GET"])
def render_table_endpoint(name: str, output_name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _render_output_fragment(dash, output_name, req, render_table)
    if content is None:
        return Div("Error loading table", cls="text-error text-center p-4")
    return content


@ar("/public/{owner_id}/{name}/_/table/{output_name}", methods=["GET"])
def render_public_table_endpoint(owner_id: int, name: str, output_name: str, req):
    dash = get_public_dashboard(name, owner_id=owner_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _render_output_fragment(dash, output_name, req, render_table)
    if content is None:
        return Div("Error loading table", cls="text-error text-center p-4")
    return content


@ar("/dashboard/{name}/_/metric/{output_name}", methods=["GET"])
def render_metric_endpoint(name: str, output_name: str, req, sess):
    user_id = _session_user_id(sess)
    if user_id is None:
        return Response("Unauthorized", status_code=401)
    dash = get_dashboard(name, user_id=user_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _render_output_fragment(dash, output_name, req, render_metric_card)
    if content is None:
        return Div("Error loading metric", cls="text-error text-center p-4")
    return content


@ar("/public/{owner_id}/{name}/_/metric/{output_name}", methods=["GET"])
def render_public_metric_endpoint(owner_id: int, name: str, output_name: str, req):
    dash = get_public_dashboard(name, owner_id=owner_id)
    if not dash:
        return Response("Dashboard not found", status_code=404)

    content = _render_output_fragment(dash, output_name, req, render_metric_card)
    if content is None:
        return Div("Error loading metric", cls="text-error text-center p-4")
    return content
