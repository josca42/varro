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


FILES = [
    "borgere/befolkning/befolkningstal.md",
    "kultur_og_fritid/kulturarv/arkiver.md",
    "miljø_og_energi/energiforbrug_og_energipriser/energiforbrug.md",
    "miljø_og_energi/grønt_nationalregnskab_/materiale-_og_affaldsregnskaber.md",
    "økonomi/offentlig_økonomi/regionernes_regnskaber_og_budgetter.md",
    "transport/godstransport/godstransport_med_tog.md",
]


def main():
    remaining = [SUBJECTS_DIR / f for f in FILES if not subject_has_notes(SUBJECTS_DIR / f)]

    print(f"{len(FILES)} files, {len(FILES) - len(remaining)} done, {len(remaining)} remaining")

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
