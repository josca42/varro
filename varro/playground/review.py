from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

from pydantic_ai import BinaryContent
from pydantic_ai.messages import ModelMessage

from varro.chat.trace import TraceEvent, extract_trace
from varro.chat.turn_store import load_turn_messages
from varro.config import DATA_DIR, REVIEWS_DIR
from varro.db.crud.chat import chat as chat_crud

MAX_RESULT_CHARS = 500
REVIEW_FORMAT_VERSION = "3"


def _truncate(text: str, max_chars: int = MAX_RESULT_CHARS) -> tuple[str, bool]:
    if len(text) <= max_chars:
        return text, False
    return text[:max_chars] + f"... ({len(text)} total chars)", True


def _format_tool_args(tool_name: str, args: dict[str, Any]) -> str:
    if tool_name == "Bash":
        return f"`{args.get('command', '')}`"
    if tool_name == "Sql":
        parts = []
        if args.get("df_name"):
            parts.append(f"df_name=`{args['df_name']}`")
        return " | ".join(parts)
    if tool_name == "Jupyter":
        return ""
    if tool_name == "Read":
        fp = args.get("file_path", "")
        extra = []
        if args.get("offset"):
            extra.append(f"offset={args['offset']}")
        if args.get("limit"):
            extra.append(f"limit={args['limit']}")
        suffix = f" ({', '.join(extra)})" if extra else ""
        return f"[{fp}]({fp}){suffix}"
    if tool_name in ("Write", "Edit"):
        fp = args.get("file_path", "")
        return f"[{fp}]({fp})"
    if tool_name == "ColumnValues":
        table = args.get("table", "")
        column = args.get("column", "")
        fuzzy = args.get("fuzzy_match_str")
        text = f"table=`{table}` column=`{column}`"
        if fuzzy:
            text += f" fuzzy=`{fuzzy}`"
        return text
    if tool_name in ("Snapshot", "UpdateUrl"):
        val = args.get("url") or args.get("path") or ""
        return f"`{val}`" if val else ""
    return f"`{json.dumps(args, ensure_ascii=False)}`"


def _image_ext(media_type: str) -> str:
    if "jpeg" in media_type or "jpg" in media_type:
        return "jpg"
    if "gif" in media_type:
        return "gif"
    if "webp" in media_type:
        return "webp"
    return "png"


def _collect_output(
    content: Any, text_chunks: list[str], binaries: list[BinaryContent]
) -> None:
    if content is None:
        return
    if isinstance(content, BinaryContent):
        binaries.append(content)
        return
    if isinstance(content, (list, tuple)):
        for item in content:
            _collect_output(item, text_chunks, binaries)
        return
    text = str(content)
    if text.strip():
        text_chunks.append(text)


def _extract_images(
    content: Any, images_dir: Path, prefix: str
) -> list[tuple[str, str]]:
    chunks: list[str] = []
    binaries: list[BinaryContent] = []
    _collect_output(content, chunks, binaries)

    images = []
    for i, item in enumerate(binaries):
        if not item.is_image:
            continue
        fname = f"{prefix}_{i}.{_image_ext(item.media_type)}"
        images_dir.mkdir(parents=True, exist_ok=True)
        data = item.data
        if isinstance(data, str):
            import base64

            data = base64.b64decode(data)
        (images_dir / fname).write_bytes(data)
        images.append((fname, f"{prefix} image {i}"))
    return images


def _render_thinking(lines: list[str], events: list[TraceEvent]) -> None:
    lines.append("**Thinking**")
    if not events:
        lines.append("_None_")
        return
    for event in events:
        if event.text:
            lines.append(event.text)
            lines.append("")
    if lines[-1] == "":
        lines.pop()


def _render_actions(
    lines: list[str],
    events: list[TraceEvent],
    tc_dir: Path,
) -> None:
    lines.append("**Actions**")
    if not events:
        lines.append("_None_")
        return

    for i, event in enumerate(events, start=1):
        tool = event.tool_name or "Unknown"
        args = event.args or {}
        args_str = _format_tool_args(tool, args)
        seq = event.call_seq or i
        nn = f"{seq:02d}"

        if tool == "Sql" and args.get("query"):
            tc_dir.mkdir(parents=True, exist_ok=True)
            (tc_dir / f"{nn}_sql.sql").write_text(args["query"])
            line = f"**{i}. {tool}** [query](tool_calls/{nn}_sql.sql)"
            if args_str:
                line += f" | {args_str}"
        elif tool == "Jupyter" and args.get("code"):
            tc_dir.mkdir(parents=True, exist_ok=True)
            (tc_dir / f"{nn}_jupyter.py").write_text(args["code"])
            line = f"**{i}. {tool}** [code](tool_calls/{nn}_jupyter.py)"
        else:
            line = f"**{i}. {tool}**"
            if args_str:
                line += f" {args_str}"
        lines.append(line)
        lines.append("")

    if lines[-1] == "":
        lines.pop()


