from pydantic_ai.messages import ModelMessagesTypeAdapter
import chainlit as cl

import asyncio
import json
import re
from typing import Any, Awaitable, Callable, List, Optional
import pandas as pd
import plotly.graph_objects as go
from pydantic_ai import Agent, RunContext
from pydantic_ai.messages import (
    PartDeltaEvent,
    PartStartEvent,
    ThinkingPart,
    ThinkingPartDelta,
    TextPart,
    TextPartDelta,
    ToolCallPart,
    BuiltinToolCallPart,
)
from varro.agent.memory import SessionStore
from varro.agent.assistant import agent


async def assistant_msg(msg_content: str):
    history = ModelMessagesTypeAdapter.validate_python(
        cl.user_session.get("message_history", [])
    )
    store = cl.user_session.get("session_store")
    handler = MessageStreamHandler(store)

    async with agent.iter(
        msg_content,
        deps=store,
        message_history=history or None,
    ) as run:
        async for node in run:
            await handler.process_node(node, run.ctx)

    history += run.result.new_messages()
    cl.user_session.set("message_history", history)
    cl.user_session.set("session_store", run.ctx.deps.user_deps)


# ---------------------------------------------------------------------------
# PlaceholderParser
# ---------------------------------------------------------------------------


class PlaceholderParser:
    """
    Detect and yield <df>id</df> and <fig>id</fig> placeholders while streaming text.

    - Handles placeholders split across arbitrary chunk boundaries.
    - Streams plain text as soon as it's safe.
    - Emits a callback for each detected placeholder in-order.
    - `flush` will still try to parse any complete placeholders before outputting leftovers.
    """

    # Accept optional whitespace around tag names: <fig >key</ fig>
    _PATTERN = re.compile(
        r"<\s*(?P<atype>df|fig)\s*>(?P<akey>[^<]*?)</\s*(?P=atype)\s*>",
        re.DOTALL,
    )
    _OPEN_TAG = re.compile(r"<\s*(?:df|fig)\s*>")  # to find last unmatched start tag

    def __init__(self) -> None:
        self._buffer: str = ""

    async def process_chunk(
        self,
        chunk: str,
        on_text: Callable[[str], Awaitable[None]],
        on_placeholder: Callable[[str, str], Awaitable[Optional[cl.Message]]],
    ) -> List[cl.Message]:
        """
        Split a text chunk into normal text and placeholders.

        - `on_text(text)` is called with safe-to-output plain text.
        - `on_placeholder(atype, akey)` is called for each detected <atype>akey</atype>.
        - Returns any cl.Message elements produced by on_placeholder.
        """
        if not chunk:
            return []

        self._buffer += chunk
        elements: List[cl.Message] = []

        while True:
            m = self._PATTERN.search(self._buffer)
            if not m:
                # No full placeholder available yet.
                # Keep the last start tag (if any) in the buffer; flush everything before it.
                last_start = -1
                for st in self._OPEN_TAG.finditer(self._buffer):
                    last_start = st.start()

                if last_start != -1:
                    if last_start:
                        await on_text(self._buffer[:last_start])
                    self._buffer = self._buffer[last_start:]
                else:
                    # No recognizable start tag; keep from the last '<', flush the rest.
                    last_lt = self._buffer.rfind("<")
                    if last_lt == -1:
                        await on_text(self._buffer)
                        self._buffer = ""
                    else:
                        if last_lt:
                            await on_text(self._buffer[:last_lt])
                        self._buffer = self._buffer[last_lt:]
                break

            # Stream any plain text before the placeholder.
            if m.start():
                await on_text(self._buffer[: m.start()])

            # Emit the placeholder element (strip the key to avoid stray whitespace)
            element_msg = await on_placeholder(
                m.group("atype"), m.group("akey").strip()
            )
            if element_msg:
                elements.append(element_msg)

            # Consume the matched span and continue scanning.
            self._buffer = self._buffer[m.end() :]

        return elements

    async def flush(
        self,
        on_text: Callable[[str], Awaitable[None]],
        on_placeholder: Callable[[str, str], Awaitable[Optional[cl.Message]]],
    ) -> None:
        """
        Finalize the stream:
        - First, parse any remaining complete placeholders in the buffer.
        - Then emit any leftover text (e.g., an incomplete tag).
        """
        while True:
            m = self._PATTERN.search(self._buffer)
            if not m:
                break
            if m.start():
                await on_text(self._buffer[: m.start()])
            await on_placeholder(m.group("atype"), m.group("akey").strip())
            self._buffer = self._buffer[m.end() :]

        if self._buffer:
            await on_text(self._buffer)
            self._buffer = ""


