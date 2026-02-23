import pandas as pd

from varro.data.disk_to_db.create_db_table import make_dimension_plan
from varro.data.disk_to_db.process_tables import process_dim_table


def test_process_dim_table_derives_parent_kode_for_int_codes():
    df = pd.DataFrame(
        {
            "SEKVENS": [1, 2, 3, 4, 5],
            "KODE": [84, 1, 101, 147, 2],
            "NIVEAU": [1, 2, 3, 3, 2],
            "TITEL": [
                "Region Hovedstaden",
                "Landsdel Byen København",
                "København",
                "Frederiksberg",
                "Landsdel Københavns omegn",
            ],
        }
    )

    result = process_dim_table(df)

    assert list(result.columns) == ["kode", "niveau", "titel", "parent_kode"]
    parents = result["parent_kode"].tolist()
    assert pd.isna(parents[0])
    assert parents[1:] == [84, 1, 1, 84]


def test_process_dim_table_derives_parent_kode_for_string_codes():
    df = pd.DataFrame(
        {
            "SEKVENS": [1, 2, 3, 4],
            "KODE": ["A", "01", "01.1", "01.11"],
            "NIVEAU": [1, 2, 3, 4],
            "TITEL": ["A", "01", "01.1", "01.11"],
        }
    )

    result = process_dim_table(df)

    assert result["kode"].tolist() == ["A", "01", "01.1", "01.11"]
    assert result["parent_kode"].tolist() == [None, "A", "01", "01.1"]


def test_make_dimension_plan_includes_parent_kode_and_no_comments():
    df = pd.DataFrame(
        {
            "kode": [84, 1, 101],
            "niveau": [1, 2, 3],
            "titel": ["Region", "Landsdel", "Kommune"],
            "parent_kode": pd.Series([pd.NA, 84, 1], dtype="Int64"),
        }
    )

    plan = make_dimension_plan(df, "nuts")

    assert '"parent_kode" smallint' in plan.create_sql
    assert "COMMENT ON TABLE" not in plan.post_sql
    assert "COMMENT ON COLUMN" not in plan.post_sql
    assert len(plan.post_statements) == 2
