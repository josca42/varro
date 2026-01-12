"""ui.app.chat

Chat panel compositions used by the demo app.

These mirror the structure that was previously in `main.py`, but implemented
using `ui.components`.
"""

from __future__ import annotations

from typing import Iterable, Sequence

from fasthtml.common import *

from ..core import cn
from ..components.button import Button
from ..components.textarea import Textarea
from ..components.prose import MarkdownProse


def UserMessage(content, cls: str = "", **kw):
    """User message bubble (right aligned)."""

    return Div(
        Div(
            content,
            cls="bg-base-200 text-base-content px-4 py-3 rounded-box max-w-[85%]",
            data_slot="chat-user-bubble",
        ),
        cls=cn("flex justify-end mb-4", cls),
        data_slot="chat-user-message",
        **kw,
    )


def ThinkingSteps(duration: str, steps: Sequence[tuple[str, str]], cls: str = "", **kw):
    """Expandable "thinking" panel with smooth animations (claude.ai style).

    Uses Alpine.js x-disclosure + x-collapse for smooth expand/collapse transitions.
    """

    return Div(
        # x-disclosure container
        Div(
            # Trigger button
            Div(
                Div(
                    "▶",
                    cls="text-xs transition-transform inline-block mr-1",
                    **{":class": "{'rotate-90': $disclosure.isOpen}"},
                ),
                f"Thought for {duration}",
                cls="inline",
                **{"x-disclosure:button": True},
            ),
            # Collapsible panel with smooth height animation
            Div(
                *[
                    Div(
                        Div(title, cls="text-sm font-medium text-base-content/70"),
                        Div(desc, cls="text-sm text-base-content/60"),
                        cls="py-1",
                    )
                    for title, desc in steps
                ],
                cls="pl-4 border-l border-base-300 space-y-2 mt-2 mb-3",
                **{"x-disclosure:panel": True, "x-collapse": True},
            ),
            **{"x-disclosure": True},
            cls="cursor-pointer text-sm text-base-content/50 hover:text-base-content/70",
        ),
        x_data=True,
        cls=cn("mb-2", cls),
        data_slot="chat-thinking",
        **kw,
    )


def EditsIndicator(count: int = 8, cls: str = "", **kw):
    """Small "edits made" row."""

    return Div(
        Div(
            Div("✎", cls="text-base-content/40"),
            Div(f"{count} edits made", cls="text-sm text-base-content/60"),
            cls="flex items-center gap-2",
        ),
        Button("Show all", variant="ghost", size="sm", cls="text-base-content/60"),
        cls=cn("flex items-center justify-between py-2 mb-2", cls),
        data_slot="chat-edits",
        **kw,
    )


def AssistantMessage(
    content,
    thinking_time: str | None = None,
    thinking_steps: Sequence[tuple[str, str]] | None = None,
    show_edits: bool = False,
    cls: str = "",
    **kw,
):
    """Assistant message block with optional thinking accordion."""

    parts = []
    if thinking_time and thinking_steps:
        parts.append(ThinkingSteps(thinking_time, thinking_steps))
    if show_edits:
        parts.append(EditsIndicator())

    parts.append(MarkdownProse(content))

    return Div(
        *parts,
        cls=cn("mb-6", cls),
        data_slot="chat-assistant-message",
        **kw,
    )


def ChatInput(
    *,
    action: str = "/msg",
    target: str = "#chat-messages",
    placeholder: str = "Ask Lovable...",
    textarea_id: str = "msg-input",
    cls: str = "",
    **kw,
):
    """Bottom input bar (HTMX-friendly)."""

    return Form(
        Div(
            Textarea(
                placeholder=placeholder,
                name="user_msg",
                id=textarea_id,
                rows="2",
                cls="w-full resize-none",
                size="default",
            ),
            Button("Send", type="submit", variant="default", size="default"),
            cls="flex gap-2 items-end",
        ),
        hx_post=action,
        hx_target=target,
        hx_swap="beforeend",
        hx_on__after_request="this.reset()",
        cls=cn("border-t border-base-300 p-4", cls),
        data_slot="chat-input",
        **kw,
    )


__all__ = [
    "UserMessage",
    "AssistantMessage",
    "ThinkingSteps",
    "EditsIndicator",
    "ChatInput",
]
