from datetime import datetime
import json
import pandas as pd
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from pydantic_ai import (
    Agent,
    RunContext,
    WebSearchTool,
    WebSearchUserLocation,
    ModelRetry,
)
from pydantic_ai.messages import ToolReturn
from pydantic_ai.models.anthropic import AnthropicModel, AnthropicModelSettings
from varro.data.utils import df_preview
from varro.context.utils import fuzzy_match
from varro.agent.utils import show_element
from varro.agent.utils import get_dim_tables
from varro.agent.filesystem import read_file, write_file, edit_file
from varro.db.db import engine
from varro.config import COLUMN_VALUES_DIR
from varro.db import crud
from varro.context.tools import generate_hierarchy
from sqlalchemy import text
from varro.chat.session import UserSession
from varro.agent.bash import run_bash_command
import logfire

logfire.configure(scrubbing=False)
logfire.instrument_pydantic_ai()

DIM_TABLES = get_dim_tables()

sonnet_model = AnthropicModel("claude-sonnet-4-5")
sonnet_settings = AnthropicModelSettings(
    anthropic_thinking={"type": "enabled", "budget_tokens": 3000},
    parallel_tool_calls=True,
)


agent = Agent(
    model=sonnet_model,
    model_settings=sonnet_settings,
    deps_type=UserSession,
    builtin_tools=[
        # MemoryTool(),
        WebSearchTool(
            search_context_size="medium",
            user_location=WebSearchUserLocation(
                city="Copenhagen",
                country="DK",
                region="DK",
                timezone="Europe/Copenhagen",
            ),
            blocked_domains=None,
            allowed_domains=None,
            max_uses=None,
        ),
    ],
)


@agent.instructions
async def get_system_prompt(ctx: RunContext[UserSession]) -> str:
    prompts = ctx.deps.cached_prompts
    if not prompts:
        prompts = get_prompts(prompts)
        ctx.deps.cached_prompts = prompts

    return crud.prompt.render_prompt(name="rigsstatistiker", **prompts)


def get_prompts(prompts):
    prompts["CURRENT_DATE"] = datetime.now().strftime("%Y-%m-%d")
    prompts["SUBJECT_HIERARCHY"] = generate_hierarchy()
    return prompts


@agent.tool_plain(docstring_format="google")
def ColumnValues(
    table: str, column: str, fuzzy_match_str: str | None = None, n: int | None = 5
):
    """
    View the unique values for a column in a dimension or fact table. If fuzzy_match_str is provided then the unique values are fuzzy matched against the fuzzy_match_str and the n best matches are returned. If no fuzzy_match_str is provided then the first n unique values are returned.

    Args:
        table: The name of the table.
        column: The name of the column.
        fuzzy_match_str: A string to fuzzy match against the unique values.
        n: The maximum number of unique values to return.
    """
    table = table.strip().lower().replace("fact.", "").replace("dim.", "")
    if table in DIM_TABLES:
        df = pd.read_parquet(COLUMN_VALUES_DIR / f"{table}.parquet")
        name = f"df_{table}_titel"
        schema = "dim"
    else:
        df = pd.read_parquet(COLUMN_VALUES_DIR / f"{table}/{column}.parquet")
        name = f"df_{table}_{column}"
        schema = "fact"
    if fuzzy_match_str:
        return fuzzy_match(fuzzy_match_str, df=df, limit=n, schema=schema, name=name)
    else:
        return df_preview(df, max_rows=n, name=name)


@agent.tool(docstring_format="google")
def Sql(ctx: RunContext[UserSession], query: str, df_name: str | None = None):
    """
    Execute a SQL query against the PostgreSQL database containing the dimension and fact tables. If df_name is provided then the result is stored in the <session_store> with the name specified by df_name.

    Args:
        query: The SQL query to execute.
        df_name: The name of the dataframe containing the data from the query.
    """
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text(query), conn)
    except Exception as e:
        raise ModelRetry(str(e))
    if df_name:
        ctx.deps.shell.user_ns[df_name] = df
        max_rows = 20 if len(df) < 21 else 5
        return f"Stored as {df_name}\n{df_preview(df, max_rows=max_rows)}"
    else:
        return df_preview(df, max_rows=30)


