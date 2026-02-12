from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from pydantic_ai.messages import ToolReturnPart, UserPromptPart


@dataclass
class ToolRenderRecord:
    part: ToolReturnPart
    tool_content: Any = None


def extract_tool_render_records(request) -> list[ToolRenderRecord]:
    tool_parts: list[ToolReturnPart] = []
    supplemental_contents: list[Any] = []
    seen: set[str | int] = set()

    for part in _iter_request_parts(request):
        if isinstance(part, ToolReturnPart):
            key = part.tool_call_id or id(part)
            if key in seen:
                continue
            seen.add(key)
            tool_parts.append(part)
            continue
        if isinstance(part, UserPromptPart) and _has_content(part.content):
            supplemental_contents.append(part.content)

    if not tool_parts:
        return []

    records = [ToolRenderRecord(part=part) for part in tool_parts]
    expected = [record for record in records if _tool_exposes_content(record.part)]

    content_idx = 0
    for record in expected:
        if content_idx >= len(supplemental_contents):
            break
        record.tool_content = supplemental_contents[content_idx]
        content_idx += 1

    if not expected and len(records) == 1 and len(supplemental_contents) == 1:
        records[0].tool_content = supplemental_contents[0]

    return records


def _iter_request_parts(request):
    for part in getattr(request, "parts", []) or []:
        yield part

    for msg in getattr(request, "messages", []) or []:
        for part in getattr(msg, "parts", []) or []:
            yield part


def _tool_exposes_content(part: ToolReturnPart) -> bool:
    if not isinstance(part.metadata, dict):
        return False
    ui = part.metadata.get("ui")
    if not isinstance(ui, dict):
        return False
    return bool(ui.get("has_tool_content"))


def _has_content(content: Any) -> bool:
    if content is None:
        return False
    if isinstance(content, str):
        return bool(content.strip())
    try:
        return len(content) > 0
    except TypeError:
        return True
