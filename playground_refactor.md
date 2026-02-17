You’re already *very* close to a “playground” architecture — not in the Gymnasium/RL sense, but in the sense you actually care about:

* a **bounded environment** (DB + filesystem + shell + dashboard renderer),
* an **agent** that runs an internal **Observe → Decide → Act** loop,
* and a **canonical, replayable trace** that can be inspected by humans and by a review agent.

The key is to make the *trajectory* (decisions, actions, observations) first-class **without inventing a second logging system**. Given your constraint (“pydantic-ai messages already contain the full trace”), the right move is:

1. keep `.mpk` messages as the *only* source of truth,
2. build **better extraction + representation** of the loop from those messages,
3. optionally tighten the “environment boundary” so tool side-effects become more explicit and reviewable.

Below is a thorough analysis and a concrete direction.

---

## 1) What you have today is already a playground

### Canonical trace is already persisted

Per turn you save:

* `data/chats/{user_id}/{chat_id}/{idx}.mpk` via `save_turn_messages()` (msgpack+zstd)
* plus a render cache `.../{idx}.cache.json` via `save_turn_render_cache()`
* DB row `Turn(...)` with `obj_fp` pointing at the `.mpk`

That `.mpk` contains the pydantic-ai message objects (`ModelRequest`, `ModelResponse`, parts like `ThinkingPart`, `ToolCallPart`, `ToolReturnPart`, etc.). That *is* the trajectory log.

This matches the “no extra logs” requirement: your turn file is the trajectory.

### You already have a derived, inspectable view (`review.py`)

`review_turn()` is a *derived artifact generator*:

* extracts tool calls into `tool_calls/NN_sql.sql`, `tool_calls/NN_jupyter.py`
* extracts images into `images/`
* writes a readable `turn.md`

That fits your “source vs derived” principle in `AGENTS.md` perfectly.

### Where it falls short relative to “Observe → Decide → Act”

The current review format is “sectional”:

* Thinking (all combined)
* Tool Calls (flat list)
* Response (final)
* Usage

But the loop you care about is **temporal and causal**:

> decision → tool call → tool result → next decision…

Right now, the review does not preserve that structure (and it likely mis-associates some rich tool content; more on that below). That’s the main gap.

---

## 2) The simplest way to make the Observe–Decide–Act loop explicit

### Don’t implement a new loop engine

You don’t need to reify a Gym-like `env.step()` or implement a separate “agent loop runner”.

pydantic-ai already ran the loop.

So the simplest “playground” implementation is:

* **Run exactly as you do today** (pydantic-ai is the loop driver),
* **Persist the messages** (your `.mpk` is the trace),
* **Derive a *trajectory view*** that makes decisions/actions/observations legible.

In other words: *the “playground” is your trace + derived views*, not a new runtime system.

### Make “trajectory extraction” the explicit layer

Add a small internal module whose job is:

> take `list[ModelMessage]` → produce an ordered stream of **events** (or grouped “steps”).

This is the missing abstraction. It’s what turns your raw trace into a reviewable trajectory.

A good “minimal” model:

* **Event stream** (fully ordered) is the canonical derived representation.
* Optionally group into “steps” where a step is:

  * one assistant “decision” (thinking/text + tool calls),
  * followed by the corresponding tool returns (observations).

This is *simple*, and it decouples review/UI from pydantic-ai node types.

---

## 3) Important: your current review likely mishandles rich tool content

You added `varro/chat/tool_results.py` and use `extract_tool_render_records()` in the UI path (`agent_run.py`) to pair tool return parts with supplemental “content”.

That’s a big clue about pydantic-ai’s trace format:

* The **tool return “value”** is in `ToolReturnPart`.
* But the **tool return “content”** (images, tables) may be encoded as a *separate* `UserPromptPart` (so the model can “see” images in a user-role message, depending on provider constraints).

Your UI renderer already compensates by pairing:

* ToolReturnPart (with metadata flag `has_tool_content`)
* with the next UserPromptPart content payload(s)

`review.py` does **not** use that pairing logic. It tries to read `ToolReturnPart.content` directly, and separately extracts all `UserPromptPart` images as “user images”.

So for multimodal tool returns, the current review likely:

* misses the actual tool content, **or**
* mislabels tool content images as user prompt images.

For a “trajectory-first” system, this is exactly the kind of thing that makes review painful.

**Actionable conclusion:** your review generator should reuse the same pairing logic as your UI renderer (or share a common “trace extraction” utility).

