# The Observation-Action Loop: Varro as a Playground Environment

## The Core Idea

At its heart, every agent system — whether an RL policy playing Atari or an LLM
analyzing Danish statistics — runs the same loop:

```
observe → decide → act → observe → decide → act → ...
```

The Gymnasium interface distills this to a handful of concepts:

```python
obs, info = env.reset()
while not done:
    action = agent.decide(obs)
    obs, reward, terminated, truncated, info = env.step(action)
```

An environment is a function of `(state, action) → (new_state, observation)`.
An agent is a function of `observation → action`.
They communicate through a narrow, well-defined interface. Everything else —
reward, memory, planning, UI — is layered on top.

The question is: what does this look like when the agent is an LLM with tool
calls, the environment is a sandboxed data analysis workspace, and the "game"
is understanding Danish society through statistics?

---

## Simple Made Easy

Rich Hickey draws a distinction between **simple** (not interleaved, one role,
one concept) and **easy** (familiar, near at hand). The observation-action loop
is simple in his sense:

**The agent and environment only communicate through a narrow channel.** The
agent doesn't reach into the environment's database connection pool. The
environment doesn't peek at the agent's context window. They exchange values —
an action string in, an observation string out.

**Simple things compose.** Because the interface is just `obs → action` and
`(state, action) → (state, obs)`, you can swap agents without touching the
environment, stack wrappers around either side (observation transformers,
action filters, reward shapers), and record everything flowing through the
interface.

**Values, not places.** The environment doesn't hand the agent a mutable
reference to its world. It hands it a value. The agent doesn't mutate the
environment — it returns an action value. Even if the implementation uses
mutation internally, the conceptual model is functional.

**Decoupling when and what.** The loop separates what happens (transition
logic) from when it happens (the loop driver). You could run it synchronously,
batch it, distribute it, or replay it from a log.

---

## What We Did: Extracting the Environment

### Before

The environment was scattered. The Sql tool reached into `ctx.deps.shell` to
mutate the IPython namespace, called `ctx.deps.touch_shell()` for keepalive,
imported the database engine directly. The Bash tool loaded and saved CWD state
through three separate function calls. `AssistantRunDeps` bundled five unrelated
concerns into one bag:

```python
# Before
@dataclass
class AssistantRunDeps:
    user_id: int
    chat_id: int
    shell: object                      # mutable execution state
    request_current_url: Callable      # UI state
    touch_shell: Callable              # infrastructure keepalive
```

Every tool reached through deps to manipulate shared mutable state. The "step
function" was implicit — spread across a dozen tool definitions, each with its
own imports and side effects.

### After

The `Environment` class owns the mutable state and exposes step functions that
return immutable `StepResult` values:

```python
@dataclass(frozen=True)
class StepResult:
    text: str                              # what the agent sees
    content: list[Any] | None = None       # rich content (figures, images)
    has_ui_content: bool = False

class Environment:
    def __init__(self, *, user_id, chat_id, shell):
        self.user_id = user_id
        self.chat_id = chat_id
        self._shell = shell
        self._bash_cwd = load_bash_cwd(user_id, chat_id)

    def sql(self, query, df_name=None) -> StepResult: ...
    async def jupyter(self, code, show=None) -> StepResult: ...
    def bash(self, command) -> StepResult: ...
```

Tools become thin adapters between pydantic-ai's protocol and the environment:

```python
@agent.tool
def Sql(ctx, query, df_name=None):
    try:
        result = ctx.deps.env.sql(query, df_name)
    except Exception as e:
        raise ModelRetry(str(e))
    return ToolReturn(
        return_value=result.text,
        metadata={"ui": {"has_tool_content": result.has_ui_content}},
    )
```

And `AssistantRunDeps` collapses to two fields:

```python
@dataclass
class AssistantRunDeps:
    env: Environment
    request_current_url: Callable[[], str]
```

### The Three Requirements

This design had to satisfy three concrete constraints:

**1. Tell the agent that a dataset is stored and accessible by name.**
`Environment.sql()` returns `StepResult(text="Stored as salary_df\n...")`. The
text goes to `ToolReturn.return_value`, which is what the LLM sees. The agent
knows the name because the environment told it through the observation channel.

**2. Add the dataset to the IPython namespace.**
`self._shell.user_ns[df_name] = df` happens inside `Environment.sql()`. It's
an internal state transition — the environment managing its own state, invisible
to the agent except through the observation. Exactly like a game engine updating
its physics: the agent sees the new frame, not the internal mutation.

**3. Stream UI events to the user.**
`StepResult.content` carries rich content (plotly PNGs, DataFrames). The tool
adapter wraps it as `ToolReturn(content=result.content)`. Pydantic-ai sends it
through its node protocol. `node_to_blocks` converts to UI blocks. The SSE
stream delivers them to the browser. The streaming pipeline is a wrapper around
the loop — it observes the observations, it doesn't participate in them.

### What Got Removed

