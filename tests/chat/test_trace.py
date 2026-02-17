from __future__ import annotations

from pydantic_ai import BinaryContent
from pydantic_ai.messages import (
    ModelRequest,
    ModelResponse,
    RetryPromptPart,
    TextPart,
    ThinkingPart,
    ToolCallPart,
    ToolReturnPart,
    UserPromptPart,
)

from varro.chat.trace import extract_trace


def test_extract_trace_single_call_roundtrip() -> None:
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="Hi")]),
        ModelResponse(
            parts=[
                ThinkingPart(content="Need SQL"),
                ToolCallPart(
                    tool_name="Sql",
                    args={"query": "select 1", "df_name": "df_x"},
                    tool_call_id="call_sql",
                ),
            ],
            finish_reason="tool_call",
            model_name="model-a",
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="Sql",
                    content="Stored as df_x",
                    tool_call_id="call_sql",
                    metadata={"ui": {"has_tool_content": False}},
                )
            ]
        ),
        ModelResponse(parts=[TextPart(content="Done")], finish_reason="stop"),
    ]

    trace = extract_trace(msgs)

    assert trace.steps == 2
    assert trace.usage.responses == 2
    assert [event.kind for event in trace.events] == [
        "user",
        "thinking",
        "tool_call",
        "tool_return",
        "assistant_text",
    ]
    tool_call = [event for event in trace.events if event.kind == "tool_call"][0]
    tool_return = [event for event in trace.events if event.kind == "tool_return"][0]
    final_text = [event for event in trace.events if event.kind == "assistant_text"][0]

    assert tool_call.call_seq == 1
    assert tool_call.step_idx == 1
    assert tool_return.call_seq == 1
    assert tool_return.step_idx == 1
    assert tool_return.tool_call_id == "call_sql"
    assert final_text.is_final is True


def test_extract_trace_parallel_calls_and_supplemental_content_mapping() -> None:
    image_a = BinaryContent(data=b"a", media_type="image/png")
    image_b = BinaryContent(data=b"b", media_type="image/png")
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="Plot")]),
        ModelResponse(
            parts=[
                ToolCallPart(
                    tool_name="Jupyter",
                    args={"code": "fig_a = 1", "show": ["fig_a"]},
                    tool_call_id="call_a",
                ),
                ToolCallPart(
                    tool_name="Jupyter",
                    args={"code": "fig_b = 1", "show": ["fig_b"]},
                    tool_call_id="call_b",
                ),
            ],
            finish_reason="tool_call",
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="Jupyter",
                    content="stdout a",
                    tool_call_id="call_a",
                    metadata={"ui": {"has_tool_content": True}},
                ),
                ToolReturnPart(
                    tool_name="Jupyter",
                    content="stdout b",
                    tool_call_id="call_b",
                    metadata={"ui": {"has_tool_content": True}},
                ),
                UserPromptPart(content=[image_a]),
                UserPromptPart(content=[image_b]),
            ]
        ),
    ]

    trace = extract_trace(msgs)

    returns = [event for event in trace.events if event.kind == "tool_return"]
    assert len(returns) == 2
    assert returns[0].call_seq == 1
    assert returns[1].call_seq == 2
    assert returns[0].supplemental_content == [image_a]
    assert returns[1].supplemental_content == [image_b]


def test_extract_trace_captures_retry_events() -> None:
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="Run")]),
        ModelResponse(
            parts=[
                ToolCallPart(
                    tool_name="Sql",
                    args={"query": "select *"},
                    tool_call_id="call_retry",
                )
            ],
            finish_reason="tool_call",
        ),
        ModelRequest(
            parts=[
                RetryPromptPart(
                    content="syntax error",
                    tool_name="Sql",
                    tool_call_id="call_retry",
                )
            ]
        ),
    ]

    trace = extract_trace(msgs)

    retries = [event for event in trace.events if event.kind == "tool_retry"]
    assert len(retries) == 1
    assert retries[0].tool_name == "Sql"
    assert retries[0].step_idx == 1
    assert retries[0].call_seq == 1
    assert retries[0].text == "syntax error"


def test_extract_trace_ignores_user_prompt_parts_in_tool_requests() -> None:
    image = BinaryContent(data=b"img", media_type="image/png")
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="first")]),
        ModelResponse(
            parts=[
                ToolCallPart(
                    tool_name="Read",
                    args={"file_path": "/dashboard/a.png"},
                    tool_call_id="read_1",
                )
            ],
            finish_reason="tool_call",
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="Read",
                    content="Read image",
                    tool_call_id="read_1",
                    metadata={"ui": {"has_tool_content": True}},
                ),
                UserPromptPart(content=[image]),
            ]
        ),
    ]

    trace = extract_trace(msgs)

    user_events = [event for event in trace.events if event.kind == "user"]
    assert len(user_events) == 1
    assert user_events[0].text == "first"


def test_extract_trace_legacy_mapping_without_metadata_when_counts_align() -> None:
    image_a = BinaryContent(data=b"a", media_type="image/png")
    image_b = BinaryContent(data=b"b", media_type="image/png")
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="Legacy")]),
        ModelResponse(
            parts=[
                ToolCallPart(
                    tool_name="Jupyter",
                    args={"code": "fig_a = 1"},
                    tool_call_id="legacy_a",
                ),
                ToolCallPart(
                    tool_name="Jupyter",
                    args={"code": "fig_b = 1"},
                    tool_call_id="legacy_b",
                ),
            ],
            finish_reason="tool_call",
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="Jupyter",
                    content="stdout a",
                    tool_call_id="legacy_a",
                ),
                ToolReturnPart(
                    tool_name="Jupyter",
                    content="stdout b",
                    tool_call_id="legacy_b",
                ),
                UserPromptPart(content=[image_a]),
                UserPromptPart(content=[image_b]),
            ]
        ),
    ]

    trace = extract_trace(msgs)

    returns = [event for event in trace.events if event.kind == "tool_return"]
    assert len(returns) == 2
    assert returns[0].supplemental_content == [image_a]
    assert returns[1].supplemental_content == [image_b]
