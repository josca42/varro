from __future__ import annotations

import json
from typing import TYPE_CHECKING

import mistletoe
from fasthtml.common import (
    Div,
    Span,
    Button,
    Form,
    Input,
    Textarea,
    Pre,
    Code,
    Img,
    Main,
    Script,
    Table,
    Thead,
    Tbody,
    Tr,
    Th,
    Td,
    H1,
    Header,
    Ul,
    Li,
    A,
    NotStr,
)
from ui.components import DataTable, Figure
from pydantic_ai import BinaryContent
from pydantic_ai.messages import (
    ThinkingPart,
    TextPart,
    ToolCallPart,
    ToolReturnPart,
)
from varro.dashboard.parser import (
    parse_dashboard_md,
    MarkdownNode,
    ComponentNode,
    ContainerNode,
)
from plotly.basedatatypes import BaseFigure
import pandas as pd

if TYPE_CHECKING:
    from varro.db.models.chat import Chat, Turn
    from varro.agent.ipython_shell import TerminalInteractiveShell


def ChatPage(chat: "Chat | None", shell: "TerminalInteractiveShell | None" = None):
    turns = chat.turns if chat else []
    chat_id = chat.id if chat else None
    return Main(
        ChatHeader(chat),
        ChatMessages(turns, shell=shell),
        ChatForm(chat_id=chat_id),
        ChatClientScript(),
        cls="flex flex-col h-screen",
        id="chat-root",
        hx_ext="ws",
    )


def ChatMessages(
    turns: list["Turn"], shell: "TerminalInteractiveShell | None" = None, **attrs
):
    return Div(
        *[TurnComponent(t, shell=shell) for t in turns],
        id="chat-messages",
        cls="flex-1 overflow-y-auto px-4 py-6",
        **attrs,
    )


def TurnComponent(turn: "Turn", shell: "TerminalInteractiveShell | None" = None):
    """Render a complete turn from stored data."""
    from pathlib import Path
    from varro.chat.session import UserSession

    parts = [UserMessage(turn.user_text)]

    msgs = UserSession._load_turn(Path(turn.obj_fp))
    for msg in msgs:
        from pydantic_ai.messages import ModelResponse

        if not isinstance(msg, ModelResponse):
            continue
        parts.extend(_render_model_parts(msg.parts, shell=shell))

    return Div(*parts, id=f"turn-{turn.idx}", cls="mb-6")


def ChatForm(chat_id: int | None = None, disabled: bool = False):
    return Form(
        Div(
            Textarea(
                id="message-input",
                name="msg",
                placeholder="Ask about Danish statistics...",
                rows="1",
                disabled=disabled,
                cls="textarea textarea-bordered w-full resize-none",
            ),
            Button(
                "Send",
                type="submit",
                disabled=disabled,
                cls="btn btn-primary btn-sm",
            ),
            cls="flex gap-2 items-end",
        ),
        Input(type="hidden", name="sid", value=""),
        Input(type="hidden", name="chat_id", value=chat_id)
        if chat_id is not None
        else None,
        ws_send=True,
        id="chat-form",
        cls="px-4 py-3 border-t",
    )


def ChatFormDisabled(chat_id: int | None = None):
    return Div(
        ChatForm(chat_id=chat_id, disabled=True), hx_swap_oob="outerHTML:#chat-form"
    )


def ChatFormEnabled(chat_id: int | None = None):
    return Div(
        ChatForm(chat_id=chat_id, disabled=False), hx_swap_oob="outerHTML:#chat-form"
    )


