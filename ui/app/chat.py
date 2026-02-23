from __future__ import annotations

from typing import TYPE_CHECKING

import mistletoe
import pandas as pd
from pandas.io.formats.style import Styler
from fasthtml.common import (
    A,
    Button,
    Div,
    Form,
    Header,
    Input,
    Li,
    Main,
    NotStr,
    Script,
    Span,
    Textarea,
    Ul,
)
from plotly.basedatatypes import BaseFigure
from pydantic_ai.messages import (
    ModelRequest,
    ModelResponse,
    TextPart,
    ThinkingPart,
    ToolCallPart,
)

from ui.app.tool import (
    ReasoningBlock,
    ThinkingBlock,
    ToolCallsGroup,
    ToolResultsGroup,
    _tool_call_item,
)
from ui.components import DataTable, Figure, GameOfLifeAnimation
from varro.chat.tool_results import ToolRenderRecord, extract_tool_render_records
from varro.config import DATA_DIR
from varro.dashboard.parser import (
    ComponentNode,
    ContainerNode,
    MarkdownNode,
    parse_dashboard_md,
)

if TYPE_CHECKING:
    from varro.agent.ipython_shell import TerminalInteractiveShell
    from varro.db.models.chat import Chat, Turn


class _CacheShell:
    def __init__(self, cache: dict):
        self.user_ns = cache


def ChatPage(chat: "Chat | None", shell: "TerminalInteractiveShell | None" = None):
    return Main(
        ChatPanel(chat, shell=shell),
        ChatClientScript(),
        cls="flex flex-col h-screen",
        id="chat-root",
    )


def ChatPanel(
    chat: "Chat | None",
    shell: "TerminalInteractiveShell | None" = None,
    **attrs,
):
    turns = chat.turns if chat else []
    chat_id = chat.id if chat else None
    return Div(
        ChatHeader(chat),
        ChatMessages(turns, shell=shell),
        ChatRunStream(),
        ChatForm(chat_id=chat_id),
        cls="flex flex-col min-h-0 h-full",
        id="chat-panel",
        **attrs,
    )


def ChatMessages(
    turns: list["Turn"], shell: "TerminalInteractiveShell | None" = None, **attrs
):
    return Div(
        *[TurnComponent(t, shell=shell) for t in turns],
        ChatProgressPlaceholder(),
        id="chat-messages",
        cls="flex-1 overflow-y-auto px-4 py-6",
        **attrs,
    )


def TurnComponent(turn: "Turn", shell: "TerminalInteractiveShell | None" = None):
    from varro.chat.turn_store import load_turn_messages

    fp = DATA_DIR / turn.obj_fp
    msgs = load_turn_messages(fp)
    if shell is None:
        cache = _load_render_cache(fp)
        if cache:
            shell = _CacheShell(cache)

    parts = [UserMessage(turn.user_text)]
    parts.extend(_render_turn_messages(msgs, shell=shell))

    return Div(*parts, id=f"turn-{turn.idx}", cls="mb-6")


def _load_render_cache(turn_fp) -> dict:
    import json

    cache_fp = turn_fp.with_suffix(".cache.json")
    if cache_fp.exists():
        return json.loads(cache_fp.read_text())
    return {}


def ChatRunStream(run_id: str | None = None, **attrs):
    if not run_id:
        return Div(id="chat-run-stream", **attrs)
    return Div(
        id="chat-run-stream",
        hx_ext="sse",
        sse_connect=f"/chat/runs/{run_id}/stream",
        sse_swap="message",
        sse_close="done",
        hx_swap="none",
        **attrs,
    )


