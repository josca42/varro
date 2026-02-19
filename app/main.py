import argparse
from datetime import timedelta

from fasthtml.common import Beforeware, RedirectResponse, serve

from app.routes.auth import AUTH_SKIP, ar as auth_routes
from app.routes.chat import ar as chat_routes
from app.routes.commands import ar as command_routes
from app.routes.content import ar as content_routes
from ui.app.frontpage import Frontpage
from ui.core import daisy_app
from varro.chat.run_manager import run_manager
from varro.chat.shell_pool import shell_pool
from varro.config import DATA_DIR
from varro.dashboard.routes import mount_dashboard_routes
from varro.db import crud
from varro.db.db import dst_read_engine

STATIC_SKIP = [
    r"/favicon\.ico",
    r"/static/.*",
    r".*\.css",
    r".*\.js",
]

LOGIN_REDIRECT = RedirectResponse("/login", status_code=303)
DEV_USER_ID = 1  # Just for development purposes.


def before(req, sess):
    # auth = req.scope["auth"] = sess.get("auth")
    # if not auth:
    #     return LOGIN_REDIRECT
    auth = DEV_USER_ID
    sess["user_id"] = auth
    req.state.chats = crud.chat.for_user(auth)


beforeware = Beforeware(before, skip=[*STATIC_SKIP, *AUTH_SKIP, r"/"])

app, rt = daisy_app(before=beforeware, live=True)

mount_dashboard_routes(app, DATA_DIR, dst_read_engine)
chat_routes.to_app(app)
command_routes.to_app(app)
content_routes.to_app(app)
auth_routes.to_app(app)


@app.get("/")
def frontpage(sess):
    if sess.get("auth"):
        return RedirectResponse("/app", status_code=303)
    return Frontpage()


@app.on_event("startup")
async def start_chat_cleanup():
    run_manager.start_cleanup_task(retention=timedelta(minutes=5), interval=30)
    shell_pool.start_cleanup_task(ttl=timedelta(minutes=10), interval=60)


@app.on_event("shutdown")
async def stop_chat_cleanup():
    run_manager.stop_cleanup_task()
    shell_pool.stop_cleanup_task()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5001)
    args = parser.parse_args()
    serve(port=args.port)
