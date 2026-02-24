from __future__ import annotations

import importlib
import json

import pandas as pd
import pytest


@pytest.fixture
def assistant_module(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")

    import logfire

    monkeypatch.setattr(logfire, "configure", lambda **kwargs: None)
    monkeypatch.setattr(logfire, "instrument_pydantic_ai", lambda: None)

    utils = importlib.import_module("varro.agent.utils")
    monkeypatch.setattr(utils, "get_dim_tables", lambda: ("overtraedtype",))

    assistant = importlib.import_module("varro.agent.assistant")
    return importlib.reload(assistant)


def setup_column_values_files(tmp_path, assistant_module):
    column_values_dir = tmp_path / "column_values"
    links_dir = tmp_path / "dimension_links"
    column_values_dir.mkdir()
    links_dir.mkdir()

    dim_df = pd.DataFrame(
        {
            "kode": [1, 2, 3],
            "niveau": [1, 1, 1],
            "titel": ["Straffelov", "Faerdselslov", "Saerlov"],
            "parent_kode": [None, None, None],
        }
    )
    dim_df.to_parquet(column_values_dir / "overtraedtype.parquet")

    fact_dir = column_values_dir / "straf10"
    fact_dir.mkdir()
    pd.DataFrame(
        {"id": ["TOT", "1", "3"], "text": ["I alt", "Straffelov i alt", "Saerlov i alt"]}
    ).to_parquet(fact_dir / "overtraed.parquet")

    (links_dir / "STRAF10.json").write_text(
        json.dumps(
            [
                {
                    "column": "OVERTRAED",
                    "dimension": "overtraedtype",
                }
            ]
        )
    )

    assistant_module.COLUMN_VALUES_DIR = column_values_dir
    assistant_module.DIMENSION_LINKS_DIR = links_dir
    assistant_module.DIM_TABLES = ("overtraedtype",)


def setup_empty_links_files(tmp_path, assistant_module):
    column_values_dir = tmp_path / "column_values"
    links_dir = tmp_path / "dimension_links"
    column_values_dir.mkdir()
    links_dir.mkdir()

    dim_df = pd.DataFrame(
        {
            "kode": [1, 2, 3],
            "niveau": [1, 1, 1],
            "titel": ["Straffelov", "Faerdselslov", "Saerlov"],
            "parent_kode": [None, None, None],
        }
    )
    dim_df.to_parquet(column_values_dir / "overtraedtype.parquet")

    fact_dir = column_values_dir / "straf40"
    fact_dir.mkdir()
    pd.DataFrame(
        {"id": ["TOT", "1", "2", "3"], "text": ["I alt", "Straffelov", "Faerdselslov", "Saerlov"]}
    ).to_parquet(fact_dir / "overtraed.parquet")
    pd.DataFrame(
        {"id": ["TOT", "M", "K"], "text": ["I alt", "Maend", "Kvinder"]}
    ).to_parquet(fact_dir / "kon.parquet")

    (links_dir / "STRAF40.json").write_text("[]")

    assistant_module.COLUMN_VALUES_DIR = column_values_dir
    assistant_module.DIMENSION_LINKS_DIR = links_dir
    assistant_module.DIM_TABLES = ("overtraedtype",)


def test_column_values_filters_dim_values_by_for_table(assistant_module, tmp_path):
    setup_column_values_files(tmp_path, assistant_module)

    result = assistant_module.ColumnValues(
        table="overtraedtype",
        column="titel",
        for_table="straf10",
        n=10,
    )

    assert "Straffelov" in result
    assert "Saerlov" in result
    assert "Faerdselslov" not in result


def test_column_values_keeps_dim_universe_without_for_table(assistant_module, tmp_path):
    setup_column_values_files(tmp_path, assistant_module)

    result = assistant_module.ColumnValues(
        table="overtraedtype",
        column="titel",
        n=10,
    )

    assert "Straffelov" in result
    assert "Saerlov" in result
    assert "Faerdselslov" in result


def test_column_values_for_table_requires_dimension_link(assistant_module, tmp_path):
    setup_column_values_files(tmp_path, assistant_module)

    with pytest.raises(assistant_module.ModelRetry):
        assistant_module.ColumnValues(
            table="overtraedtype",
            column="titel",
            for_table="straf20",
        )


def test_column_values_fuzzy_match_with_for_table_filtered_index(assistant_module, tmp_path):
    setup_column_values_files(tmp_path, assistant_module)

    result = assistant_module.ColumnValues(
        table="overtraedtype",
        column="titel",
        fuzzy_match_str="straf",
        for_table="straf10",
        n=5,
    )

    assert "Straffelov" in result
    assert "Faerdselslov" not in result


def test_column_values_infers_fact_column_when_links_are_empty(assistant_module, tmp_path):
    setup_empty_links_files(tmp_path, assistant_module)

    result = assistant_module.ColumnValues(
        table="overtraedtype",
        column="titel",
        for_table="straf40",
        n=10,
    )

    assert "Straffelov" in result
    assert "Faerdselslov" in result
    assert "Saerlov" in result
