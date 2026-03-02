from __future__ import annotations

from dataclasses import dataclass

import pytest
from starlette.testclient import TestClient

from app.routes import auth as auth_routes
from ui.core import daisy_app


@dataclass
class _FakeUser:
    id: int
    email: str
    is_active: bool = True
    password_hash: str | None = "$argon2id$fake"


@pytest.fixture
def auth_client():
    app, _ = daisy_app()
    auth_routes.ar.to_app(app)
    client = TestClient(app)
    yield client
    client.close()


def test_login_page_includes_hidden_next(auth_client) -> None:
    response = auth_client.get("/login", params={"next": "/public/1/population/fork"})

    assert response.status_code == 200
    assert 'name="next"' in response.text
    assert 'value="/public/1/population/fork"' in response.text


def test_login_post_redirects_to_valid_next(auth_client, monkeypatch) -> None:
    monkeypatch.setattr(
        auth_routes.user_crud,
        "get_by_email",
        lambda email: _FakeUser(id=7, email=email),
    )
    monkeypatch.setattr(auth_routes.user_crud, "verify_password", lambda *_: True)

    response = auth_client.post(
        "/login",
        data={
            "email": "user@example.com",
            "password": "secret",
            "next": "/public/1/population/fork",
        },
        follow_redirects=False,
    )

    assert response.status_code == 303
    assert response.headers["location"] == "/public/1/population/fork"


def test_login_post_ignores_invalid_next(auth_client, monkeypatch) -> None:
    monkeypatch.setattr(
        auth_routes.user_crud,
        "get_by_email",
        lambda email: _FakeUser(id=9, email=email),
    )
    monkeypatch.setattr(auth_routes.user_crud, "verify_password", lambda *_: True)

    response = auth_client.post(
        "/login",
        data={
            "email": "user@example.com",
            "password": "secret",
            "next": "https://example.com/evil",
        },
        follow_redirects=False,
    )

    assert response.status_code == 303
    assert response.headers["location"] == "/app"


def test_google_flow_preserves_next_redirect(auth_client, monkeypatch) -> None:
    class _FakeGoogleClient:
        def login_link(self, redirect_uri, scope, state):
            assert redirect_uri
            assert scope
            assert state == "state-1"
            return "https://google.test/oauth"

        def retr_info(self, code, redirect_uri):
            assert code == "code-1"
            assert redirect_uri
            return {
                "email": "user@example.com",
                "email_verified": True,
                "name": "User",
            }

    monkeypatch.setattr(auth_routes, "google_client", lambda: _FakeGoogleClient())
    monkeypatch.setattr(auth_routes.secrets, "token_urlsafe", lambda n: "state-1")
    monkeypatch.setattr(
        auth_routes.user_crud,
        "get_by_email",
        lambda email: _FakeUser(id=11, email=email),
    )

    login_start = auth_client.get(
        "/auth/google",
        params={"next": "/public/1/population/fork"},
        follow_redirects=False,
    )
    assert login_start.status_code == 303
    assert login_start.headers["location"] == "https://google.test/oauth"

    callback = auth_client.get(
        "/auth/google/callback",
        params={"code": "code-1", "state": "state-1"},
        follow_redirects=False,
    )
    assert callback.status_code == 303
    assert callback.headers["location"] == "/public/1/population/fork"
