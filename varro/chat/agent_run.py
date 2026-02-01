from __future__ import annotations

from dataclasses import dataclass, field
from typing import AsyncIterator

from pydantic_ai import Agent
from pydantic_ai.messages import ThinkingPart, TextPart, ToolCallPart, ToolReturnPart

from ui.app.chat import UserPromptBlock, ModelRequestBlock, CallToolsBlock
from ui.app.tool import ReasoningBlock
from varro.agent.assistant import agent
from varro.chat.session import UserSession


@dataclass
class ReasoningState:
    turn_idx: int
    sequence: list[dict] = field(default_factory=list)
    returns: list[ToolReturnPart] = field(default_factory=list)
    sent: bool = False

    @property
    def block_id(self) -> str:
        return f"reasoning-{self.turn_idx}"

    def build_block(self, shell) -> object | None:
        block = ReasoningBlock(
            self.sequence, self.returns,
            shell=shell, block_id=self.block_id, swap_oob=self.sent,
        )
        if block:
            self.sent = True
        return block

    def clear(self):
        self.sequence.clear()
        self.returns.clear()
        self.sent = False


async def run_agent(user_text: str, session: UserSession) -> AsyncIterator[object]:
    """Run the agent and yield one HTML block per completed node."""
    state = ReasoningState(session.turn_idx)
    async with agent.iter(user_text, message_history=session.msgs, deps=session) as run:
        async for node in run:
            for block in node_to_blocks(node, session, state):
                if block:
                    yield block

    new_msgs = run.result.new_messages()
    session.save_turn(new_msgs, user_text)


def node_to_blocks(
    node,
    session: UserSession,
    state: ReasoningState,
) -> list[object]:
    """Convert a completed pydantic-ai node to a UI block."""

    if Agent.is_user_prompt_node(node):
        return [UserPromptBlock(node)]

    if Agent.is_model_request_node(node):
        tool_parts = _tool_return_parts(node.request)
        if not tool_parts:
            return []
        state.returns.extend(tool_parts)
        if state.sequence:
            return [state.build_block(session.shell)]
        return [ModelRequestBlock(node)]

    if Agent.is_call_tools_node(node):
        if node.model_response.finish_reason != "stop":
            cache_tool_calls(node.model_response.parts, state.sequence)
            return []
        blocks = []
        block = state.build_block(session.shell)
        if block:
            blocks.append(block)
        blocks.append(CallToolsBlock(node, shell=session.shell, connected=False))
        state.clear()
        return blocks

    if Agent.is_end_node(node):
        block = state.build_block(session.shell)
        state.clear()
        return [block] if block else []

    return []


def cache_tool_calls(
    parts,
    reasoning_sequence: list[dict],
) -> None:
    for part in parts:
        if isinstance(part, ThinkingPart):
            if part.content and part.content.strip():
                reasoning_sequence.append({"kind": "thinking", "content": part.content})
            continue
        if isinstance(part, TextPart):
            if part.content and part.content.strip():
                reasoning_sequence.append({"kind": "text", "content": part.content})
            continue
        if isinstance(part, ToolCallPart):
            reasoning_sequence.append(
                {
                    "kind": "tool_call",
                    "tool": part.tool_name,
                    "args": part.args or {},
                    "call_id": part.tool_call_id,
                }
            )


def _tool_return_parts(request) -> list[ToolReturnPart]:
    parts: list[ToolReturnPart] = []
    seen: set[str | int] = set()

    def add(part: ToolReturnPart) -> None:
        key = part.tool_call_id or id(part)
        if key in seen:
            return
        seen.add(key)
        parts.append(part)

    for part in getattr(request, "parts", []) or []:
        if isinstance(part, ToolReturnPart):
            add(part)

    for msg in getattr(request, "messages", []) or []:
        for part in getattr(msg, "parts", []) or []:
            if isinstance(part, ToolReturnPart):
                add(part)

    return parts
