from __future__ import annotations

import importlib.util
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
INIT_SCRIPT = REPO_ROOT / "scripts" / "init_project.py"
AUDIT_SCRIPT = REPO_ROOT / "scripts" / "audit_project.py"


def load_audit_module():
    spec = importlib.util.spec_from_file_location("audit_project", AUDIT_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load audit_project.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_audit_module()


def add_table_row(content: str, heading: str) -> str:
    section_start = content.index(heading) + len(heading)
    lines = content.splitlines(keepends=True)
    offset = 0
    for index, line in enumerate(lines):
        offset += len(line)
        if offset <= section_start:
            continue
        if re.fullmatch(r"\|(?:\s*:?-+:?\s*\|)+\s*\n?", line):
            column_count = len(line.strip().strip("|").split("|"))
            row = "| " + " | ".join(["Confirmed", *(["Recorded"] * (column_count - 1))]) + " |\n"
            lines.insert(index + 1, row)
            return "".join(lines)
    raise AssertionError(f"table separator not found after {heading}")


class ProjectScriptTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project = Path(self.temp_dir.name) / "sample"
        result = subprocess.run(
            [
                sys.executable,
                str(INIT_SCRIPT),
                str(self.project),
                "--name",
                "Sample Project",
                "--mode",
                "greenfield",
                "--scoped",
                "apps/web",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def run_audit(self, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(AUDIT_SCRIPT), str(self.project), *extra],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_initializer_preserves_existing_files(self) -> None:
        readme = self.project / "README.md"
        readme.write_text("# Existing project\n", encoding="utf-8")
        result = subprocess.run(
            [
                sys.executable,
                str(INIT_SCRIPT),
                str(self.project),
                "--name",
                "Different name",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(readme.read_text(encoding="utf-8"), "# Existing project\n")

    def test_initializer_includes_capability_decision_points(self) -> None:
        plan = (self.project / "PLAN.md").read_text(encoding="utf-8")
        agents = (self.project / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("## Capability decisions", plan)
        self.assertIn("## Capability and tool routing", agents)

    def test_initializer_includes_lean_project_controls(self) -> None:
        plan = (self.project / "PLAN.md").read_text(encoding="utf-8")
        product_spec = (
            self.project / "docs/specs/product-spec.md"
        ).read_text(encoding="utf-8")

        self.assertIn("- Acceptance owner:", plan)
        self.assertIn("- Next checkpoint:", plan)
        self.assertIn("### Expected outcome or value signal", plan)
        self.assertIn("| Risk or uncertainty |", plan)
        self.assertIn("how the approval owner will recognize value", product_spec)

    def test_initializer_rejects_scoped_symlink_escape(self) -> None:
        outside = Path(self.temp_dir.name) / "outside"
        outside.mkdir()
        (self.project / "linked").symlink_to(outside, target_is_directory=True)
        result = subprocess.run(
            [
                sys.executable,
                str(INIT_SCRIPT),
                str(self.project),
                "--name",
                "Sample Project",
                "--scoped",
                "linked/module",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("target leaves project directory", result.stderr)
        self.assertFalse((outside / "module/AGENTS.md").exists())

    def test_fresh_scaffold_warns_and_fails_strict_audit(self) -> None:
        normal = self.run_audit()
        self.assertEqual(normal.returncode, 0, normal.stdout)
        self.assertIn("17 warnings, 0 errors", normal.stdout)
        self.assertIn("apps/web/AGENTS.md still has starter text", normal.stdout)

        strict = self.run_audit("--strict")
        self.assertEqual(strict.returncode, 1, strict.stdout)
        self.assertIn("0 warnings, 17 errors", strict.stdout)

    def test_completed_standard_layout_passes_strict_audit(self) -> None:
        for relative, entries in AUDIT.UNFINISHED_TEXT.items():
            path = self.project / relative
            content = path.read_text(encoding="utf-8")
            for starter_text, label in entries:
                content = content.replace(starter_text, f"Confirmed {label}.")
            path.write_text(content, encoding="utf-8")

        for relative, entries in AUDIT.REQUIRED_TABLE_ROWS.items():
            path = self.project / relative
            content = path.read_text(encoding="utf-8")
            for heading, _label in entries:
                content = add_table_row(content, heading)
            path.write_text(content, encoding="utf-8")

        scoped_path = self.project / "apps/web/AGENTS.md"
        scoped = scoped_path.read_text(encoding="utf-8")
        for starter_text, label in AUDIT.SCOPED_STARTER_TEXT:
            scoped = scoped.replace(starter_text, f"Confirmed {label}.")
        scoped_path.write_text(scoped, encoding="utf-8")

        strict = self.run_audit("--strict")
        self.assertEqual(strict.returncode, 0, strict.stdout)
        self.assertIn("0 warnings, 0 errors", strict.stdout)


if __name__ == "__main__":
    unittest.main()
