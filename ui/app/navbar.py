"""ui.app.navbar

Mock navbar used in the demo app (`main.py`).

This is intentionally specific to the Lovable-style mock layout.
"""

from __future__ import annotations

from fasthtml.common import *

from ui.core import cn
from ui.components import Button
from ui.daisy import Navbar as DaisyNavbar, NavbarStart, NavbarCenter, NavbarEnd


def Navbar(
    project_name: str = "Dash Companion",
    status: str = "Previewing last saved version",
    cls: str = "",
    **kw,
):
    """Top navigation bar."""

    start = NavbarStart(
        Div(
            Div("🔥", cls="text-lg"),
            Div(
                Div(project_name, cls="font-semibold text-sm"),
                Div(status, cls="text-xs text-base-content/60"),
            ),
            cls="flex items-center gap-2",
        )
    )

    tabs = Div(
        Button("↩", variant="ghost", size="icon"),
        Button("↪", variant="ghost", size="icon"),
        Button(
            "🌐 Preview",
            variant="ghost",
            size="default",
            cls="bg-base-200 hover:bg-base-200",
        ),
        Button("</>", variant="ghost", size="default"),
        Button("📊", variant="ghost", size="icon"),
        Button("+", variant="ghost", size="icon"),
        cls="flex gap-1",
    )

    url_bar = Div(
        Div("□", cls="text-base-content/40 text-sm"),
        Div("/", cls="text-base-content/70 text-sm"),
        cls="flex items-center gap-2 bg-base-200 rounded-field px-4 py-1.5 ml-4 min-w-32",
    )

    center = NavbarCenter(
        Div(
            tabs,
            url_bar,
            cls="flex items-center",
        ),
        cls="hidden lg:flex",
    )

    end = NavbarEnd(
        Button("Share", variant="ghost", size="default"),
        Button("⚙", variant="ghost", size="icon"),
        Button("⚡ Upgrade", variant="outline", size="default"),
        Button("Publish", variant="default", size="default"),
        cls="flex gap-2",
    )

    return DaisyNavbar(
        start,
        center,
        end,
        cls=cn("navbar bg-base-100 px-4 min-h-14 border-b border-base-300", cls),
        data_slot="app-navbar",
        **kw,
    )

