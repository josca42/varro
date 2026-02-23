from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from pandas.io.formats.style import Styler
from fasthtml.common import to_xml
from plotly.basedatatypes import BaseFigure
from pydantic_ai.messages import ModelMessage, ModelResponse, TextPart

from ui.components import DataTable
from varro.dashboard.parser import ComponentNode, ContainerNode, parse_dashboard_md


def iter_component_nodes(nodes):
    for node in nodes:
        if isinstance(node, ComponentNode):
            yield node
        elif isinstance(node, ContainerNode):
            yield from iter_component_nodes(node.children)


def save_turn_render_cache(msgs: list[ModelMessage], fp: Path, shell) -> None:
    cache = {}
    for msg in msgs:
        if not isinstance(msg, ModelResponse) or msg.finish_reason != "stop":
            continue
        for part in msg.parts:
            if not isinstance(part, TextPart):
                continue
            nodes = parse_dashboard_md(part.content)
            for node in iter_component_nodes(nodes):
                name = (node.attrs.get("name") or "").strip()
                if not name or node.type not in ("fig", "df"):
                    continue
                obj = shell.user_ns.get(name)
                if obj is None:
                    continue
                key = f"{node.type}:{name}"
                if key in cache:
                    continue
                if node.type == "fig" and isinstance(obj, BaseFigure):
                    cache[key] = obj.to_html(include_plotlyjs=False, full_html=False)
                elif node.type == "df" and isinstance(obj, pd.DataFrame):
                    df = obj
                    if not isinstance(df.index, pd.RangeIndex):
                        df = df.reset_index()
                    cache[key] = to_xml(DataTable(df, cls="my-2"))
                elif node.type == "df" and isinstance(obj, Styler):
                    cache[key] = obj.to_html()
    if cache:
        fp.with_suffix(".cache.json").write_text(json.dumps(cache, ensure_ascii=False))
