import base64
import hashlib
import hmac
import json
import os
import secrets
import time

import resend
from fasthtml.common import APIRouter, RedirectResponse
from fasthtml.oauth import GoogleAppClient, redir_url

from ui.app import (
    AuthFormCard,
    AuthSimpleCard,
    AuthNotices,
    AuthLinks,
    AuthGoogleCta,
    AuthLoginForm,
    AuthSignupForm,
    AuthVerificationResendForm,
    AuthPasswordResetForm,
    AuthPasswordResetConfirmForm,
)
from ui.components import Link, LinkButton

from varro.config import settings
from varro.db.crud.user import user as user_crud
from varro.db.models.user import User

GOOGLE_SCOPE = "openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
VERIFY_TTL_SECONDS = 60 * 60 * 24
RESET_TTL_SECONDS = 60 * 60

AUTH_SKIP = [
    r"/login",
    r"/signup",
    r"/logout",
    r"/auth/.*",
    r"/verify-email.*",
    r"/password-reset.*",
]

ERROR_MESSAGES = {
    "missing_fields": "Email and password are required.",
    "missing_email": "Email is required.",
    "missing_password": "Password is required.",
    "invalid_credentials": "Invalid email or password.",
    "email_exists": "An account with this email already exists.",
    "oauth_only": "This email is linked to Google login. Use Google to sign in.",
    "invalid_token": "This link is invalid or expired.",
    "oauth_state": "Login session expired. Please try again.",
    "oauth_failed": "Google login failed. Please try again.",
    "oauth_email": "Google did not return an email address.",
    "oauth_unverified": "Google account email is not verified.",
    "account_inactive": "This account is disabled or not verified.",
    "google_not_configured": "Google login is not configured.",
}

INFO_MESSAGES = {
    "verify_sent": "Check your email to verify your account.",
    "email_verified": "Email verified. You can sign in.",
    "reset_sent": "If the email exists, a reset link is on the way.",
    "password_updated": "Password updated. You can sign in.",
}

ar = APIRouter()


def config_value(key: str) -> str | None:
    return settings.get(key) or os.environ.get(key)


def auth_notices(error_code: str | None, info_code: str | None):
    error = ERROR_MESSAGES.get(error_code) if error_code else None
    info = INFO_MESSAGES.get(info_code) if info_code else None
    if error_code and not error:
        error = "Something went wrong. Please try again."
    return error, info


def google_settings():
    return (
        config_value("GOOGLE_CLIENT_ID"),
        config_value("GOOGLE_CLIENT_SECRET"),
        config_value("GOOGLE_PROJECT_ID"),
    )


def google_enabled() -> bool:
    client_id, client_secret, _ = google_settings()
    return bool(client_id and client_secret)


def google_client() -> GoogleAppClient | None:
    client_id, client_secret, project_id = google_settings()
    if not client_id or not client_secret:
        return None
    return GoogleAppClient(
        client_id=client_id,
        client_secret=client_secret,
        code=None,
        scope=GOOGLE_SCOPE,
        project_id=project_id,
    )


def oauth_redirect_uri(req) -> str:
    scheme = config_value("OAUTH_SCHEME") or req.url.scheme
    return redir_url(req, "/auth/google/callback", scheme)


def token_secret() -> str:
    secret = config_value("AUTH_TOKEN_SECRET") or config_value("SESSION_SECRET")
    if not secret:
        raise RuntimeError("AUTH_TOKEN_SECRET or SESSION_SECRET is required.")
    return secret


def _b64encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def _b64decode(data: str) -> bytes:
    pad = "=" * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + pad)


def make_token(user: User, purpose: str, ttl_seconds: int) -> str:
    payload = {
        "uid": user.id,
        "email": user.email,
        "purpose": purpose,
        "exp": int(time.time()) + ttl_seconds,
    }
    body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    sig = hmac.new(token_secret().encode(), body, hashlib.sha256).digest()
    return f"{_b64encode(body)}.{_b64encode(sig)}"


