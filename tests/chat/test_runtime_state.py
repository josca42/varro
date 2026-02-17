from __future__ import annotations

import varro.chat.runtime_state as runtime_state


def test_load_bash_cwd_defaults_to_root_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(runtime_state, "DATA_DIR", tmp_path)

    cwd = runtime_state.load_bash_cwd(user_id=4, chat_id=8)

    assert cwd == "/"


def test_save_and_load_bash_cwd_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(runtime_state, "DATA_DIR", tmp_path)

    runtime_state.save_bash_cwd(user_id=1, chat_id=2, cwd="/subjects/economy")
    cwd = runtime_state.load_bash_cwd(user_id=1, chat_id=2)

    assert cwd == "/subjects/economy"


def test_load_bash_cwd_falls_back_for_malformed_json(tmp_path, monkeypatch):
    monkeypatch.setattr(runtime_state, "DATA_DIR", tmp_path)

    fp = runtime_state.runtime_state_fp(user_id=3, chat_id=9)
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text("{not valid json")

    cwd = runtime_state.load_bash_cwd(user_id=3, chat_id=9)

    assert cwd == "/"
