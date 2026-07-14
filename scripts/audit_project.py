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
    "docs/specs/behavior-and-flow-spec.md",
    "docs/specs/traceability-matrix.md",
    "docs/operations/testing-and-acceptance.md",
    "docs/operations/test-evidence-matrix.md",
    "docs/operations/release-runbook.md",
)

LEGACY_EQUIVALENTS = {
    "docs/specs/behavior-and-flow-spec.md": (
        "docs/specs/business-flow-spec.md",
    ),
}

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

UNFINISHED_TEXT = {
    "README.md": (
        (
            "Describe the product, who it is for, and the problem it solves in plain language.",
            "project purpose",
        ),
        (
            "Document the main applications, services, packages, documentation, "
            "and operations directories after the initial structure is known.",
            "repository map",
        ),
        (
            "List the supported runtime versions, required services, environment "
            "file setup, install command, migration or seed command, and start command.",
            "local setup",
        ),
        (
            "Link to `docs/operations/testing-and-acceptance.md` and list the shortest "
            "checks a contributor should run before committing.",
            "validation commands",
        ),
    ),
    "AGENTS.md": (
        (
            "Describe the project purpose, current stage, actors, main workflow, "
            "and hard capability boundaries.",
            "project purpose and boundaries",
        ),
    ),
    "PLAN.md": (
        ("- Readiness: not assessed", "readiness"),
        ("- Branch and revision: record after checking Git", "Git revision"),
        (
            "Recover or establish the smallest trustworthy baseline for the project.",
            "current goal",
        ),
        ("List work that is explicitly outside the current task.", "non-goals"),
        (
            "Record product sources, repository state, working behavior, failures, "
            "tests, and unknowns.",
            "current evidence",
        ),
        (
            "Describe the next implementation slice and its dependencies after the "
            "evidence review.",
            "implementation approach",
        ),
        (
            "Record security, data, external-write, production, migration, cost, "
            "and permission boundaries.",
            "risks and boundaries",
        ),
        (
            "List the commands, tests, reviews, or manual records required before "
            "this task can close.",
            "acceptance evidence",
        ),
        ("State when to revert, stop, or request a decision.", "stop conditions"),
        (
            "- Establish current facts and the active slice.",
            "current execution queue",
        ),
    ),
    "docs/specs/product-spec.md": (
        ("- Approval owner: name the person or role", "approval owner"),
        (
            "Describe the actor or system, the problem, and the desired outcome "
            "without implementation detail.",
            "product purpose",
        ),
        (
            "Document rules, calculations, state invariants, time windows, ownership, "
            "and visibility in testable language.",
            "domain rules",
        ),
        (
            "Cover security, privacy, accessibility, performance, availability, "
            "audit, retention, and supported environments where they matter.",
            "non-functional requirements",
        ),
    ),
    "docs/operations/testing-and-acceptance.md": (
        (
            "Define the project test layers, supported environments, fixtures, "
            "and evidence rules.",
            "test strategy",
        ),
    ),
    "docs/operations/release-runbook.md": (
        (
            "List Git, artifact, environment, backup, migration, permission, capacity, "
            "and dependency checks.",
            "release preflight",
        ),
        (
            "List exact commands or operator actions after the environment is known.",
            "release procedure",
        ),
        (
            "Check the deployed revision, health, changed APIs or pages, stateful "
            "behavior, background work, logs, and user-visible paths affected by "
            "the release.",
            "post-release verification",
        ),
        (
            "List technical blockers, failed health or migration checks, missing "
            "backups, uncertain revision, and owner `NO_GO` conditions.",
            "release stop conditions",
        ),
        (
            "Record timestamps, revision, commands, results, manual checks, unresolved "
            "risks, and the rollback target used for this release.",
            "release evidence",
        ),
    ),
}

