# AGENTS.md

## Scope

This file applies to the entire {{PROJECT_NAME}} repository. A scoped `AGENTS.md` adds rules for its directory and inherits these root rules.

## Purpose and stage

Describe the project purpose, current stage, actors, main workflow, and hard capability boundaries. Keep planned features separate from implemented ones.

## Required context

Before changing the project, read:

- `AGENTS.md`;
- every scoped `AGENTS.md` on the path to the target file;
- `PLAN.md`;
- `README.md` and `docs/README.md`;
- `docs/CODEX_DOC_ROUTER.md`;
- the contracts routed for the task;
- current code, tests, Git state, and runtime examples.

## Scoped rule routing

Add a row only when the scoped file exists.

| Work area | Required rules |
|---|---|
| Whole project | `AGENTS.md` |
{{SCOPED_RULE_ROWS}}

## Fact sources

For current implementation facts, prefer current code, Git, generated inventories, runtime evidence, and fresh tests. Use `PLAN.md`, `CHANGELOG.md`, and canonical contracts to explain current intent and history. Treat derived documents and conversation history as secondary.

If approved behavior and implementation disagree, record the gap and repair the correct source. Do not silently turn one into the other.

## Rules

- Check Git status before editing and preserve unrelated user changes.
- Reuse current code, framework features, dependencies, components, services, scripts, and documents before adding a new abstraction.
- Preserve user-approved and existing choices for implementation and documentation languages, frameworks, data stores, architecture, hosting, and tooling.
- For an open choice that is expensive to reverse, recommend an option from current constraints and get confirmation before scaffolding unless the user delegates the decision. Record the result in `PLAN.md` or an ADR.
- Make the smallest change that closes the current behavior without weakening security, validation, transactions, idempotency, errors, accessibility, or evidence.
- For a defect, collect failing evidence and locate the first divergence before changing code.
- For a high-risk or cross-system change, record the goal, non-goal, evidence, dependencies, risk, acceptance, rollback, and stop conditions in `PLAN.md` and affected contracts.
- Keep product, flow, page, API, data, permission, test, and release documents consistent with the implementation actually verified.
- Do not expose credentials, secrets, private user or organization data, or production values.
- Do not deploy, push, perform destructive data changes, or write to external systems without clear authority.

## Validation

Choose checks from the changed scope and the nearest scoped rules. Read their output before reporting success. Distinguish automated evidence, manual evidence, partial checks, and blocked checks.

## Definition of done

- The requested behavior is implemented or the requested spec is complete.
- Current facts, `PLAN.md`, direct contracts, traceability, and `CHANGELOG.md` agree.
- Fresh checks support every completion claim.
- Manual, blocked, and out-of-scope items remain explicit.
- The diff contains no unrelated work or sensitive data.

## Do not

- Do not start a cross-module task without reading the routed rules and contracts.
- Do not describe planned, partial, simulated, or unverified behavior as implemented.
- Do not create a second planning or specification system alongside the repository's canonical files.
- Do not hide a failing check, unresolved decision, external dependency, or production risk.
