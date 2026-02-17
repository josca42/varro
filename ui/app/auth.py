from __future__ import annotations

from typing import Iterable

from fasthtml.common import Div, H2, P, Span, Title

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
    GameOfLifeAnimation,
    Input,
    Separator,
    Stack,
)


def _auth_logo():
    return GameOfLifeAnimation(
        width=36, height=32, cell_size=2,
        text="V", color="#9b2743",
    )


def AuthPage(title: str, *content, cls: str = "", **kw):
    return Title(title + " — Varro"), Div(
        Div(
            _auth_logo(),
            *content,
            cls=cn("w-full max-w-sm flex flex-col gap-6", cls),
            data_slot="auth-card",
            **kw,
        ),
        cls="min-h-screen flex items-center justify-center bg-base-200 px-4 py-12",
        data_slot="auth-page",
    )


def AuthFormCard(
    title: str,
    form,
    *,
    subtitle: str = "",
    notices: Iterable | None = None,
    oauth_cta=None,
    links=None,
    cls: str = "",
    **kw,
):
    parts = []

    heading = Div(
        H2(title, cls="text-2xl font-bold tracking-tight"),
        P(subtitle, cls="text-base-content/50 text-sm") if subtitle else None,
        cls="space-y-1",
    )
    parts.append(heading)

    if notices:
        parts.extend(notices)

    if oauth_cta:
        parts.append(oauth_cta)
        parts.append(Separator("OR", cls="my-0 text-xs"))

    parts.append(form)

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
        justify="justify-center",
        wrap=True,
        cls=cn("text-sm text-base-content/50", cls),
        **kw,
    )


def _google_icon():
    return Span(
        Span("G", cls="font-bold text-base"),
        cls="w-5 h-5 flex items-center justify-center",
    )


def AuthGoogleCta(enabled: bool, href, cls: str = "", **kw):
    if enabled:
        return LinkButton(
            _google_icon(),
            "Continue with Google",
            href=href,
            variant="outline",
            size="lg",
            cls=cn("w-full", cls),
            **kw,
        )
    return None


def AuthLoginForm(action):
    return Form(
        FormField(
            "Email",
            Input(
                id="login-email",
                name="email",
                type="email",
                placeholder="name@example.com",
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
                placeholder="Enter your password",
                autocomplete="current-password",
            ),
            id="login-password",
        ),
        Button("Sign in", type="submit", cls="w-full", size="lg"),
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
                placeholder="Your name",
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
                placeholder="name@example.com",
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
                placeholder="Create a password",
                autocomplete="new-password",
            ),
            id="signup-password",
        ),
        Button("Create account", type="submit", cls="w-full", size="lg"),
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
                placeholder="name@example.com",
                autocomplete="email",
            ),
            id="verify-email",
        ),
        Button("Resend verification", type="submit", cls="w-full", size="lg"),
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
                placeholder="name@example.com",
                autocomplete="email",
            ),
            id="reset-email",
        ),
        Button("Send reset link", type="submit", cls="w-full", size="lg"),
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
                placeholder="Enter new password",
                autocomplete="new-password",
            ),
            id="reset-password",
        ),
        Button("Update password", type="submit", cls="w-full", size="lg"),
        action=action,
        method="post",
        layout="vertical",
    )
