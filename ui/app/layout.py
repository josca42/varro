"""ui.app.layout

Split-panel application shell for chat + URL-driven content.
"""

from __future__ import annotations

from fasthtml.common import A, Div, H1, Li, P, Script, Span, Ul

from ui.core import cn
from ui.app.chat import ChatPanel, ChatClientScript
from ui.app.navbar import Navbar
from ui.app.command_palette import CommandPalette, CommandPaletteScript


def DashboardOverviewPage(dashboard_slugs: list[str]):
    items = [
        Li(
            A(
                slug,
                href=f"/dashboard/{slug}",
                cls="link link-hover font-medium",
            )
        )
        for slug in dashboard_slugs
    ]

    return Div(
        Div(
            H1("Dashboards", cls="text-2xl font-semibold mb-2"),
            P(
                "Select a dashboard. URL state is shareable and bookmarkable.",
                cls="text-base-content/70",
            ),
            Ul(*items, cls="list-disc pl-6 mt-4")
            if items
            else P(
                "No dashboards found for this user.", cls="mt-4 text-base-content/70"
            ),
            cls="p-6",
        ),
        data_slot="dashboard-overview-page",
    )


def WelcomePage():
    return DashboardOverviewPage([])


def OverviewPage():
    return DashboardOverviewPage([])


def SettingsPage(user_name: str | None = None, user_email: str | None = None):
    initial = (user_name or user_email or "U")[0].upper()

    profile_section = Div(
        Div(
            Div(
                Span(initial, cls="text-lg font-semibold"),
                cls="w-14 h-14 rounded-full bg-base-300 flex items-center justify-center",
            ),
            Div(
                Div(user_name or "—", cls="text-base font-semibold"),
                Div(user_email or "—", cls="text-sm text-base-content/50"),
                cls="flex flex-col gap-0.5",
            ),
            cls="flex items-center gap-4",
        ),
        cls="pb-6 border-b border-base-300",
    )

    account_section = Div(
        H1("Account", cls="text-lg font-semibold mb-4"),
        Div(
            Div(
                Div("Email", cls="text-sm font-medium"),
                Div(user_email or "—", cls="text-sm text-base-content/60"),
                cls="flex flex-col gap-1",
            ),
            Div(
                Div("Name", cls="text-sm font-medium"),
                Div(user_name or "—", cls="text-sm text-base-content/60"),
                cls="flex flex-col gap-1",
            ),
            cls="space-y-4",
        ),
        cls="py-6 border-b border-base-300",
    )

    danger_section = Div(
        A(
            "Log out",
            href="/logout",
            cls="btn btn-outline btn-error btn-sm",
        ),
        cls="pt-6",
    )

    return Div(
        Div(
            H1("Settings", cls="text-2xl font-semibold mb-6"),
            profile_section,
            account_section,
            danger_section,
            cls="max-w-2xl p-6",
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
      const max = 1200;
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


# TODO: Is this needed?. Could I replace with native htmx functionality?
def UrlStateScript():
    return Script(
        """
(() => {
  if (window.__varroNavigate) return;
  const appliedUpdateCalls = new Set();

  function isValidPath(url) {
    return typeof url === 'string' && url.startsWith('/');
  }

  window.__varroNavigate = function(url, opts = {}) {
    if (!isValidPath(url) || !window.htmx) return false;
    const target = opts.target || '#content-panel';
    const swap = opts.swap || 'innerHTML';
    htmx.ajax('GET', url, { target, swap });
    if (swap !== 'none') {
      if (opts.replace) {
        history.replaceState({}, '', url);
      } else {
        history.pushState({}, '', url);
      }
    }
    return true;
  };

  window.__varroApplyUpdateUrl = function(callId, payload) {
    if (!payload || typeof payload !== 'object') return false;
    if (!isValidPath(payload.url)) return false;
    if (callId && appliedUpdateCalls.has(callId)) return false;
    const ok = window.__varroNavigate(payload.url, { replace: !!payload.replace });
    if (ok && callId) appliedUpdateCalls.add(callId);
    return ok;
  };
})();
"""
    )


def AppShell(
    chat,
    content,
    user_name: str | None = None,
    user_email: str | None = None,
):
    chat_root = Div(
        ChatPanel(chat),
        ChatClientScript(),
        id="chat-root",
        cls="flex flex-col min-h-0 h-full shrink-0 border-r border-base-300 bg-base-200 min-w-[280px] max-w-[1200px] w-[700px]",
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

    return Div(
        chat_root,
        Div(
            id="resize-handle",
            cls="w-1 bg-base-300 hover:bg-primary/30 cursor-col-resize",
            data_slot="resize-handle",
        ),
        Div(
            Navbar(user_name=user_name, user_email=user_email),
            content_panel,
            cls="flex flex-col min-h-0 flex-1",
            data_slot="content-wrap",
        ),
        CommandPalette(),
        UrlStateScript(),
        CommandPaletteScript(),
        ResizerScript(),
        x_data="splitResizer()",
        cls=cn("h-screen flex bg-base-100"),
        data_slot="app-shell",
    )
