import argparse
from datetime import timedelta
from pathlib import Path

from fasthtml.common import Beforeware, serve

from ui.core import daisy_app
from ui.app.layout import AppShell, WelcomePage, OverviewPage, SettingsPage
from varro.dashboard.routes import mount_dashboard_routes
from varro.db.db import engine
from app.routes.chat import ar as chat_routes
from app.routes.commands import ar as command_routes
from varro.chat.session import sessions
from varro.db import crud
from varro.agent.workspace import ensure_user_workspace

STATIC_SKIP = [
    r"/favicon\.ico",
    r"/static/.*",
    r".*\.css",
    r".*\.js",
]

DEMO_USER_ID = 1


def before(req, sess):
    user_id = sess.get("user_id", DEMO_USER_ID)
    sess["user_id"] = user_id
    ensure_user_workspace(user_id)
    req.state.chats = crud.chat.for_user(user_id)


beforeware = Beforeware(before, skip=STATIC_SKIP)

app, rt = daisy_app(exts="ws", before=beforeware, live=True)

mount_dashboard_routes(app, Path("example_dashboard_folder"), engine)
chat_routes.to_app(app)
command_routes.to_app(app)


def _app_or_fragment(req, sess, content):
    if req.headers.get("HX-Request"):
        return content
    chat = None
    if chat_id := sess.get("chat_id"):
        chat = req.state.chats.get(chat_id, with_turns=True)
    return AppShell(chat, content)


@app.get("/")
def index(req, sess):
    return _app_or_fragment(req, sess, WelcomePage())


@app.get("/dash/overview")
def dash_overview(req, sess):
    return _app_or_fragment(req, sess, OverviewPage())


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
