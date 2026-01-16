from pathlib import Path

from fasthtml.common import Script, RedirectResponse

from ui import daisy_app
from varro.dashboard import dashboard_routes, configure_dashboards
from varro.db.db import engine

# Auth imports (commented out)
# from routes.auth import AUTH_CSS, AUTH_SKIP, config_value
# from routes.auth import ar as auth_routes
# from routes.index import ar as index_routes

# STATIC_SKIP = [
#     r"/favicon\.ico",
#     r"/static/.*",
#     r".*\.css",
#     r".*\.js",
# ]

# def require_auth(req, sess):
#     auth = sess.get("auth")
#     req.scope["auth"] = auth
#     if not auth:
#         return RedirectResponse("/login", status_code=303)

# beforeware = Beforeware(require_auth, skip=AUTH_SKIP + STATIC_SKIP)

# Create FastHTML app with DaisyUI + Plotly + Alpine.js
# To re-enable auth, uncomment beforeware and add: before=beforeware, secret_key=config_value("SESSION_SECRET")
app, rt = daisy_app()

# Auth routes (commented out)
# auth_routes.to_app(app)
# index_routes.to_app(app)

# Configure and mount dashboard routes
configure_dashboards(Path("example_dashboard_folder"), engine)
dashboard_routes.to_app(app)


@app.get("/")
def index():
    return RedirectResponse("/dash/sales", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5001)
