from pathlib import Path

from fasthtml.common import Script, RedirectResponse, Beforeware

from ui.core import daisy_app
from varro.db.db import engine
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
    user = crud.user.get(DEMO_USER_ID)

    # Attach scoped instances to request
    req.scope["user"] = user
    req.scope["chats"] = crud.chat.for_user(user.id)


beforeware = Beforeware(before, skip=STATIC_SKIP)

# Create FastHTML app with DaisyUI + Plotly + Alpine.js
app, rt = daisy_app()

# Configure and mount dashboard routes
chat_routes.to_app(app)


@app.get("/")
def index():
    return RedirectResponse("/chat", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5001)
