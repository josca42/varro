from __future__ import annotations

from types import SimpleNamespace

from pydantic_ai.messages import ModelRequest, ModelResponse, TextPart, UserPromptPart

import varro.chat.turn_store as turn_store


def _build_messages(user_text: str, model_text: str):
    return [
        ModelRequest(parts=[UserPromptPart(content=user_text)]),
        ModelResponse(parts=[TextPart(content=model_text)], finish_reason="stop"),
    ]


def test_turn_fp_creates_expected_path(tmp_path, monkeypatch):
    monkeypatch.setattr(turn_store, "DATA_DIR", tmp_path)

    fp = turn_store.turn_fp(user_id=7, chat_id=11, turn_idx=3)

    assert fp == tmp_path / "chat" / "7" / "11" / "3.mpk"
    assert fp.parent.exists()


def test_save_and_load_turn_messages_roundtrip(tmp_path, monkeypatch):
    monkeypatch.setattr(turn_store, "DATA_DIR", tmp_path)
    fp = turn_store.turn_fp(user_id=1, chat_id=2, turn_idx=0)
    msgs = _build_messages("Hello", "Hi")

    turn_store.save_turn_messages(msgs, fp)
    loaded = turn_store.load_turn_messages(fp)

    assert len(loaded) == 2
    assert loaded[0].parts[0].content == "Hello"
    assert loaded[1].parts[0].content == "Hi"


def test_load_messages_for_turns_reads_all_turn_files(tmp_path, monkeypatch):
    monkeypatch.setattr(turn_store, "DATA_DIR", tmp_path)

    fp0 = turn_store.turn_fp(user_id=3, chat_id=5, turn_idx=0)
    fp1 = turn_store.turn_fp(user_id=3, chat_id=5, turn_idx=1)

    turn_store.save_turn_messages(_build_messages("U1", "M1"), fp0)
    turn_store.save_turn_messages(_build_messages("U2", "M2"), fp1)

    turns = [
        SimpleNamespace(obj_fp=str(fp0.relative_to(tmp_path))),
        SimpleNamespace(obj_fp=str(fp1.relative_to(tmp_path))),
    ]

    loaded = turn_store.load_messages_for_turns(turns)

    texts = [part.content for msg in loaded for part in msg.parts if hasattr(part, "content")]
    assert texts == ["U1", "M1", "U2", "M2"]