def _render_observations(
    lines: list[str],
    events: list[TraceEvent],
    tc_dir: Path,
    img_dir: Path,
) -> None:
    lines.append("**Observations**")
    if not events:
        lines.append("_None_")
        return

    for i, event in enumerate(events, start=1):
        tool = event.tool_name or "Unknown"
        seq = event.call_seq or i
        label = f"**{i}. {tool}**"
        if seq:
            label += f" (call {seq})"

        if event.kind == "tool_retry":
            retry_text = event.text or ""
            if retry_text:
                trunc, was = _truncate(retry_text)
                if was:
                    tc_dir.mkdir(parents=True, exist_ok=True)
                    rf = f"{seq:02d}_{tool.lower()}_retry.txt"
                    (tc_dir / rf).write_text(retry_text)
                    label += f"\n[{len(retry_text)} chars](tool_calls/{rf})"
                else:
                    label += f"\n{trunc}"
            lines.append(label)
            lines.append("")
            continue

        text_chunks: list[str] = []
        binaries: list[BinaryContent] = []
        _collect_output(event.content, text_chunks, binaries)
        _collect_output(event.supplemental_content, text_chunks, binaries)

        text_output = "\n".join(text_chunks).strip()
        if text_output:
            trunc, was = _truncate(text_output)
            if was:
                tc_dir.mkdir(parents=True, exist_ok=True)
                rf = f"{seq:02d}_{tool.lower()}_result.txt"
                (tc_dir / rf).write_text(text_output)
                label += f"\n[{len(text_output)} chars](tool_calls/{rf})"
            else:
                label += f"\n{trunc}"

        for fname, alt in _extract_images(
            binaries,
            img_dir,
            f"obs_{event.idx:03d}_{seq:02d}",
        ):
            label += f"\n[{alt}](images/{fname})"

        non_image = [item for item in binaries if not item.is_image]
        for item in non_image:
            label += f"\nBinary output: {item.media_type}"

        lines.append(label)
        lines.append("")

    if lines[-1] == "":
        lines.pop()


def review_turn(msgs: list[ModelMessage], turn_dir: Path, turn_idx: int) -> None:
    turn_dir.mkdir(parents=True, exist_ok=True)
    tc_dir = turn_dir / "tool_calls"
    img_dir = turn_dir / "images"
    trace = extract_trace(msgs)

    lines = [f"## Turn {turn_idx}", ""]

    user_events = [event for event in trace.events if event.kind == "user"]
    lines.append("### User")
    if not user_events:
        lines.append("_None_")
    else:
        for event in user_events:
            if event.text:
                lines.append(event.text)
            for fname, alt in _extract_images(
                event.content, img_dir, f"user_{event.idx:03d}"
            ):
                lines.append(f"[{alt}](images/{fname})")
            lines.append("")
        if lines[-1] == "":
            lines.pop()
    lines.append("")

    lines.append("### Trajectory")
    lines.append("")
    for step in range(1, trace.steps + 1):
        lines.append(f"#### Step {step}")
        lines.append("")

        decision_events = [
            event
            for event in trace.events
            if event.step_idx == step
            and event.kind in ("thinking", "assistant_text")
            and not event.is_final
        ]
        _render_thinking(lines, decision_events)
        lines.append("")

        action_events = [
            event
            for event in trace.events
            if event.step_idx == step and event.kind == "tool_call"
        ]
        _render_actions(lines, action_events, tc_dir)
        lines.append("")

        observation_events = [
            event
            for event in trace.events
            if event.step_idx == step and event.kind in ("tool_return", "tool_retry")
        ]
        _render_observations(lines, observation_events, tc_dir, img_dir)
        lines.append("")

    final_parts = [
        event.text
        for event in trace.events
        if event.kind == "assistant_text" and event.is_final and event.text
    ]
    lines.append("### Final response")
    if final_parts:
        lines.append("\n".join(final_parts))
    else:
        lines.append("_None_")
    lines.append("")

    lines.append("### Usage")
    lines.append(
        f"{trace.usage.model_name or 'unknown'} | {trace.usage.input_tokens:,} in | {trace.usage.output_tokens:,} out | {trace.steps} steps"
    )
    lines.append("")

    (turn_dir / "turn.md").write_text("\n".join(lines))
    (turn_dir / ".review_version").write_text(REVIEW_FORMAT_VERSION)