---

## 4) What “explicit playground” should mean in Varro

Given your goals and the codebase principles, I’d define it as:

### A) One canonical source: pydantic-ai message trace per turn

You already have this (`.mpk`).

### B) One canonical derived representation: a trajectory event stream

Generated from `.mpk`, deterministic, idempotent.

### C) Optional: tool-side “observability upgrades”

Not new logs, but better **observations** returned by tools (so the trace itself becomes more self-describing).

### D) Wrappers compose around the loop, not inside it

Your own reflection in `playground_reflections.md` is correct: `run_agent` currently mixes loop + persistence + rendering + DB updates + title generation.

That mixing doesn’t break the loop conceptually, but it makes it harder to treat “trajectory” as a first-class artifact.

---

## 5) Concretely: implement “trajectory extraction” (simple and high leverage)

### The mapping from messages to ODA

You can derive ODA directly from pydantic-ai message types:

* **Observe**

  * `ToolReturnPart` (and the paired content payload)
  * plus any “user prompt content” (actual user message/images)
* **Decide**

  * `ThinkingPart` + intermediate `TextPart` in `ModelResponse`
* **Act**

  * `ToolCallPart` in `ModelResponse`

### Minimal derived schema

A simple event list (JSON-like) is enough:

```python
{"kind": "user", "text": "...", "images": [...]}
{"kind": "assistant_thinking", "text": "..."}
{"kind": "tool_call", "tool": "Sql", "args": {...}, "call_id": "..."}
{"kind": "tool_return", "tool": "Sql", "call_id": "...", "text": "...", "content_refs": [...]}
{"kind": "assistant_text", "text": "..."}  # final answer segments too
```

This does **two** things immediately:

1. review output can be chronological (which is what you want),
2. UI rendering can stop depending on pydantic-ai node types (`UserPromptNode`, `CallToolsNode`, etc.) and render from the event stream.

That’s the simplest path to your “playground” framing.

### Why an *event stream* beats a *step struct* initially

Grouping into “steps” is nice, but events are strictly simpler and more faithful.

Once you have events, steps are just a view:

* group events from one model decision until tool returns complete, etc.

---

## 6) Update `review.py` to be trajectory-first

### What to change in review output

Instead of (Thinking / Tool Calls / Response), emit:

* **User**
* **Trajectory**

  * Step 1

    * Decision (thinking excerpt + any text)
    * Actions (tool calls)
    * Observations (tool returns + images/tables)
  * Step 2 …
* **Final response**
* **Usage**

Even better: emit an **event log** with light grouping by model-response boundaries.

### Fix tool-content association

Make review reuse the same logic you already use for UI:

* call `extract_tool_render_records(node.request)` in UI
* do something equivalent in review, but on the stored messages

In practice, you want a shared function:

* `extract_tool_return_payloads(model_request) -> list[{tool_call_id, return_value, content}]`

Then review can:

* correctly attach images/tables to the right tool call
* stop misclassifying tool-content images as “user images”

This is a *direct* improvement in reviewability, and it’s 100% aligned with “no extra logs”.

---

## 7) Make observations more self-describing (without “extra logs”)

This is where you can materially improve trajectory quality.

Right now some tool observations are too thin for later inspection:

* `Write`: returns `Wrote N bytes.` (no path; the path is only in the action args)
* `Edit`: returns `Replaced X occurrence(s).`
* `Snapshot`: returns only the URL (even though the whole point is “saved to disk”)

Because the trace is your ground truth, **observations should carry enough semantics** that a reviewer doesn’t have to mentally join “action args” with “side effects”.

### Concrete, minimal upgrades

These do not add new logs; they make tool *observations* more legible:

* **Write tool return_value**: include path and maybe a short preview/hash
  Example: `Wrote 431 bytes to /dashboard/foo/dashboard.md (sha256=...)`

* **Edit tool return_value**: include path + replaced count + maybe a short diff excerpt
  Even a 10-line unified diff makes review *dramatically* easier.
  This also helps the agent avoid compounding mistakes.

* **Bash tool**: include the resulting cwd (since it persists across calls)
  Example: append `\n[cwd=/...]` to output.

* **Snapshot tool**: return the snapshot folder path (that’s the actual artifact)
  Right now it returns `result.url` and discards `result.folder`. That’s the opposite of what a reviewer needs.

These changes keep the trace self-contained and reduce “review friction”.

