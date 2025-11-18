from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from typing import Any


class CrudPrompt:
    def __init__(self, prompt_dir: Path):
        self.prompt_dir = prompt_dir
        self.env = Environment(
            loader=FileSystemLoader(prompt_dir),
            auto_reload=False,
        )

    def render_markdown(self, name: str) -> str:
        """Load prompt he markdown file."""
        prompt_file = self.prompt_dir / f"{name}.md"
        return prompt_file.read_text(encoding="utf-8").strip()

    def render_prompt(self, name: str, **variables: Any) -> str:
        """Render a template with provided variables.

        Args:
            name: Name of the prompt template file without extension
            template_dir: Directory containing prompt templates
            **variables: Variables to pass to the prompt

        Returns:
            Rendered prompt text
        """
        template = self.env.get_template(f"{name}.j2")
        return template.render(**variables)


prompt = CrudPrompt(Path(__file__).parent.parent.parent / "prompts")