def _excerpt(text: str, max_chars: int) -> str:
    compact = " ".join(text.split())
    if not compact:
        return "_None_"
    if len(compact) <= max_chars:
        return compact
    return compact[:max_chars] + "..."


def review_turn_summary(
    msgs: list[ModelMessage], turn_idx: int, created_at=None
) -> str:
    trace = extract_trace(msgs)
    user_text = ""
    for event in trace.events:
        if event.kind == "user" and event.text:
            user_text = event.text
            break

    tool_counts: Counter = Counter()
    for event in trace.events:
        if event.kind == "tool_call" and event.tool_name:
            tool_counts[event.tool_name] += 1

    user_excerpt = _excerpt(user_text, max_chars=100)
    final_parts = [
        event.text
        for event in trace.events
        if event.kind == "assistant_text" and event.is_final and event.text
    ]
    final_excerpt = _excerpt("\n".join(final_parts), max_chars=120)

    date_str = f" — {created_at.strftime('%Y-%m-%d')}" if created_at else ""

    parts = [
        f"## Turn {turn_idx}{date_str}",
        f"**User**: {user_excerpt}",
    ]
    if tool_counts:
        tools = ", ".join(f"{n}({c})" for n, c in tool_counts.items())
        parts.append(f"Tools: {tools}")
    parts.append(f"Final: {final_excerpt}")
    parts.append(f"[Details]({turn_idx}/turn.md)")
    return "\n".join(parts)


def _load_chat_instructions(user_id: int, chat_id: int) -> str:
    fp = DATA_DIR / "chat" / str(user_id) / str(chat_id) / "0.mpk"
    msgs = load_turn_messages(fp)
    for msg in msgs:
        instructions = getattr(msg, "instructions", None)
        if isinstance(instructions, str) and instructions.strip():
            return instructions.strip()
    raise ValueError(f"No instructions found in {fp}")


def _load_tool_instructions() -> str:
    from varro.agent.assistant import agent

    lines = ["# Tool Instructions", ""]
    for name, tool in agent._function_toolset.tools.items():
        lines.append(f"## {name} tool")
        description = (tool.description or "").strip()
        if description:
            lines.append(description)
        else:
            lines.append("_None_")
        lines.append("")
        lines.append("Parameters schema:")
        lines.append("```json")
        lines.append(json.dumps(tool.function_schema.json_schema, ensure_ascii=False, indent=2))
        lines.append("```")
        lines.append("")
    return "\n".join(lines)


def _turn_review_is_current(turn_dir: Path) -> bool:
    version_fp = turn_dir / ".review_version"
    turn_fp = turn_dir / "turn.md"
    if not turn_fp.exists() or not version_fp.exists():
        return False
    return version_fp.read_text().strip() == REVIEW_FORMAT_VERSION


def review_chat(user_id: int, chat_id: int) -> Path:
    db_chat = chat_crud.for_user(user_id).get(chat_id, with_turns=True)
    if not db_chat:
        raise ValueError(f"Chat {chat_id} not found for user {user_id}")

    review_base = REVIEWS_DIR / str(user_id) / str(chat_id)
    review_base.mkdir(parents=True, exist_ok=True)
    system_instructions = _load_chat_instructions(user_id, chat_id)
    tool_instructions = _load_tool_instructions()
    (review_base / "system_instructions.md").write_text(system_instructions)
    (review_base / "tool_instructions.md").write_text(tool_instructions)
    turn_summaries: list[str] = []

    for turn in db_chat.turns:
        msgs = load_turn_messages(DATA_DIR / turn.obj_fp)
        turn_dir = review_base / str(turn.idx)
        if _turn_review_is_current(turn_dir):
            turn_summaries.append(
                review_turn_summary(msgs, turn.idx, created_at=turn.created_at)
            )
            continue
        review_turn(msgs, turn_dir, turn.idx)
        turn_summaries.append(review_turn_summary(msgs, turn.idx, created_at=turn.created_at))

    chat_lines = [f"# Chat {chat_id}", ""]
    for summary in turn_summaries:
        chat_lines.append(summary)
        chat_lines.append("")
    (review_base / "chat.md").write_text("\n".join(chat_lines))
    return review_base


if __name__ == "__main__":
    review_chat(1, 62)