**`touch_shell` was redundant.** The shell pool's `evict_idle()` method skips
any entry with `in_use_count != 0`. While the shell is leased (which it is for
the entire agent run), it can't be evicted. The per-tool-call keepalive was
threading infrastructure into the observation-action boundary for no reason.

**`shell_replay` stopped going through tool adapters.** The old version
monkeypatched `Sql` and `Jupyter` functions and built fake pydantic-ai contexts
with `SimpleNamespace`. The new version calls `env.sql()` and `env.jupyter()`
directly. Replay is an environment operation — it doesn't need the agent
framework.

---

## Where the Architecture Stands Now

### What's Simple

The **bash sandbox** is the cleanest embodiment. `run_bash_command` is
essentially `(state, action) → (state, observation)`:

```python
def run_bash_command(user_id, cwd_rel, command) -> tuple[str, str]:
    # action: command string
    # state in: cwd_rel
    # ... validation, execution ...
    # state out: new cwd_rel
    # observation: output string
    return output, cwd_rel
```

Agent submits a string. Sandbox returns a string. The sandbox doesn't know about
Claude's thinking tokens. Claude doesn't know about bwrap container internals.
This is "takes a string, returns a string."

The **tool interfaces** are narrow and typed. Each tool has a well-defined
signature. The agent communicates with the environment through these channels —
it can't reach into the database connection pool or mutate the shell pool's
internal state.

The **Environment** now owns the three stateful operations (sql, jupyter, bash)
and returns immutable values. The stateless operations (Read, Write, Edit,
ColumnValues) stay as direct function calls — they don't need the environment
because they don't manage mutable state.

### Where Complecting Still Lives

**`run_agent` still mixes the loop with persistence and rendering.** The
function that runs the observation-action loop also saves turn messages to disk,
creates database records, triggers chat title generation, and converts nodes to
UI blocks. These are all wrappers that should compose around the loop, not live
inside it:

```python
# What it does today (simplified)
async def run_agent(user_text, *, chats, env, current_url):
    # 1. Load history
    # 2. Run the loop, yielding UI blocks     ← the actual loop
    # 3. Save messages to disk                 ← persistence wrapper
    # 4. Create Turn in database               ← persistence wrapper
    # 5. Auto-generate chat title              ← UX wrapper
```

**The IPython shell is still a mutable shared reference.** The `Environment`
owns it, but exposes it via `env.shell` for the rendering layer
(`node_to_blocks`, `CallToolsBlock`). The rendering layer reads from the shell's
namespace to render DataFrames and figures. This is read-only access, which is
acceptable, but it means the rendering and the environment share a mutable
object. A future step could have the environment produce snapshots of renderable
state instead.

**`node_to_blocks` couples the loop to pydantic-ai's node types.** The
rendering logic knows about `UserPromptNode`, `ModelRequestNode`,
`CallToolsNode`, `EndNode`. If you wanted to replay the loop from a log or swap
the agent framework, the rendering would need to change too.

---

## Where This Could Go

### Separating the Loop Driver from Its Wrappers

The purest expression would be:

```python
# The core loop — pure, replayable, testable
async for obs in loop(env, agent, user_text):
    yield obs

# Wrappers layered on top
stream_wrapper(loop)      # SSE streaming
persist_wrapper(loop)     # save turns to disk
render_wrapper(loop)      # convert to UI blocks
```

Each wrapper is independent. You could strip them off and run the bare loop in a
test. You could add a logging wrapper without touching the others. You could
replay from a log without the streaming layer.

### Observations as Immutable Snapshots

Right now `env.shell` leaks a mutable reference. The stricter version: the
Environment's step functions return everything the outside world needs as
values within `StepResult`. If the rendering layer needs a DataFrame, the
`StepResult` carries it — the renderer never reaches into the environment.

### The Dashboard as a Second Environment

The dashboard framework already has this shape. Filters are state, HTMX
requests are actions, rendered components are observations. The lazy-loading
pattern (`hx-trigger="load, filtersChanged"`) is a loop driver. HTTP's
request-response discipline naturally enforces the separation that the agent
loop needs explicitly.

### Reset and Episode Boundaries

The Gymnasium has `env.reset()`. Varro's closest equivalent is creating a new
chat — which creates a new shell, fresh namespace, CWD at `/`. But there's no
explicit `reset()` method. Making this explicit would clarify the episode
boundary: what state carries over between conversations and what doesn't.

---

## Summary

The observation-action loop was always there — pydantic-ai's `agent.iter()`
runs it internally. What changed is making the environment side explicit. The
`Environment` class is the Gymnasium `env`. Its methods are `step` functions.
`StepResult` is the observation. Tool functions are adapters between the
agent framework and the environment interface.

The principle throughout: the agent submits values (tool calls), the environment
returns values (StepResult), and mutable state is internal to the environment.
Streaming, persistence, and rendering are wrappers around the loop, not
entangled with it. Simple, not easy.