REQUIRED_TABLE_ROWS = {
    "AGENTS.md": (("## Work area routing", "work-area routing"),),
    "PLAN.md": (
        ("## Applicable work areas", "work-area decisions"),
        ("## Validation baseline", "validation baseline"),
    ),
    "docs/specs/product-spec.md": (("## Capabilities", "capabilities"),),
    "docs/specs/behavior-and-flow-spec.md": (("## Flow index", "flow index"),),
    "docs/specs/traceability-matrix.md": (("# Traceability matrix", "traceability"),),
    "docs/operations/testing-and-acceptance.md": (("## Commands", "validation commands"),),
    "docs/operations/test-evidence-matrix.md": (("# Test evidence matrix", "test evidence"),),
    "docs/operations/release-runbook.md": (
        ("## Environments", "environment ownership"),
        ("## Backup and rollback", "backup or rollback decisions"),
    ),
}

SCOPED_STARTER_TEXT = (
    (
        "List the confirmed website, frontend, backend, API, database, operations, "
        "or project-specific work areas served by this directory.",
        "work areas",
    ),
    (
        "Describe what this directory owns and what belongs elsewhere.",
        "responsibility",
    ),
    (
        "List the product, architecture, interface, API, data, security, test, or "
        "release documents required for work in this directory.",
        "required context",
    ),
    (
        "Document the established framework patterns, components, services, helpers, "
        "and dependencies to reuse.",
        "structure and reuse",
    ),
    (
        "Record directory-specific security, data, permission, visibility, performance, "
        "accessibility, and external-integration rules.",
        "local boundaries",
    ),
    (
        "List exact commands and any manual checks required for this directory.",
        "validation commands",
    ),
    (
        "Define the local completion conditions that supplement the root rules.",
        "definition of done",
    ),
    (
        "List concrete bad patterns, forbidden operations, and common mistakes for "
        "this directory.",
        "prohibited actions",
    ),
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
        help="Treat missing headings and unfinished starter content as errors",
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


def add_completion_finding(
    message: str,
    strict: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    (errors if strict else warnings).append(message)


def section_text(content: str, heading: str) -> str:
    start = content.find(heading)
    if start == -1:
        return ""
    body = content[start + len(heading) :]
    next_heading = re.search(r"^#{1,2} ", body, flags=re.MULTILINE)
    return body[: next_heading.start()] if next_heading else body


def table_has_data_row(content: str, heading: str) -> bool:
    table_lines = [
        line.strip()
        for line in section_text(content, heading).splitlines()
        if line.strip().startswith("|") and line.strip().endswith("|")
    ]
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if any(cells):
            return True
    return False


def check_completion(
    relative: str,
    content: str,
    strict: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    unfinished_labels = [
        label
        for starter_text, label in UNFINISHED_TEXT.get(relative, ())
        if starter_text in content
    ]
    if unfinished_labels:
        add_completion_finding(
            f"{relative} still has starter text for: {', '.join(unfinished_labels)}",
            strict,
            errors,
            warnings,
        )
    for heading, label in REQUIRED_TABLE_ROWS.get(relative, ()):
        if heading in content and not table_has_data_row(content, heading):
            add_completion_finding(
                f"{relative} has no project row for {label}",
                strict,
                errors,
                warnings,
            )


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
        candidates = (relative, *LEGACY_EQUIVALENTS.get(relative, ()))
        selected = next(
            (candidate for candidate in candidates if (root / candidate).is_file()),
            None,
        )
        if selected is None:
            errors.append(f"missing required file: {relative}")
            continue
        if selected != relative:
            warnings.append(
                f"legacy path accepted: {selected}; prefer {relative} for new projects"
            )
        path = root / selected
        content = read_text(path, errors)
        contents[relative] = content
        marker = TEMPLATE_MARKER.search(content)
        if marker:
            errors.append(f"unresolved template marker in {selected}: {marker.group(0)}")
        check_completion(
            relative,
            content,
            args.strict,
            errors,
            warnings,
        )

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
        unfinished_labels = [
            label
            for starter_text, label in SCOPED_STARTER_TEXT
            if starter_text in content
        ]
        if unfinished_labels:
            add_completion_finding(
                f"{relative} still has starter text for: {', '.join(unfinished_labels)}",
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

    found_count = len(REQUIRED_FILES) - sum(
        1 for item in REQUIRED_FILES if item not in contents
    )
    print(
        "summary: "
        f"{found_count} required files found, "
        f"{len(scoped_agents)} scoped AGENTS.md, "
        f"{len(warnings)} warnings, {len(errors)} errors"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
