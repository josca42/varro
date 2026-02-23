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