def ChatForm(
    chat_id: int | None = None,
    *,
    running: bool = False,
    run_id: str | None = None,
):
    send_icon = NotStr(
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>'
    )
    stop_icon = NotStr(
        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="6" y="6" width="12" height="12" rx="1"/></svg>'
    )
    enter_submit = (
        "if ($event.key !== 'Enter' || $event.shiftKey || $event.isComposing || $event.keyCode === 229) return;"
        " const value = ($el.value || '').trim();"
        " if (!value) { $event.preventDefault(); return; }"
        " const form = $el.form;"
        " if (!form) return;"
        " $event.preventDefault();"
        " form.requestSubmit();"
    )
    blank_submit_guard = (
        "const input = $el.querySelector('#message-input');"
        " if (!input || (input.value || '').trim()) return;"
        " $event.preventDefault();"
    )
    return Form(
        Div(
            Textarea(
                id="message-input",
                name="msg",
                placeholder="Ask about Danish statistics...",
                rows="1",
                disabled=running,
                cls="border-none bg-transparent w-full resize-none focus:outline-none text-sm placeholder:text-base-content/50",
                x_data="",
                x_init="$el.style.height = $el.scrollHeight + 'px'",
                **{
                    "@input": "$el.style.height = 'auto'; $el.style.height = $el.scrollHeight + 'px'",
                    "@keydown": enter_submit,
                },
            ),
            Div(
                Button(
                    stop_icon if running else send_icon,
                    type="button" if running else "submit",
                    hx_post=f"/chat/runs/{run_id}/cancel"
                    if running and run_id
                    else None,
                    hx_swap="none" if running else None,
                    cls="btn btn-circle btn-sm btn-primary",
                ),
                cls="flex justify-end",
            ),
            cls="bg-base-100 rounded-box p-3 flex flex-col gap-2 border border-base-300",
        ),
        Input(type="hidden", name="run_id", value=run_id or ""),
        Input(type="hidden", name="current_url", value=""),
        Input(type="hidden", name="chat_id", value=chat_id)
        if chat_id is not None
        else None,
        hx_post="/chat/runs",
        hx_swap="none",
        id="chat-form",
        cls="px-4 py-3",
        x_data="",
        **{"@submit": blank_submit_guard},
    )


def ChatFormRunning(chat_id: int | None = None, run_id: str | None = None):
    return Div(
        ChatForm(chat_id=chat_id, running=True, run_id=run_id),
        hx_swap_oob="outerHTML:#chat-form",
    )


def ChatFormEnabled(chat_id: int | None = None):
    return Div(ChatForm(chat_id=chat_id), hx_swap_oob="outerHTML:#chat-form")


def ChatClientScript():
    return Script(
        """
(() => {
  if (window.__varroChatClientInitialized) return;
  window.__varroChatClientInitialized = true;

  const setHiddenInputs = () => {
    const currentUrl = `${window.location.pathname}${window.location.search}`;
    for (const input of document.querySelectorAll("input[name='current_url']")) {
      input.value = currentUrl;
    }
  };

  const refreshUi = () => {
    setHiddenInputs();
    if (window.__golRefresh) window.__golRefresh();
  };

  document.body.addEventListener("htmx:afterSwap", refreshUi);
  document.body.addEventListener("htmx:oobAfterSwap", refreshUi);
  document.body.addEventListener(
    "submit",
    (event) => {
      const form = event.target;
      if (form && form.matches && form.matches("#chat-form")) setHiddenInputs();
    },
    true
  );
  window.addEventListener("popstate", setHiddenInputs);

  refreshUi();
})();
"""
    )


def UserMessage(content: str):
    return Div(
        Div(content, cls="bg-base-300 px-4 py-3 rounded-full max-w-[85%] text-sm"),
        cls="flex justify-end mb-4",
    )


def UserPromptBlock(node):
    return UserMessage(node.user_prompt)


def ModelRequestBlock(node):
    tool_parts = extract_tool_render_records(node.request)
    if not tool_parts:
        return None
    return ToolResultsGroup(tool_parts)


def CallToolsBlock(
    node,
    shell: "TerminalInteractiveShell | None" = None,
    connected: bool = True,
):
    parts = _render_model_parts(
        node.model_response.parts,
        shell=shell,
        connected=connected,
    )
    return Div(*parts, cls="mb-4") if parts else None


def TextBlock(content: str, shell: "TerminalInteractiveShell | None" = None):
    parts = render_markdown_blocks(content, shell=shell)
    return Div(*parts, cls="mb-4 flex flex-col gap-4")


def ErrorBlock(message: str):
    return Div(f"Error: {message}", cls="text-error text-sm mb-4")


def ChatProgressStart():
    return Div(
        GameOfLifeAnimation(run=True, text="V", cell_size=1.5, size=60),
        id="chat-progress",
        cls="chat-progress",
        hx_swap_oob="outerHTML:#chat-progress",
    )


def ChatProgressEnd():
    return Div(
        GameOfLifeAnimation(run=False, text="V", cell_size=1.5, size=60),
        id="chat-progress",
        cls="chat-progress",
        hx_swap_oob="outerHTML:#chat-progress",
    )


