from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from pydantic_ai import BinaryContent
from pydantic_ai.messages import (
    ModelMessage,
    ModelRequest,
    ModelResponse,
    TextPart,
    ThinkingPart,
    ToolCallPart,
    ToolReturnPart,
    UserPromptPart,
)

from varro.chat.turn_store import load_turn_messages
from varro.config import DATA_DIR, REVIEWS_DIR
from varro.db.crud.chat import chat as chat_crud

MAX_RESULT_CHARS = 500


def _truncate(text: str, max_chars: int = MAX_RESULT_CHARS) -> tuple[str, bool]:
    if len(text) <= max_chars:
        return text, False
    return text[:max_chars] + f"... ({len(text)} total chars)", True


def _format_tool_args(tool_name: str, args: dict) -> str:
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
        s = f"table=`{table}` column=`{column}`"
        if fuzzy:
            s += f" fuzzy=`{fuzzy}`"
        return s
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


def _extract_images(content, images_dir: Path, prefix: str) -> list[tuple[str, str]]:
    images = []
    if not isinstance(content, (list, tuple)):
        return images
    for i, item in enumerate(content):
        if isinstance(item, BinaryContent) and item.is_image:
            fname = f"{prefix}_{i}.{_image_ext(item.media_type)}"
            images_dir.mkdir(parents=True, exist_ok=True)
            data = item.data
            if isinstance(data, str):
                import base64

                data = base64.b64decode(data)
            (images_dir / fname).write_bytes(data)
            images.append((fname, f"{prefix} image {i}"))
    return images


def review_turn(msgs: list[ModelMessage], turn_dir: Path, turn_idx: int) -> None:
    turn_dir.mkdir(parents=True, exist_ok=True)
    tc_dir = turn_dir / "tool_calls"
    img_dir = turn_dir / "images"

    user_texts: list[str] = []
    user_images: list[tuple[str, str]] = []
    thinking_parts: list[str] = []
    tool_calls: list[ToolCallPart] = []
    tool_returns: dict[str, ToolReturnPart] = {}
    response_texts: list[str] = []
    total_in = 0
    total_out = 0
    model_name = None
    num_steps = 0

    for msg in msgs:
        if isinstance(msg, ModelRequest):
            for part in msg.parts:
                if isinstance(part, UserPromptPart):
                    if isinstance(part.content, str):
                        user_texts.append(part.content)
                    elif isinstance(part.content, (list, tuple)):
                        for item in part.content:
                            if isinstance(item, str):
                                user_texts.append(item)
                        user_images.extend(
                            _extract_images(part.content, img_dir, "user")
                        )
                elif isinstance(part, ToolReturnPart):
                    tool_returns[part.tool_call_id] = part
        elif isinstance(msg, ModelResponse):
            num_steps += 1
            if msg.model_name:
                model_name = msg.model_name
            total_in += msg.usage.input_tokens
            total_out += msg.usage.output_tokens
            for part in msg.parts:
                if isinstance(part, ThinkingPart) and part.content:
                    thinking_parts.append(part.content)
                elif isinstance(part, ToolCallPart):
                    tool_calls.append(part)
                elif isinstance(part, TextPart) and msg.finish_reason == "stop":
                    response_texts.append(part.content)

    lines = [f"## Turn {turn_idx}", ""]

    # User
    user_text = "\n".join(user_texts).strip()
    if user_text:
        lines.append(f"**User**: {user_text}")
    for fname, alt in user_images:
        lines.append(f"[{alt}](images/{fname})")
    if user_text or user_images:
        lines.append("")

    # Thinking
    if thinking_parts:
        lines.append("### Thinking")
        combined = "\n\n".join(thinking_parts)
        truncated, _ = _truncate(combined, 2000)
        lines.append(truncated)
        lines.append("")

    # Tool Calls
    if tool_calls:
        lines.append("### Tool Calls")
        lines.append("")
        for i, tc in enumerate(tool_calls):
            nn = f"{i + 1:02d}"
            name = tc.tool_name
            args = tc.args_as_dict() if tc.args else {}

            args_str = _format_tool_args(name, args)

            if name == "Sql" and args.get("query"):
                tc_dir.mkdir(parents=True, exist_ok=True)
                (tc_dir / f"{nn}_sql.sql").write_text(args["query"])
                line = f"**{i + 1}. {name}** [query](tool_calls/{nn}_sql.sql)"
                if args_str:
                    line += f" | {args_str}"
            elif name == "Jupyter" and args.get("code"):
                tc_dir.mkdir(parents=True, exist_ok=True)
                (tc_dir / f"{nn}_jupyter.py").write_text(args["code"])
                line = f"**{i + 1}. {name}** [code](tool_calls/{nn}_jupyter.py)"
            else:
                line = f"**{i + 1}. {name}**"
                if args_str:
                    line += f" {args_str}"

            ret = tool_returns.get(tc.tool_call_id)
            if ret and ret.content is not None:
                content_str = str(ret.content)
                if content_str:
                    trunc, was = _truncate(content_str)
                    if was:
                        tc_dir.mkdir(parents=True, exist_ok=True)
                        rf = f"{nn}_{name.lower()}_result.txt"
                        (tc_dir / rf).write_text(content_str)
                        line += f"\n→ [{len(content_str)} chars](tool_calls/{rf})"
                    else:
                        line += f"\n→ {trunc}"

                if isinstance(ret.content, (list, tuple)):
                    for fname, alt in _extract_images(
                        ret.content, img_dir, f"tool_{nn}"
                    ):
                        line += f"\n[{alt}](images/{fname})"

            lines.append(line)
            lines.append("")

    # Response
    if response_texts:
        lines.append("### Response")
        lines.append("\n".join(response_texts))
        lines.append("")

    # Usage
    lines.append("### Usage")
    lines.append(
        f"{model_name or 'unknown'} | {total_in:,} in | {total_out:,} out | {num_steps} steps"
    )
    lines.append("")

    (turn_dir / "turn.md").write_text("\n".join(lines))


