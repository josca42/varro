from __future__ import annotations

import asyncio
import importlib
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.fixture
def skills_module():
    return importlib.import_module("varro.agent.skills")


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


def test_build_available_skills_prompt_recursively_loads_and_sorts(
    skills_module, monkeypatch, tmp_path: Path
) -> None:
    workspace = tmp_path / "workspace"
    (workspace / "skills" / "zeta" / "nested").mkdir(parents=True)
    (workspace / "skills" / "alpha").mkdir(parents=True)

    (workspace / "skills" / "zeta" / "nested" / "SKILL.md").write_text(
        """---
name: "Zeta Skill"
description: 'Build zeta outputs'
---
# Zeta
""",
        encoding="utf-8",
    )
    (workspace / "skills" / "alpha" / "SKILL.md").write_text(
        """---
name: Alpha Skill
description: Build alpha outputs
---
# Alpha
""",
        encoding="utf-8",
    )

    monkeypatch.setattr(skills_module, "user_workspace_root", lambda user_id: workspace)

    output = skills_module.build_available_skills_prompt(user_id=1)

    assert output == "\n".join(
        [
            "<available_skills>",
            "<skill>",
            "<name>Alpha Skill</name>",
            "<description>Build alpha outputs</description>",
            "<location>/skills/alpha/SKILL.md</location>",
            "</skill>",
            "<skill>",
            "<name>Zeta Skill</name>",
            "<description>Build zeta outputs</description>",
            "<location>/skills/zeta/nested/SKILL.md</location>",
            "</skill>",
            "</available_skills>",
        ]
    )


def test_build_available_skills_prompt_skips_invalid_front_matter(
    skills_module, monkeypatch, tmp_path: Path
) -> None:
    workspace = tmp_path / "workspace"
    (workspace / "skills" / "valid").mkdir(parents=True)
    (workspace / "skills" / "missing-desc").mkdir(parents=True)
    (workspace / "skills" / "malformed").mkdir(parents=True)
    (workspace / "skills" / "no-frontmatter").mkdir(parents=True)

    (workspace / "skills" / "valid" / "SKILL.md").write_text(
        """---
name: Valid Skill
description: Works
---
# Valid
""",
        encoding="utf-8",
    )
    (workspace / "skills" / "missing-desc" / "SKILL.md").write_text(
        """---
name: Missing Desc
---
# Missing
""",
        encoding="utf-8",
    )
    (workspace / "skills" / "malformed" / "SKILL.md").write_text(
        """---
name: Broken
not-a-key-value
description: Broken
---
# Broken
""",
        encoding="utf-8",
    )
    (workspace / "skills" / "no-frontmatter" / "SKILL.md").write_text(
        "# No Front Matter\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(skills_module, "user_workspace_root", lambda user_id: workspace)

    output = skills_module.build_available_skills_prompt(user_id=1)

    assert output == "\n".join(
        [
            "<available_skills>",
            "<skill>",
            "<name>Valid Skill</name>",
            "<description>Works</description>",
            "<location>/skills/valid/SKILL.md</location>",
            "</skill>",
            "</available_skills>",
        ]
    )


def test_build_available_skills_prompt_fallback_when_none_found(
    skills_module, monkeypatch, tmp_path: Path
) -> None:
    workspace = tmp_path / "workspace"
    workspace.mkdir(parents=True)

    monkeypatch.setattr(skills_module, "user_workspace_root", lambda user_id: workspace)

    output = skills_module.build_available_skills_prompt(user_id=1)

    assert output == "No skills available in /skills."


def test_get_system_prompt_injects_available_skills(assistant_module, monkeypatch) -> None:
    captured: dict[str, str] = {}

    def fake_render_prompt(name: str, **variables):
        captured["name"] = name
        for key, value in variables.items():
            captured[key] = value
        return "rendered"

    monkeypatch.setattr(assistant_module.crud.prompt, "render_prompt", fake_render_prompt)
    monkeypatch.setattr(
        assistant_module,
        "build_available_skills_prompt",
        lambda user_id: "- name: Skill\n  description: Desc\n  location: /skills/x/SKILL.md",
    )
    monkeypatch.setattr(assistant_module, "get_static_prompts", lambda: {"SUBJECT_HIERARCHY": "x"})

    ctx = SimpleNamespace(deps=SimpleNamespace(user_id=7))
    result = asyncio.run(assistant_module.get_system_prompt(ctx))

    assert result == "rendered"
    assert captured["name"] == "rigsstatistiker"
    assert captured["AVAILABLE_SKILLS"] == "- name: Skill\n  description: Desc\n  location: /skills/x/SKILL.md"
    assert captured["SUBJECT_HIERARCHY"] == "x"
    assert "CURRENT_DATE" in captured