def verify_token(token: str | None, purpose: str) -> dict | None:
    if not token or "." not in token:
        return None
    body_b64, sig_b64 = token.split(".", 1)
    try:
        body = _b64decode(body_b64)
        sig = _b64decode(sig_b64)
        payload = json.loads(body)
    except Exception:
        return None
    expected = hmac.new(token_secret().encode(), body, hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected):
        return None
    if payload.get("purpose") != purpose:
        return None
    if payload.get("exp", 0) < int(time.time()):
        return None
    return payload


def app_base_url(req) -> str:
    base_url = config_value("APP_BASE_URL")
    if base_url:
        return base_url.rstrip("/")
    return f"{req.url.scheme}://{req.headers['host']}"


def send_email(to_email: str, subject: str, text: str, html: str | None = None):
    api_key = config_value("RESEND_API_KEY")
    sender = config_value("RESEND_FROM")
    if not api_key or not sender:
        print(f"Email config missing: api_key={bool(api_key)}, sender={bool(sender)}")
        return
    resend.api_key = api_key
    params: resend.Emails.SendParams = {
        "from": sender,
        "to": [to_email],
        "subject": subject,
        "text": text,
    }
    if html:
        params["html"] = html
    resend.Emails.send(params)


def send_verification_email(db_user: User, req):
    token = make_token(db_user, "verify", VERIFY_TTL_SECONDS)
    link = f"{app_base_url(req)}/verify-email?token={token}"
    greeting = f"Hi {db_user.name}," if db_user.name else "Hi,"
    text = f"""{greeting}

Please verify your email by visiting:
{link}

If you did not request this, you can ignore this email.
"""
    send_email(db_user.email, "Verify your email", text)


def send_password_reset_email(db_user: User, req):
    token = make_token(db_user, "reset", RESET_TTL_SECONDS)
    link = f"{app_base_url(req)}/password-reset/confirm?token={token}"
    greeting = f"Hi {db_user.name}," if db_user.name else "Hi,"
    text = f"""{greeting}

Reset your password by visiting:
{link}

If you did not request this, you can ignore this email.
"""
    send_email(db_user.email, "Reset your password", text)


@ar("/login", methods=["GET"])
def login(sess, error: str | None = None, info: str | None = None):
    if sess.get("auth"):
        return RedirectResponse("/", status_code=303)
    error_msg, info_msg = auth_notices(error, info)
    links = AuthLinks(
        Link("Need an account? Sign up", href=signup),
        Link("Forgot password?", href=password_reset),
        Link("Resend verification", href=verify_email_resend),
    )
    return AuthFormCard(
        "Sign in",
        AuthLoginForm(login_post),
        subtitle="Log in to your account",
        notices=AuthNotices(error_msg, info_msg),
        oauth_cta=AuthGoogleCta(google_enabled(), auth_google),
        links=links,
    )


@ar("/login", methods=["POST"])
def login_post(email: str | None = None, password: str | None = None, sess=None):
    if not email or not password:
        return RedirectResponse(login.to(error="missing_fields"), status_code=303)
    email = email.strip().lower()
    db_user = user_crud.get_by_email(email)
    if not db_user:
        return RedirectResponse(login.to(error="invalid_credentials"), status_code=303)
    if not db_user.is_active:
        return RedirectResponse(login.to(error="account_inactive"), status_code=303)
    if not db_user.password_hash:
        return RedirectResponse(login.to(error="oauth_only"), status_code=303)
    if not user_crud.verify_password(password, db_user.password_hash):
        return RedirectResponse(login.to(error="invalid_credentials"), status_code=303)
    sess["auth"] = db_user.id
    return RedirectResponse("/", status_code=303)


@ar("/signup", methods=["GET"])
def signup(sess, error: str | None = None, info: str | None = None):
    if sess.get("auth"):
        return RedirectResponse("/", status_code=303)
    error_msg, info_msg = auth_notices(error, info)
    links = AuthLinks(
        Link("Already have an account? Sign in", href=login),
        Link("Resend verification", href=verify_email_resend),
    )
    return AuthFormCard(
        "Create account",
        AuthSignupForm(signup_post),
        subtitle="Start exploring Danish statistics",
        notices=AuthNotices(error_msg, info_msg),
        oauth_cta=AuthGoogleCta(google_enabled(), auth_google),
        links=links,
    )


