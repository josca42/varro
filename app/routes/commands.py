from __future__ import annotations

from fasthtml.common import APIRouter, Li, A, Ul, Span, NotStr

from varro.dashboard.routes import list_dashboards

ar = APIRouter()

ICONS = {
    "home": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    "bar-chart": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
    "grid": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    "plus": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>',
    "settings": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
}


def _icon(name: str) -> NotStr:
    return NotStr(f'<span class="w-4 h-4 shrink-0 opacity-60">{ICONS[name]}</span>')


def _discover_dashboards(user_id: int) -> list[dict]:
    items = []
    for slug in list_dashboards(user_id):
        label = slug.replace("_", " ").replace("-", " ").title()
        items.append(dict(
            id=f"dashboard-{slug}",
            label=f"{label} Dashboard",
            icon="bar-chart",
            href=f"/dashboard/{slug}",
            target="#content-panel",
            swap="innerHTML",
        ))
    return items


def _build_commands(user_id: int) -> list[dict]:
    pages = [
        dict(id="home", label="Home", icon="home", href="/app", target="#content-panel", swap="innerHTML"),
        dict(id="settings", label="Settings", icon="settings", href="/settings", target="#content-panel", swap="innerHTML"),
    ]
    dashboards = _discover_dashboards(user_id)
    actions = [
        dict(id="new-chat", label="New Chat", icon="plus", href="/chat/new", target="body", swap="none"),
    ]
    groups = []
    if pages:
        groups.append(("Pages", pages))
    if dashboards:
        groups.append(("Dashboards", dashboards))
    if actions:
        groups.append(("Actions", actions))
    return groups


def _filter_groups(groups, q: str):
    if not q:
        return groups
    q = q.lower()
    filtered = []
    for name, items in groups:
        matched = [i for i in items if q in i["label"].lower() or q in i["id"].lower()]
        if matched:
            filtered.append((name, matched))
    return filtered


def _render_items(groups) -> list:
    els = []
    for name, items in groups:
        els.append(Li(Span(name, cls="text-xs font-medium text-base-content/50 uppercase tracking-wide"), cls="menu-title px-3 py-1.5"))
        for item in items:
            els.append(
                Li(
                    A(
                        _icon(item["icon"]),
                        Span(item["label"], cls="flex-1 text-sm"),
                        cls="flex items-center gap-3 px-3 py-2 rounded-field cursor-pointer",
                        data_href=item["href"],
                        data_target=item["target"],
                        data_swap=item["swap"],
                    ),
                    role="option",
                )
            )
    return els


@ar.get("/commands/search")
def search_commands(q: str = "", sess=None):
    user_id = sess.get("user_id", 1) if sess else 1
    groups = _build_commands(user_id)
    filtered = _filter_groups(groups, q)
    if not filtered:
        return Li(Span("No results found.", cls="px-4 py-8 text-sm text-base-content/50 text-center block"))
    return tuple(_render_items(filtered))
