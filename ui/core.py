"""ui.core

Core helpers for a small, opinionated FastHTML + DaisyUI UI kit.

Design stance (project-specific):
- DaisyUI provides semantic component styling.
- Tailwind utilities are used primarily for layout and spacing.
- Components are shadcn-inspired: compact defaults, explicit APIs, predictable slots.

Runtime notes:
- This repo loads Tailwind via `@tailwindcss/browser` and DaisyUI via CDN.
- Therefore `ui/theme.css` must be plain CSS (no @plugin / @apply build directives).
"""

from __future__ import annotations
import inspect
from pathlib import Path
from typing import Optional

from fasthtml.common import MarkdownJS, HighlightJS, Script, Style, Link, fast_app
import fasthtml.components as fh


# -----------------------------------------------------------------------------
# Opinionated tokens
# -----------------------------------------------------------------------------

DEFAULT_THEME = "warmink"
DEFAULT_DARK_THEME = "warmink-dark"

TOKENS = {
    "theme": {
        "default": DEFAULT_THEME,
        "dark": DEFAULT_DARK_THEME,
    },
    "density": "compact",
}


# -----------------------------------------------------------------------------
# Classname utilities
# -----------------------------------------------------------------------------

# Negative Tailwind utility prefixes (for proper class expansion)
_neg_twu_pfxs = set(
    "mt ml mr mb mx my translate rotate scale skew inset top bottom left right z space".split()
)


def _is_neg_twu(x: str) -> bool:
    """Check if string is a negative Tailwind utility (e.g., -mt-4)."""
    return (
        x.startswith("-")
        and len(parts := x[1:].split("-")) >= 2
        and parts[0] in _neg_twu_pfxs
    )


def cls_join(*classes: str) -> str:
    """Join class strings, filtering falsy values."""
    return " ".join(c for c in classes if c)


# Alias used in shadcn-style codebases
cn = cls_join


# -----------------------------------------------------------------------------
# CDN headers
# -----------------------------------------------------------------------------

# DaisyUI v5 + Tailwind runtime compiler.
# DaisyUI ships the component classnames; Tailwind runtime compiles utilities
daisy_link = Link(
    href="https://cdn.jsdelivr.net/npm/daisyui@5",
    rel="stylesheet",
    type="text/css",
)
tw_scr = Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4")
# Plotly JS for chart rendering
plotly_hdr = Script(src="https://cdn.plot.ly/plotly-2.35.2.min.js")
# HTMX SSE extension
sse_hdr = Script(src="https://unpkg.com/htmx-ext-sse@2.2.3/sse.js")
# Alpine.js for tab interactivity
alpine_hdrs = (
    Script(src="https://unpkg.com/@alpinejs/ui@3.15.3/dist/cdn.min.js", defer=True),
    Script(
        src="https://unpkg.com/@alpinejs/collapse@3.15.3/dist/cdn.min.js", defer=True
    ),
    Script(src="https://unpkg.com/@alpinejs/focus@3.15.3/dist/cdn.min.js", defer=True),
    Script(src="https://unpkg.com/alpinejs@3.15.3/dist/cdn.min.js", defer=True),
)
lucid_icons_hdr = [
    Script(src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"),
    Script("lucide.createIcons();", defer=True),
]
# Theme CSS
here = Path(__file__).resolve().parent
css_content = (here / "theme.css").read_text(encoding="utf-8")
theme_css = Style(css_content)
prose_css = Link(
    href="/static/css/prose.css",
    rel="stylesheet",
    type="text/css",
)

# All headers
ui_hdrs = (
    daisy_link,
    MarkdownJS(),
    HighlightJS(langs=["python", "javascript", "html", "css", "json", "bash", "sql"]),
    tw_scr,
    plotly_hdr,
    sse_hdr,
    *alpine_hdrs,
    *lucid_icons_hdr,
    theme_css,
    prose_css,
)


def daisy_app(*args, **kwargs):
    hdrs = kwargs.pop("hdrs", ())
    return fast_app(
        *args,
        hdrs=(*ui_hdrs, *hdrs),
        pico=False,
        htmlkw={"data_theme": DEFAULT_THEME},
        **kwargs,
    )


# -----------------------------------------------------------------------------
# Component factory for DaisyUI primitives
# -----------------------------------------------------------------------------


def hyphens2camel(x: str) -> str:
    """Convert `kebab-case` to `CamelCase`."""
    return "".join(o.title() for o in x.split("-"))


def mk_compfn(
    compcls: str,
    tag: str | None = None,
    name: str | None = None,
    xcls: str = "",
    *,
    slot: str | None = None,
    **compkw,
):
    """Create a thin DaisyUI primitive wrapper.

    - Always applies the base DaisyUI class (`compcls`).
    - Supports the fhdaisy-style modifier shorthand:
        cls='-primary -sm' -> '{compcls}-primary {compcls}-sm'

    Args:
        compcls: DaisyUI base class (e.g. 'btn', 'card')
        tag: FastHTML component name (e.g. 'Button', 'Div')
        name: Python function name
        xcls: Extra classes always added
        slot: If set, adds data-slot by default.
        **compkw: Default kwargs passed to the underlying element.
    """

    if not name:
        name = hyphens2camel(compcls)
    if not tag:
        tag = name

    compfunc = getattr(fh, tag)

    def fn(*c, cls: str = "", **kw):
        # Expand modifier shortcuts: '-primary' -> 'btn-primary' (unless it's a negative Tailwind utility)
        cls_expanded = " ".join(
            f"{compcls if x and x.startswith('-') and not _is_neg_twu(x) else ''}{x}"
            for x in cls.split()
        )

        if slot is not None and "data_slot" not in kw:
            kw["data_slot"] = slot

        return compfunc(
            *c, cls=f"{compcls} {cls_expanded} {xcls}".strip(), **compkw, **kw
        )

    fn.__name__ = name
    fn.__doc__ = f"DaisyUI primitive: .{compcls}. Use cls='-modifier' to expand to {compcls}-modifier."

    # Register in caller's namespace
    inspect.currentframe().f_back.f_globals[name] = fn
    return fn
