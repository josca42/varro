"""ui.app.command_palette

HTMX-native cmdk-style command palette. Server-side filtering via /commands/search,
vanilla JS for open/close and keyboard navigation.
"""

from __future__ import annotations

from fasthtml.common import Div, Input, Ul, Script, NotStr

from ui.daisy import Modal, ModalBox, ModalBackdrop


SEARCH_ICON = (
    '<svg class="h-4 w-4 opacity-50 shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    '<g stroke-linejoin="round" stroke-linecap="round" stroke-width="2.5" fill="none" stroke="currentColor">'
    '<circle cx="11" cy="11" r="8"></circle>'
    '<path d="m21 21-4.3-4.3"></path>'
    '</g></svg>'
)


def CommandPalette():
    return Modal(
        ModalBox(
            Div(
                NotStr(SEARCH_ICON),
                Input(
                    type="text",
                    id="command-search",
                    name="q",
                    placeholder="Type a command or search...",
                    cls="flex-1 bg-transparent border-none outline-none text-sm placeholder:text-base-content/40",
                    autocomplete="off",
                    hx_get="/commands/search",
                    hx_trigger="search, keyup delay:200ms changed",
                    hx_target="#command-list",
                ),
                cls="flex items-center gap-3 px-4 py-3 border-b border-base-300",
            ),
            Ul(
                id="command-list",
                role="listbox",
                cls="max-h-72 overflow-y-auto py-2 menu",
            ),
            cls="p-0 max-w-lg",
        ),
        ModalBackdrop(method="dialog"),
        id="command-palette",
    )


def CommandPaletteScript():
    return Script("""
(function() {
  const dlg = document.getElementById('command-palette');
  if (!dlg) return;
  const input = document.getElementById('command-search');
  const list = document.getElementById('command-list');
  let active = -1;

  function getOptions() {
    return list.querySelectorAll('li[role="option"]');
  }

  function clearActive() {
    getOptions().forEach(el => el.querySelector('a')?.classList.remove('bg-base-200'));
  }

  function setActive(idx) {
    const opts = getOptions();
    if (opts.length === 0) { active = -1; return; }
    active = ((idx % opts.length) + opts.length) % opts.length;
    clearActive();
    const a = opts[active]?.querySelector('a');
    if (a) {
      a.classList.add('bg-base-200');
      a.scrollIntoView({ block: 'nearest' });
    }
  }

  function openPalette() {
    input.value = '';
    dlg.showModal();
    input.focus();
    htmx.ajax('GET', '/commands/search?q=', { target: '#command-list' });
  }

  function navigate(item) {
    const a = item.querySelector('a');
    if (!a) return;
    const href = a.dataset.href;
    const target = a.dataset.target;
    const swap = a.dataset.swap;
    dlg.close();
    if (href) {
      htmx.ajax('GET', href, { target: target, swap: swap });
      if (swap !== 'none') history.pushState({}, '', href);
    }
  }

  // Cmd+K / Ctrl+K toggle
  document.addEventListener('keydown', function(e) {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      dlg.open ? dlg.close() : openPalette();
    }
  });

  // Navbar trigger
  window.addEventListener('open-command-palette', openPalette);

  // Keyboard nav inside the input
  input.addEventListener('keydown', function(e) {
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      setActive(active + 1);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      setActive(active - 1);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      const opts = getOptions();
      if (active >= 0 && active < opts.length) navigate(opts[active]);
    }
  });

  // Reset active on new results
  document.body.addEventListener('htmx:afterSwap', function(e) {
    if (e.detail.target === list) setActive(0);
  });

  // Click on option
  list.addEventListener('click', function(e) {
    const li = e.target.closest('li[role="option"]');
    if (li) navigate(li);
  });
})();
""")
