from __future__ import annotations

import json
from typing import TYPE_CHECKING
from fasthtml.common import (
    Div,
    Span,
    Pre,
    Code,
    Img,
    Script,
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    NotStr,
)
from pydantic_ai import BinaryContent
from pydantic_ai.messages import ToolReturnPart

if TYPE_CHECKING:
    from varro.agent.ipython_shell import TerminalInteractiveShell


def ThinkingBlock(content: str):
    return Div(
        Div(
            Span(
                ">",
                cls="text-xs transition-transform duration-200 mr-2",
                **{":class": "{'rotate-90': open}"},
            ),
            "Thinking...",
            cls="cursor-pointer text-sm text-base-content/50 flex items-center",
            **{"@click": "open = !open"},
        ),
        Div(
            content,
            cls="pl-4 border-l-2 border-base-300 mt-2 text-sm text-base-content/60 whitespace-pre-wrap",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: false}",
        cls="mb-2",
    )


def ToolCallBlock(
    tool: str,
    args: dict,
    result: str,
    attachments: list,
    call_id: str | None = None,
):
    return ToolCallsGroup(
        [
            _tool_call_item(
                tool=tool,
                args=args,
                result=result,
                attachments=attachments,
                call_id=call_id,
                status="running",
            )
        ]
    )


def ToolResultBlock(part: ToolReturnPart):
    """Render a tool result from a ModelRequestNode."""
    return ToolResultsGroup([part])


def ToolCallsGroup(
    tool_calls: list[dict],
    connected: bool = True,
    intro_parts: list | None = None,
    title: str = "Tool calls",
):
    if not tool_calls:
        return None
    steps_cls = (
        f"tool-steps {'tool-steps-connected' if connected else 'tool-steps-final'}"
    )
    group_cls = "tool-call-group mb-4"
    if not connected:
        group_cls = f"{group_cls} tool-call-final"
    return Div(
        ToolGroupHeader(title, len(tool_calls)),
        Div(*intro_parts, cls="tool-call-text", x_show="open", x_collapse=True)
        if intro_parts
        else None,
        Div(
            *[
                ToolCallStep(
                    tool=item["tool"],
                    args=item["args"],
                    result=item.get("result", ""),
                    attachments=item.get("attachments", []),
                    status=item.get("status", "running"),
                    call_id=item.get("call_id"),
                )
                for item in tool_calls
            ],
            cls=steps_cls,
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: true}",
        cls=group_cls,
    )


def ToolResultsGroup(tool_parts: list[ToolReturnPart]):
    if not tool_parts:
        return None
    return Div(
        ToolGroupHeader("Tool results", len(tool_parts)),
        Div(
            *[ToolResultStep(part) for part in tool_parts],
            cls="tool-steps",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: true}",
        cls="tool-call-group mb-4",
    )


def ReasoningBlock(
    sequence: list[dict],
    tool_parts: list[ToolReturnPart],
    shell: "TerminalInteractiveShell | None" = None,
    block_id: str | None = None,
    swap_oob: bool = False,
):
    if not sequence:
        return None
    results = {part.tool_call_id: part for part in tool_parts}
    steps = []
    tool_count = 0
    for item in sequence:
        kind = item.get("kind")
        if kind == "tool_call":
            tool_count += 1
            call_id = item.get("call_id")
            part = results.get(call_id) if call_id else None
            result_text = _format_tool_result(part.content) if part else ""
            status = _tool_result_status(result_text) if part else "running"
            steps.append(
                ToolCallStep(
                    tool=item["tool"],
                    args=item["args"],
                    result=result_text,
                    attachments=[],
                    status=status,
                    call_id=call_id,
                )
            )
        elif kind == "thinking":
            steps.append(ReasoningNoteStep("Thinking", item.get("content", ""), shell))
        elif kind == "text":
            steps.append(ReasoningNoteStep(None, item.get("content", ""), shell))
    if not steps:
        return None
    return ReasoningGroup(steps, tool_count, block_id=block_id, swap_oob=swap_oob)


