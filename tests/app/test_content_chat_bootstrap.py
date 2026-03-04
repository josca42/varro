from __future__ import annotations

from types import SimpleNamespace

from app.routes import content as content_routes


def _write_welcome(tmp_path, text: str = "# Welcome\n"):
    path = tmp_path / "welcome.md"
    path.write_text(text, encoding="utf-8")
    return path


def test_app_home_full_page_clears_chat_id(monkeypatch, tmp_path) -> None:
    req = SimpleNamespace(headers={})
    sess = {"user_id": 3, "chat_id": 41}

    monkeypatch.setattr(content_routes, "_welcome_path", lambda _user_id: _write_welcome(tmp_path))
    monkeypatch.setattr(content_routes, "list_dashboards", lambda _user_id: [])
    monkeypatch.setattr(content_routes, "_render_welcome_page", lambda content, dashboards: (content, dashboards))

    captured = {}

    def fake_app_or_fragment(_req, current_sess, content):
        captured["chat_id"] = current_sess.get("chat_id")
        captured["content"] = content
        return "ok"

    monkeypatch.setattr(content_routes, "_app_or_fragment", fake_app_or_fragment)

    result = content_routes.app_home(req, sess)

    assert result == "ok"
    assert "chat_id" not in sess
    assert captured["chat_id"] is None


def test_app_home_htmx_keeps_chat_id(monkeypatch, tmp_path) -> None:
    req = SimpleNamespace(headers={"HX-Request": "true"})
    sess = {"user_id": 3, "chat_id": 41}

    monkeypatch.setattr(content_routes, "_welcome_path", lambda _user_id: _write_welcome(tmp_path))
    monkeypatch.setattr(content_routes, "list_dashboards", lambda _user_id: [])
    monkeypatch.setattr(content_routes, "_render_welcome_page", lambda content, dashboards: (content, dashboards))

    captured = {}

    def fake_app_or_fragment(_req, current_sess, _content):
        captured["chat_id"] = current_sess.get("chat_id")
        return "ok"

    monkeypatch.setattr(content_routes, "_app_or_fragment", fake_app_or_fragment)

    result = content_routes.app_home(req, sess)

    assert result == "ok"
    assert sess["chat_id"] == 41
    assert captured["chat_id"] == 41


def test_app_code_full_page_keeps_chat_id(monkeypatch, tmp_path) -> None:
    req = SimpleNamespace(headers={})
    sess = {"user_id": 3, "chat_id": 41}

    monkeypatch.setattr(content_routes, "_welcome_path", lambda _user_id: _write_welcome(tmp_path))
    monkeypatch.setattr(content_routes, "_render_welcome_editor", lambda _content: "editor")

    captured = {}

    def fake_app_or_fragment(_req, current_sess, _content):
        captured["chat_id"] = current_sess.get("chat_id")
        return "ok"

    monkeypatch.setattr(content_routes, "_app_or_fragment", fake_app_or_fragment)

    result = content_routes.app_code(req, sess)

    assert result == "ok"
    assert sess["chat_id"] == 41
    assert captured["chat_id"] == 41


def test_app_or_fragment_restores_session_chat(monkeypatch) -> None:
    expected_chat = object()
    calls = []

    def fake_get(chat_id, with_turns=False):
        calls.append((chat_id, with_turns))
        return expected_chat

    captured = {}

    def fake_app_shell(chat, content, user_name=None, user_email=None):
        captured["chat"] = chat
        captured["content"] = content
        captured["user_name"] = user_name
        captured["user_email"] = user_email
        return "shell"

    monkeypatch.setattr(content_routes, "AppShell", fake_app_shell)
    monkeypatch.setattr(content_routes.crud.user, "get", lambda _user_id: None)

    req = SimpleNamespace(
        headers={},
        state=SimpleNamespace(chats=SimpleNamespace(get=fake_get)),
    )
    sess = {"user_id": 7, "chat_id": 55}

    result = content_routes._app_or_fragment(req, sess, "content")

    assert result == "shell"
    assert calls == [(55, True)]
    assert captured["chat"] is expected_chat
    assert captured["content"] == "content"
