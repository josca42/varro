from __future__ import annotations

from pydantic_ai import BinaryContent
from pydantic_ai.messages import ModelRequest, ToolReturnPart, UserPromptPart

from varro.chat.tool_results import extract_tool_render_records


def test_extract_tool_render_records_uses_metadata_mapping() -> None:
    image_a = BinaryContent(data=b"a", media_type="image/png")
    image_b = BinaryContent(data=b"b", media_type="image/png")
    request = ModelRequest(
        parts=[
            ToolReturnPart(
                tool_name="Sql",
                content="sql output",
                tool_call_id="call_sql",
                metadata={"ui": {"has_tool_content": False}},
            ),
            ToolReturnPart(
                tool_name="Jupyter",
                content="stdout",
                tool_call_id="call_jupyter",
                metadata={"ui": {"has_tool_content": True}},
            ),
            ToolReturnPart(
                tool_name="Read",
                content="read image",
                tool_call_id="call_read",
                metadata={"ui": {"has_tool_content": True}},
            ),
            UserPromptPart(content=[image_a]),
            UserPromptPart(content=[image_b]),
        ]
    )

    records = extract_tool_render_records(request)

    assert [record.part.tool_name for record in records] == ["Sql", "Jupyter", "Read"]
    assert records[0].tool_content is None
    assert records[1].tool_content == [image_a]
    assert records[2].tool_content == [image_b]


def test_extract_tool_render_records_legacy_fallback_for_single_tool() -> None:
    image = BinaryContent(data=b"legacy", media_type="image/png")
    request = ModelRequest(
        parts=[
            ToolReturnPart(
                tool_name="Jupyter",
                content="stdout",
                tool_call_id="legacy_call",
            ),
            UserPromptPart(content=[image]),
        ]
    )

    records = extract_tool_render_records(request)

    assert len(records) == 1
    assert records[0].part.tool_name == "Jupyter"
    assert records[0].tool_content == [image]


def test_extract_tool_render_records_legacy_fallback_when_counts_align() -> None:
    image_a = BinaryContent(data=b"a", media_type="image/png")
    image_b = BinaryContent(data=b"b", media_type="image/png")
    request = ModelRequest(
        parts=[
            ToolReturnPart(
                tool_name="Jupyter",
                content="stdout a",
                tool_call_id="legacy_a",
            ),
            ToolReturnPart(
                tool_name="Jupyter",
                content="stdout b",
                tool_call_id="legacy_b",
            ),
            UserPromptPart(content=[image_a]),
            UserPromptPart(content=[image_b]),
        ]
    )

    records = extract_tool_render_records(request)

    assert len(records) == 2
    assert records[0].tool_content == [image_a]
    assert records[1].tool_content == [image_b]