def review_turn_summary(
    msgs: list[ModelMessage], turn_idx: int, created_at=None
) -> str:
    user_text = ""
    tool_counts: Counter = Counter()

    for msg in msgs:
        if isinstance(msg, ModelRequest):
            for part in msg.parts:
                if isinstance(part, UserPromptPart):
                    if isinstance(part.content, str):
                        user_text = part.content
                    elif isinstance(part.content, (list, tuple)):
                        for item in part.content:
                            if isinstance(item, str):
                                user_text = item
                                break
        elif isinstance(msg, ModelResponse):
            for part in msg.parts:
                if isinstance(part, ToolCallPart):
                    tool_counts[part.tool_name] += 1

    if len(user_text) > 100:
        user_text = user_text[:100] + "..."

    date_str = f" — {created_at.strftime('%Y-%m-%d')}" if created_at else ""

    parts = [
        f"## Turn {turn_idx}{date_str}",
        f"**User**: {user_text}",
    ]
    if tool_counts:
        tools = ", ".join(f"{n}({c})" for n, c in tool_counts.items())
        parts.append(f"Tools: {tools}")
    parts.append(f"[Details]({turn_idx}/turn.md)")
    return "\n".join(parts)


def review_chat(user_id: int, chat_id: int) -> Path:
    db_chat = chat_crud.for_user(user_id).get(chat_id, with_turns=True)
    if not db_chat:
        raise ValueError(f"Chat {chat_id} not found for user {user_id}")

    review_base = REVIEWS_DIR / str(user_id) / str(chat_id)
    review_base.mkdir(parents=True, exist_ok=True)

    for turn in db_chat.turns:
        turn_dir = review_base / str(turn.idx)
        if (turn_dir / "turn.md").exists():
            continue
        msgs = load_turn_messages(DATA_DIR / turn.obj_fp)
        review_turn(msgs, turn_dir, turn.idx)
        summary = review_turn_summary(msgs, turn.idx, created_at=turn.created_at)
        (turn_dir / "summary.md").write_text(summary)

    chat_lines = [f"# Chat {chat_id}", ""]
    for turn in db_chat.turns:
        summary_fp = review_base / str(turn.idx) / "summary.md"
        if summary_fp.exists():
            chat_lines.append(summary_fp.read_text())
            chat_lines.append("")
    (review_base / "chat.md").write_text("\n".join(chat_lines))
    return review_base


if __name__ == "__main__":
    review_chat(1, 61)
