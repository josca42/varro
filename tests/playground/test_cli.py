from __future__ import annotations

from pydantic_ai.messages import (
    ModelRequest,
    ModelResponse,
    TextPart,
    ToolReturnPart,
    UserPromptPart,
)

from varro.playground.cli import _collect_turn_outcome, parse_update_url_payload


def test_parse_update_url_payload_valid() -> None:
    payload = parse_update_url_payload(
        'UPDATE_URL {"url":"/dashboard/sales?region=North","replace":false}'
    )
    assert payload == {"url": "/dashboard/sales?region=North", "replace": False}


def test_parse_update_url_payload_invalid() -> None:
    assert parse_update_url_payload("UPDATE_URL nope") is None
    assert parse_update_url_payload("anything else") is None


def test_collect_turn_outcome_reads_final_and_url_update() -> None:
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="hello")]),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="UpdateUrl",
                    content='UPDATE_URL {"url":"/dashboard/boligmarked","replace":false}',
                    tool_call_id="call_1",
                )
            ]
        ),
        ModelResponse(parts=[TextPart(content="Final answer")], finish_reason="stop"),
    ]

    final, url = _collect_turn_outcome(msgs, "/")
    assert final == "Final answer"
    assert url == "/dashboard/boligmarked"


def test_collect_turn_outcome_defaults_when_missing_final() -> None:
    msgs = [ModelRequest(parts=[UserPromptPart(content="hello")])]
    final, url = _collect_turn_outcome(msgs, "/")
    assert final == "_None_"
    assert url == "/"