def ChatClientScript():
    return Script(
        """
(() => {
  const sidKey = "varro_chat_sid";
  let sid = sessionStorage.getItem(sidKey);
  if (!sid) {
    const makeSid = () => {
      if (window.crypto && typeof window.crypto.randomUUID === "function") {
        return window.crypto.randomUUID();
      }
      if (window.crypto && window.crypto.getRandomValues) {
        const bytes = new Uint8Array(16);
        window.crypto.getRandomValues(bytes);
        bytes[6] = (bytes[6] & 0x0f) | 0x40;
        bytes[8] = (bytes[8] & 0x3f) | 0x80;
        const hex = Array.from(bytes, (b) => b.toString(16).padStart(2, "0"));
        return `${hex.slice(0, 4).join("")}-${hex
          .slice(4, 6)
          .join("")}-${hex.slice(6, 8).join("")}-${hex
          .slice(8, 10)
          .join("")}-${hex.slice(10, 16).join("")}`;
      }
      return `${Date.now().toString(36)}-${Math.random().toString(36).slice(2)}`;
    };
    sid = makeSid();
    sessionStorage.setItem(sidKey, sid);
  }

  const root = document.getElementById("chat-root");
  if (root) {
    root.setAttribute("ws-connect", `/ws?sid=${encodeURIComponent(sid)}`);
    if (window.htmx) {
      window.htmx.process(root);
    }
  }

  const setSidInputs = () => {
    for (const input of document.querySelectorAll("input[name='sid']")) {
      input.value = sid;
    }
  };

  setSidInputs();
  document.body.addEventListener("htmx:afterSwap", () => {
    setSidInputs();
  });

  let lastInput = Date.now();
  const markActive = () => {
    lastInput = Date.now();
  };

  ["keydown", "pointerdown", "mousedown", "touchstart"].forEach((event) => {
    window.addEventListener(event, markActive, { passive: true });
  });

  document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") {
      markActive();
    }
  });

  const activeWindowMs = 2 * 60 * 1000;
  const intervalMs = 60 * 1000;

  const heartbeat = () => {
    if (document.visibilityState !== "visible") {
      return;
    }
    if (Date.now() - lastInput > activeWindowMs) {
      return;
    }
    navigator.sendBeacon(`/chat/heartbeat?sid=${encodeURIComponent(sid)}`);
  };

  setInterval(heartbeat, intervalMs);

  window.addEventListener("beforeunload", () => {
    navigator.sendBeacon(`/chat/close?sid=${encodeURIComponent(sid)}`);
  });
})();
"""
    )


def UserMessage(content: str):
    return Div(
        Div(content, cls="bg-base-200 px-4 py-3 rounded-box max-w-[85%]"),
        cls="flex justify-end mb-4",
    )


def UserPromptBlock(node):
    """Render a UserPromptNode."""
    return UserMessage(node.user_prompt)


def ModelRequestBlock(node):
    """
    Render a ModelRequestNode.
    Contains the request sent to the model (tool return parts from previous calls).
    """
    tool_parts = [
        part for part in node.request.parts if isinstance(part, ToolReturnPart)
    ]
    if not tool_parts:
        return None
    return ToolResultsGroup(tool_parts)


def CallToolsBlock(node, shell: "TerminalInteractiveShell | None" = None):
    """
    Render a CallToolsNode.
    Contains the model's response: thinking, text, and tool calls.
    """
    parts = _render_model_parts(node.model_response.parts, shell=shell)
    return Div(*parts, cls="mb-4") if parts else None


def ToolResultBlock(part: ToolReturnPart):
    """Render a tool result from a ModelRequestNode."""
    return ToolResultsGroup([part])


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


def ToolCallBlock(tool: str, args: dict, result: str, attachments: list):
    return ToolCallsGroup(
        [
            _tool_call_item(
                tool=tool,
                args=args,
                result=result,
                attachments=attachments,
                status="running",
            )
        ]
    )


