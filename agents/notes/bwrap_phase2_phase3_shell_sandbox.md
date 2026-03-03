# Bubblewrap Phase 2 + 3 Shell Sandbox

Date: 2026-03-03.

- Added `varro/agent/sandbox.py` as the runtime selector + sandbox wrapper layer.
- Added `varro/agent/ipython_worker.py` as a long-lived worker process for `TerminalInteractiveShell` inside bwrap.
- `varro/agent/shell.py` now contains the vanilla interfaces:
  - `get_shell()` for in-process IPython shell.
  - `run_bash_command(user_id, cwd_rel, command)` for vanilla bash execution rooted in user workspace.
- `varro/agent/assistant.py` now imports `run_bash_command` from `varro.agent.sandbox`.
- `varro/chat/shell_pool.py` now uses `create_shell(...)` / `close_shell(...)` from `varro.agent.sandbox`.

Sandbox behavior:

- Bash in BWRAP mode now uses explicit namespace flags:
  - `--unshare-user --unshare-pid --unshare-ipc --unshare-uts --unshare-net --unshare-cgroup`
  - `--disable-userns --assert-userns-disabled --die-with-parent --new-session`
- Bash mounts docs via read-only mounts (`/context`, `/agent_data`) and keeps workspace as `/`.
- Delete is now allowed in writable workspace paths; delete targeting readonly docs roots is blocked.
- IPython is no longer in-process in BWRAP mode:
  - per `(user_id, chat_id)` worker process.
  - state survives via existing `shell.pkl` snapshot path contract.
  - `Sql` dataframe injection still uses `ctx.deps.shell.user_ns[df_name] = df`.
  - `Jupyter(show=[...])` supports proxy rendering via `shell.render_show(name)` when available.

Operational note:

- `RLIMIT_NPROC=128` caused bwrap startup failure (`Creating new namespace failed: Resource temporarily unavailable`) on this host.
- Default sandbox NPROC was raised to `256` to keep startup reliable.
