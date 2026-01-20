from __future__ import annotations

import asyncio

from pydantic_ai import Agent, BinaryContent
from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings

from varro.db.models.chat import Chat, Message
from varro.db.models.user import User

import app.routes.chat as chat_routes


class DummySessionStore:
    def __init__(self, user: User):
        self.user = user


def _noop_create(msg):
    return msg


def build_agent() -> Agent:
    model = AnthropicModel("claude-sonnet-4-5")
    settings = AnthropicModelSettings(
        anthropic_thinking={"type": "enabled", "budget_tokens": 800},
        parallel_tool_calls=True,
    )

    agent = Agent(
        model=model,
        model_settings=settings,
        system_prompt="Use tools when asked and be concise.",
    )

    @agent.tool_plain
    def add(a: int, b: int) -> int:
        return a + b

    @agent.tool_plain
    def echo(text: str) -> str:
        return text

    @agent.tool_plain
    def fake_image(label: str):
        return [BinaryContent(data=f"fake:{label}".encode("utf-8"), media_type="image/png")]

    return agent


async def main() -> None:
    chat_routes.agent = build_agent()
    chat_routes.SessionStore = DummySessionStore
    chat_routes.crud.message.create = _noop_create

    user = User(id=1, email="debug@example.com")
    chat = Chat(
        id=42,
        user_id=1,
        messages=[
            Message(
                role="user",
                content={
                    "text": "Use tools to add 2+3, echo 'ok', then fake_image 'debug'."
                },
            )
        ],
    )

    async for chunk in chat_routes.agent_html_stream(chat, user):
        print(chunk)


if __name__ == "__main__":
    asyncio.run(main())
