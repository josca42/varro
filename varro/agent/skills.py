import frontmatter
from varro.agent.workspace import user_workspace_root


def build_available_skills_prompt(user_id: int) -> str:
    skills_dir = user_workspace_root(user_id) / "skills"
    if not skills_dir.exists():
        return "No skills available in /skills."

    skills: list[tuple[str, str, str]] = []
    for skill_file in skills_dir.rglob("SKILL.md"):
        if not skill_file.is_file():
            continue
        try:
            post = frontmatter.loads(skill_file.read_text(encoding="utf-8"))
            name = str(post.get("name", "")).strip()
            description = str(post.get("description", "")).strip()
        except Exception:
            continue
        if not name or not description:
            continue
        location = f"/skills/{skill_file.relative_to(skills_dir).as_posix()}"
        skills.append((location, name, description))

    if not skills:
        return "No skills available in /skills."

    skills.sort(key=lambda skill: skill[0])
    lines: list[str] = ["<available_skills>"]
    for location, name, description in skills:
        lines.extend(
            [
                "<skill>",
                f"<name>{name}</name>",
                f"<description>{description}</description>",
                f"<location>{location}</location>",
                "</skill>",
            ]
        )
    lines.append("</available_skills>")
    return "\n".join(lines)
