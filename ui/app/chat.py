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
from varro.dashboard.filters import Filter

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
        cls="flex flex-col h-screen",
        hx_ext="ws",
        ws_connect="/ws",
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
        for part in msg.parts:
            if isinstance(part, ThinkingPart):
                parts.append(ThinkingBlock(part.content))
            elif isinstance(part, TextPart):
                parts.append(TextBlock(part.content, shell=shell))
            elif isinstance(part, ToolCallPart):
                args = _parse_args(part.args)
                parts.append(
                    ToolCallBlock(
                        tool=part.tool_name,
                        args=args,
                        result="",
                        attachments=[],
                    )
                )

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
    parts = []
    for part in node.request.parts:
        if isinstance(part, ToolReturnPart):
            parts.append(ToolResultBlock(part))

    return Div(*parts) if parts else None


def CallToolsBlock(node, shell: "TerminalInteractiveShell | None" = None):
    """
    Render a CallToolsNode.
    Contains the model's response: thinking, text, and tool calls.
    """
    parts = []
    model_response = node.model_response

    for part in model_response.parts:
        if isinstance(part, ThinkingPart):
            parts.append(ThinkingBlock(part.content))
        elif isinstance(part, TextPart):
            parts.append(TextBlock(part.content, shell=shell))
        elif isinstance(part, ToolCallPart):
            args = _parse_args(part.args)
            parts.append(
                ToolCallBlock(
                    tool=part.tool_name,
                    args=args,
                    result="",
                    attachments=[],
                )
            )

    return Div(*parts, cls="mb-4") if parts else None


def ToolResultBlock(part: ToolReturnPart):
    """Render a tool result from a ModelRequestNode."""
    result_text = _format_tool_result(part.content)
    return Div(
        Div(f"Result from {part.tool_name}", cls="text-xs text-base-content/50"),
        Pre(result_text, cls="text-xs bg-base-200 p-2 rounded overflow-x-auto mt-1")
        if result_text
        else None,
        cls="pl-4 border-l-2 border-base-300 mb-2",
    )


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
    return Div(
        Div(
            Span(
                ">",
                cls="text-xs transition-transform duration-200 mr-2",
                **{":class": "{'rotate-90': open}"},
            ),
            f"Called {tool}",
            cls="cursor-pointer text-sm text-base-content/50 flex items-center",
            **{"@click": "open = !open"},
        ),
        Div(
            ToolArgsDisplay(tool, args),
            ToolResultDisplay(result, attachments),
            cls="pl-4 border-l-2 border-base-300 mt-2",
            x_show="open",
            x_collapse=True,
        ),
        x_data="{open: false}",
        cls="mb-2",
    )


def ToolArgsDisplay(tool: str, args: dict):
    if tool == "sql_query":
        return Div(
            Pre(
                Code(args.get("query", ""), cls="language-sql"),
                cls="text-xs bg-base-200 p-2 rounded overflow-x-auto",
            ),
            Span(f"-> {args.get('df_name')}", cls="text-xs text-base-content/50")
            if args.get("df_name")
            else None,
        )
    if tool == "jupyter_notebook":
        return Pre(
            Code(args.get("code", ""), cls="language-python"),
            cls="text-xs bg-base-200 p-2 rounded overflow-x-auto",
        )
    return Pre(
        json.dumps(args, indent=2, ensure_ascii=False),
        cls="text-xs bg-base-200 p-2 rounded overflow-x-auto",
    )


def ToolResultDisplay(result: str, attachments: list):
    parts = []
    if result:
        if "|" in result and "\n" in result:
            parts.append(MarkdownTable(result))
        else:
            parts.append(Pre(result, cls="text-xs overflow-x-auto mt-2"))
    for att in attachments:
        parts.append(Img(src=f"/uploads/{att['path']}", cls="max-w-full rounded mt-2"))
    return Div(*parts) if parts else None


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


def render_markdown(content: str) -> str:
    if not content or not content.strip():
        return ""
    return mistletoe.markdown(content)


def render_markdown_blocks(
    content: str, shell: "TerminalInteractiveShell | None" = None
):
    if not content:
        return []
    nodes = parse_dashboard_md(content)
    return _render_chat_nodes(nodes, shell)


def _render_chat_nodes(
    nodes, shell: "TerminalInteractiveShell | None" = None
):
    parts = []
    for node in nodes:
        if isinstance(node, MarkdownNode):
            html = render_markdown(node.content)
            if html.strip():
                parts.append(Div(NotStr(html), cls="prose prose-sm max-w-none"))
        elif isinstance(node, ComponentNode):
            name = (node.attrs.get("name") or "").strip()
            if node.type in ("fig", "df"):
                parts.append(_render_placeholder(node.type, name, shell))
            elif node.type == "metric":
                parts.append(_missing_placeholder("metric", name))
            else:
                parts.append(_missing_placeholder(node.type, name))
        elif isinstance(node, ContainerNode):
            parts.extend(_render_chat_nodes(node.children, shell))
        elif isinstance(node, Filter):
            parts.append(_missing_placeholder("filter", node.name))

    return [p for p in parts if p is not None]


def _render_placeholder(
    kind: str, name: str, shell: "TerminalInteractiveShell | None" = None
):
    if not name:
        return None
    if not shell or not getattr(shell, "user_ns", None):
        return _missing_placeholder(kind, name)

    obj = shell.user_ns.get(name)
    if obj is None:
        return _missing_placeholder(kind, name)

    if kind == "df":
        import pandas as pd

        if isinstance(obj, pd.DataFrame):
            df = obj
            if not isinstance(df.index, pd.RangeIndex):
                df = df.reset_index()
            return DataTable(df, cls="my-2")
    elif kind == "fig":
        try:
            from plotly.basedatatypes import BaseFigure
        except Exception:
            BaseFigure = None

        if BaseFigure is None or isinstance(obj, BaseFigure):
            return Div(Figure(obj), cls="my-2")

    return _missing_placeholder(kind, name)


def _missing_placeholder(kind: str, name: str):
    label_map = {
        "fig": "figure",
        "df": "dataframe",
        "metric": "metric",
        "filter": "filter",
    }
    label = label_map.get(kind, kind)
    return Div(
        f"Missing {label}: {name}",
        cls="text-xs text-base-content/50 italic",
    )


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
