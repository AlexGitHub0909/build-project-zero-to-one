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
SKILL_FILE = REPO_ROOT / "SKILL.md"
README_FILES = (REPO_ROOT / "README.md", REPO_ROOT / "README.en.md")


def load_audit_module():
    spec = importlib.util.spec_from_file_location("audit_project", AUDIT_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load audit_project.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


AUDIT = load_audit_module()


def add_table_row(
    content: str,
    heading: str,
    cells: list[str] | None = None,
) -> str:
    section_start = content.index(heading) + len(heading)
    lines = content.splitlines(keepends=True)
    offset = 0
    for index, line in enumerate(lines):
        offset += len(line)
        if offset <= section_start:
            continue
        if re.fullmatch(r"\|(?:\s*:?-+:?\s*\|)+\s*\n?", line):
            column_count = len(line.strip().strip("|").split("|"))
            row_cells = cells or ["Confirmed", *(["Recorded"] * (column_count - 1))]
            if len(row_cells) != column_count:
                raise AssertionError(
                    f"{heading} needs {column_count} cells, got {len(row_cells)}"
                )
            row = "| " + " | ".join(row_cells) + " |\n"
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
                "--mode",
                "brownfield",
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
        self.assertIn("### Human decisions and review gates", plan)
        self.assertIn("## Capability and tool routing", agents)
        self.assertIn("## Human decisions and prototypes", agents)

    def test_initializer_profiles_and_prototype_are_on_demand(self) -> None:
        self.assertFalse(
            (self.project / "docs/operations/release-runbook.md").exists()
        )
        self.assertFalse((self.project / "docs/specs/prototype-review.md").exists())

        release_project = Path(self.temp_dir.name) / "release-sample"
        result = subprocess.run(
            [
                sys.executable,
                str(INIT_SCRIPT),
                str(release_project),
                "--name",
                "Release Sample",
                "--profile",
                "release",
                "--prototype",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(
            (release_project / "docs/operations/release-runbook.md").is_file()
        )
        self.assertTrue(
            (release_project / "docs/specs/prototype-review.md").is_file()
        )
        prototype_audit = subprocess.run(
            [
                sys.executable,
                str(AUDIT_SCRIPT),
                str(release_project),
                "--strict",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(prototype_audit.returncode, 1, prototype_audit.stdout)
        self.assertIn("prototype artifact", prototype_audit.stdout)

    def test_initializer_records_all_project_modes(self) -> None:
        for mode, recorded in (
            ("greenfield", "GREENFIELD"),
            ("brownfield", "BROWNFIELD"),
            ("spec-only", "SPEC_ONLY"),
        ):
            project = Path(self.temp_dir.name) / f"mode-{mode}"
            result = subprocess.run(
                [
                    sys.executable,
                    str(INIT_SCRIPT),
                    str(project),
                    "--name",
                    f"Mode {mode}",
                    "--mode",
                    mode,
                    "--profile",
                    "core",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            plan = (project / "PLAN.md").read_text(encoding="utf-8")
            self.assertIn(f"- Mode: `{recorded}`", plan)
            self.assertIn("- Governance profile: `CORE`", plan)

    def test_spec_only_creates_handoff_without_application_code(self) -> None:
        project = Path(self.temp_dir.name) / "spec-only-handoff"
        result = subprocess.run(
            [
                sys.executable,
                str(INIT_SCRIPT),
                str(project),
                "--name",
                "Specification Handoff",
                "--mode",
                "spec-only",
                "--profile",
                "delivery",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((project / "docs/specs/product-spec.md").is_file())
        self.assertTrue((project / "docs/specs/traceability-matrix.md").is_file())
        self.assertFalse((project / "src").exists())
        self.assertFalse((project / "app").exists())

    def test_initializer_uses_platform_neutral_document_router(self) -> None:
        self.assertTrue((self.project / "docs/DOC_ROUTER.md").is_file())
        self.assertFalse((self.project / "docs/CODEX_DOC_ROUTER.md").exists())
        docs_readme = (self.project / "docs/README.md").read_text(encoding="utf-8")
        self.assertIn("`DOC_ROUTER.md`", docs_readme)

    def test_audit_accepts_legacy_codex_router(self) -> None:
        current = self.project / "docs/DOC_ROUTER.md"
        legacy = self.project / "docs/CODEX_DOC_ROUTER.md"
        current.rename(legacy)

        result = self.run_audit()

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("legacy path accepted: docs/CODEX_DOC_ROUTER.md", result.stdout)

    def test_audit_infers_profile_for_projects_created_by_older_versions(self) -> None:
        plan_path = self.project / "PLAN.md"
        plan = plan_path.read_text(encoding="utf-8").replace(
            "- Governance profile: `DELIVERY`\n",
            "",
        )
        plan_path.write_text(plan, encoding="utf-8")

        result = self.run_audit()

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn(
            "PLAN.md has no governance profile; inferred DELIVERY",
            result.stdout,
        )
        self.assertIn("summary: profile DELIVERY", result.stdout)

    def test_skill_trigger_is_platform_neutral(self) -> None:
        content = SKILL_FILE.read_text(encoding="utf-8")
        self.assertIn("Use when an AI coding agent must", content)
        self.assertNotIn("Use when Codex must", content)

    def test_readmes_cover_supported_agent_platforms(self) -> None:
        platforms = (
            "Codex",
            "Claude Code",
            "GitHub Copilot",
            "Cursor",
            "Gemini CLI",
            "OpenCode",
            "TRAE",
        )
        for readme in README_FILES:
            content = readme.read_text(encoding="utf-8")
            for platform in platforms:
                self.assertIn(platform, content, f"{platform} missing from {readme.name}")
            self.assertNotIn("待平台端到端验证", content)
            self.assertNotIn("platform end-to-end validation pending", content)
            self.assertNotIn("Compatible agents: 7", content)

    def test_readmes_present_direct_download_before_git(self) -> None:
        archive_url = (
            "https://github.com/AlexGitHub0909/SpecToDelivery/"
            "archive/refs/heads/main.zip"
        )
        for readme in README_FILES:
            content = readme.read_text(encoding="utf-8")
            self.assertIn(archive_url, content)
            self.assertIn("git clone", content)
            self.assertLess(content.index(archive_url), content.index("git clone"))

    def test_readmes_explain_human_review_and_prototypes(self) -> None:
        chinese = README_FILES[0].read_text(encoding="utf-8")
        english = README_FILES[1].read_text(encoding="utf-8")
        self.assertIn("## 人与 Agent 的分工", chinese)
        self.assertIn("### 什么时候先做原型", chinese)
        self.assertIn("## Human and agent responsibilities", english)
        self.assertIn("### When to prototype first", english)
        for content in (chinese, english):
            self.assertIn("--profile delivery", content)
            self.assertIn("--prototype", content)

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
        self.assertIn("profile DELIVERY", normal.stdout)
        self.assertIn("15 warnings, 0 errors", normal.stdout)
        self.assertIn("apps/web/AGENTS.md still has starter text", normal.stdout)

        strict = self.run_audit("--strict")
        self.assertEqual(strict.returncode, 1, strict.stdout)
        self.assertIn("0 warnings, 15 errors", strict.stdout)

    def test_completed_standard_layout_passes_strict_audit(self) -> None:
        plan_path = self.project / "PLAN.md"
        plan = plan_path.read_text(encoding="utf-8")
        plan = plan.replace("- Readiness: not assessed", "- Readiness: VERIFIED_LOCAL")
        plan = plan.replace(
            "- Branch and revision: record after checking Git",
            "- Branch and revision: main@fixture",
        )
        plan = plan.replace(
            "- Acceptance owner: name the person or role",
            "- Acceptance owner: Product owner",
        )
        plan = plan.replace(
            "- Next checkpoint: date, event, decision, or not required",
            "- Next checkpoint: not required",
        )
        plan_path.write_text(plan, encoding="utf-8")

        product_path = self.project / "docs/specs/product-spec.md"
        product = product_path.read_text(encoding="utf-8").replace(
            "- Approval owner: name the person or role",
            "- Approval owner: Product owner",
        )
        product_path.write_text(product, encoding="utf-8")

        for relative, entries in AUDIT.UNFINISHED_TEXT.items():
            path = self.project / relative
            if not path.exists():
                continue
            content = path.read_text(encoding="utf-8")
            for starter_text, label in entries:
                content = content.replace(starter_text, f"Confirmed {label}.")
            path.write_text(content, encoding="utf-8")

        table_rows = {
            "## Work area routing": [
                "CLI",
                "Command-line greeting",
                "`AGENTS.md`, product spec",
            ],
            "## Applicable work areas": [
                "CLI",
                "APPLIES",
                "Approved product brief",
                "`AGENTS.md`",
                "Product owner",
            ],
            "### Human decisions and review gates": [
                "CLI transcript",
                "No",
                "Product owner",
                "NOT_REQUIRED",
                "Approved examples fully define the interaction",
            ],
            "## Validation baseline": [
                "CLI unit test",
                "PASS",
                "fixture run",
                "`tests/test_greet.py`",
            ],
            "## Capabilities": [
                "REQ-CLI-001",
                "Personal greeting",
                "Print a greeting for a supplied name",
                "IMPLEMENTED",
                "`greet.py`, `tests/test_greet.py`",
            ],
            "## Flow index": [
                "FLOW-CLI-001",
                "Print greeting",
                "User",
                "Run command",
                "Greeting printed",
                "IMPLEMENTED",
            ],
            "# Traceability matrix": [
                "REQ-CLI-001",
                "Print a greeting",
                "FLOW-CLI-001",
                "CLI transcript",
                "NOT_APPLICABLE",
                "`greet.py`",
                "EV-CLI-001",
                "IMPLEMENTED",
                "None",
            ],
            "## Commands": [
                "CLI",
                "`python3 -m unittest discover -s tests -v`",
                "Greeting behavior",
                "Local Python 3",
            ],
            "# Test evidence matrix": [
                "EV-CLI-001",
                "REQ-CLI-001",
                "P0",
                "local",
                "automated",
                "`python3 -m unittest discover -s tests -v`",
                "Test passes",
                "PASS",
                "`tests/test_greet.py` current output",
                "Product owner",
            ],
        }
        for relative, entries in AUDIT.REQUIRED_TABLE_ROWS.items():
            path = self.project / relative
            if not path.exists():
                continue
            content = path.read_text(encoding="utf-8")
            for heading, _label in entries:
                content = add_table_row(content, heading, table_rows.get(heading))
            path.write_text(content, encoding="utf-8")

        scoped_path = self.project / "apps/web/AGENTS.md"
        scoped = scoped_path.read_text(encoding="utf-8")
        for starter_text, label in AUDIT.SCOPED_STARTER_TEXT:
            scoped = scoped.replace(starter_text, f"Confirmed {label}.")
        scoped_path.write_text(scoped, encoding="utf-8")

        (self.project / "product-brief.md").write_text(
            "# Greeting CLI\n\nAccept a name and print `Hello, <name>!`.\n",
            encoding="utf-8",
        )
        (self.project / "greet.py").write_text(
            "def greet(name: str) -> str:\n"
            "    return f\"Hello, {name}!\"\n",
            encoding="utf-8",
        )
        tests_dir = self.project / "tests"
        tests_dir.mkdir()
        (tests_dir / "test_greet.py").write_text(
            "import unittest\n\n"
            "from greet import greet\n\n\n"
            "class GreetingTests(unittest.TestCase):\n"
            "    def test_greeting(self):\n"
            "        self.assertEqual(greet(\"Alex\"), \"Hello, Alex!\")\n\n\n"
            "if __name__ == \"__main__\":\n"
            "    unittest.main()\n",
            encoding="utf-8",
        )

        app_test = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
            cwd=self.project,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(app_test.returncode, 0, app_test.stdout + app_test.stderr)

        strict = self.run_audit("--strict")
        self.assertEqual(strict.returncode, 0, strict.stdout)
        self.assertIn("0 warnings, 0 errors", strict.stdout)

        trace_path = self.project / "docs/specs/traceability-matrix.md"
        trace = trace_path.read_text(encoding="utf-8").replace(
            "| IMPLEMENTED | None |",
            "| CONFIRMED | None |",
        )
        trace_path.write_text(trace, encoding="utf-8")
        rejected = self.run_audit("--strict")
        self.assertEqual(rejected.returncode, 1, rejected.stdout)
        self.assertIn("unknown status: CONFIRMED", rejected.stdout)

        trace = trace_path.read_text(encoding="utf-8").replace(
            "| CONFIRMED | None |",
            "| IMPLEMENTED | None |",
        ).replace("EV-CLI-001", "EV-MISSING")
        trace_path.write_text(trace, encoding="utf-8")
        missing_evidence = self.run_audit("--strict")
        self.assertEqual(missing_evidence.returncode, 1, missing_evidence.stdout)
        self.assertIn("references missing evidence ID: EV-MISSING", missing_evidence.stdout)


if __name__ == "__main__":
    unittest.main()
