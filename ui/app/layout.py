"""ui.app.layout

Split-panel application shell for chat + URL-driven content.
"""

from __future__ import annotations

from fasthtml.common import Div, H1, H2, P, A, Script

from ui.core import cn
from ui.app.chat import ChatPanel, ChatClientScript
from ui.app.navbar import Navbar


def ContentNavbar(
    title: str = "Dashboard",
    subtitle: str | None = None,
):
    subtitle = subtitle or "Analytics overview"
    return Div(
        Div(
            H2(title, cls="text-lg font-semibold"),
            P(subtitle, cls="text-sm text-base-content/60"),
            cls="flex flex-col",
        ),
        Div(
            A(
                "Overview",
                href="/dash/overview",
                cls="btn btn-ghost btn-sm",
                hx_get="/dash/overview",
                hx_target="#content-panel",
                hx_swap="innerHTML",
                hx_push_url="true",
            ),
            A(
                "Settings",
                href="/settings",
                cls="btn btn-ghost btn-sm",
                hx_get="/settings",
                hx_target="#content-panel",
                hx_swap="innerHTML",
                hx_push_url="true",
            ),
            cls="flex items-center gap-2",
        ),
        cls="flex items-center justify-between px-6 py-4 border-b border-base-300 bg-base-100",
        data_slot="content-navbar",
    )


def WelcomePage():
    return Div(
        ContentNavbar(
            title="Welcome",
            subtitle="Choose a dashboard or ask the assistant.",
        ),
        Div(
            H1("Welcome", cls="text-2xl font-semibold mb-2"),
            P(
                "Choose a dashboard or ask the assistant to navigate for you.",
                cls="text-base-content/70",
            ),
            cls="p-6",
        ),
        data_slot="welcome-page",
    )


def OverviewPage():
    return Div(
        ContentNavbar(
            title="Overview",
            subtitle="All dashboards at a glance.",
        ),
        Div(
            H1("Dashboard Overview", cls="text-2xl font-semibold mb-2"),
            P("Overview page placeholder.", cls="text-base-content/70"),
            cls="p-6",
        ),
        data_slot="overview-page",
    )


def SettingsPage():
    return Div(
        ContentNavbar(
            title="Settings",
            subtitle="App preferences and defaults.",
        ),
        Div(
            H1("Settings", cls="text-2xl font-semibold mb-2"),
            P("Settings page placeholder.", cls="text-base-content/70"),
            cls="p-6",
        ),
        data_slot="settings-page",
    )


def ResizerScript():
    return Script(
        """
document.addEventListener('alpine:init', () => {
  Alpine.data('splitResizer', () => ({
    dragging: false,
    init() {
      const handle = this.$el.querySelector('#resize-handle');
      const panel = this.$el.querySelector('#chat-root');
      if (!handle || !panel) return;
      const min = 280;
      const max = 520;
      handle.addEventListener('pointerdown', (e) => {
        this.dragging = true;
        handle.setPointerCapture(e.pointerId);
      });
      window.addEventListener('pointermove', (e) => {
        if (!this.dragging) return;
        const rect = this.$el.getBoundingClientRect();
        const next = Math.min(max, Math.max(min, e.clientX - rect.left));
        panel.style.width = `${next}px`;
      });
      window.addEventListener('pointerup', () => {
        this.dragging = false;
      });
    },
  }));
});
"""
    )


def AppShell(
    chat,
    content,
):
    chat_root = Div(
        ChatPanel(chat),
        ChatClientScript(),
        id="chat-root",
        hx_ext="ws",
        cls="flex flex-col min-h-0 h-full shrink-0 border-r border-base-300 bg-base-100 min-w-[280px] max-w-[520px] w-[360px]",
        data_slot="chat-root",
    )

    content_panel = Div(
        content,
        id="content-panel",
        cls="flex-1 overflow-y-auto bg-base-100",
        hx_history_elt="true",
        hx_target="#content-panel",
        hx_swap="innerHTML",
        hx_boost="true",
        data_slot="content-panel",
    )

    body = Div(
        chat_root,
        Div(
            id="resize-handle",
            cls="w-1 bg-base-200 hover:bg-base-300 cursor-col-resize",
            data_slot="resize-handle",
        ),
        Div(
            content_panel,
            cls="flex flex-col min-h-0 flex-1",
            data_slot="content-wrap",
        ),
        x_data="splitResizer()",
        cls="flex flex-1 min-h-0",
        data_slot="app-body",
    )

    return Div(
        Navbar(),
        body,
        ResizerScript(),
        cls=cn("h-screen flex flex-col bg-base-100"),
        data_slot="app-shell",
    )
