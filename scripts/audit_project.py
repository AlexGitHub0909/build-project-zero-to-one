#!/usr/bin/env python3
"""Audit the stable governance files created by this skill."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


CORE_REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "PLAN.md",
)

DELIVERY_REQUIRED_FILES = (
    "CHANGELOG.md",
    "docs/README.md",
    "docs/DOC_ROUTER.md",
    "docs/DOCS_DICTIONARY.md",
    "docs/specs/product-spec.md",
    "docs/specs/behavior-and-flow-spec.md",
    "docs/specs/traceability-matrix.md",
    "docs/operations/testing-and-acceptance.md",
    "docs/operations/test-evidence-matrix.md",
)

RELEASE_REQUIRED_FILES = (
    "docs/operations/release-runbook.md",
)

PROTOTYPE_FILE = "docs/specs/prototype-review.md"

PROFILE_REQUIRED_FILES = {
    "CORE": CORE_REQUIRED_FILES,
    "DELIVERY": (*CORE_REQUIRED_FILES, *DELIVERY_REQUIRED_FILES),
    "RELEASE": (
        *CORE_REQUIRED_FILES,
        *DELIVERY_REQUIRED_FILES,
        *RELEASE_REQUIRED_FILES,
    ),
}

LEGACY_EQUIVALENTS = {
    "docs/DOC_ROUTER.md": (
        "docs/CODEX_DOC_ROUTER.md",
    ),
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
        ("- Acceptance owner: name the person or role", "acceptance owner"),
        ("- Next checkpoint: date, event, decision, or not required", "next checkpoint"),
        (
            "Recover or establish the smallest trustworthy baseline for the project.",
            "current goal",
        ),
        (
            "Describe the observable user, business, operational, or learning outcome "
            "that would make this task worthwhile.",
            "expected outcome or value signal",
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
            "For each material risk or uncertainty, record the likely impact, response, "
            "owner, and the condition that triggers escalation, rollback, or a stop.",
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
            "Describe the actor or system, the problem, the desired outcome, and how "
            "the approval owner will recognize value.",
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
    PROTOTYPE_FILE: (
        (
            "Artifact: describe or link the prototype, mock, transcript, or diagram",
            "prototype artifact",
        ),
        (
            "State the product, interaction, visual, workflow, or contract decision "
            "the reviewer must make.",
            "review decision",
        ),
    ),
}

REQUIRED_TABLE_ROWS = {
    "AGENTS.md": (("## Work area routing", "work-area routing"),),
    "PLAN.md": (
        ("## Applicable work areas", "work-area decisions"),
        ("### Human decisions and review gates", "human review decision"),
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
    PROTOTYPE_FILE: (("## Scenarios and states", "prototype scenarios"),),
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
PROFILE_LINE = re.compile(
    r"^- Governance profile:\s*`?(CORE|DELIVERY|RELEASE)`?\s*$",
    re.MULTILINE | re.IGNORECASE,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check required project governance files and scoped AGENTS.md routes."
    )
    parser.add_argument("project_root", help="Project directory to audit")
    parser.add_argument(
        "--strict",
        action="store_true",
        help=(
            "Treat missing structure, unfinished content, and evidence "
            "inconsistencies as errors"
        ),
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
    next_heading = re.search(r"^#{1,6} ", body, flags=re.MULTILINE)
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


def table_rows(content: str, heading: str) -> list[list[str]]:
    lines = [
        line.strip()
        for line in section_text(content, heading).splitlines()
        if line.strip().startswith("|") and line.strip().endswith("|")
    ]
    rows: list[list[str]] = []
    for line in lines[2:]:
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if any(cells):
            rows.append(cells)
    return rows


def meaningful(value: str) -> bool:
    return value.strip().lower() not in {"", "-", "none", "n/a", "tbd", "todo"}


def detect_profile(root: Path, warnings: list[str]) -> str:
    plan_path = root / "PLAN.md"
    if plan_path.is_file():
        try:
            plan = plan_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            plan = ""
        match = PROFILE_LINE.search(plan)
        if match:
            return match.group(1).upper()

    if (root / "docs/operations/release-runbook.md").is_file():
        inferred = "RELEASE"
    elif (root / "docs/specs/product-spec.md").is_file():
        inferred = "DELIVERY"
    else:
        inferred = "CORE"
    warnings.append(
        f"PLAN.md has no governance profile; inferred {inferred} from existing files"
    )
    return inferred


def check_semantic_consistency(
    root: Path,
    contents: dict[str, str],
    profile: str,
    strict: bool,
    errors: list[str],
    warnings: list[str],
) -> None:
    def finding(message: str) -> None:
        add_completion_finding(message, strict, errors, warnings)

    plan = contents.get("PLAN.md", "")
    readiness_match = re.search(
        r"^- Readiness:\s*`?([A-Za-z_ ]+)`?\s*$", plan, flags=re.MULTILINE
    )
    readiness = (
        readiness_match.group(1).strip().upper().replace(" ", "_")
        if readiness_match
        else ""
    )
    readiness_levels = {
        "NOT_ASSESSED",
        "SPEC_READY",
        "IMPLEMENTED_LOCAL",
        "VERIFIED_LOCAL",
        "RELEASE_READY",
        "DEPLOYED_VERIFIED",
        "BLOCKED_EXTERNAL",
    }
    if readiness and readiness not in readiness_levels:
        finding(f"PLAN.md has unknown readiness level: {readiness}")

    review_rows = table_rows(plan, "### Human decisions and review gates")
    review_statuses = {
        "DRAFT",
        "REVIEW_REQUIRED",
        "APPROVED",
        "CHANGES_REQUESTED",
        "NOT_REQUIRED",
    }
    implementation_levels = {
        "IMPLEMENTED_LOCAL",
        "VERIFIED_LOCAL",
        "RELEASE_READY",
        "DEPLOYED_VERIFIED",
    }
    for index, row in enumerate(review_rows, start=1):
        if len(row) < 5:
            finding(f"PLAN.md human review row {index} has fewer than 5 columns")
            continue
        required = row[1].strip().upper() in {"YES", "REQUIRED", "TRUE", "是", "需要"}
        status = row[3].strip().upper().replace(" ", "_")
        if status not in review_statuses:
            finding(f"PLAN.md human review row {index} has unknown status: {row[3]}")
        if status in {"APPROVED", "NOT_REQUIRED"} and not meaningful(row[4]):
            finding(
                f"PLAN.md human review row {index} needs decision evidence or a skip reason"
            )
        if required and readiness in implementation_levels and status != "APPROVED":
            finding(
                f"PLAN.md human review row {index} is required but not approved at {readiness}"
            )

    if profile in {"DELIVERY", "RELEASE"}:
        product_rows = table_rows(
            contents.get("docs/specs/product-spec.md", ""), "## Capabilities"
        )
        trace_rows = table_rows(
            contents.get("docs/specs/traceability-matrix.md", ""),
            "# Traceability matrix",
        )
        evidence_rows = table_rows(
            contents.get("docs/operations/test-evidence-matrix.md", ""),
            "# Test evidence matrix",
        )
        delivery_statuses = {
            "IMPLEMENTED",
            "PARTIAL",
            "TODO / GAP",
            "MANUAL_REQUIRED",
            "BLOCKED",
            "FORBIDDEN / OUT_OF_SCOPE",
        }
        evidence_statuses = {
            "PASS",
            "FAIL",
            "PARTIAL",
            "TODO / GAP",
            "MANUAL_REQUIRED",
            "BLOCKED",
            "NOT_APPLICABLE",
        }

        product_ids: set[str] = set()
        for index, row in enumerate(product_rows, start=1):
            if len(row) < 5:
                finding(f"product capabilities row {index} has fewer than 5 columns")
                continue
            requirement_id, status = row[0], row[3].upper()
            if requirement_id in product_ids:
                finding(f"duplicate product requirement ID: {requirement_id}")
            product_ids.add(requirement_id)
            if status not in delivery_statuses:
                finding(
                    f"product requirement {requirement_id} has unknown status: {row[3]}"
                )
            if status == "IMPLEMENTED" and not meaningful(row[4]):
                finding(
                    f"implemented product requirement {requirement_id} has no evidence"
                )

        trace_ids: set[str] = set()
        implemented_product_ids = {
            row[0]
            for row in product_rows
            if len(row) >= 5 and row[3].upper() == "IMPLEMENTED"
        }
        trace_evidence_refs: dict[str, list[str]] = {}
        implemented_traces = 0
        for index, row in enumerate(trace_rows, start=1):
            if len(row) < 9:
                finding(f"traceability row {index} has fewer than 9 columns")
                continue
            requirement_id, status = row[0], row[7].upper()
            if requirement_id in trace_ids:
                finding(f"duplicate traceability requirement ID: {requirement_id}")
            trace_ids.add(requirement_id)
            if requirement_id not in product_ids:
                finding(
                    f"traceability requirement {requirement_id} is missing from product capabilities"
                )
            if status not in delivery_statuses:
                finding(
                    f"traceability requirement {requirement_id} has unknown status: {row[7]}"
                )
            if status == "IMPLEMENTED":
                implemented_traces += 1
                if not meaningful(row[5]) or not meaningful(row[6]):
                    finding(
                        f"implemented traceability requirement {requirement_id} needs implementation and test evidence"
                    )
                trace_evidence_refs[requirement_id] = [
                    item.strip().strip("`")
                    for item in re.split(r"[,;]", row[6])
                    if item.strip()
                ]

        for requirement_id in sorted(implemented_product_ids - trace_ids):
            finding(
                f"implemented product requirement {requirement_id} is missing from traceability"
            )

        evidence_ids: set[str] = set()
        passed_evidence = 0
        for index, row in enumerate(evidence_rows, start=1):
            if len(row) < 10:
                finding(f"test evidence row {index} has fewer than 10 columns")
                continue
            evidence_id, status = row[0], row[7].upper()
            if evidence_id in evidence_ids:
                finding(f"duplicate evidence ID: {evidence_id}")
            evidence_ids.add(evidence_id)
            if status not in evidence_statuses:
                finding(f"evidence {evidence_id} has unknown status: {row[7]}")
            if status == "PASS":
                passed_evidence += 1
                if not meaningful(row[5]) or not meaningful(row[8]):
                    finding(
                        f"passing evidence {evidence_id} needs a procedure and evidence location"
                    )

        for requirement_id, references in trace_evidence_refs.items():
            for evidence_id in references:
                if evidence_id.upper().startswith("EV-") and evidence_id not in evidence_ids:
                    finding(
                        f"traceability requirement {requirement_id} references missing evidence ID: {evidence_id}"
                    )

        if readiness == "SPEC_READY" and (not product_rows or not trace_rows):
            finding("SPEC_READY requires product capabilities and traceability rows")
        if readiness in {
            "IMPLEMENTED_LOCAL",
            "VERIFIED_LOCAL",
            "RELEASE_READY",
            "DEPLOYED_VERIFIED",
        }:
            if implemented_traces == 0:
                finding(f"{readiness} requires an implemented traceability row")
        if readiness in {"VERIFIED_LOCAL", "RELEASE_READY", "DEPLOYED_VERIFIED"}:
            if passed_evidence == 0:
                finding(f"{readiness} requires a passing test evidence row")
        if readiness == "DEPLOYED_VERIFIED":
            passed_environments = {
                row[3].strip().lower()
                for row in evidence_rows
                if len(row) >= 10 and row[7].upper() == "PASS"
            }
            if not passed_environments or passed_environments <= {
                "local",
                "dev",
                "development",
            }:
                finding(
                    "DEPLOYED_VERIFIED requires passing evidence from a target environment"
                )

    if readiness in {"RELEASE_READY", "DEPLOYED_VERIFIED"} and not (
        root / "docs/operations/release-runbook.md"
    ).is_file():
        finding(f"{readiness} requires docs/operations/release-runbook.md")

    prototype = contents.get(PROTOTYPE_FILE, "")
    if prototype:
        status_match = re.search(
            r"^- Status:\s*`?([A-Z_]+)`?\s*$", prototype, flags=re.MULTILINE
        )
        if not status_match:
            finding(f"{PROTOTYPE_FILE} has no recognized review status")
        elif status_match.group(1) not in review_statuses:
            finding(
                f"{PROTOTYPE_FILE} has unknown review status: {status_match.group(1)}"
            )
        elif status_match.group(1) == "APPROVED" and not table_has_data_row(
            prototype, "## Review record"
        ):
            finding(f"{PROTOTYPE_FILE} is approved but has no review record")


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
    profile = detect_profile(root, warnings)
    required_files = list(PROFILE_REQUIRED_FILES[profile])
    if (root / PROTOTYPE_FILE).is_file():
        required_files.append(PROTOTYPE_FILE)

    for relative in required_files:
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

    check_semantic_consistency(
        root,
        contents,
        profile,
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

    found_count = len(required_files) - sum(
        1 for item in required_files if item not in contents
    )
    print(
        "summary: "
        f"profile {profile}, "
        f"{found_count} required files found, "
        f"{len(scoped_agents)} scoped AGENTS.md, "
        f"{len(warnings)} warnings, {len(errors)} errors"
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