def ToolCallsGroup(tool_calls: list[dict]):
    if not tool_calls:
        return None
    return Div(
        ToolGroupHeader("Tool calls", len(tool_calls)),
        Div(
            *[
                ToolCallStep(
                    tool=item["tool"],
                    args=item["args"],
                    result=item.get("result", ""),
                    attachments=item.get("attachments", []),
                    status=item.get("status", "running"),
                )
                for item in tool_calls
            ],
            cls="tool-steps",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: true}",
        cls="tool-call-group mb-4",
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
    args: dict,
    result: str,
    attachments: list,
    status: str = "running",
):
    label = _format_tool_label(tool)
    summary = _tool_arg_summary(args)
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
            ToolCallDetailCard(tool, args, result, attachments),
            cls="tool-step-details",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: false}",
        cls="tool-step",
        data_status=status,
    )


def ToolResultStep(part: ToolReturnPart):
    result_text = _format_tool_result(part.content)
    status = _tool_result_status(result_text)
    summary = _tool_result_summary(part.content)
    label = _format_tool_label(part.tool_name)
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
            ToolResultDetailCard(result_text, []),
            cls="tool-step-details",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: false}",
        cls="tool-step",
        data_status=status,
    )


def ToolCallDetailCard(tool: str, args: dict, result: str, attachments: list):
    sections = [
        Div(
            Span("Input", cls="tool-card-label"),
            ToolArgsDisplay(tool, args),
            cls="tool-card-section",
        )
    ]
    if result or attachments:
        sections.append(
            Div(
                Span("Output", cls="tool-card-label"),
                ToolResultDisplay(result, attachments),
                cls="tool-card-section",
            )
        )
    return Div(*sections, cls="tool-card")


def ToolResultDetailCard(result: str, attachments: list):
    return Div(
        Div(
            Span("Output", cls="tool-card-label"),
            ToolResultDisplay(result, attachments),
            cls="tool-card-section",
        ),
        cls="tool-card",
    )


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


def ToolResultDisplay(result: str, attachments: list):
    parts = []
    if result:
        if "|" in result and "\n" in result:
            parts.append(Div(MarkdownTable(result), cls="tool-output-block"))
        else:
            parts.append(Pre(result, cls="tool-output-block"))
    for att in attachments:
        parts.append(Img(src=f"/uploads/{att['path']}", cls="tool-output-asset"))
    if not parts:
        return Span("No output", cls="tool-empty")
    return Div(*parts, cls="flex flex-col gap-2")


def TextBlock(content: str, shell: "TerminalInteractiveShell | None" = None):
    parts = render_markdown_blocks(content, shell=shell)
    return Div(*parts, cls="mb-4 flex flex-col gap-4")


def ErrorBlock(message: str):
    return Div(f"Error: {message}", cls="text-error text-sm mb-4")


def ChatHeader(chat: "Chat | None"):
    return Header(
        Div(
            H1("Rigsstatistikeren", cls="text-xl font-semibold"),
            ChatDropdownTrigger(chat),
            cls="flex items-center gap-4",
        ),
        A("New Chat", href="/chat/new", cls="btn btn-primary btn-sm"),
        cls="flex justify-between items-center px-4 py-3 border-b",
    )


def ChatDropdownTrigger(chat: "Chat | None"):
    title = chat.title if chat else "New chat"
    return Div(
        Button(
            title,
            Span("v", cls="ml-2 text-xs"),
            cls="btn btn-ghost btn-sm",
            **{"@click": "open = !open"},
        ),
        Div(
            id="chat-dropdown",
            hx_get="/chat/history",
            hx_trigger="click from:previous",
            cls="absolute mt-2 w-64 bg-base-100 shadow-lg rounded-box z-50",
            x_show="open",
            **{"@click.outside": "open = false"},
        ),
        x_data="{open: false}",
        cls="relative",
    )


def ChatDropdown(chats: list["Chat"]):
    return Ul(*[ChatDropdownItem(c) for c in chats], cls="menu p-2")