---

## 8) Environment boundary: useful, but not required for “playground”

Your `playground_reflections.md` argument for extracting an `Environment` is solid:

* tool adapters should be thin,
* mutable state should live in one place,
* step methods should return values (`StepResult`),
* and replay should call the environment directly.

That said, in terms of *bang-for-buck for trajectory reviewability*:

1. trajectory extraction + review rewrite is the biggest win,
2. tool observation upgrades is the next biggest win,
3. environment extraction is architectural hygiene that will pay off later (especially if you want replay/testing).

### Why environment extraction helps trajectory work

If the environment methods return a consistent `StepResult` shape (text + content + metadata), you can:

* standardize how tool returns appear in the trace,
* standardize artifact paths (where outputs land on disk),
* and make replay deterministic *as far as possible*.

It also lets you remove some current complecting:

* `touch_shell` is arguably redundant given `ShellPool.in_use_count` eviction logic (as you noted).
* bash cwd persistence is already “environment state”.

So: **good idea**, but I’d still implement the trajectory layer first.

---

## 9) Should you add other tools?

If the primary goal is “reviewable trajectories that help you improve the program”, the best tools are the ones that:

* reduce agent errors, and
* improve the trace quality of what happened.

Instead of adding many new tools, I’d do one of these:

### Option A: strengthen existing tools’ observations (preferred)

The return strings become richer, and reviewers get clarity “for free”.

### Option B: one new introspection tool (high leverage)

Add something like:

* `LsVars()` / `WorkspaceState()`
  returns a short summary of:

  * shell namespace keys and types (df/fig),
  * cwd,
  * recently created/modified files under `/dashboard/...` maybe

This is useful because it turns implicit state into explicit observations, which helps both:

* the agent (better decisions),
* the reviewer (less guessing).

But keep it small: if it turns into a second logging system, it violates your simplicity goal.

---

## 10) Is this a good idea overall?

Yes — for *this* project specifically, making “trajectory + reviewability” the core organizing principle is aligned with:

* your stated goal (“AI state statistician” that improves over time),
* your design principles in `AGENTS.md` (source vs derived, built for AI review),
* and the reality that agentic systems improve fastest when you can systematically inspect failures.

### The main caveat: determinism and “replay”

Some environment interactions are inherently non-deterministic over time:

* DB contents can change,
* web search results can change,
* filesystem state can be mutated by other runs/chats.

So if you want *true reproducibility*, you eventually need to snapshot more than the message trace (e.g., query results or dashboard outputs). But if your primary goal is **debuggability and iterative improvement**, not scientific reproducibility, you can postpone this.

A pragmatic stance:

* **Phase 1:** Make trajectories legible and evaluable (derive event stream + better review).
* **Phase 2:** Add selective artifact snapshotting where it matters (dashboards, key SQL outputs).
* **Phase 3:** Only then worry about full “replayable environment” semantics.

---

## 11) A practical, minimal roadmap

If I were sequencing this for maximum value with minimal code churn:

### Step 1: Add `trace` extraction module

* Parse pydantic-ai `ModelMessage`s → ordered events.
* Reuse/port the tool-content pairing logic you already built (`tool_results.py`).

### Step 2: Rewrite `review.py` to render the trajectory

* Chronological steps/events.
* Correct tool content association.
* Link extracted SQL/Jupyter/code as you do now.

### Step 3: Upgrade tool observations

* Write/Edit include path and (optionally) diff excerpt.
* Bash includes cwd.
* Snapshot returns folder path.

### Step 4: (Optional) move toward Environment abstraction

* Collapse deps.
* Move state transitions into `Environment`.
* Make replay and tests simpler.

### Step 5: (Optional) expose review in the UI

* A “Trace” or “Review” tab that loads the derived markdown.
* This turns the app into a literal playground UI without changing the runtime.

---

## The essence

You don’t need to build a Gymnasium-like environment or store extra logs.

You need a **better projection of the existing trace** into an explicit, readable ODA trajectory, plus slightly richer tool observations so the trace is self-describing.

If you do only one thing: make the review output *chronological and correctly associated with tool outputs*. That’s the single biggest step toward “playground as the app”.

If you want, I can go one level deeper and sketch the exact extraction algorithm for pydantic-ai message sequences (including parallel tool calls and the “supplemental UserPromptPart content” pattern you’re already handling in UI), and show how I’d structure the derived event stream so both the UI and `review.py` can share it.
