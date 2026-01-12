from fasthtml.common import *

from varro.db.crud.user import user as user_crud

ar = APIRouter()


@ar("/", methods=["GET"])
def index(auth):
    current_user = user_crud.get_by_id(auth)
    if not current_user:
        return RedirectResponse("/login", status_code=303)
    return Titled(
        "Welcome",
        Card(
            P(f"Signed in as {current_user.email}"),
            A("Log out", href=logout, role="button"),
            cls="auth-card",
        ),
    )


@ar("/logout", methods=["GET"])
def logout(sess):
    sess.pop("auth", None)
    sess.pop("oauth_state", None)
    return RedirectResponse("/login", status_code=303)