# ---------------------------------------------------------------------------
# ToolStepBuilder
# ---------------------------------------------------------------------------
TOOL_NAME2TITLE = {
    "sql_query": "henter data",
    "view_column_values": "henter data",
    "memory": "konsulterer hukommelse",
    "jupyter_notebook": "beregner",
    "web_search": "søger på internettet",
}


class ToolStepBuilder:
    """Create a rich cl.Step for a tool call."""

    @staticmethod
    async def build(
        tool_call: ToolCallPart | BuiltinToolCallPart,
        error: Optional[str] = None,
        result: Any | None = None,
    ) -> None:
        async with cl.Step(name=TOOL_NAME2TITLE[tool_call.tool_name]) as step:
            kwargs = json.loads(tool_call.args)
            if tool_call.tool_name == "jupyter_notebook":
                step.input = kwargs["code"]
                step.language = "python"
            else:
                step.input = json.dumps(kwargs, indent=2)

            if error:
                step.output = f"❌ {error}"
            elif result is not None and isinstance(result, str):
                step.output = result[:500] + "…" if len(result) > 500 else result
            else:
                step.output = "✓ Completed"


# ---------------------------------------------------------------------------
# MessageStreamHandler
# ---------------------------------------------------------------------------


class MessageStreamHandler:
    """
    Finite‑state helper that turns Pydantic‑AI streaming nodes into
    Chainlit UI elements.

    Contract
    --------
    * At most ONE open `cl.Step` (thinking) or `cl.Message` (response)
      exists at any time.
    * When a new thinking step, new response message, or a tool call
      starts, the previous artefact is **closed** (update / __aexit__).
    """

    # ------------------------------------------------------------------ init
    def __init__(self, store: "SessionStore") -> None:
        self._store = store

        self._placeholder_parser: PlaceholderParser = PlaceholderParser()
        self._container_step: cl.Step | None = None
        self._thinking_step: cl.Step | None = None
        self._response_msg: cl.Message | None = None
        self.last_part = None
        self._pending_builtin_tool_id: Optional[str] = None
        self._builtin_text_buffer: List[str] = []
        self._builtin_step_displayed: bool = False

    # ---------------------------------------------------------------- helpers
    async def _ensure_response_message(self) -> cl.Message:
        if self._response_msg is None:
            self._response_msg = cl.Message(content="")
            await self._response_msg.send()
        return self._response_msg

    async def _stream_text(self, text: str) -> None:
        if not text:
            return
        msg = await self._ensure_response_message()
        await msg.stream_token(text)

    # ---------------------------------------------------------------- public
    async def process_node(self, node: Any, ctx: RunContext) -> None:
        if Agent.is_model_request_node(node):
            await self._handle_model_stream(node, ctx)

        elif Agent.is_call_tools_node(node):
            # Close thinking but keep response open so placeholders can finish
            await self._close_thinking()
            if self._response_msg:
                await self._response_msg.update()
            await self._handle_tool_calls(node)

        elif Agent.is_end_node(node):
            await self._finalize()

    # ------------------------------------------------------------- model‑stream
    async def _handle_model_stream(self, node: Any, ctx: RunContext) -> None:
        async with node.stream(ctx) as stream:
            async for event in stream:
                if isinstance(event, PartStartEvent):
                    await self._handle_part_start(event)
                elif isinstance(event, PartDeltaEvent):
                    await self._handle_part_delta(event)

    # ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑
    #  Part‑START  → decide what to open next
    # ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑
    async def _handle_part_start(self, ev: PartStartEvent) -> None:
        if isinstance(ev.part, ThinkingPart):
            # close any response message first
            await self._close_response()
            await self._close_thinking()

            # open container if not already open
            if not self._container_step:
                self._container_step = cl.Step(name="Steps", default_open=True)
                await self._container_step.__aenter__()

            # open fresh thinking step inside container
            self._thinking_step = cl.Step(
                name="Tænker", type="thinking", show_input=False
            )
            await self._thinking_step.__aenter__()

            # stream any initial content immediately
            if ev.part.content:
                await self._thinking_step.stream_token(ev.part.content)

            self.last_part = "thinking"

        elif isinstance(ev.part, BuiltinToolCallPart):
            await self._close_thinking()
            if self._response_msg:
                await self._response_msg.update()

            self._pending_builtin_tool_id = self._builtin_key(ev.part.tool_call_id)
            self._builtin_text_buffer = []
            self._builtin_step_displayed = False
            self.last_part = "builtin_tool"

        elif isinstance(ev.part, TextPart):
            await self._close_thinking()
            await self._close_container()  # close container before response
            await self._close_response()  # previous message ends

            if self._should_buffer_builtin_text():
                if ev.part.content:
                    self._builtin_text_buffer.append(ev.part.content)
                self.last_part = "builtin_text_buffer"
                return

            self._placeholder_parser = PlaceholderParser()  # reset buffer
            self._response_msg = cl.Message(content="")
            await self._response_msg.send()

            if ev.part.content:
                await self._placeholder_parser.process_chunk(
                    ev.part.content,
                    on_text=self._stream_text,
                    on_placeholder=self._render_placeholder,
                )
            self.last_part = "text"

    # ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑
    #  Part‑DELTA  → stream incremental tokens
    # ‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑‑
    async def _handle_part_delta(self, ev: PartDeltaEvent) -> None:
        if isinstance(ev.delta, ThinkingPartDelta):
            # thinking step *must* exist here
            await self._thinking_step.stream_token(ev.delta.content_delta)
            self.last_part = "thinking"

        elif isinstance(ev.delta, TextPartDelta):
            if self._should_buffer_builtin_text():
                if ev.delta.content_delta:
                    self._builtin_text_buffer.append(ev.delta.content_delta)
                self.last_part = "builtin_text_buffer"
                return
            await self._placeholder_parser.process_chunk(
                ev.delta.content_delta,
                on_text=self._stream_text,
                on_placeholder=self._render_placeholder,
            )
            self.last_part = "text"

    # ------------------------------------------------------------- placeholders
    async def _render_placeholder(self, atype: str, akey: str) -> cl.Message | None:
        if self._response_msg:
            await self._response_msg.update()

        if atype == "df":
            obj = self._store.dfs.get(akey)
            df = obj.reset_index() if not isinstance(obj.index, pd.RangeIndex) else obj
            element = cl.Dataframe(name=akey, data=df.round(4), display="inline")
        elif atype == "fig":
            obj = self._store.figs.get(akey)
            element = cl.Plotly(name=akey, figure=obj, display="inline")
        else:
            raise ValueError(f"Invalid object type: {atype}")

        await cl.Message(content="", elements=[element]).send()
        self._response_msg = None
        return None

    def _should_buffer_builtin_text(self) -> bool:
        return (
            self._pending_builtin_tool_id is not None
            and not self._builtin_step_displayed
        )

    @staticmethod
    def _builtin_key(tool_call_id: Optional[str]) -> str:
        return tool_call_id or "__builtin__"

    # ---------------------------------------------------------------- tool‑calls
    async def _handle_tool_calls(self, node: Any) -> None:
        if not any(
            isinstance(part, (ToolCallPart, BuiltinToolCallPart))
            for part in node.model_response.parts
        ):
            return

        # open container if not already open
        if not self._container_step:
            self._container_step = cl.Step(name="Steps", type="container")
            await self._container_step.__aenter__()

        for part in node.model_response.parts:
            if isinstance(part, (ToolCallPart, BuiltinToolCallPart)):
                await ToolStepBuilder.build(part)
                if isinstance(part, BuiltinToolCallPart):
                    self._builtin_step_displayed = True
                    if (
                        self._pending_builtin_tool_id
                        and self._pending_builtin_tool_id
                        == self._builtin_key(part.tool_call_id)
                    ):
                        await self._flush_builtin_buffer()
                await asyncio.sleep(0)

    async def _flush_builtin_buffer(self) -> None:
        if not self._pending_builtin_tool_id:
            return

        buffered_text = "".join(self._builtin_text_buffer)
        self._builtin_text_buffer = []

        await self._close_container()
        await self._close_response()

        if buffered_text:
            self._placeholder_parser = PlaceholderParser()
            self._response_msg = cl.Message(content="")
            await self._response_msg.send()
            await self._placeholder_parser.process_chunk(
                buffered_text,
                on_text=self._stream_text,
                on_placeholder=self._render_placeholder,
            )
            self.last_part = "text"

        self._pending_builtin_tool_id = None
        self._builtin_step_displayed = False

    # ----------------------------------------------------------------‑‑ cleanup
    async def _close_thinking(self) -> None:
        if self._thinking_step:
            await self._thinking_step.__aexit__(None, None, None)
            self._thinking_step = None

    async def _close_container(self) -> None:
        if self._container_step:
            await self._container_step.__aexit__(None, None, None)
            self._container_step = None

    async def _close_response(self) -> None:
        await self._placeholder_parser.flush(
            self._stream_text, self._render_placeholder
        )

        if self._response_msg:
            await self._response_msg.update()
            self._response_msg = None

    async def _finalize(self) -> None:
        await self._close_response()
        await self._close_thinking()
        await self._close_container()
