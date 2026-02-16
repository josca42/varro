from __future__ import annotations

from datetime import datetime
from types import SimpleNamespace

from pydantic_ai import BinaryContent
from pydantic_ai.messages import (
    ModelRequest,
    ModelResponse,
    RetryPromptPart,
    TextPart,
    ThinkingPart,
    ToolCallPart,
    ToolReturnPart,
    UserPromptPart,
)

from varro.chat import review as review_module
from varro.chat.review import REVIEW_FORMAT_VERSION, review_turn, review_turn_summary

SYSTEM_PROMPT = """
<role>
You are the state statistician.
</role>

<tools>
**Sql(query, df_name?)** — Execute SQL against the database.
**Read(file_path, offset?, limit?)** — Read files from the workspace.
</tools>
""".strip()


def _build_review_messages() -> list:
    image = BinaryContent(data=b"img", media_type="image/png")
    return [
        ModelRequest(
            parts=[UserPromptPart(content="Analyse this")],
            instructions=SYSTEM_PROMPT,
        ),
        ModelResponse(
            parts=[
                ThinkingPart(content="Need query and plot"),
                ToolCallPart(
                    tool_name="Sql",
                    args={"query": "select 1 as x", "df_name": "df_x"},
                    tool_call_id="call_sql",
                ),
                ToolCallPart(
                    tool_name="Jupyter",
                    args={"code": "fig = 1", "show": ["fig"]},
                    tool_call_id="call_plot",
                ),
            ],
            finish_reason="tool_call",
            model_name="model-a",
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="Sql",
                    content="Stored as df_x\ndf.head(1)\nx\n1",
                    tool_call_id="call_sql",
                    metadata={"ui": {"has_tool_content": False}},
                ),
                RetryPromptPart(
                    content="NameError('fig')",
                    tool_name="Jupyter",
                    tool_call_id="call_plot",
                ),
            ]
        ),
        ModelResponse(
            parts=[
                TextPart(content="Retry with a valid figure."),
                ToolCallPart(
                    tool_name="Jupyter",
                    args={"code": "fig = 2", "show": ["fig"]},
                    tool_call_id="call_plot_2",
                ),
            ],
            finish_reason="tool_call",
            model_name="model-a",
        ),
        ModelRequest(
            parts=[
                ToolReturnPart(
                    tool_name="Jupyter",
                    content="Rendered",
                    tool_call_id="call_plot_2",
                    metadata={"ui": {"has_tool_content": True}},
                ),
                UserPromptPart(content=[image]),
            ]
        ),
        ModelResponse(
            parts=[TextPart(content="Final answer.")],
            finish_reason="stop",
            model_name="model-a",
        ),
    ]


def test_review_turn_renders_chronological_trajectory(tmp_path) -> None:
    turn_dir = tmp_path / "0"
    review_turn(_build_review_messages(), turn_dir, 0)

    md = (turn_dir / "turn.md").read_text()

    assert "### User" in md
    assert "### Trajectory" in md
    assert "#### Step 1" in md
    assert "#### Step 2" in md
    assert "#### Step 3" in md
    assert "**Thinking**" in md
    assert "**Decision**" not in md
    assert "**Actions**" in md
    assert "**Observations**" in md
    assert "### Final response" in md
    assert "Final answer." in md
    assert "### Usage" in md


def test_review_turn_links_sql_and_jupyter_artifacts(tmp_path) -> None:
    turn_dir = tmp_path / "1"
    review_turn(_build_review_messages(), turn_dir, 1)

    md = (turn_dir / "turn.md").read_text()

    assert "tool_calls/01_sql.sql" in md
    assert "tool_calls/02_jupyter.py" in md
    assert "tool_calls/03_jupyter.py" in md
    assert (turn_dir / "tool_calls" / "01_sql.sql").exists()
    assert (turn_dir / "tool_calls" / "02_jupyter.py").exists()
    assert (turn_dir / "tool_calls" / "03_jupyter.py").exists()


def test_review_turn_attaches_tool_images_to_observations_not_user(tmp_path) -> None:
    turn_dir = tmp_path / "2"
    review_turn(_build_review_messages(), turn_dir, 2)

    md = (turn_dir / "turn.md").read_text()

    assert "user_" not in md
    assert "obs_" in md
    assert "NameError('fig')" in md
    assert "→" not in md
    assert (turn_dir / "images").exists()


def test_review_turn_writes_review_version(tmp_path) -> None:
    turn_dir = tmp_path / "3"
    review_turn(_build_review_messages(), turn_dir, 3)

    assert (turn_dir / ".review_version").read_text() == REVIEW_FORMAT_VERSION


def test_review_turn_summary_includes_final_excerpt() -> None:
    summary = review_turn_summary(
        _build_review_messages(),
        0,
        created_at=datetime(2026, 2, 12),
    )

    assert "## Turn 0 — 2026-02-12" in summary
    assert "**User**: Analyse this" in summary
    assert "Tools: Sql(1), Jupyter(2)" in summary
    assert "Final: Final answer." in summary


def test_review_turn_summary_truncates_final_excerpt() -> None:
    msgs = [
        ModelRequest(parts=[UserPromptPart(content="User prompt")]),
        ModelResponse(
            parts=[TextPart(content="A " * 200)],
            finish_reason="stop",
            model_name="model-a",
        ),
    ]

    summary = review_turn_summary(msgs, 0)
    final_line = [line for line in summary.splitlines() if line.startswith("Final:")][0]

    assert final_line.endswith("...")
    assert len(final_line) == len("Final: ") + 123


def test_review_chat_does_not_generate_summary_md(tmp_path, monkeypatch) -> None:
    review_dir = tmp_path / "chat_reviews"
    monkeypatch.setattr(review_module, "REVIEWS_DIR", review_dir)
    monkeypatch.setattr(review_module, "DATA_DIR", tmp_path)
    monkeypatch.setattr(review_module, "load_turn_messages", lambda fp: _build_review_messages())
    monkeypatch.setattr(
        review_module,
        "_load_tool_instructions",
        lambda: "\n".join(
            [
                "# Tool Instructions",
                "",
                "## Read tool",
                "Reads a file from /.",
                "",
                "Parameters schema:",
                "```json",
                '{"type":"object","properties":{"file_path":{"type":"string"}}}',
                "```",
                "",
            ]
        ),
    )

    fake_turn = SimpleNamespace(
        idx=0,
        obj_fp="chats/1/62/0.mpk",
        created_at=datetime(2026, 2, 12),
    )
    fake_chat = SimpleNamespace(turns=[fake_turn])
    monkeypatch.setattr(
        review_module.chat_crud,
        "for_user",
        lambda user_id: SimpleNamespace(
            get=lambda chat_id, with_turns=True: fake_chat,
        ),
    )

    out = review_module.review_chat(1, 62)

    assert out == review_dir / "1" / "62"
    assert (out / "0" / "turn.md").exists()
    assert not (out / "0" / "summary.md").exists()
    assert (out / "system_instructions.md").exists()
    assert (out / "system_instructions.md").read_text() == SYSTEM_PROMPT
    assert (out / "tool_instructions.md").exists()
    tool_md = (out / "tool_instructions.md").read_text()
    assert "# Tool Instructions" in tool_md
    assert "## Read tool" in tool_md
    assert "Parameters schema:" in tool_md

    chat_md = (out / "chat.md").read_text()
    assert "Final: Final answer." in chat_md
    assert "[Details](0/turn.md)" in chat_md
