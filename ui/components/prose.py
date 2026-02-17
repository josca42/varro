"""ui.components.prose

Typography helpers for content rendered as "prose".

Typography is provided by `static/css/prose.css`, built via Tailwind Typography.
These components simply apply the right classes.

If you use `MarkdownJS()` from FastHTML, it targets elements with the `marked`
class. So we expose `MarkdownProse`.
"""

from __future__ import annotations

from fasthtml.common import *

from ui.core import cn


def Prose(*c, cls: str = "", **kw):
    """Generic prose container."""

    return Div(
        *c,
        cls=cn("prose max-w-none", cls),
        data_slot="prose",
        **kw,
    )


def MarkdownProse(content, cls: str = "", **kw):
    """A prose container that will be markdown-rendered by `MarkdownJS()`."""

    return Div(
        content,
        cls=cn("marked prose max-w-none", cls),
        data_slot="markdown",
        **kw,
    )
