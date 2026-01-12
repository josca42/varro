from fasthtml.common import *

from routes.auth import AUTH_CSS, AUTH_SKIP, config_value
from routes.auth import ar as auth_routes
from routes.index import ar as index_routes

STATIC_SKIP = [
    r"/favicon\.ico",
    r"/static/.*",
    r".*\.css",
    r".*\.js",
]


def require_auth(req, sess):
    auth = sess.get("auth")
    req.scope["auth"] = auth
    if not auth:
        return RedirectResponse("/login", status_code=303)


beforeware = Beforeware(require_auth, skip=AUTH_SKIP + STATIC_SKIP)

app, _ = fast_app(
    before=beforeware,
    hdrs=(Style(AUTH_CSS),),
    secret_key=config_value("SESSION_SECRET"),
)

auth_routes.to_app(app)
index_routes.to_app(app)

serve()