@ar("/signup", methods=["POST"])
def signup_post(
    req,
    email: str | None = None,
    password: str | None = None,
    name: str | None = None,
    sess=None,
):
    if not email or not password:
        return RedirectResponse(signup.to(error="missing_fields"), status_code=303)
    email = email.strip().lower()
    existing = user_crud.get_by_email(email)
    if existing:
        if not existing.is_active and existing.password_hash:
            send_verification_email(existing, req)
            return RedirectResponse(login.to(info="verify_sent"), status_code=303)
        if not existing.password_hash:
            return RedirectResponse(signup.to(error="oauth_only"), status_code=303)
        return RedirectResponse(signup.to(error="email_exists"), status_code=303)
    new_user = user_crud.create_with_password(
        email=email,
        password=password,
        name=name,
        is_active=False,
    )
    send_verification_email(new_user, req)
    return RedirectResponse(login.to(info="verify_sent"), status_code=303)


@ar("/verify-email", methods=["GET"])
def verify_email(token: str | None = None):
    payload = verify_token(token, "verify")
    if not payload:
        return AuthSimpleCard(
            "Email verification",
            *AuthNotices(ERROR_MESSAGES["invalid_token"], None),
            LinkButton(
                "Resend verification",
                href=verify_email_resend,
                variant="outline",
            ),
        )
    db_user = user_crud.get(payload.get("uid"))
    if not db_user or db_user.email != payload.get("email"):
        return AuthSimpleCard(
            "Email verification",
            *AuthNotices(ERROR_MESSAGES["invalid_token"], None),
            LinkButton(
                "Resend verification",
                href=verify_email_resend,
                variant="outline",
            ),
        )
    if not db_user.is_active:
        db_user.is_active = True
        user_crud.update(db_user)
    return RedirectResponse(login.to(info="email_verified"), status_code=303)


@ar("/verify-email/resend", methods=["GET"])
def verify_email_resend(error: str | None = None, info: str | None = None):
    error_msg, info_msg = auth_notices(error, info)
    links = AuthLinks(Link("Back to sign in", href=login))
    return AuthFormCard(
        "Resend verification",
        AuthVerificationResendForm(verify_email_resend_post),
        notices=AuthNotices(error_msg, info_msg),
        links=links,
    )


@ar("/verify-email/resend", methods=["POST"])
def verify_email_resend_post(req, email: str | None = None):
    if not email:
        return RedirectResponse(
            verify_email_resend.to(error="missing_email"), status_code=303
        )
    email = email.strip().lower()
    db_user = user_crud.get_by_email(email)
    if db_user and db_user.password_hash and not db_user.is_active:
        send_verification_email(db_user, req)
    return RedirectResponse(verify_email_resend.to(info="verify_sent"), status_code=303)


@ar("/password-reset", methods=["GET"])
def password_reset(error: str | None = None, info: str | None = None):
    error_msg, info_msg = auth_notices(error, info)
    links = AuthLinks(
        Link("Back to sign in", href=login),
        Link("Need an account? Sign up", href=signup),
    )
    return AuthFormCard(
        "Reset password",
        AuthPasswordResetForm(password_reset_post),
        notices=AuthNotices(error_msg, info_msg),
        links=links,
    )


@ar("/password-reset", methods=["POST"])
def password_reset_post(req, email: str | None = None):
    if not email:
        return RedirectResponse(password_reset.to(error="missing_email"), status_code=303)
    email = email.strip().lower()
    db_user = user_crud.get_by_email(email)
    if db_user and db_user.password_hash:
        send_password_reset_email(db_user, req)
    return RedirectResponse(password_reset.to(info="reset_sent"), status_code=303)


