from __future__ import annotations

from fasthtml.common import to_xml
from pydantic_ai import BinaryContent
from pydantic_ai.messages import ToolReturnPart

from ui.app.tool import ToolArgsDisplay, ToolResultDisplay, ToolResultStep
from varro.chat.tool_results import ToolRenderRecord


def test_tool_args_display_formats_sql_input() -> None:
    html = to_xml(
        ToolArgsDisplay(
            "Sql",
            {"query": "SELECT\n  1 AS x", "df_name": "df_x"},
        )
    )

    assert "language-sql" in html
    assert "SELECT" in html
    assert "df_name: df_x" in html


def test_tool_args_display_formats_jupyter_input() -> None:
    html = to_xml(
        ToolArgsDisplay(
            "Jupyter",
            {"code": "x = 1\nprint(x)", "show": ["fig", "df"]},
        )
    )

    assert "language-python" in html
    assert "print(x)" in html
    assert "show: fig, df" in html


def test_tool_result_display_renders_inline_image_for_jupyter_and_read() -> None:
    image = BinaryContent(data=b"img", media_type="image/png")
    jupyter_html = to_xml(ToolResultDisplay("", [image], tool="Jupyter"))
    read_html = to_xml(ToolResultDisplay("", [image], tool="Read"))

    assert "data:image/png;base64,aW1n" in jupyter_html
    assert "data:image/png;base64,aW1n" in read_html


def test_tool_result_step_renders_mixed_text_and_image() -> None:
    image = BinaryContent(data=b"mix", media_type="image/png")
    record = ToolRenderRecord(
        part=ToolReturnPart(
            tool_name="Jupyter",
            content="stdout line",
            tool_call_id="tool_1",
        ),
        tool_content=[image],
    )

    html = to_xml(ToolResultStep(record))

    assert "stdout line" in html
    assert "data:image/png;base64,bWl4" in html


def test_tool_result_display_shows_non_image_binary_placeholder() -> None:
    binary = BinaryContent(data=b"pdf", media_type="application/pdf")

    html = to_xml(ToolResultDisplay("", [binary], tool="Jupyter"))

    assert "Binary output: application/pdf" in html
    assert "data:application/pdf" not in html
