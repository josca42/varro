import hashlib

import mistletoe
from fasthtml.common import APIRouter, A, Button, Div, Form, Input, NotStr, Textarea

from ui.app.layout import AppShell, SettingsPage
from varro.agent.workspace import user_workspace_root
from varro.config import DATA_DIR
from varro.dashboard.public_fs import has_public_dashboard
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
        "# Velkommen til Varro\n\n"
        "Varro er din AI-statistiker til dansk data. "
        "Stil spørgsmål om danske tal i chatten til venstre, "
        "og udforsk dashboards med interaktive grafer og nøgletal.\n\n"
        "## Kom i gang\n\n"
        "1. **Stil et spørgsmål** — brug chatten til venstre til at spørge om dansk statistik\n"
        "2. **Lav dit eget dashboard** — bed Varro om at bygge et dashboard til dig\n\n"
        "3. **Iterer** — forbered dine analyser - i form af annoterede dashboards - og brug dem som skabelon fremadrettet\n"
        "## Dine dashboards\n\n"
        f"{WELCOME_DASHBOARD_TOKEN}\n"
    )


def _welcome_path(user_id: int):
    path = user_workspace_root(user_id) / WELCOME_FILE_NAME
    if not path.exists():
        path.write_text(_default_welcome_markdown(), encoding="utf-8")
    return path


def _dashboard_list_markdown(dashboards: list[str], user_id: int, data_root) -> str:
    if not dashboards:
        return "- _(Ingen dashboards endnu. Spørg Varro i chatten om at bygge et til dig.)_"
    lines = []
    for slug in dashboards:
        line = f"- [{slug}](/dashboard/{slug})"
        if has_public_dashboard(data_root, user_id, slug):
            line += f" — [public](/public/{user_id}/{slug})"
        lines.append(line)
    return "\n".join(lines)


def _render_welcome_page(content: str, dashboards: list[str], user_id: int):
    rendered_md = content.replace(
        WELCOME_DASHBOARD_TOKEN,
        _dashboard_list_markdown(dashboards, user_id, DATA_DIR),
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
    if not req.headers.get("HX-Request"):
        sess.pop("chat_id", None)
    user_id = sess["user_id"]
    welcome_content = _welcome_path(user_id).read_text(encoding="utf-8")
    content = _render_welcome_page(welcome_content, list_dashboards(user_id), user_id)
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
        user_balance=db_user.balance if db_user else None,
    )
    return _app_or_fragment(req, sess, page)