def ReasoningGroup(
    steps: list,
    count: int,
    block_id: str | None = None,
    swap_oob: bool = False,
):
    attrs = {}
    if block_id:
        attrs["id"] = block_id
    if swap_oob:
        if block_id:
            attrs["hx-swap-oob"] = f"outerHTML:#{block_id}"
        else:
            attrs["hx-swap-oob"] = "outerHTML"
    return Div(
        ToolGroupHeader("Reasoning", count),
        Div(
            *steps,
            cls="tool-steps tool-steps-connected",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: true}",
        cls="tool-call-group mb-4",
        **attrs,
    )


def ReasoningNoteStep(label: str | None, content: str, shell=None):
    if not content or not content.strip():
        return None
    if label == "Thinking":
        body = Div(content, cls="tool-note-body tool-note-thinking")
    else:
        from ui.app.chat import render_markdown_blocks

        body = Div(*render_markdown_blocks(content, shell=shell), cls="tool-note-body")
    return Div(
        Span(label, cls="tool-note-label") if label else None,
        body,
        cls="tool-step tool-step-note",
        data_status="note",
    )


def ToolGroupHeader(title: str, count: int):
    return Div(
        Div(
            Span(title, cls="tool-call-title"),
            Span(f"{count} steps", cls="tool-call-meta"),
            cls="flex items-center gap-2",
        ),
        Div(
            Span(
                "Hide steps",
                cls="tool-call-toggle",
                x_text="open ? 'Hide steps' : 'Show steps'",
            ),
            Span(
                ">",
                cls="tool-call-chevron",
                **{":class": "{'rotate-90': open}"},
            ),
            cls="flex items-center gap-2",
        ),
        cls="tool-call-header",
        **{"@click": "open = !open"},
    )


def ToolCallStep(
    tool: str,
    args: dict | None = None,
    result: str = "",
    attachments: list | None = None,
    status: str = "running",
    call_id: str | None = None,
):
    label = _format_tool_label(tool)
    summary = _tool_arg_summary(args) if args else _tool_result_summary_text(result)
    pending = status == "running"
    update_url_payload = _parse_update_url_payload(tool, result) if call_id else None
    attrs = {"data_status": status}
    if call_id:
        attrs["id"] = f"tool-step-{call_id}"
    return Div(
        Div(
            Div(
                Span(label, cls="tool-step-title"),
                Span(summary, cls="tool-step-meta"),
                cls="flex flex-col",
            ),
            Span(
                ">",
                cls="tool-step-chevron",
                **{":class": "{'rotate-90': open}"},
            ),
            cls="tool-step-summary",
            **{"@click": "open = !open"},
        ),
        Div(
            ToolDetailCard(
                tool=tool,
                args=args,
                result=result,
                attachments=attachments or [],
                pending=pending,
            ),
            cls="tool-step-details",
            x_show="open",
            x_collapse=True,
        ),
        Script(
            f"window.__varroApplyUpdateUrl({json.dumps(call_id)}, {json.dumps(update_url_payload)});"
        )
        if update_url_payload
        else None,
        x_data="{open: false}",
        cls="tool-step",
        **attrs,
    )


def ToolResultStep(part: ToolReturnPart):
    result_text = _format_tool_result(part.content)
    status = _tool_result_status(result_text)
    return ToolCallStep(
        tool=part.tool_name,
        result=result_text,
        status=status,
    )


def ToolDetailCard(
    tool: str | None = None,
    args: dict | None = None,
    result: str = "",
    attachments: list | None = None,
    pending: bool = False,
):
    sections = []
    if args is not None:
        sections.append(
            Div(
                Span("Input", cls="tool-card-label"),
                ToolArgsDisplay(tool, args),
                cls="tool-card-section",
            )
        )
    sections.append(
        Div(
            Span("Output", cls="tool-card-label"),
            ToolResultDisplay(
                result,
                attachments or [],
                empty_label="Waiting for output" if pending else "No output",
            ),
            cls="tool-card-section",
        )
    )
    return Div(*sections, cls="tool-card")


def ToolArgsDisplay(tool: str, args: dict):
    if tool == "sql_query":
        return Div(
            Pre(
                Code(args.get("query", ""), cls="language-sql"),
                cls="tool-code-block",
            ),
            Span(f"-> {args.get('df_name')}", cls="tool-code-meta")
            if args.get("df_name")
            else None,
            cls="flex flex-col gap-2",
        )
    if tool == "jupyter_notebook":
        return Pre(
            Code(args.get("code", ""), cls="language-python"),
            cls="tool-code-block",
        )
    return Pre(
        json.dumps(args, indent=2, ensure_ascii=False),
        cls="tool-code-block",
    )


