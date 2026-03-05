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
  - exchange storage is scoped per chat at `.varro_exchange/{chat_id}` and cleaned on shell close/eviction.
  - when a chat resumes later, snapshot state is loaded and a fresh `.varro_exchange/{chat_id}` directory is created.

Operational note:

- `RLIMIT_NPROC=128` caused bwrap startup failure (`Creating new namespace failed: Resource temporarily unavailable`) on this host.
- Default sandbox NPROC was raised to `256` to keep startup reliable.
- Plot/image-heavy workloads can require more worker processes/FDs than bash commands. Worker limits now support `SANDBOX_WORKER_NPROC`/`SANDBOX_WORKER_NOFILE` (fallback to shared limits), with defaults `1024`/`4096`.
- Worker env now uses writable home/cache paths under `/home/dev` (`HOME`, `XDG_CACHE_HOME`, `XDG_CONFIG_HOME`, `MPLCONFIGDIR`) to avoid Fontconfig cache failures in sandboxed plotting flows.
- Worker env also constrains native thread pools (`ARROW_NUM_THREADS=1`, `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`) to avoid `std::system_error: Resource temporarily unavailable` during parquet dataframe transfer in `set_dataframe`.
