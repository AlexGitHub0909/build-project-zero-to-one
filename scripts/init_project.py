#!/usr/bin/env python3
"""Create missing project governance files without overwriting existing work."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path, PurePosixPath
import sys


SKILL_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "templates" / "project"

CORE_FILES = {
    "README.md": "README.md",
    "AGENTS.md": "root-AGENTS.md",
    "PLAN.md": "PLAN.md",
    "CHANGELOG.md": "CHANGELOG.md",
    "docs/README.md": "docs-README.md",
    "docs/CODEX_DOC_ROUTER.md": "CODEX_DOC_ROUTER.md",
    "docs/DOCS_DICTIONARY.md": "DOCS_DICTIONARY.md",
    "docs/specs/product-spec.md": "product-spec.md",
    "docs/specs/business-flow-spec.md": "business-flow-spec.md",
    "docs/specs/traceability-matrix.md": "traceability-matrix.md",
    "docs/operations/testing-and-acceptance.md": "testing-and-acceptance.md",
    "docs/operations/test-evidence-matrix.md": "test-evidence-matrix.md",
    "docs/operations/release-runbook.md": "release-runbook.md",
    "docs/architecture/decisions/0000-template.md": "ADR-template.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy missing zero-to-one governance templates into a project."
    )
    parser.add_argument("project_root", help="Target project directory")
    parser.add_argument("--name", required=True, help="Human-readable project name")
    parser.add_argument(
        "--mode",
        choices=("greenfield", "brownfield", "spec-only"),
        default="greenfield",
        help="Project mode recorded in generated files",
    )
    parser.add_argument(
        "--scoped",
        action="append",
        default=[],
        metavar="RELATIVE_DIR",
        help="Add a scoped AGENTS.md in this relative directory; repeat as needed",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without creating directories or files",
    )
    return parser.parse_args()


def safe_relative_dir(raw: str) -> Path:
    posix = PurePosixPath(raw.replace("\\", "/"))
    if posix.is_absolute() or not posix.parts or any(part in {"", ".", ".."} for part in posix.parts):
        raise ValueError(f"invalid scoped directory: {raw!r}")
    return Path(*posix.parts)


def render(template_name: str, values: dict[str, str]) -> str:
    source = TEMPLATE_ROOT / template_name
    if not source.is_file():
        raise FileNotFoundError(f"missing template: {source}")
    content = source.read_text(encoding="utf-8")
    for key, value in values.items():
        content = content.replace("{{" + key + "}}", value)
    return content


def write_missing(target: Path, content: str, dry_run: bool) -> str:
    if target.exists():
        return "skip"
    if dry_run:
        return "create"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    return "create"


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    try:
        scoped_dirs = [safe_relative_dir(raw) for raw in args.scoped]
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    scoped_rows = "\n".join(
        f"| `{scope.as_posix()}/**` | `{scope.as_posix()}/AGENTS.md` |"
        for scope in scoped_dirs
    )
    values = {
        "PROJECT_NAME": args.name.strip(),
        "MODE": args.mode.upper().replace("-", "_"),
        "DATE": date.today().isoformat(),
        "SCOPED_RULE_ROWS": scoped_rows or "| No scoped work area yet | Add a row when a scoped `AGENTS.md` is created |",
    }
    if not values["PROJECT_NAME"] or any(char in values["PROJECT_NAME"] for char in "\r\n"):
        print("error: --name must be a non-empty single line", file=sys.stderr)
        return 2

    actions: list[tuple[str, Path]] = []
    try:
        for relative, template_name in CORE_FILES.items():
            target = project_root / relative
            result = write_missing(target, render(template_name, values), args.dry_run)
            actions.append((result, target))

        for scope in scoped_dirs:
            target = project_root / scope / "AGENTS.md"
            scope_values = {**values, "SCOPED_PATH": scope.as_posix()}
            result = write_missing(
                target,
                render("scoped-AGENTS.md", scope_values),
                args.dry_run,
            )
            actions.append((result, target))
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    verb = "would create" if args.dry_run else "created"
    for action, target in actions:
        if action == "create":
            print(f"{verb}: {target}")
        else:
            print(f"kept existing: {target}")

    created = sum(1 for action, _ in actions if action == "create")
    skipped = len(actions) - created
    print(f"summary: {created} create, {skipped} existing")
    if scoped_dirs and (project_root / "AGENTS.md").exists() and not args.dry_run:
        root_rules = (project_root / "AGENTS.md").read_text(encoding="utf-8")
        missing_routes = [
            f"{scope.as_posix()}/AGENTS.md"
            for scope in scoped_dirs
            if f"{scope.as_posix()}/AGENTS.md" not in root_rules
        ]
        if missing_routes:
            print(
                "warning: existing AGENTS.md was preserved; add scoped routes for: "
                + ", ".join(missing_routes)
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