def ToolResultDisplay(result: str, attachments: list, empty_label: str = "No output"):
    parts = []
    if result:
        if "|" in result and "\n" in result:
            parts.append(Div(MarkdownTable(result), cls="tool-output-block"))
        else:
            parts.append(Pre(result, cls="tool-output-block"))
    for att in attachments:
        parts.append(Img(src=f"/uploads/{att['path']}", cls="tool-output-asset"))
    if not parts:
        return Span(empty_label, cls="tool-empty")
    return Div(*parts, cls="flex flex-col gap-2")


# TODO: remove MarkdownTable function and replace with DataTable rendering instead. Or user mistletoe to render the markdown table.
def MarkdownTable(content: str):
    lines = [line for line in content.splitlines() if line.strip()]
    if not lines:
        return Pre(content, cls="text-xs overflow-x-auto mt-2")

    title = None
    if lines[0].startswith("df.") and len(lines) > 1:
        title = lines.pop(0)

    rows = [line.split("|") for line in lines]
    if not rows:
        return Pre(content, cls="text-xs overflow-x-auto mt-2")

    header = rows[0]
    body = rows[1:]

    return Div(
        Div(title, cls="text-xs text-base-content/50 mb-1") if title else None,
        Div(
            Table(
                Thead(Tr(*[Th(cell.strip()) for cell in header])),
                Tbody(*[Tr(*[Td(cell.strip()) for cell in row]) for row in body]),
                cls="table table-xs",
            ),
            cls="overflow-x-auto bg-base-200/60 p-2 rounded",
        ),
        cls="mt-2",
    )


# --- Private helpers ---


def _tool_call_item(
    tool: str,
    args: dict,
    result: str = "",
    attachments: list | None = None,
    status: str = "running",
    call_id: str | None = None,
):
    return {
        "tool": tool,
        "args": args,
        "result": result,
        "attachments": attachments or [],
        "status": status,
        "call_id": call_id,
    }


def _format_tool_label(tool: str) -> str:
    label = tool.replace("_", " ").replace("-", " ").strip()
    return label.title() if label else "Tool"


def _tool_arg_summary(args: dict) -> str:
    if not args:
        return "No input"
    keys = [str(key) for key in args.keys() if key]
    if not keys:
        return "No input"
    shown = ", ".join(keys[:3])
    if len(keys) > 3:
        shown = f"{shown} +{len(keys) - 3} more"
    return f"Input: {shown}"


def _tool_result_summary(content) -> str:
    if content is None:
        return "No output"
    if isinstance(content, list):
        items = [item for item in content if not isinstance(item, BinaryContent)]
        if not items:
            return "No output"
        return f"Output: {len(items)} items"
    text = str(content).strip()
    if not text:
        return "No output"
    preview = text.replace("\n", " ")
    if len(preview) > 80:
        preview = f"{preview[:77]}..."
    return f"Output: {preview}"


def _tool_result_summary_text(result: str) -> str:
    if not result:
        return "No output"
    preview = result.replace("\n", " ")
    if len(preview) > 80:
        preview = f"{preview[:77]}..."
    return f"Output: {preview}"


def _tool_result_status(result_text: str) -> str:
    if result_text and result_text.strip().lower().startswith("error"):
        return "error"
    return "success"


def _parse_update_url_payload(tool: str, result: str) -> dict | None:
    if tool != "UpdateUrl":
        return None
    text = (result or "").strip()
    if not text.startswith("UPDATE_URL "):
        return None
    raw_json = text.removeprefix("UPDATE_URL ").strip()
    if not raw_json:
        return None
    try:
        payload = json.loads(raw_json)
    except json.JSONDecodeError:
        return None
    if not isinstance(payload, dict):
        return None
    url = payload.get("url")
    if not isinstance(url, str) or not url.startswith("/"):
        return None
    return {"url": url, "replace": bool(payload.get("replace", False))}


def _format_tool_result(content) -> str:
    if content is None:
        return ""
    if isinstance(content, list):
        items = [item for item in content if not isinstance(item, BinaryContent)]
        return "\n".join(str(item) for item in items if str(item).strip())
    return str(content)
