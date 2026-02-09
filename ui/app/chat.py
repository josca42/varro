from __future__ import annotations

from typing import TYPE_CHECKING

import mistletoe
from fasthtml.common import (
    Div,
    Span,
    Button,
    Form,
    Input,
    Textarea,
    Main,
    Script,
    Header,
    Ul,
    Li,
    A,
    NotStr,
)
from ui.components import DataTable, Figure, GameOfLifeAnimation
from pydantic_ai.messages import (
    ModelRequest,
    ModelResponse,
    ThinkingPart,
    TextPart,
    ToolCallPart,
    ToolReturnPart,
)
from ui.app.tool import (
    ThinkingBlock,
    ToolCallsGroup,
    ToolResultsGroup,
    ReasoningBlock,
    _tool_call_item,
)
from varro.dashboard.parser import (
    parse_dashboard_md,
    MarkdownNode,
    ComponentNode,
    ContainerNode,
)
from varro.config import DATA_DIR
from plotly.basedatatypes import BaseFigure
import pandas as pd

if TYPE_CHECKING:
    from varro.db.models.chat import Chat, Turn
    from varro.agent.ipython_shell import TerminalInteractiveShell


class _CacheShell:
    """Lightweight stand-in for shell that serves cached HTML for fig/df placeholders."""

    def __init__(self, cache: dict):
        self.user_ns = cache


def ChatPage(chat: "Chat | None", shell: "TerminalInteractiveShell | None" = None):
    return Main(
        ChatPanel(chat, shell=shell),
        ChatClientScript(),
        cls="flex flex-col h-screen",
        id="chat-root",
        hx_ext="ws",
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
    """Render a complete turn from stored data."""
    from varro.chat.session import UserSession

    fp = DATA_DIR / turn.obj_fp
    msgs = UserSession._load_turn(fp)
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


def ChatForm(chat_id: int | None = None, disabled: bool = False):
    return Form(
        Div(
            Textarea(
                id="message-input",
                name="msg",
                placeholder="Ask about Danish statistics...",
                rows="1",
                disabled=disabled,
                cls="border-none bg-transparent w-full resize-none focus:outline-none text-sm placeholder:text-base-content/50",
                x_data="",
                x_init="$el.style.height = $el.scrollHeight + 'px'",
                **{
                    "@input": "$el.style.height = 'auto'; $el.style.height = $el.scrollHeight + 'px'"
                },
            ),
            Div(
                Button(
                    NotStr(
                        '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg>'
                    ),
                    type="submit",
                    disabled=disabled,
                    cls="btn btn-circle btn-sm btn-primary",
                ),
                cls="flex justify-end",
            ),
            cls="bg-base-100 rounded-box p-3 flex flex-col gap-2 border border-base-300",
        ),
        Input(type="hidden", name="sid", value=""),
        Input(type="hidden", name="current_url", value=""),
        Input(type="hidden", name="chat_id", value=chat_id)
        if chat_id is not None
        else None,
        ws_send=True,
        id="chat-form",
        cls="px-4 py-3",
    )


def ChatFormDisabled(chat_id: int | None = None):
    return Div(
        ChatForm(chat_id=chat_id, disabled=True), hx_swap_oob="outerHTML:#chat-form"
    )


def ChatFormEnabled(chat_id: int | None = None):
    return Div(
        ChatForm(chat_id=chat_id, disabled=False), hx_swap_oob="outerHTML:#chat-form"
    )


# TODO: Does it make sense to have the client script in the UI library?
# Maybe it would make more sense to have it in the app folder. And can this be simplified somehow?. Essentially, the script does two things:
# 1. It creates a random view UID, enabling a user to have multiple sessions in different tabs.
# 2. These sessions are then closed after a time interval if the user is inactive.
def ChatClientScript():
    return Script(
        """
(() => {
  const makeSid = () => {
    if (window.crypto && crypto.randomUUID) {
      return crypto.randomUUID();
    }
    if (window.crypto && crypto.getRandomValues) {
      const bytes = new Uint8Array(16);
      crypto.getRandomValues(bytes);
      bytes[6] = (bytes[6] & 0x0f) | 0x40;
      bytes[8] = (bytes[8] & 0x3f) | 0x80;
      const hex = Array.from(bytes, (b) => b.toString(16).padStart(2, "0"));
      return `${hex.slice(0, 4).join("")}-${hex.slice(4, 6).join("")}-${hex
        .slice(6, 8)
        .join("")}-${hex.slice(8, 10).join("")}-${hex
        .slice(10, 16)
        .join("")}`;
    }
    return `sid-${Date.now().toString(36)}-${Math.random()
      .toString(36)
      .slice(2, 10)}`;
  };

  const sidKey = "varro_chat_sid";
  let sid = sessionStorage.getItem(sidKey);
  if (!sid) {
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

  const setHiddenInputs = () => {
    const currentUrl = `${window.location.pathname}${window.location.search}`;
    for (const input of document.querySelectorAll("input[name='sid']")) {
      input.value = sid;
    }
    for (const input of document.querySelectorAll("input[name='current_url']")) {
      input.value = currentUrl;
    }
  };

  setHiddenInputs();
  document.body.addEventListener("htmx:afterSwap", () => {
    setHiddenInputs();
    if (window.__golRefresh) {
      window.__golRefresh();
    }
  });

  window.addEventListener("popstate", setHiddenInputs);

  if (window.__golRefresh) {
    window.__golRefresh();
  }

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
        Div(content, cls="bg-base-300 px-4 py-3 rounded-full max-w-[85%] text-sm"),
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


def CallToolsBlock(
    node,
    shell: "TerminalInteractiveShell | None" = None,
    connected: bool = True,
):
    """
    Render a CallToolsNode.
    Contains the model's response: thinking, text, and tool calls.
    """
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
        GameOfLifeAnimation(run=True),
        id="chat-progress",
        cls="chat-progress",
        hx_swap_oob="outerHTML:#chat-progress",
    )


def ChatProgressEnd():
    return Div(
        GameOfLifeAnimation(run=False),
        id="chat-progress",
        cls="chat-progress",
        hx_swap_oob="outerHTML:#chat-progress",
    )


def ChatProgressPlaceholder():
    return Div(
        GameOfLifeAnimation(run=False),
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


# --- Markdown rendering ---


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
        if kind == "df" and isinstance(obj, pd.DataFrame):
            df = obj
            if not isinstance(df.index, pd.RangeIndex):
                df = df.reset_index()
            return DataTable(df, cls="my-2")
        elif kind == "fig" and isinstance(obj, BaseFigure):
            return Div(Figure(obj), cls="my-2")

    return _missing_placeholder(kind, name)


def _missing_placeholder(kind: str, name: str):
    label = "figure" if kind == "fig" else "dataframe"
    return Div(
        f"Missing {label}: {name}",
        cls="text-xs text-base-content/50 italic",
    )


# --- Turn / model part rendering ---


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
                    attachments=[],
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
    reasoning_tool_returns: list[ToolReturnPart] = []

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
            for part in msg.parts:
                if isinstance(part, ToolReturnPart):
                    reasoning_tool_returns.append(part)
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
