import importlib


def test_create_subject_readme_includes_coverage_notes(monkeypatch):
    subjects = importlib.import_module("varro.context.subjects")

    monkeypatch.setattr(subjects.insp, "has_table", lambda table, schema="fact": True)
    monkeypatch.setattr(
        subjects,
        "get_short_dim_descrs_md",
        lambda dim_tables: "<table>overtraedtype</table>",
    )
    monkeypatch.setattr(
        subjects,
        "format_fact_table_info",
        lambda table_info: f"<table>{table_info['id']}</table>",
    )
    monkeypatch.setattr(
        subjects,
        "get_dim_level_1_values",
        lambda dim_table: ("Straffelov", "Faerdselslov", "Saerlov"),
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

    assert "<coverage notes>" in readme
    assert "overtraedtype: full level-1 [Straffelov, Faerdselslov, Saerlov]" in readme
    assert "straf10=[Straffelov, Saerlov]" in readme
    assert "straf40=[Straffelov, Faerdselslov, Saerlov]" in readme


def test_create_subject_readme_skips_coverage_notes_when_coverage_matches(monkeypatch):
    subjects = importlib.import_module("varro.context.subjects")

    monkeypatch.setattr(subjects.insp, "has_table", lambda table, schema="fact": True)
    monkeypatch.setattr(
        subjects,
        "get_short_dim_descrs_md",
        lambda dim_tables: "<table>overtraedtype</table>",
    )
    monkeypatch.setattr(
        subjects,
        "format_fact_table_info",
        lambda table_info: f"<table>{table_info['id']}</table>",
    )
    monkeypatch.setattr(
        subjects,
        "get_dim_level_1_values",
        lambda dim_table: ("Straffelov", "Saerlov"),
    )

    table_info = {
        "dimensions": {
            "overtraed": {
                "dimension_table": "overtraedtype",
                "level_1_values": ["Straffelov", "Saerlov"],
            }
        },
    }
    monkeypatch.setattr(
        subjects,
        "get_fact_table_info",
        lambda table: ({**table_info, "id": table}, ["overtraedtype"]),
    )

    readme = subjects.create_subject_readme(["straf10", "straf20"])

    assert "<coverage notes>" not in readme


def test_create_subject_readme_adds_coverage_notes_for_shared_subset(monkeypatch):
    subjects = importlib.import_module("varro.context.subjects")

    monkeypatch.setattr(subjects.insp, "has_table", lambda table, schema="fact": True)
    monkeypatch.setattr(
        subjects,
        "get_short_dim_descrs_md",
        lambda dim_tables: "<table>overtraedtype</table>",
    )
    monkeypatch.setattr(
        subjects,
        "format_fact_table_info",
        lambda table_info: f"<table>{table_info['id']}</table>",
    )
    monkeypatch.setattr(
        subjects,
        "get_dim_level_1_values",
        lambda dim_table: ("Straffelov", "Faerdselslov", "Saerlov"),
    )

    table_info = {
        "dimensions": {
            "overtraed": {
                "dimension_table": "overtraedtype",
                "level_1_values": ["Straffelov", "Saerlov"],
            }
        },
    }
    monkeypatch.setattr(
        subjects,
        "get_fact_table_info",
        lambda table: ({**table_info, "id": table}, ["overtraedtype"]),
    )

    readme = subjects.create_subject_readme(["straf10", "straf20"])

    assert "<coverage notes>" in readme
    assert "full level-1 [Straffelov, Faerdselslov, Saerlov]" in readme
    assert "straf10, straf20=[Straffelov, Saerlov]" in readme
