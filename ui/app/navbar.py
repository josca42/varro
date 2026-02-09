"""ui.app.navbar

Mock navbar used in the demo app (`main.py`).

This is intentionally specific to the Lovable-style mock layout.
"""

from __future__ import annotations

from fasthtml.common import *
from fasthtml.components import ft_hx

from ui.core import cn
from ui.components import Button
from ui.daisy import Navbar as DaisyNavbar, NavbarStart, NavbarCenter, NavbarEnd, Kbd


_ICONS = {
    "dashboard": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "overview": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    "settings": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/></svg>',
    "search": '<svg class="h-4 w-4 opacity-50" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><g stroke-linejoin="round" stroke-linecap="round" stroke-width="2.5" fill="none" stroke="currentColor"><circle cx="11" cy="11" r="8"></circle><path d="m21 21-4.3-4.3"></path></g></svg>',
}

_TAB_ITEMS = [
    ("dashboard", "Dashboard", "dashboard"),
    ("code", "Code", "code"),
    ("overview", "Overview", "overview"),
]


def _nav_tab(icon_key: str, label: str, action: str):
    return ft_hx(
        "button",
        NotStr(f'<span class="w-4 h-4 shrink-0">{_ICONS[icon_key]}</span>'),
        Span(label, cls="text-sm whitespace-nowrap overflow-hidden"),
        cls="btn btn-ghost btn-sm h-8 min-h-0 min-w-8 px-2 gap-1.5 transition-all duration-200 rounded-lg border border-transparent",
        onclick=f"window.__varroNavTab('{action}')",
    )


def NavbarNavScript():
    return Script(
        """
(() => {
  if (window.__varroNavTab) return;

  function dashboardSlug(pathname) {
    const match = pathname.match(/^\\/dashboard\\/([^/]+?)(?:\\/code)?$/);
    if (!match) return null;
    try {
      return decodeURIComponent(match[1]);
    } catch {
      return match[1];
    }
  }

  function pathFor(tab) {
    const pathname = window.location.pathname || '/';
    const slug = dashboardSlug(pathname);
    if (tab === 'dashboard') {
      return slug ? `/dashboard/${encodeURIComponent(slug)}` : '/';
    }
    if (tab === 'code') {
      return slug ? `/dashboard/${encodeURIComponent(slug)}/code` : '/welcome/code';
    }
    return '/';
  }

  window.__varroNavTab = function(tab) {
    const url = pathFor(tab);
    if (!url) return;
    const current = `${window.location.pathname}${window.location.search || ''}`;
    if (url === current) return;
    if (window.__varroNavigate) {
      window.__varroNavigate(url, { target: '#content-panel', swap: 'innerHTML' });
      return;
    }
    if (window.htmx) {
      htmx.ajax('GET', url, { target: '#content-panel', swap: 'innerHTML' });
      history.pushState({}, '', url);
      return;
    }
    window.location.assign(url);
  };
})();
"""
    )


def Navbar(
    project_name: str = "Dash Companion",
    status: str = "Previewing last saved version",
    cls: str = "",
    **kw,
):
    """Top navigation bar."""

    tabs = Div(
        *[_nav_tab(icon, label, action) for icon, label, action in _TAB_ITEMS],
        cls="flex gap-1",
    )

    start = NavbarStart(tabs)

    cmdk_bar = Div(
        NotStr(_ICONS["search"]),
        Span("Search...", cls="text-sm text-base-content/40 flex-1"),
        Kbd("⌘", cls="kbd kbd-sm"),
        Kbd("K", cls="kbd kbd-sm"),
        cls="flex items-center gap-2 bg-base-100 rounded-field px-3 py-1.5 min-w-48 cursor-pointer hover:bg-base-200 transition-colors border border-base-300",
        **{"onclick": "window.dispatchEvent(new Event('open-command-palette'))"},
    )

    center = NavbarCenter(
        cmdk_bar,
        cls="hidden lg:flex",
    )

    end = NavbarEnd(
        Button(NotStr(_ICONS["settings"]), variant="ghost", size="icon"),
        Button("Publish", variant="default", size="default"),
        cls="flex gap-2",
    )

    return DaisyNavbar(
        start,
        center,
        end,
        NavbarNavScript(),
        cls=cn("navbar bg-base-200 px-4 min-h-14 border-b border-base-300", cls),
        data_slot="app-navbar",
        **kw,
    )
