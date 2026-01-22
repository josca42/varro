from __future__ import annotations

import asyncio
import json
import uuid
from pathlib import Path
from typing import Any

from fasthtml.common import Div, to_xml
from pydantic_ai import Agent, BinaryContent
from pydantic_ai.messages import (
    BaseToolCallPart,
    ThinkingPart,
    TextPart,
    FunctionToolResultEvent,
)

from ui.app import (
    ChatFormEnabled,
    ProgressIndicator,
    ErrorBlock,
    ThinkingBlock,
    ToolCallBlock,
    TextBlock,
)
from varro.agent.assistant import agent
from varro.chat.session import ChatSession


async def agent_html_stream(user_msg: str, chat_sess: ChatSession):
    rendered_text = False
    async with agent.iter(
        user_msg, deps=chat_sess, message_history=chat_sess.msgs
    ) as run:
        async for node in run:
            if Agent.is_model_request_node(node):
                yield ws_html("progress", ProgressIndicator("Thinking..."))

            elif Agent.is_call_tools_node(node):
                for part in node.model_response.parts:
                    if isinstance(part, ThinkingPart):
                        yield ws_html("content", ThinkingBlock(part.content))

                tool_calls = [
                    part
                    for part in node.model_response.parts
                    if isinstance(part, BaseToolCallPart)
                ]

                if tool_calls:
                    yield ws_html("progress", ProgressIndicator("Running tools..."))
                    tool_results = await _execute_tools(node, run)

                    for part in tool_calls:
                        args = part.args or {}
                        if isinstance(args, str):
                            args = json.loads(args)
                        result = tool_results.get(part.tool_call_id)
                        result_text, attachments = _extract_tool_result(result)
                        yield ws_html(
                            "content",
                            ToolCallBlock(
                                part.tool_name,
                                args,
                                result_text,
                                attachments,
                            ),
                        )

                for part in node.model_response.parts:
                    if isinstance(part, TextPart):
                        rendered_text = True
                        yield ws_html("content", TextBlock(part.content))

            elif Agent.is_end_node(node):
                if run.result and run.result.output and not rendered_text:
                    yield ws_html("content", TextBlock(run.result.output))

    if run.result:
        chat_sess.msgs += run.result.new_messages()
        chat_sess.save_run_msgs(run.result)


async def _execute_tools(node, run) -> dict[str, object]:
    results = {}
    async with node.stream(run.ctx) as stream:
        async for event in stream:
            if isinstance(event, FunctionToolResultEvent):
                results[event.tool_call_id] = event.result
    return results


def _extract_tool_result(result): ...


def ws_html(event: str, component) -> str:
    html = to_xml(component)
    html_escaped = html.replace("\n", "&#10;")
    return html_escaped
