from __future__ import annotations

from typing import AsyncIterator

from fasthtml.common import to_xml
from pydantic_ai import Agent

from ui.app.chat import (
    UserPromptBlock,
    ModelRequestBlock,
    CallToolsBlock,
    ErrorBlock,
)
from varro.agent.assistant import agent
from varro.chat.session import UserSession


async def run_agent(user_text: str, session: UserSession) -> AsyncIterator[str]:
    """
    Run the agent and yield HTML blocks for each completed node.

    One node = one HTML block = one websocket send.
    """
    try:
        async with agent.iter(
            user_text, message_history=session.msgs, deps=session
        ) as run:
            async for node in run:
                html = node_to_html(node)
                if html:
                    yield html

        new_msgs = run.result.new_messages()
        session.save_turn(new_msgs, user_text)

    except Exception as e:
        yield to_xml(ErrorBlock(str(e)))


def node_to_html(node) -> str | None:
    """Convert a completed pydantic-ai node to HTML."""

    if Agent.is_user_prompt_node(node):
        return to_xml(UserPromptBlock(node))

    elif Agent.is_model_request_node(node):
        html = ModelRequestBlock(node)
        return to_xml(html) if html else None

    elif Agent.is_call_tools_node(node):
        html = CallToolsBlock(node)
        return to_xml(html) if html else None

    elif Agent.is_end_node(node):
        return None

    return None
