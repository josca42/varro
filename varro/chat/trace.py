from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pydantic_ai import BinaryContent
from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    RetryPromptPart,
    TextPart,
    ThinkingPart,
    ToolCallPart,
    ToolReturnPart,
    UserPromptPart,
)

from varro.chat.tool_results import extract_tool_render_records


# TODO: Why not use Pydantic models?
@dataclass
class TraceUsage:
    model_name: str | None
    input_tokens: int
    output_tokens: int
    responses: int


@dataclass
class TraceEvent:
    idx: int
    kind: str
    step_idx: int | None = None
    tool_name: str | None = None
    tool_call_id: str | None = None
    call_seq: int | None = None
    text: str | None = None
    args: dict[str, Any] | None = None
    content: Any = None
    supplemental_content: Any = None
    is_final: bool = False


@dataclass
class Trace:
    events: list[TraceEvent]
    usage: TraceUsage
    steps: int


def extract_trace(msgs: list[ModelMessage]) -> Trace:
    events: list[TraceEvent] = []
    step_idx = 0
    call_seq = 0
    call_links: dict[str, tuple[int, int]] = {}
    total_in = 0
    total_out = 0
    responses = 0
    model_name: str | None = None

    for msg in msgs:
        if isinstance(msg, ModelRequest):
            has_tool_parts = any(
                isinstance(part, (ToolReturnPart, RetryPromptPart))
                for part in msg.parts
            )
            if has_tool_parts:
                for record in extract_tool_render_records(msg):
                    part = record.part
                    linked_call, linked_step = _linked_call(
                        call_links,
                        part.tool_call_id,
                        step_idx,
                    )
                    events.append(
                        TraceEvent(
                            idx=len(events),
                            kind="tool_return",
                            step_idx=linked_step,
                            tool_name=part.tool_name,
                            tool_call_id=part.tool_call_id,
                            call_seq=linked_call,
                            text=_flatten_text(part.content),
                            content=part.content,
                            supplemental_content=record.tool_content,
                        )
                    )
                for part in msg.parts:
                    if not isinstance(part, RetryPromptPart):
                        continue
                    linked_call, linked_step = _linked_call(
                        call_links,
                        part.tool_call_id,
                        step_idx,
                    )
                    events.append(
                        TraceEvent(
                            idx=len(events),
                            kind="tool_retry",
                            step_idx=linked_step,
                            tool_name=part.tool_name,
                            tool_call_id=part.tool_call_id,
                            call_seq=linked_call,
                            text=_flatten_text(part.content),
                            content=part.content,
                        )
                    )
                continue

            for part in msg.parts:
                if not isinstance(part, UserPromptPart):
                    continue
                text = _flatten_text(part.content)
                has_binary = _has_binary(part.content)
                if not text and not has_binary:
                    continue
                events.append(
                    TraceEvent(
                        idx=len(events),
                        kind="user",
                        text=text or None,
                        content=part.content,
                    )
                )
            continue

        if not isinstance(msg, ModelResponse):
            continue

        step_idx += 1
        responses += 1
        if msg.model_name:
            model_name = msg.model_name
        if msg.usage:
            total_in += msg.usage.input_tokens
            total_out += msg.usage.output_tokens

        is_final = msg.finish_reason == "stop"
        for part in msg.parts:
            if isinstance(part, ThinkingPart):
                if part.content and part.content.strip():
                    events.append(
                        TraceEvent(
                            idx=len(events),
                            kind="thinking",
                            step_idx=step_idx,
                            text=part.content,
                        )
                    )
                continue
            if isinstance(part, TextPart):
                if part.content and part.content.strip():
                    events.append(
                        TraceEvent(
                            idx=len(events),
                            kind="assistant_text",
                            step_idx=step_idx,
                            text=part.content,
                            is_final=is_final,
                        )
                    )
                continue
            if isinstance(part, ToolCallPart):
                call_seq += 1
                args = part.args_as_dict() if part.args else {}
                if part.tool_call_id:
                    call_links[part.tool_call_id] = (call_seq, step_idx)
                events.append(
                    TraceEvent(
                        idx=len(events),
                        kind="tool_call",
                        step_idx=step_idx,
                        tool_name=part.tool_name,
                        tool_call_id=part.tool_call_id,
                        call_seq=call_seq,
                        args=args,
                    )
                )

    return Trace(
        events=events,
        usage=TraceUsage(
            model_name=model_name,
            input_tokens=total_in,
            output_tokens=total_out,
            responses=responses,
        ),
        steps=step_idx,
    )


def _linked_call(
    links: dict[str, tuple[int, int]],
    tool_call_id: str | None,
    step_idx: int,
) -> tuple[int | None, int | None]:
    if tool_call_id and tool_call_id in links:
        return links[tool_call_id]
    if step_idx > 0:
        return None, step_idx
    return None, None


def _flatten_text(content: Any) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, BinaryContent):
        return ""
    if isinstance(content, (list, tuple)):
        values = [_flatten_text(item) for item in content]
        values = [value for value in values if value.strip()]
        return "\n".join(values)
    text = str(content)
    return text if text.strip() else ""


def _has_binary(content: Any) -> bool:
    if isinstance(content, BinaryContent):
        return True
    if isinstance(content, (list, tuple)):
        return any(_has_binary(item) for item in content)
    return False