@agent.tool(docstring_format="google")
async def Jupyter(ctx: RunContext[UserSession], code: str, show: list[str] = []):
    """
    Stateful Jupyter notebook environment. Each call executes as a new cell.
    All printed output in the notebook cell will be included in the response.

    To see figures and dataframes in the response then add the name of the figure or dataframe to the show list.

    The notebook has access to all dataframes added to it's name space by the sql_query tool. You can reference the dataframes by their name, df_name.

    The notebook is initialized by running the following code in the first cell.
    ```python
    import pandas as pd
    import numpy as np
    import plotly.express as px
    import plotly.graph_objects as go
    import matplotlib.pyplot as plt
    ```

    Args:
        code (str): The Python code to execute.
    """
    res = ctx.deps.shell.run_cell(code)
    if res.error_before_exec:
        raise ModelRetry(repr(res.error_before_exec))
    if res.error_in_exec:
        raise ModelRetry(repr(res.error_in_exec))

    if not show:
        return res.stdout

    elements_rendered = []
    for name in show:
        element = ctx.deps.shell.user_ns.get(name)
        rendered = await show_element(element)
        elements_rendered.append(rendered)

    return ToolReturn(return_value=res.stdout, content=elements_rendered)


@agent.tool(docstring_format="google")
def Read(
    ctx: RunContext[UserSession],
    file_path: str,
    offset: int | None = None,
    limit: int | None = None,
) -> str:
    """Reads a file from the sandboxed local filesystem rooted at `/`.

    Usage:
    - The file_path parameter must be an absolute path, not a relative path.
    - Paths are resolved from the sandbox root (`/`) within the current user's workspace.
    - By default, it reads up to 2000 lines starting from the beginning of the file
    - You can optionally specify a line offset and limit (especially handy for long files), but it's recommended to read the whole file by not providing these parameters
    - Any lines longer than 2000 characters will be truncated
    - Results are returned using cat -n format, with line numbers starting at 1
    - This tool allows Claude Code to read images (eg PNG, JPG, etc). When reading an image file the contents are presented visually as Claude Code is a multimodal LLM.
    - This tool can only read files, not directories. To read a directory, use an ls command via the Bash tool.
    - You can call multiple tools in a single response. It is always better to speculatively read multiple potentially useful files in parallel.
    - If you read a file that exists but has empty contents you will receive a system reminder warning in place of file contents.

    Args:
        file_path: The absolute path to the file to read
        offset: The line number to start reading from. Only provide if the file is too large to read at once
        limit: The number of lines to read. Only provide if the file is too large to read at once.
    """
    return read_file(file_path, offset=offset, limit=limit, user_id=ctx.deps.user_id)


@agent.tool(docstring_format="google")
def Write(ctx: RunContext[UserSession], file_path: str, content: str) -> str:
    """Writes a file to the sandboxed local filesystem rooted at `/`.

    Usage:
    - Paths are resolved from the sandbox root (`/`) within the current user's workspace.
    - This tool will overwrite the existing file if there is one at the provided path.
    - If this is an existing file, you MUST use the Read tool first to read the file's contents. This tool will fail if you did not read the file first.
    - ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
    - NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.
    - Only use emojis if the user explicitly requests it. Avoid writing emojis to files unless asked.

    Args:
        file_path: The absolute path to the file to write (must be absolute, not relative)
        content: The content to write to the file
    """
    return write_file(file_path, content, user_id=ctx.deps.user_id)


