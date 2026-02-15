## What you have today is already an Observation–Action Loop (just not named that way)

If we translate Varro into Gymnasium terms:

* **Environment state** (mutable, internal):

  * IPython shell namespace (`TerminalInteractiveShell.user_ns`) managed by `ShellPool`
  * bash CWD persisted in `data/chats/{user_id}/{chat_id}/runtime.json`
  * workspace filesystem rooted at `data/user/{user_id}/...` (mutable)
  * DB is effectively read-only state from the agent’s POV

* **Actions** (agent → env):

  * tool calls: `Sql`, `Jupyter`, `Bash`, `Read`, `Write`, `Edit`, `Snapshot`, `UpdateUrl`, `ColumnValues`

* **Observations** (env → agent):

  * `ToolReturn.return_value` text
  * optional `ToolReturn.content` (images, df previews, etc.)
  * tool metadata (`metadata={"ui": ...}`)

* **Loop driver**:

  * pydantic-ai’s internal loop inside `agent.iter(...)`, which alternates:

    * model inference → tool calls → tool returns → model inference → … → stop

And you already have a trajectory log:

* `varro/chat/turn_store.py` stores the full pydantic-ai message stream per turn as immutable `{idx}.mpk` (msgpack+zstd).
* `varro/chat/review.py` is a derived “inspection view” over that log.

So: the OAL *exists*. The question is whether making the **environment boundary explicit** (and treating replay/snapshots as first-class) will simplify the system and improve reliability under your constraints.

---

## First constraint check: “TTL 10 minutes, reset on each shell use”

### Current behavior (from `varro/chat/shell_pool.py`)

* Shells are cached per `(user_id, chat_id)`.
* `ttl` default is **10 minutes**.
* `evict_idle()` evicts only when:

  * `entry.in_use_count == 0`, and
  * `now - entry.last_active > ttl`
* `last_active` is updated on:

  * `_acquire()` (lease start)
  * `_release()` (lease end)
  * explicit `touch(user_id, chat_id)`

### Tool-level “touch”

Your tools currently call `ctx.deps.touch_shell()`:

* `Sql(...)` calls it at end
* `Jupyter(...)` calls it at end (both show and non-show paths)

This can satisfy “reset on each use” *if* `touch_shell` is wired to `shell_pool.touch`.

But note a subtlety:

* While a run is active, the shell is leased and `in_use_count != 0`, so **it cannot be evicted anyway**.
* After the run ends, `_release()` updates `last_active` to “end of run”, which is usually **≥ last tool call time**.

So from a pure eviction standpoint, “touch on each tool call” is **mostly redundant** with the current eviction rule (exactly the point you made in `playground_reflections.md`).

### Where your constraint *might* not be satisfied

The constraint becomes meaningful if either of these are true:

1. You want to treat “shell use” as something that can happen **outside a lease**, i.e. other code reads the shell without going through `ShellPool.lease(...)`.

   * Example: rendering layers reaching into `shell.user_ns` without an env wrapper.
2. You want a stricter invariant like:

   * “evict after 10 minutes since the last time the shell was *actually used*, even if a run is still ongoing”
   * That would require changing `evict_idle()` semantics (evict even with `in_use_count != 0`), which is a bigger change and implies the loop driver must tolerate shell loss mid-run.

Given how your runtime is structured (shell leased for the entire agent run), the **current TTL model is already correct** for typical workloads.

**Recommendation:** keep “touch on use” but move it into the *environment* layer so it’s not passed around as `touch_shell` and not forgotten.

---

## Second constraint check: “only dump the most recent namespace; replay recovers earlier states”

### What you do now

* Shell snapshots are saved in `ShellPool._close_shell(..., save_snapshot=True)` **only on eviction**.
* Snapshot file: `data/chats/{user_id}/{chat_id}/shell.pkl`
* It is overwritten (so it’s “most recent”, not versioned).

This *already* matches “only dump the most recent namespace”.

### What you *don’t* get with the current approach

If the process dies or the shell is invalidated before idle eviction happens, you may lose the in-memory namespace changes since the last eviction snapshot.

You can still recover via replay, but only if:

* you have a working replay mechanism, and
* replay is acceptably fast and sufficiently deterministic for your use-case.

### Replay today (`varro/chat/shell_replay.py`)

Current replay:

* replays only `Sql` calls *when* `df_name` is set, and
* replays all `Jupyter` calls
* it monkeypatches by importing tool functions and fabricating a pydantic-ai-ish `ctx`

