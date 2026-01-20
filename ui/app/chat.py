from __future__ import annotations

import json
from typing import TYPE_CHECKING

import mistletoe
from fasthtml.common import (
    Div,
    Span,
    Button,
    Form,
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

if TYPE_CHECKING:
    from varro.db.models.chat import Chat, Message


def ChatPage(chat: "Chat" | None):
    messages = chat.messages if chat else []
    return Main(
        ChatHeader(chat),
        ChatMessages(messages),
        ChatForm(disabled=False),
        cls="flex flex-col h-screen",
    )


def ChatMessages(messages: list["Message"]):
    return Div(
        *[MessageComponent(m) for m in messages],
        Div(id="stream-container"),
        id="chat-messages",
        cls="flex-1 overflow-y-auto px-4 py-6",
    )


def MessageComponent(message: "Message"):
    if message.role == "user":
        return UserMessage(message.content.get("text", ""))
    return AssistantMessage(message.content)


def StreamContainer(chat_id: int):
    return Div(
        ProgressIndicator("Thinking..."),
        Div(id="streaming-content", sse_swap="content:beforeend"),
        Button(
            "Stop",
            hx_get=f"/chat/stop/{chat_id}",
            hx_target="#stream-container",
            hx_swap="outerHTML",
            cls="btn btn-error btn-sm mt-2",
        ),
        id="stream-container",
        hx_ext="sse",
        sse_connect=f"/chat/stream/{chat_id}",
        sse_swap="done:outerHTML",
    )


def ProgressIndicator(status: str):
    return Div(
        Span(cls="loading loading-dots loading-sm"),
        Span(status, cls="ml-2 text-sm text-base-content/50"),
        id="progress-indicator",
        hx_swap_oob="true",
        cls="flex items-center mb-4",
    )


def ChatForm(disabled: bool = False, **kw):
    return Form(
        Div(
            Textarea(
                id="message-input",
                name="message",
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
        hx_post="/chat/send",
        hx_target="#stream-container",
        hx_swap="outerHTML",
        id="chat-form",
        cls="px-4 py-3 border-t",
        **kw,
    )


def ChatFormDisabled():
    return ChatForm(disabled=True, hx_swap_oob="true")


def ChatFormEnabled():
    return Div(ChatForm(disabled=False), hx_swap_oob="outerHTML:#chat-form")


def UserMessage(content: str):
    return Div(
        Div(content, cls="bg-base-200 px-4 py-3 rounded-box max-w-[85%]"),
        cls="flex justify-end mb-4",
    )


def AssistantMessage(content: dict):
    parts = []
    for node in content.get("nodes", []):
        for part in node.get("parts", []):
            if part.get("type") == "thinking":
                parts.append(ThinkingBlock(part.get("content", "")))
            elif part.get("type") == "tool_call":
                parts.append(
                    ToolCallBlock(
                        part.get("tool", ""),
                        part.get("args", {}),
                        part.get("result", ""),
                        part.get("attachments", []),
                    )
                )
            elif part.get("type") == "text":
                parts.append(TextBlock(part.get("content", "")))
    return Div(*parts, cls="mb-6")


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
        parts.append(
            Img(src=f"/uploads/{att['path']}", cls="max-w-full rounded mt-2")
        )
    return Div(*parts) if parts else None


def TextBlock(content: str):
    return Div(
        NotStr(render_markdown(content)),
        cls="prose prose-sm max-w-none mb-6",
    )


def ErrorBlock(message: str):
    return Div(f"Error: {message}", cls="text-error text-sm mb-4")


def ChatHeader(chat: "Chat" | None):
    return Header(
        Div(
            H1("Rigsstatistikeren", cls="text-xl font-semibold"),
            ChatDropdownTrigger(chat),
            cls="flex items-center gap-4",
        ),
        Button("New Chat", hx_get="/chat/new", cls="btn btn-primary btn-sm"),
        cls="flex justify-between items-center px-4 py-3 border-b",
    )


def ChatDropdownTrigger(chat: "Chat" | None):
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
                hx_get=f"/chat/switch/{chat.id}",
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
    return mistletoe.markdown(content or "")


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
                Tbody(
                    *[
                        Tr(*[Td(cell.strip()) for cell in row])
                        for row in body
                    ]
                ),
                cls="table table-xs",
            ),
            cls="overflow-x-auto bg-base-200/60 p-2 rounded",
        ),
        cls="mt-2",
    )


def ChatInput(*args, **kwargs):
    return ChatForm(*args, **kwargs)
