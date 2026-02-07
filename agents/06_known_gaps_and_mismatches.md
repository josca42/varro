# Known Gaps and Mismatches

Last verified: 2026-02-07.

## Resolved since previous revision

- **Dashboard AGENTS docs drift**: fixed. `varro/dashboard/AGENTS.md` now documents `queries/*.sql` and `queries/` folder structure.
- **DB config hardcoded DSN**: fixed. `varro/db/db.py` no longer overwrites `POSTGRES_DSN` with a hardcoded credential string.

## Open gaps

### Agent tool name mismatch in session restore

- `varro/chat/session.py` `_restore_shell_namespace()` imports `sql_query` and `jupyter_notebook` from `varro/agent/assistant.py`.
- `varro/agent/assistant.py` defines `Sql` and `Jupyter` tool functions (no `sql_query` / `jupyter_notebook` symbols).
- Impact: replay of historical tool calls for shell restoration can fail.

### App route drift

- Auth routes exist (`app/routes/auth.py`, `ui/app/auth.py`) but are not mounted in `app/main.py`.
- `app/routes/index.py` also appears unused by the current unified app entrypoint.

### Data script portability risks

- `varro/data/statbank_to_disk/copy_tables_statbank.py` imports `get_all_table_ids` from `create_table_info_dict`, but that module is not present in this repo.
- Multiple scripts/docs still hardcode machine-specific roots (`/root/varro/...`, `/mnt/HC_Volume_103849439/...`), for example:
  - `varro/data/statbank_to_disk/get_table_info.py`
  - `varro/data/statbank_to_disk/get_cat_tables_and_descriptions.py`
  - `varro/data/fact_col_to_dim_table/create_dimension_links.py`
  - `varro/data/fact_col_to_dim_table/*.md`

### Filesystem sandbox mismatch for Read/Write/Edit

- `varro/agent/bash.py` sandboxes shell commands to `DATA_DIR/user/{user_id}/`.
- `varro/agent/filesystem.py` (`read_file`, `write_file`, `edit_file`) directly uses absolute host paths with no equivalent sandbox/root mapping.
- `varro/prompts/agent/rigsstatistiker.j2` describes a sandboxed root filesystem (`/subjects`, `/fact`, `/dim`, `/dashboards`), but file tools do not currently enforce or map to that model.

### Documentation references to legacy/current behavior mismatch

- Top-level `README.md` still describes old Chainlit-based chat and `ui_chat/app.py`, while current runtime is FastHTML split-panel + websocket chat.
- `docs/varro/app_structure.md` and `docs/varro/dashboard_spec.md` still mention `ContentNavbar`, but `ui/app/layout.py` currently exposes `Navbar` and no `ContentNavbar` component.
