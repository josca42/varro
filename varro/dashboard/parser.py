"""dashboard.parser

Parse dashboard.md into an AST.

Syntax:
- ::: container attrs  (open container)
- :::                  (close container)
- {% tag attrs /%}     (component tag)
- Everything else is markdown
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Union

from .filters import Filter, filter_from_component


@dataclass
class ContainerNode:
    """A container block like ::: filters or ::: grid cols=2"""

    type: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list["ASTNode"] = field(default_factory=list)


@dataclass
class ComponentNode:
    """A component tag like {% figure name="revenue" /%}"""

    type: str
    attrs: dict[str, str] = field(default_factory=dict)


@dataclass
class MarkdownNode:
    """Plain markdown content"""

    content: str


ASTNode = Union[ContainerNode, ComponentNode, MarkdownNode, Filter]


# Regex patterns
CONTAINER_OPEN = re.compile(r"^:::\s*(\w+)(?:\s+(.+))?$")
CONTAINER_CLOSE = re.compile(r"^:::\s*$")
COMPONENT_TAG = re.compile(r"\{%\s*(\w+)\s+([^%]*?)\s*/%\}")
ATTR_PATTERN = re.compile(r'(\w+)=(?:"([^"]*)"|(\S+))')


def parse_attrs(attr_str: str) -> dict[str, str]:
    """Parse key=value or key="value" pairs."""
    if not attr_str:
        return {}
    attrs = {}
    for match in ATTR_PATTERN.finditer(attr_str):
        key = match.group(1)
        value = match.group(2) if match.group(2) is not None else match.group(3)
        attrs[key] = value
    return attrs


def parse_dashboard_md(content: str) -> list[ASTNode]:
    """Parse dashboard.md into an AST.

    Uses stack-based container closing (like HTML tags).
    """
    lines = content.split("\n")
    root: list[ASTNode] = []
    stack: list[list[ASTNode]] = [root]
    container_stack: list[ContainerNode] = []
    md_buffer: list[str] = []

    def flush_markdown():
        nonlocal md_buffer
        if md_buffer:
            text = "\n".join(md_buffer).strip()
            if text:
                stack[-1].append(MarkdownNode(content=text))
            md_buffer = []

    for line in lines:
        # Container close: :::
        if CONTAINER_CLOSE.match(line):
            flush_markdown()
            if len(stack) > 1:
                stack.pop()
                if container_stack:
                    container_stack.pop()
            continue

        # Container open: ::: type attrs
        if match := CONTAINER_OPEN.match(line):
            flush_markdown()
            type_ = match.group(1)
            attrs = parse_attrs(match.group(2) or "")
            node = ContainerNode(type=type_, attrs=attrs, children=[])
            stack[-1].append(node)
            stack.append(node.children)
            container_stack.append(node)
            continue

        # Component tag: {% type attrs /%}
        if match := COMPONENT_TAG.search(line):
            flush_markdown()
            type_ = match.group(1)
            attrs = parse_attrs(match.group(2))
            if container_stack and container_stack[-1].type == "filters":
                f = filter_from_component(type_, attrs)
                if f:
                    stack[-1].append(f)
                    continue
            stack[-1].append(ComponentNode(type=type_, attrs=attrs))
            continue

        # Regular markdown
        md_buffer.append(line)

    flush_markdown()
    return root


def extract_filters(ast: list[ASTNode]) -> list[Filter]:
    """Extract filter definitions from AST.

    Returns validated filter objects found in ::: filters containers.
    """
    filters: list[Filter] = []

    def walk(nodes: list[ASTNode]):
        for node in nodes:
            if isinstance(node, ContainerNode):
                if node.type == "filters":
                    for f in node.children:
                        if isinstance(f, Filter):
                            filters.append(f)
                else:
                    walk(node.children)

    walk(ast)
    return filters


__all__ = [
    "ASTNode",
    "ContainerNode",
    "ComponentNode",
    "MarkdownNode",
    "parse_dashboard_md",
    "parse_attrs",
    "extract_filters",
]