def ChatDropdownItem(chat: "Chat"):
    return Li(
        Div(
            A(
                Span(chat.title or "Untitled", cls="truncate"),
                Span(
                    chat.created_at.strftime("%Y-%m-%d"),
                    cls="text-xs text-base-content/50",
                ),
                href=f"/chat/switch/{chat.id}",
                cls="flex flex-col",
            ),
            Button(
                "x",
                hx_delete=f"/chat/delete/{chat.id}",
                hx_confirm="Delete?",
                cls="btn btn-ghost btn-xs",
            ),
            cls="flex justify-between items-center",
        )
    )


def render_markdown_blocks(
    content: str, shell: "TerminalInteractiveShell | None" = None
):
    if not content:
        return []
    nodes = parse_dashboard_md(content)
    return _render_chat_nodes(nodes, shell)


def _render_chat_nodes(nodes, shell: "TerminalInteractiveShell | None" = None):
    parts = []
    for node in nodes:
        if isinstance(node, MarkdownNode):
            html = mistletoe.markdown(node.content) if node.content.strip() else ""
            if html:
                parts.append(Div(NotStr(html), cls="prose prose-sm max-w-none"))
        elif isinstance(node, ComponentNode):
            name = (node.attrs.get("name") or "").strip()
            if node.type in ("fig", "df"):
                parts.append(_render_placeholder(node.type, name, shell))
        elif isinstance(node, ContainerNode):
            parts.extend(_render_chat_nodes(node.children, shell))

    return [p for p in parts if p is not None]


def _render_placeholder(
    kind: str, name: str, shell: "TerminalInteractiveShell | None" = None
):
    if shell is None:
        return _missing_placeholder(kind, name)
    obj = shell.user_ns.get(name)
    if obj is None:
        return _missing_placeholder(kind, name)

    if kind == "df":
        if isinstance(obj, pd.DataFrame):
            df = obj
            if not isinstance(df.index, pd.RangeIndex):
                df = df.reset_index()
            return DataTable(df, cls="my-2")
    elif kind == "fig":
        if isinstance(obj, BaseFigure):
            return Div(Figure(obj), cls="my-2")

    return _missing_placeholder(kind, name)


def _missing_placeholder(kind: str, name: str):
    label = "figure" if kind == "fig" else "dataframe"
    return Div(
        f"Missing {label}: {name}",
        cls="text-xs text-base-content/50 italic",
    )


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


def _render_model_parts(parts, shell: "TerminalInteractiveShell | None" = None):
    rendered = []
    tool_calls = []

    def flush_tool_calls():
        nonlocal tool_calls
        if tool_calls:
            rendered.append(ToolCallsGroup(tool_calls))
            tool_calls = []

    for part in parts:
        if isinstance(part, ThinkingPart):
            flush_tool_calls()
            rendered.append(ThinkingBlock(part.content))
        elif isinstance(part, TextPart):
            flush_tool_calls()
            rendered.append(TextBlock(part.content, shell=shell))
        elif isinstance(part, ToolCallPart):
            tool_calls.append(
                _tool_call_item(
                    tool=part.tool_name,
                    args=_parse_args(part.args),
                    result="",
                    attachments=[],
                    status="running",
                )
            )
    flush_tool_calls()
    return rendered


def _tool_call_item(
    tool: str,
    args: dict,
    result: str = "",
    attachments: list | None = None,
    status: str = "running",
):
    return {
        "tool": tool,
        "args": args,
        "result": result,
        "attachments": attachments or [],
        "status": status,
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


def _tool_result_status(result_text: str) -> str:
    if result_text and result_text.strip().lower().startswith("error"):
        return "error"
    return "success"


def _parse_args(args) -> dict:
    if isinstance(args, dict):
        return args
    if isinstance(args, str):
        return json.loads(args or "{}")
    return {}


def _format_tool_result(content) -> str:
    if content is None:
        return ""
    if isinstance(content, list):
        items = [item for item in content if not isinstance(item, BinaryContent)]
        return "\n".join(str(item) for item in items if str(item).strip())
    return str(content)
