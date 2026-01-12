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

from fasthtml.common import *
import fasthtml.components as fh

try:
    # Python 3.9+
    from importlib import resources as importlib_resources
except Exception:  # pragma: no cover
    import importlib_resources  # type: ignore

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
    return x.startswith("-") and len(parts := x[1:].split("-")) >= 2 and parts[0] in _neg_twu_pfxs


def cls_join(*classes: str) -> str:
    """Join class strings, filtering falsy values."""
    return " ".join(c for c in classes if c)


# Alias used in shadcn-style codebases
cn = cls_join


# -----------------------------------------------------------------------------
# CDN headers
# -----------------------------------------------------------------------------

# DaisyUI v5 + Tailwind runtime compiler.
# DaisyUI ships the component classnames; Tailwind runtime compiles utilities.

daisy_link = Link(
    href="https://cdn.jsdelivr.net/npm/daisyui@5",
    rel="stylesheet",
    type="text/css",
)

tw_scr = Script(src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4")

# Base headers (framework only)

daisy_hdrs = (daisy_link, tw_scr)


def _read_pkg_text(filename: str) -> str:
    """Read a text file shipped inside the `ui` package."""
    try:
        return (
            importlib_resources.files(__package__)  # type: ignore[attr-defined]
            .joinpath(filename)
            .read_text(encoding="utf-8")
        )
    except Exception:
        # Fallback: relative to this file (useful when running from source)
        here = Path(__file__).resolve().parent
        return (here / filename).read_text(encoding="utf-8")


def theme_css(path: str | None = None) -> Style:
    """Return a <style> tag containing theme CSS.

    - If `path` is None, loads `ui/theme.css` from the package.
    - If `path` is provided, loads that file from disk.

    This keeps app headers ergonomic:
        app, rt = daisy_app()

    You can still override:
        app, rt = daisy_app(hdrs=(theme_css('static/css/theme.css'),))
    """

    if path is None:
        return Style(_read_pkg_text("theme.css"))

    css_content = Path(path).read_text(encoding="utf-8")
    return Style(css_content)


# Opinionated default headers (framework + theme)
ui_hdrs = (*daisy_hdrs, theme_css())


def daisy_app(*, with_theme: bool = True, **kw):
    """Create a FastHTML app with DaisyUI (+ Tailwind runtime) headers.

    Args:
        with_theme: If True, injects `ui/theme.css` into the document.
        **kw: Passed through to `fast_app`.

    Returns:
        (app, rt)
    """

    hdrs = kw.pop("hdrs", ())
    base_hdrs = ui_hdrs if with_theme else daisy_hdrs
    return fast_app(hdrs=(*base_hdrs, *hdrs), pico=False, **kw)


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
            f"{compcls if x and x.startswith('-') and not _is_neg_twu(x) else ''}{x}" for x in cls.split()
        )

        if slot is not None and "data_slot" not in kw:
            kw["data_slot"] = slot

        return compfunc(*c, cls=f"{compcls} {cls_expanded} {xcls}".strip(), **compkw, **kw)

    fn.__name__ = name
    fn.__doc__ = f"DaisyUI primitive: .{compcls}. Use cls='-modifier' to expand to {compcls}-modifier."

    # Register in caller's namespace
    inspect.currentframe().f_back.f_globals[name] = fn
    return fn