@agent.tool(docstring_format="google")
def Edit(
    ctx: RunContext[UserSession],
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> str:
    """Performs exact string replacements in files.

    Usage:
    - Paths are resolved from the sandbox root (`/`) within the current user's workspace.
    - You must use your `Read` tool at least once in the conversation before editing. This tool will error if you attempt an edit without reading the file.
    - When editing text from Read tool output, ensure you preserve the exact indentation (tabs/spaces) as it appears AFTER the line number prefix. The line number prefix format is: spaces + line number + tab. Everything after that tab is the actual file content to match. Never include any part of the line number prefix in the old_string or new_string.
    - ALWAYS prefer editing existing files in the codebase. NEVER write new files unless explicitly required.
    - Only use emojis if the user explicitly requests it. Avoid adding emojis to files unless asked.
    - The edit will FAIL if `old_string` is not unique in the file. Either provide a larger string with more surrounding context to make it unique or use `replace_all` to change every instance of `old_string`.
    - Use `replace_all` for replacing and renaming strings across the file. This parameter is useful if you want to rename a variable for instance.

    Args:
        file_path: The absolute path to the file to modify
        old_string: The text to replace
        new_string: The text to replace it with (must be different from old_string)
        replace_all: Replace all occurences of old_string (default false)
    """
    return edit_file(
        file_path,
        old_string=old_string,
        new_string=new_string,
        replace_all=replace_all,
        user_id=ctx.deps.user_id,
    )


@agent.tool(docstring_format="google")
def Bash(ctx: RunContext[UserSession], command: str, description: str | None = None):
    """Executes a given bash command. Working directory persists between commands; shell state (everything else) does not. The shell environment is initialized from the user working directory, which appears as root.

    IMPORTANT: This tool is for terminal operations like ls, grep, find, glop. DO NOT use it for file operations (reading, writing, editing) - use the specialized tools for this instead.

    Before executing the command, please follow these steps:
    1. Directory Verification:
    - If the command will create new directories or files, first use `ls` to verify the parent directory exists and is the correct location
    - For example, before running "mkdir foo/bar", first use `ls foo` to check that "foo" exists and is the intended parent directory
    2. Command Execution:
    - Always quote file paths that contain spaces with double quotes (e.g., cd "path with spaces/file.txt")
    - Examples of proper quoting:
        - cd "/Users/name/My Documents" (correct)
        - cd /Users/name/My Documents (incorrect - will fail)
    - After ensuring proper quoting, execute the command.
    - Capture the output of the command.

    Usage notes:
    - It is very helpful if you write a clear, concise description of what this command does. For simple commands, keep it brief (5-10 words). For complex commands (piped commands, obscure flags, or anything hard to understand at a glance), add enough context to clarify what it does.
    - If the output exceeds 30000 characters, output will be truncated before being returned to you.
    - Avoid using Bash with the `cat`, `head`, `tail`, `sed`, `awk`, or `echo` commands, unless explicitly instructed or when these commands are truly necessary for the task. Instead, always prefer using the dedicated tools for these commands:
    - Read files: Use Read (NOT cat/head/tail)
    - Edit files: Use Edit (NOT sed/awk)
    - Write files: Use Write (NOT echo >/cat <<EOF)
    - Communication: Output text directly (NOT echo/printf)
    - When issuing multiple commands:
    - If the commands are independent and can run in parallel, make multiple Bash tool calls in a single message.
    - If the commands depend on each other and must run sequentially, use a single Bash call with '&&' to chain them together. For instance, if one operation must complete before another starts (like mkdir before cp), run these operations sequentially instead.
    - Use ';' only when you need to run commands sequentially but don't care if earlier commands fail
    - DO NOT use newlines to separate commands (newlines are ok in quoted strings)
    - Try to maintain your current working directory throughout the session by using absolute paths and avoiding usage of `cd`. You may use `cd` if the User explicitly requests it.

    Args:
        command: The command to execute.
        description: Clear, concise description of what this command does in active voice. Never use words like complex or risk in the description - just describe what it does. For simple commands (git, npm, standard CLI tools), keep it brief (5-10 words). For commands that are harder to parse at a glance (piped commands, obscure flags, etc.), add enough context to clarify what it does.
    """
    cwd_rel = getattr(ctx.deps, "bash_cwd", "/")
    output, new_cwd = run_bash_command(ctx.deps.user_id, cwd_rel, command)
    ctx.deps.bash_cwd = new_cwd
    return output


@agent.tool(docstring_format="google")
def UpdateUrl(
    ctx: RunContext[UserSession],
    path: str | None = None,
    params: dict[str, str | bool | None] | None = None,
):
    """Build and apply a URL update for the content panel.

    Args:
        path: Optional absolute app path (for example `/dashboard/sales`). If omitted, uses current content URL.
        params: Query parameters to merge. `None` or empty values remove keys.
    """
    source = (path or getattr(ctx.deps, "current_url", "/") or "/").strip()
    if not source.startswith("/"):
        raise ModelRetry("path must start with '/'")

    parsed = urlsplit(source)
    if parsed.scheme or parsed.netloc:
        raise ModelRetry("path must be relative to this app")

    query: dict[str, str] = dict(parse_qsl(parsed.query, keep_blank_values=False))
    if params:
        for key, value in params.items():
            key = (key or "").strip()
            if not key:
                continue
            if value is None:
                query.pop(key, None)
                continue
            if isinstance(value, bool):
                query[key] = "true" if value else "false"
                continue
            text = str(value).strip()
            if text:
                query[key] = text
            else:
                query.pop(key, None)

    merged_query = urlencode(query)
    next_url = urlunsplit(("", "", parsed.path or "/", merged_query, ""))
    ctx.deps.current_url = next_url

    payload = {"url": next_url, "replace": False}
    return f"UPDATE_URL {json.dumps(payload, ensure_ascii=False)}"
