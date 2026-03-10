# DEV Bash absolute path translation

Date: 2026-03-04.

- `varro/agent/sandbox.py` now rewrites absolute path starts in DEV mode (`if not _use_bwrap()`) before delegating to `run_bash_command_vanilla(...)`.
- Rewrite uses a single regex substitution that prefixes token-start `/` with the active `user_workspace_root`.
- This is intentionally brittle and DEV-only.
- BWRAP behavior is unchanged.
- Added DEV rewrite assertion in `tests/agent/test_bash_command.py`.
