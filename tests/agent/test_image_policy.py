from __future__ import annotations

import asyncio
import importlib
import io

import plotly.graph_objects as go
from pydantic_ai import BinaryContent
from PIL import Image

from varro.agent.images import JUPYTER_SHOW_MAX_PIXELS, optimize_png_bytes


def _png_bytes(width: int, height: int) -> bytes:
    image = Image.new("RGBA", (width, height), color=(180, 60, 20, 255))
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    return buf.getvalue()


def test_optimize_png_bytes_keeps_size_when_under_threshold() -> None:
    original = _png_bytes(500, 400)

    optimized = optimize_png_bytes(original, max_pixels=500 * 400 + 1)

    with Image.open(io.BytesIO(optimized)) as image:
        assert image.size == (500, 400)


def test_optimize_png_bytes_resizes_proportionally_above_threshold() -> None:
    original = _png_bytes(2200, 1100)
    original_ratio = 2200 / 1100

    optimized = optimize_png_bytes(original, max_pixels=1_000_000)

    with Image.open(io.BytesIO(optimized)) as image:
        assert image.width * image.height <= 1_000_000
        assert abs((image.width / image.height) - original_ratio) < 0.01


def test_show_element_plotly_uses_jupyter_pixel_cap(monkeypatch) -> None:
    utils = importlib.import_module("varro.agent.utils")

    async def fake_html_to_png(*args, **kwargs):
        return _png_bytes(2000, 2000)

    monkeypatch.setattr(utils, "html_to_png", fake_html_to_png)

    figure = go.Figure(data=[go.Scatter(x=[1, 2], y=[1, 3])])
    rendered = asyncio.run(utils.show_element(figure))

    assert isinstance(rendered, BinaryContent)
    with Image.open(io.BytesIO(rendered.data)) as image:
        assert image.width * image.height <= JUPYTER_SHOW_MAX_PIXELS
