import argparse
import hashlib
from datetime import timedelta

import mistletoe
from fasthtml.common import A, Beforeware, Button, Div, Form, Input, NotStr, Textarea, serve

from ui.core import daisy_app
from ui.app.layout import AppShell, SettingsPage
from varro.dashboard.routes import mount_dashboard_routes, list_dashboards
from varro.db.db import engine
from app.routes.chat import ar as chat_routes
from app.routes.commands import ar as command_routes
from varro.chat.session import sessions
from varro.db import crud
from varro.agent.workspace import ensure_user_workspace
from varro.config import DATA_DIR

STATIC_SKIP = [
    r"/favicon\.ico",
    r"/static/.*",
    r".*\.css",
    r".*\.js",
]

DEMO_USER_ID = 1
WELCOME_FILE_NAME = "welcome.md"
WELCOME_DASHBOARD_TOKEN = "{{dashboard_list}}"


def before(req, sess):
    user_id = sess.get("user_id", DEMO_USER_ID)
    sess["user_id"] = user_id
    ensure_user_workspace(user_id)
    req.state.chats = crud.chat.for_user(user_id)


beforeware = Beforeware(before, skip=STATIC_SKIP)

app, rt = daisy_app(exts="ws", before=beforeware, live=True)

mount_dashboard_routes(app, DATA_DIR, engine)
chat_routes.to_app(app)
command_routes.to_app(app)


def _app_or_fragment(req, sess, content):
    if req.headers.get("HX-Request"):
        return content
    chat = None
    if chat_id := sess.get("chat_id"):
        chat = req.state.chats.get(chat_id, with_turns=True)
    return AppShell(chat, content)


def _content_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def _default_welcome_markdown() -> str:
    return (
        "# Welcome to Varro\n\n"
        "This page is markdown-first. Edit it from the Code tab.\n\n"
        "## Dashboards\n\n"
        f"{WELCOME_DASHBOARD_TOKEN}\n"
    )


def _welcome_path(user_id: int):
    path = ensure_user_workspace(user_id) / WELCOME_FILE_NAME
    if not path.exists():
        path.write_text(_default_welcome_markdown(), encoding="utf-8")
    return path


def _dashboard_list_markdown(dashboards: list[str]) -> str:
    if not dashboards:
        return "- _(No dashboards found for this user.)_"
    return "\n".join(f"- [{slug}](/dashboard/{slug})" for slug in dashboards)


def _render_welcome_page(content: str, dashboards: list[str]):
    rendered_md = content.replace(
        WELCOME_DASHBOARD_TOKEN,
        _dashboard_list_markdown(dashboards),
    )
    html = mistletoe.markdown(rendered_md)
    return Div(
        Div(NotStr(html), cls="prose prose-sm max-w-none"),
        cls="p-6",
        data_slot="welcome-page",
    )


def _render_welcome_editor(content: str):
    return Div(
        Form(
            Input(type="hidden", name="file_hash", value=_content_hash(content)),
            Textarea(
                content,
                name="content",
                cls="textarea textarea-bordered w-full font-mono text-sm min-h-[28rem]",
            ),
            Div(
                Button("Save", type="submit", cls="btn btn-primary"),
                A(
                    "View welcome page",
                    href="/",
                    cls="btn btn-ghost",
                    hx_get="/",
                    hx_target="#content-panel",
                    hx_swap="innerHTML",
                    hx_push_url="true",
                ),
                cls="flex items-center gap-2",
            ),
            hx_put="/welcome/code",
            hx_target="#content-panel",
            hx_swap="innerHTML",
            cls="space-y-4",
        ),
        cls="p-6 space-y-4",
        data_slot="welcome-code-page",
    )


@app.get("/")
def index(req, sess):
    user_id = sess.get("user_id", DEMO_USER_ID)
    welcome_content = _welcome_path(user_id).read_text(encoding="utf-8")
    content = _render_welcome_page(welcome_content, list_dashboards(user_id))
    return _app_or_fragment(req, sess, content)


@app.get("/welcome/code")
def welcome_code(req, sess):
    user_id = sess.get("user_id", DEMO_USER_ID)
    content = _render_welcome_editor(_welcome_path(user_id).read_text(encoding="utf-8"))
    return _app_or_fragment(req, sess, content)


@app.put("/welcome/code")
async def welcome_code_save(req, sess):
    user_id = sess.get("user_id", DEMO_USER_ID)
    path = _welcome_path(user_id)
    current_content = path.read_text(encoding="utf-8")
    form = await req.form()
    form_hash = str(form.get("file_hash", ""))
    next_content = str(form.get("content", "")).replace("\r\n", "\n")

    if form_hash != _content_hash(current_content):
        content = _render_welcome_editor(current_content)
        return _app_or_fragment(req, sess, content)

    path.write_text(next_content, encoding="utf-8")
    content = _render_welcome_editor(next_content)
    return _app_or_fragment(req, sess, content)


@app.get("/settings")
def settings(req, sess):
    return _app_or_fragment(req, sess, SettingsPage())


@app.on_event("startup")
async def start_session_cleanup():
    sessions.start_cleanup_task(ttl=timedelta(minutes=20), interval=60)


@app.on_event("shutdown")
async def stop_session_cleanup():
    sessions.stop_cleanup_task()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5001)
    args = parser.parse_args()
    serve(port=args.port)