@ar("/password-reset/confirm", methods=["GET"])
def password_reset_confirm(
    token: str | None = None,
    error: str | None = None,
):
    payload = verify_token(token, "reset")
    if not payload:
        return AuthSimpleCard(
            "Reset password",
            *AuthNotices(ERROR_MESSAGES["invalid_token"], None),
            LinkButton(
                "Request a new reset link",
                href=password_reset,
                variant="outline",
            ),
        )
    error_msg, info_msg = auth_notices(error, None)
    links = AuthLinks(Link("Back to sign in", href=login))
    return AuthFormCard(
        "Reset password",
        AuthPasswordResetConfirmForm(password_reset_confirm_post, token),
        notices=AuthNotices(error_msg, info_msg),
        links=links,
    )


@ar("/password-reset/confirm", methods=["POST"])
def password_reset_confirm_post(
    token: str | None = None,
    password: str | None = None,
):
    if not token:
        return AuthSimpleCard(
            "Reset password",
            *AuthNotices(ERROR_MESSAGES["invalid_token"], None),
            LinkButton(
                "Request a new reset link",
                href=password_reset,
                variant="outline",
            ),
        )
    if not password:
        return RedirectResponse(
            password_reset_confirm.to(token=token, error="missing_password"),
            status_code=303,
        )
    payload = verify_token(token, "reset")
    if not payload:
        return AuthSimpleCard(
            "Reset password",
            *AuthNotices(ERROR_MESSAGES["invalid_token"], None),
            LinkButton(
                "Request a new reset link",
                href=password_reset,
                variant="outline",
            ),
        )
    db_user = user_crud.get(payload.get("uid"))
    if not db_user or db_user.email != payload.get("email"):
        return AuthSimpleCard(
            "Reset password",
            *AuthNotices(ERROR_MESSAGES["invalid_token"], None),
            LinkButton(
                "Request a new reset link",
                href=password_reset,
                variant="outline",
            ),
        )
    db_user.password_hash = user_crud.hash_password(password)
    user_crud.update(db_user)
    return RedirectResponse(login.to(info="password_updated"), status_code=303)


@ar("/auth/google", methods=["GET"])
def auth_google(req, sess):
    client = google_client()
    if not client:
        return RedirectResponse(login.to(error="google_not_configured"), status_code=303)
    state = secrets.token_urlsafe(16)
    sess["oauth_state"] = state
    login_url = client.login_link(
        oauth_redirect_uri(req),
        scope=GOOGLE_SCOPE,
        state=state,
    )
    return RedirectResponse(login_url, status_code=303)


@ar("/auth/google/callback", methods=["GET"])
def auth_google_callback(
    req,
    sess,
    code: str | None = None,
    state: str | None = None,
    error: str | None = None,
):
    if error or not code:
        return RedirectResponse(login.to(error="oauth_failed"), status_code=303)
    if state != sess.get("oauth_state"):
        return RedirectResponse(login.to(error="oauth_state"), status_code=303)
    sess.pop("oauth_state", None)
    client = google_client()
    if not client:
        return RedirectResponse(login.to(error="google_not_configured"), status_code=303)
    info = client.retr_info(code, oauth_redirect_uri(req))
    email = info.get("email") if info else None
    if not email:
        return RedirectResponse(login.to(error="oauth_email"), status_code=303)
    email = email.strip().lower()
    verified = info.get("email_verified") if info else None
    if verified is None:
        verified = info.get("verified_email") if info else None
    if verified is False:
        return RedirectResponse(login.to(error="oauth_unverified"), status_code=303)
    db_user = user_crud.get_by_email(email)
    if db_user and not db_user.is_active:
        return RedirectResponse(login.to(error="account_inactive"), status_code=303)
    if not db_user:
        name = info.get("name") if info else None
        db_user = user_crud.create(User(email=email, name=name))
    sess["auth"] = db_user.id
    return RedirectResponse("/", status_code=303)


@ar("/logout", methods=["GET"])
def logout(sess):
    sess.pop("auth", None)
    sess.pop("oauth_state", None)
    return RedirectResponse("/login", status_code=303)
