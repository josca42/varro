import importlib


def test_create_subject_readme_fact_tables_only(monkeypatch):
    subjects = importlib.import_module("varro.context.subjects")

    monkeypatch.setattr(subjects.insp, "has_table", lambda table, schema="fact": True)
    monkeypatch.setattr(
        subjects,
        "format_fact_table_info",
        lambda table_info: f"<table>{table_info['id']}</table>",
    )

    table_infos = {
        "straf10": {
            "id": "straf10",
            "dimensions": {
                "overtraed": {
                    "dimension_table": "overtraedtype",
                    "level_1_values": ["Straffelov", "Saerlov"],
                }
            },
        },
        "straf40": {
            "id": "straf40",
            "dimensions": {
                "overtraed": {
                    "dimension_table": "overtraedtype",
                    "level_1_values": ["Straffelov", "Faerdselslov", "Saerlov"],
                }
            },
        },
    }
    monkeypatch.setattr(
        subjects,
        "get_fact_table_info",
        lambda table: (table_infos[table], ["overtraedtype"]),
    )

    readme = subjects.create_subject_readme(["straf10", "straf40"])

    assert "<fact tables>" in readme
    assert "</fact tables>" in readme
    assert "<table>straf10</table>" in readme
    assert "<table>straf40</table>" in readme
    assert "<dim tables>" not in readme
    assert "<coverage notes>" not in readme
