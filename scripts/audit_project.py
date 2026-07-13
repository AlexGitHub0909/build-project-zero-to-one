#!/usr/bin/env python3
"""Audit the stable governance files created by this skill."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "PLAN.md",
    "CHANGELOG.md",
    "docs/README.md",
    "docs/CODEX_DOC_ROUTER.md",
    "docs/DOCS_DICTIONARY.md",
    "docs/specs/product-spec.md",
    "docs/specs/business-flow-spec.md",
    "docs/specs/traceability-matrix.md",
    "docs/operations/testing-and-acceptance.md",
    "docs/operations/test-evidence-matrix.md",
    "docs/operations/release-runbook.md",
)

AGENT_HEADINGS = (
    "## Scope",
    "## Required context",
    "## Rules",
    "## Validation",
    "## Definition of done",
    "## Do not",
)

PLAN_HEADINGS = (
    "## Current status",
    "## Current task",
    "## Execution queue",
    "## Recent completions",
    "## Blockers and external actions",
    "## Validation baseline",
)

TEMPLATE_MARKER = re.compile(r"\{\{[A-Z_]+\}\}")
AGENT_PATH = re.compile(r"`([^`]*AGENTS\.md)`")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check required project governance files and scoped AGENTS.md routes."
    )
    parser.add_argument("project_root", help="Project directory to audit")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat missing standard headings as errors instead of warnings",
    )
    return parser.parse_args()


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"not UTF-8: {path}")
    except OSError as exc:
        errors.append(f"cannot read {path}: {exc}")
    return ""


def check_headings(
    relative: str,
    content: str,
    required: tuple[str, ...],
    strict: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    for heading in required:
        if heading not in content:
            message = f"{relative} is missing heading: {heading}"
            (errors if strict else warnings).append(message)


def main() -> int:
    args = parse_args()
    root = Path(args.project_root).expanduser().resolve()
    if not root.is_dir():
        print(f"error: project directory not found: {root}", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    contents: dict[str, str] = {}

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")
            continue
        content = read_text(path, errors)
        contents[relative] = content
        marker = TEMPLATE_MARKER.search(content)
        if marker:
            errors.append(f"unresolved template marker in {relative}: {marker.group(0)}")

    root_agents = contents.get("AGENTS.md", "")
    if root_agents:
        check_headings(
            "AGENTS.md",
            root_agents,
            AGENT_HEADINGS,
            args.strict,
            errors,
            warnings,
        )
        for raw_path in AGENT_PATH.findall(root_agents):
            if raw_path == "AGENTS.md" or "*" in raw_path or raw_path.startswith("../"):
                continue
            if "/" not in raw_path:
                continue
            if not (root / raw_path).is_file():
                errors.append(f"AGENTS.md routes to a missing scoped rule: {raw_path}")

    plan = contents.get("PLAN.md", "")
    if plan:
        check_headings(
            "PLAN.md",
            plan,
            PLAN_HEADINGS,
            args.strict,
            errors,
            warnings,
        )

    scoped_agents = sorted(
        path for path in root.rglob("AGENTS.md") if path != root / "AGENTS.md"
    )
    for path in scoped_agents:
        relative = path.relative_to(root).as_posix()
        content = read_text(path, errors)
        marker = TEMPLATE_MARKER.search(content)
        if marker:
            errors.append(f"unresolved template marker in {relative}: {marker.group(0)}")
        check_headings(
            relative,
            content,
            AGENT_HEADINGS,
            args.strict,
            errors,
            warnings,
        )
        if root_agents and relative not in root_agents:
            errors.append(f"root AGENTS.md does not route to scoped rule: {relative}")

    for message in warnings:
        print(f"warning: {message}")
    for message in errors:
        print(f"error: {message}")

    print(
        "summary: "
        f"{len(REQUIRED_FILES) - sum(1 for item in REQUIRED_FILES if item not in contents)} required files found, "
        f"{len(scoped_agents)} scoped AGENTS.md, "
        f"{len(warnings)} warnings, {len(errors)} errors"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
