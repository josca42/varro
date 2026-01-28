from __future__ import annotations

from typing import AsyncIterator

from pydantic_ai import Agent

from ui.app.chat import (
    UserPromptBlock,
    ModelRequestBlock,
    CallToolsBlock,
)
from varro.agent.assistant import agent
from varro.chat.session import UserSession


async def run_agent(user_text: str, session: UserSession) -> AsyncIterator[object]:
    """
    Run the agent and yield blocks for each completed node.

    One node = one HTML block = one websocket send.
    """
    async with agent.iter(user_text, message_history=session.msgs, deps=session) as run:
        async for node in run:
            block = node_to_block(node)
            if block:
                yield block

    new_msgs = run.result.new_messages()
    session.save_turn(new_msgs, user_text)


def node_to_block(node) -> object | None:
    """Convert a completed pydantic-ai node to a UI block."""

    if Agent.is_user_prompt_node(node):
        return UserPromptBlock(node)

    elif Agent.is_model_request_node(node):
        return ModelRequestBlock(node)

    elif Agent.is_call_tools_node(node):
        return CallToolsBlock(node)

    elif Agent.is_end_node(node):
        return None

    return None
