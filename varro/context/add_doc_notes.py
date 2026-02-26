"""Run the audit-dim-joins skill on each subject file via claude CLI."""

import subprocess
from pathlib import Path
from varro.config import SUBJECTS_DIR
import time
NOTES_MARKER = "notes:"


def subject_has_notes(path: Path) -> bool:
    return NOTES_MARKER in path.read_text()


def all_subject_files() -> list[Path]:
    return sorted(SUBJECTS_DIR.rglob("*.md"))


def main():
    subjects = all_subject_files()
    done = [s for s in subjects if subject_has_notes(s)]
    remaining = [s for s in subjects if not subject_has_notes(s)]

    print(f"Subjects: {len(subjects)} total, {len(done)} done, {len(remaining)} remaining")

    for i, subject_file in enumerate(remaining):
        rel = subject_file.relative_to(SUBJECTS_DIR)
        print(f"\n[{i + 1}/{len(remaining)}] {rel}")

        prompt = f"/audit-dim-joins Review this subject file and add notes: {subject_file}"

        subprocess.run(
            [
                "claude",
                "-p", prompt,
                "--allowedTools",
                "Bash Read Write Grep Edit",
                "--permission-mode",
                "acceptEdits",
            ],
            check=True,
        )

        print(f"Done: {rel}")
        time.sleep(60*5)

if __name__ == "__main__":
    main()
