from __future__ import annotations

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

from varro.chat.review import REVIEW_FORMAT_VERSION, review_turn


def _build_review_messages() -> list:
    image = BinaryContent(data=b"img", media_type="image/png")
    return [
        ModelRequest(parts=[UserPromptPart(content="Analyse this")]),
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
    assert "**Decision**" in md
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
    assert (turn_dir / "images").exists()


def test_review_turn_writes_review_version(tmp_path) -> None:
    turn_dir = tmp_path / "3"
    review_turn(_build_review_messages(), turn_dir, 3)

    assert (turn_dir / ".review_version").read_text() == REVIEW_FORMAT_VERSION