def ChatProgressPlaceholder():
    return Div(
        GameOfLifeAnimation(run=False, text="V", cell_size=1.5, size=60),
        id="chat-progress",
        cls="chat-progress",
    )


def ChatHeader(chat: "Chat | None"):
    return Header(
        ChatDropdownTrigger(chat),
        Button(
            NotStr(
                '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>'
            ),
            type="button",
            hx_get="/chat/new",
            hx_swap="none",
            cls="btn btn-ghost btn-sm btn-circle absolute right-4",
        ),
        cls="relative flex justify-center items-center px-4 min-h-14 border-b border-base-300 bg-base-200",
    )


def ChatDropdownTrigger(chat: "Chat | None"):
    title = chat.title if chat else "New chat"
    return Div(
        Button(
            title,
            Span("v", cls="ml-2 text-xs"),
            cls="btn btn-ghost btn-sm bg-base-100",
            **{"@click": "open = !open"},
        ),
        Div(
            id="chat-dropdown",
            hx_get="/chat/history",
            hx_trigger="click from:previous",
            cls="absolute left-1/2 -translate-x-1/2 mt-2 w-90 max-h-96 overflow-y-auto bg-base-100 shadow-lg rounded-box z-50 border border-base-300",
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
                hx_get=f"/chat/switch/{chat.id}",
                hx_swap="none",
                cls="flex flex-col min-w-0 flex-1",
            ),
            Button(
                "x",
                hx_delete=f"/chat/delete/{chat.id}",
                hx_confirm="Delete?",
                cls="btn btn-ghost btn-xs shrink-0",
            ),
            cls="flex items-center gap-2 w-full",
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
    if isinstance(shell, _CacheShell):
        cached_html = shell.user_ns.get(f"{kind}:{name}")
        if cached_html:
            return Div(NotStr(cached_html), cls="my-2")
        return _missing_placeholder(kind, name)

    if shell is None:
        return _missing_placeholder(kind, name)

    obj = shell.user_ns.get(name)
    if obj is not None:
        if kind == "df":
            if isinstance(obj, pd.DataFrame):
                df = obj
                if not isinstance(df.index, pd.RangeIndex):
                    df = df.reset_index()
                return DataTable(df, cls="my-2")
            if isinstance(obj, Styler):
                return Div(NotStr(obj.to_html()), cls="my-2 overflow-x-auto")
        if kind == "fig" and isinstance(obj, BaseFigure):
            return Div(Figure(obj), cls="my-2")

    return _missing_placeholder(kind, name)


def _missing_placeholder(kind: str, name: str):
    label = "figure" if kind == "fig" else "dataframe"
    return Div(
        f"Missing {label}: {name}",
        cls="text-xs text-base-content/50 italic",
    )


def _render_model_parts(
    parts,
    shell: "TerminalInteractiveShell | None" = None,
    connected: bool = True,
):
    rendered = []
    tool_calls = []

    def flush_tool_calls():
        nonlocal tool_calls
        if tool_calls:
            rendered.append(
                ToolCallsGroup(
                    tool_calls,
                    connected=connected,
                )
            )
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
                    args=part.args_as_dict(),
                    result="",
                    binary_outputs=[],
                    status="running",
                    call_id=part.tool_call_id,
                )
            )
    flush_tool_calls()
    return rendered


def _render_turn_messages(
    msgs: list[ModelResponse | ModelRequest],
    shell: "TerminalInteractiveShell | None" = None,
):
    from varro.chat.agent_run import cache_tool_calls

    parts = []
    reasoning_sequence: list[dict] = []
    reasoning_tool_returns: list[ToolRenderRecord] = []

    def flush_reasoning():
        nonlocal reasoning_sequence, reasoning_tool_returns
        if reasoning_sequence:
            block = ReasoningBlock(
                reasoning_sequence,
                reasoning_tool_returns,
                shell=shell,
            )
            if block:
                parts.append(block)
        reasoning_sequence = []
        reasoning_tool_returns = []

    for msg in msgs:
        if isinstance(msg, ModelRequest):
            reasoning_tool_returns.extend(extract_tool_render_records(msg))
            continue
        if not isinstance(msg, ModelResponse):
            continue
        if msg.finish_reason == "stop":
            flush_reasoning()
            parts.extend(
                _render_model_parts(
                    msg.parts,
                    shell=shell,
                    connected=False,
                )
            )
        else:
            cache_tool_calls(msg.parts, reasoning_sequence)
    flush_reasoning()
    return parts
