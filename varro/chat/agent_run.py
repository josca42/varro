from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import AsyncIterator

from pydantic_ai import Agent
from pydantic_ai.messages import ThinkingPart, TextPart, ToolCallPart

from ui.app.chat import UserPromptBlock, ModelRequestBlock, CallToolsBlock
from ui.app.tool import ReasoningBlock
from varro.agent.assistant import AssistantRunDeps, agent
from varro.chat.render_cache import save_turn_render_cache
from varro.chat.tool_results import ToolRenderRecord, extract_tool_render_records
from varro.chat.turn_store import load_messages_for_turns, save_turn_messages, turn_fp
from varro.config import DATA_DIR
from varro.db.models.chat import Chat, Turn
from varro.db import crud


@dataclass
class ReasoningState:
    turn_idx: int
    sequence: list[dict] = field(default_factory=list)
    returns: list[ToolRenderRecord] = field(default_factory=list)
    sent: bool = False

    @property
    def block_id(self) -> str:
        return f"reasoning-{self.turn_idx}"

    def build_block(self, shell) -> object | None:
        block = ReasoningBlock(
            self.sequence,
            self.returns,
            shell=shell,
            block_id=self.block_id,
            swap_oob=self.sent,
        )
        if block:
            self.sent = True
        return block

    def clear(self):
        self.sequence.clear()
        self.returns.clear()
        self.sent = False


async def run_agent(
    user_text: str,
    *,
    user_id: int,
    chats,
    shell,
    chat_id: int,
    current_url: str | None = None,
) -> AsyncIterator[object]:
    chat = chats.get(chat_id, with_turns=True)
    if not chat:
        return

    msg_history = load_messages_for_turns(chat.turns)
    turn_idx = len(chat.turns)
    state = ReasoningState(turn_idx)

    request_url = (current_url or "").strip()
    if not request_url.startswith("/"):
        request_url = "/"

    deps = AssistantRunDeps(
        user_id=user_id,
        chat_id=chat_id,
        shell=shell,
        request_current_url=lambda: request_url,
    )
    async with agent.iter(user_text, message_history=msg_history, deps=deps) as run:
        async for node in run:
            for block in node_to_blocks(node, shell, state):
                if block:
                    yield block

    new_msgs = run.result.new_messages()
    fp = turn_fp(user_id, chat_id, turn_idx)
    save_turn_messages(new_msgs, fp)
    save_turn_render_cache(new_msgs, fp, shell)

    crud.turn.create(
        Turn(
            chat_id=chat_id,
            user_text=user_text,
            obj_fp=str(fp.relative_to(DATA_DIR)),
            idx=turn_idx,
        )
    )
    crud.chat.update(Chat(id=chat_id, updated_at=datetime.now(timezone.utc)))

    if turn_idx == 0:
        asyncio.create_task(_set_chat_title(chat_id, user_text))


_title_agent = Agent(
    "anthropic:claude-haiku-4-5",
    system_prompt=(
        "Generate a short chat title (4-5 words) for a conversation that starts with "
        "the user message below. Return ONLY the title, no quotes or punctuation."
    ),
)


async def _set_chat_title(chat_id: int, user_text: str) -> None:
    try:
        result = await _title_agent.run(user_text)
        title = result.output.strip()[:100]
        crud.chat.update(Chat(id=chat_id, title=title))
    except Exception:
        pass


def node_to_blocks(
    node,
    shell,
    state: ReasoningState,
) -> list[object]:
    if Agent.is_user_prompt_node(node):
        return [UserPromptBlock(node)]

    if Agent.is_model_request_node(node):
        tool_parts = extract_tool_render_records(node.request)
        if not tool_parts:
            return []
        state.returns.extend(tool_parts)
        if state.sequence:
            return [state.build_block(shell)]
        return [ModelRequestBlock(node)]

    if Agent.is_call_tools_node(node):
        if node.model_response.finish_reason != "stop":
            cache_tool_calls(node.model_response.parts, state.sequence)
            return []
        blocks = []
        block = state.build_block(shell)
        if block:
            blocks.append(block)
        blocks.append(CallToolsBlock(node, shell=shell, connected=False))
        state.clear()
        return blocks

    if Agent.is_end_node(node):
        block = state.build_block(shell)
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
                    "args": part.args_as_dict(),
                    "call_id": part.tool_call_id,
                }
            )
