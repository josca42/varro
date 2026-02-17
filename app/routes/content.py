import hashlib

import mistletoe
from fasthtml.common import APIRouter, A, Button, Div, Form, Input, NotStr, Textarea

from ui.app.layout import AppShell, SettingsPage
from varro.agent.workspace import ensure_user_workspace
from varro.dashboard.routes import list_dashboards
from varro.db import crud

ar = APIRouter()

WELCOME_FILE_NAME = "welcome.md"
WELCOME_DASHBOARD_TOKEN = "{{dashboard_list}}"


def _app_or_fragment(req, sess, content):
    if req.headers.get("HX-Request"):
        return content
    chat = None
    if chat_id := sess.get("chat_id"):
        chat = req.state.chats.get(chat_id, with_turns=True)
    db_user = crud.user.get(sess.get("user_id"))
    return AppShell(
        chat,
        content,
        user_name=db_user.name if db_user else None,
        user_email=db_user.email if db_user else None,
    )


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
        data_slot="app-intro-page",
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
                    "View intro page",
                    href="/app",
                    cls="btn btn-ghost",
                    hx_get="/app",
                    hx_target="#content-panel",
                    hx_swap="innerHTML",
                    hx_push_url="true",
                ),
                cls="flex items-center gap-2",
            ),
            hx_put="/app/code",
            hx_target="#content-panel",
            hx_swap="innerHTML",
            cls="space-y-4",
        ),
        cls="p-6 space-y-4",
        data_slot="app-intro-code-page",
    )


@ar.get("/app")
def app_home(req, sess):
    user_id = sess["user_id"]
    welcome_content = _welcome_path(user_id).read_text(encoding="utf-8")
    content = _render_welcome_page(welcome_content, list_dashboards(user_id))
    return _app_or_fragment(req, sess, content)


@ar.get("/app/code")
def app_code(req, sess):
    user_id = sess["user_id"]
    content = _render_welcome_editor(_welcome_path(user_id).read_text(encoding="utf-8"))
    return _app_or_fragment(req, sess, content)


@ar.put("/app/code")
async def app_code_save(req, sess):
    user_id = sess["user_id"]
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


@ar.get("/settings")
def settings(req, sess):
    db_user = crud.user.get(sess.get("user_id"))
    page = SettingsPage(
        user_name=db_user.name if db_user else None,
        user_email=db_user.email if db_user else None,
    )
    return _app_or_fragment(req, sess, page)