This works as a bootstrap, but it’s exactly the kind of coupling that becomes painful if you change tool implementations or switch agent frameworks.

**Key point:** the replay approach is viable, but it should be replaying “environment operations”, not “pydantic-ai tools”.

---

## Where the “explicit Environment + StepResult” idea *actually* pays off

Your `playground_reflections.md` “After” architecture is pointing at two concrete wins:

1. **Make the environment boundary real** (and keep mutable state behind it)
2. **Make replay a property of the environment** (independent of pydantic-ai node types and tool wrappers)

The simplest version that stays within your codebase’s style and avoids overengineering is:

### 1) Environment owns stateful runtime: shell + bash cwd (+ optional snapshot bookkeeping)

Stateful things today:

* shell namespace
* bash cwd
* (maybe) render cache generation that currently peeks into `shell.user_ns`

So the environment should own:

* `sql(query, df_name) -> StepResult`
* `jupyter(code, show) -> StepResult`
* `bash(command) -> StepResult` (or string)
* “touch shell” semantics (internally, not passed around)

Stateless tools (`Read`, `Write`, `Edit`, `ColumnValues`, `UpdateUrl`) can either:

* stay as direct functions, **or**
* be methods for uniformity (I’d only wrap them if it simplifies dependency injection)

### 2) Tools become adapters

Pydantic-ai tool functions become thin boundaries:

* call `ctx.deps.env.sql(...)`
* convert `StepResult` to `ToolReturn`
* catch exceptions only to convert to `ModelRetry`

That removes:

* `ctx.deps.shell` reaching into mutable state
* `ctx.deps.touch_shell` threading infra concerns everywhere

### 3) Replay becomes: read log → apply env methods

Instead of:

* importing `Sql` and `Jupyter` tool adapters and faking contexts

You do:

* parse tool calls from stored messages
* call `env.sql(...)` / `env.jupyter(...)` directly

This decouples replay from:

* pydantic-ai types
* UI rendering blocks
* tool wrapper metadata conventions

### 4) Snapshot becomes a cache, not a source of truth

This aligns with your “State as values” principle:

* **source-of-truth:** immutable turn log (`{idx}.mpk`)
* **derived cache:** latest `shell.pkl` (and maybe `runtime.json`)

You can delete the snapshot at any time and reconstruct from replay.

That’s a clean “playground” story.

---

## The one big technical gotcha if you want a *simple* loop: parallel tool calls + stateful shell

Right now your Anthropic settings include:

```py
parallel_tool_calls=True
```

Your shell is stateful, and `TerminalInteractiveShell.run_cell(...)` is not designed for concurrent execution.

If the model emits multiple tool calls in one turn (especially multiple `Jupyter` calls), and pydantic-ai executes them concurrently, you have two problems:

* race conditions in `shell.user_ns`
* non-deterministic replay ordering

Even if pydantic-ai happens to execute tools sequentially today, the setting is a latent footgun because the *model* is encouraged to batch tool calls.

**For an Observation–Action loop to stay “simple” you want:**

* one action applied at a time, deterministically
* a total order of transitions

So you should do one of:

1. **Disable parallel tool calls** (simplest conceptual model)

* pro: easiest to reason about
* con: slower if the model wants to do independent IO-bound calls in parallel

2. **Keep parallel tool calls, but serialize stateful tools**

* enforce a lock around `sql/jupyter` that mutate the environment
* allow truly independent tools (web search, read-only column values) to run concurrently

Given your “Elegant minimalism” goal, I’d lean toward **(1)** unless you have clear perf pressure.

---

## About your shell memory concern: TTL helps, but it doesn’t bound peak memory

A 10-minute TTL controls *retention*, not *peak usage*:

* If a user does one query that materializes a 500MB dataframe into `user_ns`, that shell holds 500MB until eviction (or manual cleanup).
* If you have many chats active within 10 minutes, you can still spike memory.

If memory is a real constraint, you typically want at least one additional mechanism besides TTL:

* **LRU by chat count** (cap number of shells cached)
* **soft memory budget** (evict least-recently-used shells until under budget)
* **disk-backed datasets** (store large frames to parquet and only keep lightweight handles)

You didn’t ask for this explicitly, but it’s worth stating: **TTL alone is not a memory bound**, it’s a time bound.

That said, for a single-user demo environment, TTL may be enough.

---

