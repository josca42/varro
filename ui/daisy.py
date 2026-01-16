"""ui.daisy

Low-level DaisyUI primitives.

These are thin wrappers around DaisyUI class names, intended as building
blocks for `ui.components.*` and `ui.app.*`.

Conventions:
- Each function applies the DaisyUI base class.
- `cls='-primary -sm'` expands to `btn-primary btn-sm` (for `compcls='btn'`).
- Primitives are *not* the primary public API; use `ui.components` for
  opinionated shadcn-like components.
"""

from __future__ import annotations

from .core import mk_compfn

# -----------------------------------------------------------------------------
# Actions
# -----------------------------------------------------------------------------

mk_compfn("btn", tag="Button", name="Btn", slot="button")
mk_compfn("btn", tag="A", name="LinkBtn", slot="link-button")
mk_compfn("badge", tag="Span", name="Badge", slot="badge")
mk_compfn("kbd", tag="Kbd", name="Kbd", slot="kbd")

mk_compfn("dropdown", tag="Details", name="Dropdown", slot="dropdown")
mk_compfn("dropdown-content", tag="Ul", name="DropdownContent", slot="dropdown-content")

# -----------------------------------------------------------------------------
# Cards
# -----------------------------------------------------------------------------

mk_compfn("card", tag="Div", name="CardRoot", slot="card")
mk_compfn("card-body", tag="Div", name="CardBody", slot="card-body")
mk_compfn("card-title", tag="H2", name="CardTitle", slot="card-title")
mk_compfn("card-actions", tag="Div", name="CardActions", slot="card-actions")

# -----------------------------------------------------------------------------
# Feedback
# -----------------------------------------------------------------------------

mk_compfn("alert", tag="Div", name="Alert", slot="alert")
mk_compfn("loading", tag="Span", name="Loading", slot="loading")
mk_compfn("skeleton", tag="Div", name="Skeleton", slot="skeleton")
mk_compfn("divider", tag="Div", name="Divider", slot="divider")

# -----------------------------------------------------------------------------
# Forms
# -----------------------------------------------------------------------------

mk_compfn("input", tag="Input", name="Input", slot="input")
mk_compfn("select", tag="Select", name="Select", slot="select")
mk_compfn("textarea", tag="Textarea", name="Textarea", slot="textarea")

mk_compfn("checkbox", tag="Input", name="Checkbox", type="checkbox", slot="checkbox")
mk_compfn("radio", tag="Input", name="Radio", type="radio", slot="radio")
mk_compfn("toggle", tag="Input", name="Toggle", type="checkbox", slot="toggle")

# Theme controller (DaisyUI)
mk_compfn("theme-controller", tag="Input", name="ThemeController", type="checkbox", slot="theme-controller")

# -----------------------------------------------------------------------------
# Modal
# -----------------------------------------------------------------------------

mk_compfn("modal", tag="Dialog", name="Modal", slot="modal")
mk_compfn("modal-box", tag="Div", name="ModalBox", slot="modal-box")
mk_compfn("modal-action", tag="Form", name="ModalAction", slot="modal-action")
mk_compfn("modal-backdrop", tag="Form", name="ModalBackdrop", slot="modal-backdrop")

# -----------------------------------------------------------------------------
# Navigation / layout
# -----------------------------------------------------------------------------

mk_compfn("navbar", tag="Div", name="Navbar", slot="navbar")
mk_compfn("navbar-start", tag="Div", name="NavbarStart", slot="navbar-start")
mk_compfn("navbar-center", tag="Div", name="NavbarCenter", slot="navbar-center")
mk_compfn("navbar-end", tag="Div", name="NavbarEnd", slot="navbar-end")

mk_compfn("tabs", tag="Div", name="Tabs", slot="tabs")
mk_compfn("tab", tag="Button", name="Tab", slot="tab")
mk_compfn("tab-content", tag="Div", name="TabContent", slot="tab-content")

mk_compfn("join", tag="Div", name="Join", slot="join")
mk_compfn("join-item", tag="Div", name="JoinItem", slot="join-item")

# -----------------------------------------------------------------------------
# Chat (native DaisyUI chat, not the mock Lovable chat)
# -----------------------------------------------------------------------------

mk_compfn("chat", tag="Div", name="Chat", slot="chat")
mk_compfn("chat-image", tag="Div", name="ChatImage", slot="chat-image")
mk_compfn("chat-header", tag="Div", name="ChatHeader", slot="chat-header")
mk_compfn("chat-footer", tag="Div", name="ChatFooter", slot="chat-footer")
mk_compfn("chat-bubble", tag="Div", name="ChatBubble", slot="chat-bubble")


__all__ = [
    # Actions
    "Btn",
    "LinkBtn",
    "Badge",
    "Kbd",
    "Dropdown",
    "DropdownContent",
    # Cards
    "CardRoot",
    "CardBody",
    "CardTitle",
    "CardActions",
    # Feedback
    "Alert",
    "Loading",
    "Skeleton",
    "Divider",
    # Forms
    "Input",
    "Select",
    "Textarea",
    "Checkbox",
    "Radio",
    "Toggle",
    "ThemeController",
    # Modal
    "Modal",
    "ModalBox",
    "ModalAction",
    "ModalBackdrop",
    # Navigation
    "Navbar",
    "NavbarStart",
    "NavbarCenter",
    "NavbarEnd",
    "Tabs",
    "Tab",
    "TabContent",
    "Join",
    "JoinItem",
    # Chat
    "Chat",
    "ChatImage",
    "ChatHeader",
    "ChatFooter",
    "ChatBubble",
]
