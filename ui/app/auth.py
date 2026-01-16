"""ui.app.auth

Authentication UI compositions for the web app.
"""

from __future__ import annotations

from typing import Iterable

from fasthtml.common import Titled

from ui.core import cn
from ui.components import (
    Alert,
    Button,
    LinkButton,
    Card,
    CardBody,
    FieldDescription,
    FormField,
    Form,
    Input,
    Separator,
    Stack,
)


def AuthPage(title: str, *content, cls: str = "", **kw):
    return Titled(
        title,
        Card(
            CardBody(*content),
            cls=cn("auth-card", cls),
            **kw,
        ),
    )


def AuthFormCard(
    title: str,
    form,
    *,
    notices: Iterable | None = None,
    oauth_cta=None,
    links=None,
    cls: str = "",
    **kw,
):
    parts = []
    if notices:
        parts.extend(notices)
    parts.append(form)

    if oauth_cta:
        parts.append(Separator())
        parts.append(oauth_cta)
    if links:
        parts.append(links)

    return AuthPage(title, *parts, cls=cls, **kw)


def AuthSimpleCard(title: str, *content, cls: str = "", **kw):
    return AuthPage(title, *content, cls=cls, **kw)


def AuthNotices(error: str | None, info: str | None):
    blocks = []
    if error:
        blocks.append(Alert(error, variant="error", cls="text-sm"))
    if info:
        blocks.append(Alert(info, variant="success", cls="text-sm"))
    return blocks


def AuthLinks(*links, cls: str = "", **kw):
    return Stack(
        *links,
        direction="horizontal",
        gap=4,
        justify="justify-between",
        wrap=True,
        cls=cn("text-sm", cls),
        **kw,
    )


def AuthGoogleCta(enabled: bool, href, cls: str = "", **kw):
    if enabled:
        return LinkButton("Continue with Google", href=href, variant="outline", cls=cls, **kw)
    return FieldDescription("Google login not configured.", cls=cls, **kw)


def AuthLoginForm(action):
    return Form(
        FormField(
            "Email",
            Input(
                id="login-email",
                name="email",
                type="email",
                autocomplete="email",
            ),
            id="login-email",
        ),
        FormField(
            "Password",
            Input(
                id="login-password",
                name="password",
                type="password",
                autocomplete="current-password",
            ),
            id="login-password",
        ),
        Button("Sign in", type="submit"),
        action=action,
        method="post",
        layout="vertical",
    )


def AuthSignupForm(action):
    return Form(
        FormField(
            "Name",
            Input(
                id="signup-name",
                name="name",
                type="text",
                autocomplete="name",
            ),
            id="signup-name",
        ),
        FormField(
            "Email",
            Input(
                id="signup-email",
                name="email",
                type="email",
                autocomplete="email",
            ),
            id="signup-email",
        ),
        FormField(
            "Password",
            Input(
                id="signup-password",
                name="password",
                type="password",
                autocomplete="new-password",
            ),
            id="signup-password",
        ),
        Button("Create account", type="submit"),
        action=action,
        method="post",
        layout="vertical",
    )


def AuthVerificationResendForm(action):
    return Form(
        FormField(
            "Email",
            Input(
                id="verify-email",
                name="email",
                type="email",
                autocomplete="email",
            ),
            id="verify-email",
        ),
        Button("Resend verification", type="submit"),
        action=action,
        method="post",
        layout="vertical",
    )


def AuthPasswordResetForm(action):
    return Form(
        FormField(
            "Email",
            Input(
                id="reset-email",
                name="email",
                type="email",
                autocomplete="email",
            ),
            id="reset-email",
        ),
        Button("Send reset link", type="submit"),
        action=action,
        method="post",
        layout="vertical",
    )


def AuthPasswordResetConfirmForm(action, token: str):
    return Form(
        Input(type="hidden", name="token", value=token),
        FormField(
            "New password",
            Input(
                id="reset-password",
                name="password",
                type="password",
                autocomplete="new-password",
            ),
            id="reset-password",
        ),
        Button("Update password", type="submit"),
        action=action,
        method="post",
        layout="vertical",
    )

