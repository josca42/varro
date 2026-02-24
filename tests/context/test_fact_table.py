import importlib


def test_get_value_mappings_keeps_alder_by_default(monkeypatch):
    fact_table = importlib.import_module("varro.context.fact_table")

    monkeypatch.setattr(
        fact_table,
        "get_column_dtypes",
        lambda table: {"alder": "text", "tid": "date"},
    )

    variables = {
        "alder": {
            "values": [
                {"id": "IALT", "text": "Alder i alt"},
                {"id": "0", "text": "0 years"},
            ]
        },
        "tid": {"values": [{"id": "2025K1", "text": "2025K1"}]},
    }

    mappings = fact_table.get_value_mappings(
        table="folk1a",
        dim_links={},
        variables=variables,
    )

    assert "alder" in mappings
    assert mappings["alder"][0] == {"id": "IALT", "text": "Alder i alt"}
    assert "tid" not in mappings


def test_format_fact_table_overview_compacts_long_value_lists():
    fact_table = importlib.import_module("varro.context.fact_table")

    values = [{"id": "IALT", "text": "Alder i alt"}]
    values.extend({"id": str(i), "text": f"{i} years"} for i in range(25))

    table_info = {
        "id": "folk1a",
        "description": "Population by age and time",
        "unit": "Antal",
        "columns": ["alder"],
        "dimensions": {"alder": {"values": values}},
    }

    overview = fact_table.format_fact_table_overview(table_info)

    assert "- alder: values [IALT=Alder i alt, 0=0 years, 1=1 years, 2=2 years, 3=3 years" in overview
    assert " ... " in overview
    assert "20=20 years, 21=21 years, 22=22 years, 23=23 years, 24=24 years" in overview


def test_get_fact_table_info_surfaces_alder_values_in_overview(monkeypatch):
    fact_table = importlib.import_module("varro.context.fact_table")

    monkeypatch.setattr(
        fact_table,
        "load_table_info",
        lambda table: {
            "id": "FOLK1A",
            "text": "folk1a",
            "description": "Population by region and age",
            "unit": "Antal",
            "variables": [
                {
                    "id": "ALDER",
                    "values": [
                        {"id": "IALT", "text": "Alder i alt"},
                        {"id": "0", "text": "0 years"},
                    ],
                },
                {
                    "id": "TID",
                    "values": [{"id": "2025K1", "text": "2025K1"}],
                },
            ],
        },
    )
    monkeypatch.setattr(fact_table, "load_dim_links", lambda table: {})
    monkeypatch.setattr(
        fact_table,
        "get_column_dtypes",
        lambda table, schema="fact": {"alder": "text", "tid": "date"},
    )
    monkeypatch.setattr(fact_table, "get_tid_range", lambda table: ("2008-01-01", "2025-07-01"))

    info, _ = fact_table.get_fact_table_info("folk1a")
    overview = fact_table.format_fact_table_overview(info)

    assert "- alder: values [IALT=Alder i alt, 0=0 years]" in overview


def test_get_join_expression_casts_dim_for_text_fact_column():
    fact_table = importlib.import_module("varro.context.fact_table")

    join_expression = fact_table.get_join_expression(
        column="overtraed",
        fact_dtype="character varying",
        dim_dtype="integer",
    )
    sql_join_expression = fact_table.get_join_expression(
        column="overtraed",
        fact_dtype="character varying",
        dim_dtype="integer",
        fact_alias="f",
        dim_alias="n",
    )

    assert join_expression == "overtraed=kode::text"
    assert sql_join_expression == "f.overtraed=n.kode::text"


def test_get_fact_table_info_includes_dim_join_and_level_1_values(monkeypatch):
    fact_table = importlib.import_module("varro.context.fact_table")

    monkeypatch.setattr(
        fact_table,
        "load_table_info",
        lambda table: {
            "id": "STRAF10",
            "text": "straf10",
            "description": "Anmeldte forbrydelser",
            "unit": "Antal",
            "variables": [
                {
                    "id": "OVERTRAED",
                    "values": [],
                },
                {
                    "id": "TID",
                    "values": [{"id": "2024", "text": "2024"}],
                },
            ],
        },
    )
    monkeypatch.setattr(
        fact_table,
        "load_dim_links",
        lambda table: {"overtraed": "overtraedtype"},
    )

    def _get_column_dtypes(table, schema="fact"):
        if schema == "fact":
            return {"overtraed": "character varying", "tid": "integer"}
        return {"kode": "integer", "niveau": "integer", "titel": "text", "parent_kode": "integer"}

    monkeypatch.setattr(fact_table, "get_column_dtypes", _get_column_dtypes)
    monkeypatch.setattr(fact_table, "get_value_mappings", lambda **kwargs: {})
    monkeypatch.setattr(fact_table, "get_tid_range", lambda table: ("1995", "2025"))
    monkeypatch.setattr(fact_table, "get_niveau_levels", lambda *args: [1, 2, 3])
    monkeypatch.setattr(
        fact_table,
        "get_level_1_values",
        lambda **kwargs: ["Straffelov", "Saerlov"],
    )

    info, _ = fact_table.get_fact_table_info("straf10")
    overview = fact_table.format_fact_table_overview(info)
    summary = fact_table.format_fact_table_info(info)

    assert info["dimensions"]["overtraed"]["join"] == "overtraed=kode::text"
    assert info["dimensions"]["overtraed"]["level_1_values"] == ["Straffelov", "Saerlov"]
    assert "join dim.overtraedtype on overtraed=kode::text; levels [1, 2, 3]; level-1 values [Straffelov, Saerlov]" in overview
    assert "overtraed (overtraedtype; lvl [1, 2, 3]; level-1 [Straffelov, Saerlov])" in summary