## “Only dump most recent namespace” — how I’d implement it to support your replay story cleanly

If you want replay to be the universal recovery mechanism, the cleanest rule is:

* snapshot is optional, best-effort, overwriting, derived cache

But you’ll get much better ergonomics if you add one tiny piece of metadata:

* store the **turn index** that the snapshot corresponds to

Why? Because then recovery can be:

* load snapshot at turn `k`
* replay tool calls from turns `k+1..latest`

instead of “replay everything from turn 0”.

Where to put it:

* could live alongside `shell.pkl` as `shell.json`
* or inside `runtime.json` (since you already treat that as mutable runtime)

This keeps “only most recent snapshot” while enabling fast recovery.

---

## Is making the OAL explicit a good idea for Varro?

### Yes, if your goal is “simple, replayable, inspectable”

It aligns extremely well with what you already value (from `AGENTS.md`):

* **Explicit transitions**
* **State as values**
* **Built for AI review**
* **Don’t complect**

An explicit environment boundary does three high-value things:

1. **It makes the mutable state obvious and contained**

   * shell namespace, bash cwd, caches live behind one object

2. **It makes replay a first-class operation**

   * which is exactly what you want if you only keep the latest snapshot

3. **It reduces framework coupling**

   * today, `shell_replay.py` depends on tool wrappers and pydantic-ai-ish contexts
   * tomorrow, you’ll want replay to survive refactors and maybe model/tool changes

### The main risk: you can accidentally “invent an abstraction layer” that grows

The failure mode looks like:

* Environment starts owning *everything* (rendering, DB CRUD, SSE, title generation)
* StepResult becomes a kitchen sink
* You end up with more indirection without simplification

Your own reflection already identified this risk: `run_agent` still mixes loop + wrappers.

So the right move is:

* **make the environment explicit only for stateful runtime**
* keep wrappers as wrappers (streaming/persistence/review/render)

### Another risk: replay isn’t always faithful

Replay will only be as good as:

* determinism of the DB state
* determinism of Jupyter code
* whether you include all stateful actions in replay

Even if replay isn’t perfect, it can still be “good enough” as a recovery mechanism, as long as:

* the user-facing artifacts of the original run are preserved (your `.mpk` + review already do that)
* replay is primarily for *continuation*, not for *forensic truth*

---

## A pragmatic “simple OAL” target architecture for Varro

This keeps pydantic-ai, keeps your existing persistence format, and makes replay/shell TTL coherent.

### Environment

Owns:

* `shell`
* `bash cwd` (loaded once per env, saved on bash steps)
* `touch()` behavior
* `snapshot_latest()` and `restore_latest()/replay_to(turn_idx)`

Returns:

* `StepResult(text, content, has_ui_content)`

### Tool adapters

* no business logic
* no shared mutable state access
* just boundary conversion + `ModelRetry` mapping

### Loop driver (still pydantic-ai)

* unchanged: `agent.iter(...)`

### Wrappers around the loop

* stream wrapper (your `RunManager`/SSE)
* persistence wrapper (save `{idx}.mpk`, DB `Turn`)
* render-cache wrapper (extract `<fig>/<df>` refs and render them)
* optional: review wrapper (generate `chat_reviews/...` eagerly if desired)

This design is “simple” in the Rich Hickey sense because:

* the agent and environment exchange values through narrow channels
* mutable state is internal to one component
* replay is an environment concern, not a framework hack

---

## Bottom line

* **Can the Observation–Action Loop be implemented simply?**
  Yes — and you’re already 70% there. The “simple” version is: make the environment boundary explicit for stateful operations (shell + bash), keep pydantic-ai as the loop driver, and treat snapshots/replay as environment capabilities.

* **Does your TTL + “latest snapshot only” constraint fit that model?**
  Yes. `ShellPool` already enforces TTL, and a “latest snapshot only” file is consistent with replay-as-recovery. The main improvement is to formalize snapshot/replay semantics (ideally with snapshot turn index metadata) and to remove `touch_shell` from deps by moving “touch on use” inside the environment.

* **Is it a good idea?**
  For Varro’s goals (analysis playground + reviewability), yes. The explicit OAL/environment boundary will pay off in:

  * replay and debugging
  * reduced coupling (especially shell replay)
  * clearer separation between loop vs wrappers
    The main thing to watch is **not overgrowing the Environment** and to decide how to handle **parallel tool calls** with a stateful shell (disable or serialize).