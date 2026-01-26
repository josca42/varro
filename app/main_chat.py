from fasthtml.common import RedirectResponse, Beforeware, serve

from ui.core import daisy_app
from app.routes.chat import ar as chat_routes
from varro.db import crud

STATIC_SKIP = [
    r"/favicon\.ico",
    r"/static/.*",
    r".*\.css",
    r".*\.js",
]

DEMO_USER_ID = 1


def before(req, sess):
    """Beforeware to inject user and scoped CRUD."""
    user_id = sess.get("user_id", DEMO_USER_ID)
    sess["user_id"] = user_id
    req.state.chats = crud.chat.for_user(user_id)


beforeware = Beforeware(before, skip=STATIC_SKIP)

app, rt = daisy_app(exts="ws", before=beforeware, live=True)

chat_routes.to_app(app)


@app.get("/")
def index():
    return RedirectResponse("/chat", status_code=303)


serve()
