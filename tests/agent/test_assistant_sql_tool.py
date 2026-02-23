from __future__ import annotations

import importlib
from types import SimpleNamespace

import pandas as pd
import pytest


class _DummyConn:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class _DummyEngine:
    def connect(self):
        return _DummyConn()


@pytest.fixture
def assistant_module(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    import logfire

    monkeypatch.setattr(logfire, "configure", lambda **kwargs: None)
    monkeypatch.setattr(logfire, "instrument_pydantic_ai", lambda: None)

    utils = importlib.import_module("varro.agent.utils")
    monkeypatch.setattr(utils, "get_dim_tables", lambda: ())

    assistant = importlib.import_module("varro.agent.assistant")
    return importlib.reload(assistant)


def test_sql_includes_row_count_dtypes_and_stores_dataframe(assistant_module, monkeypatch):
    df = pd.DataFrame({"x": [1, 2]})
    monkeypatch.setattr(assistant_module, "dst_read_engine", _DummyEngine())
    monkeypatch.setattr(assistant_module.pd, "read_sql", lambda query, conn: df)

    ctx = SimpleNamespace(deps=SimpleNamespace(shell=SimpleNamespace(user_ns={})))
    result = assistant_module.Sql(ctx, query="select 1 as x", df_name="df_x")

    assert result.return_value.startswith("Stored as df_x\nrow_count: 2\n")
    assert "dtypes: x=int64" in result.return_value
    assert "x\n1\n2\n" in result.return_value
    assert ctx.deps.shell.user_ns["df_x"].equals(df)
    assert result.metadata == {"ui": {"has_tool_content": False}}


def test_sql_dtypes_resolve_date_columns(assistant_module, monkeypatch):
    import datetime

    df = pd.DataFrame({"tid": [datetime.date(2024, 1, 1)], "val": [1.5]})
    monkeypatch.setattr(assistant_module, "dst_read_engine", _DummyEngine())
    monkeypatch.setattr(assistant_module.pd, "read_sql", lambda query, conn: df)

    ctx = SimpleNamespace(deps=SimpleNamespace(shell=SimpleNamespace(user_ns={})))
    result = assistant_module.Sql(ctx, query="select 1", df_name="df")

    assert "dtypes: tid=datetime64[ns], val=float64" in result.return_value
    assert pd.api.types.is_datetime64_any_dtype(ctx.deps.shell.user_ns["df"]["tid"])


def test_sql_skips_datetime_conversion_without_df_name(assistant_module, monkeypatch):
    import datetime

    df = pd.DataFrame({"tid": [datetime.date(2024, 1, 1)], "val": [1.5]})
    monkeypatch.setattr(assistant_module, "dst_read_engine", _DummyEngine())
    monkeypatch.setattr(assistant_module.pd, "read_sql", lambda query, conn: df)

    def fail_to_datetime(_):
        raise AssertionError("pd.to_datetime should not be called without df_name")

    monkeypatch.setattr(assistant_module.pd, "to_datetime", fail_to_datetime)

    ctx = SimpleNamespace(deps=SimpleNamespace(shell=SimpleNamespace(user_ns={})))
    result = assistant_module.Sql(ctx, query="select 1")

    assert "dtypes:" not in result.return_value


def test_sql_warns_when_query_returns_no_rows(assistant_module, monkeypatch):
    df = pd.DataFrame(columns=["x"])
    monkeypatch.setattr(assistant_module, "dst_read_engine", _DummyEngine())
    monkeypatch.setattr(assistant_module.pd, "read_sql", lambda query, conn: df)

    ctx = SimpleNamespace(deps=SimpleNamespace(shell=SimpleNamespace(user_ns={})))
    result = assistant_module.Sql(ctx, query="select 1 as x where false")

    assert result.return_value.startswith("Warning: query returned 0 rows.")
    assert "row_count: 0" in result.return_value
    assert "ColumnValues(table, column)" in result.return_value
    assert result.metadata == {"ui": {"has_tool_content": False}}
