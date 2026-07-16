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
- `README.md`;
- `docs/README.md`, `docs/DOC_ROUTER.md`, and routed contracts when they exist;
- current code, tests, Git state, and runtime examples.

## Work area routing

List only confirmed work areas. Keep open, deferred, and not-applicable decisions in `PLAN.md`.

| Work area | Scope | Required rules and contracts |
|---|---|---|

Work areas do not have to match directories. Several areas may share one scoped rule file.

## Scoped rule routing

Add a row only when the scoped file exists.

| Path | Required rules |
|---|---|
| Whole project | `AGENTS.md` |
{{SCOPED_RULE_ROWS}}

## Fact sources

For current implementation facts, prefer current code, Git, generated inventories, runtime evidence, and fresh tests. Use `PLAN.md`, `CHANGELOG.md`, and canonical contracts to explain current intent and history. Treat derived documents and conversation history as secondary.

If approved behavior and implementation disagree, record the gap and repair the correct source. Do not silently turn one into the other.

## Capability and tool routing

- Use the repository's approved commands, dependencies, scripts, and services before adding another capability.
- Use a specialized Skill or plugin only when the task needs that capability. Keep optional tools replaceable.
- Read the capability's instructions and check availability, permissions, cost, network access, and side effects before use.
- Record required capabilities, external authority, fallback paths, and blockers in `PLAN.md`.
- Do not install, enable, authorize, or write through an external capability without clear user authority.
- Validate the resulting artifact or system state with the project's own acceptance rules. Tool execution alone is not evidence of correctness.

## Human decisions and prototypes

- Treat the human user or named owner as the authority for product intent, material trade-offs, prototype approval, and acceptance.
- Produce the smallest useful confirmation artifact before implementation when words leave a material ambiguity. Use visual prototypes only for visual or interactive decisions; use examples, transcripts, diagrams, decision tables, or dry runs for other product surfaces.
- Record the artifact, reviewer, status, requested changes, and evidence in `PLAN.md` or the routed review document.
- Do not approve the agent's own proposal or treat silence as approval. Prototype approval confirms target intent, not implementation or release.

## Rules

- Check Git status before editing and preserve unrelated user changes.
- Reuse current code, framework features, dependencies, components, services, scripts, and documents before adding a new abstraction.
- Preserve user-approved and existing choices for implementation and documentation languages, frameworks, data stores, architecture, hosting, and tooling.
- For an open choice that is expensive to reverse, recommend an option from current constraints and get confirmation before scaffolding unless the user delegates the decision. Record the result in `PLAN.md` or an ADR.
- Keep the active slice tied to an expected outcome or value signal, an acceptance owner, and a next checkpoint when a date, decision, review, dependency, or release gate matters.
- Make the smallest change that closes the current behavior without weakening security, validation, transactions, idempotency, errors, accessibility, or evidence.
- For a defect, collect failing evidence and locate the first divergence before changing code.
- For a high-risk or cross-system change, record the goal, non-goal, evidence, dependencies, material-risk response and owner, acceptance, rollback, and stop conditions in `PLAN.md` and affected contracts.
- Do not cross a required human review gate until it is approved, marked not required, or explicitly waived with the rework risk recorded.
- When approved scope or approach changes, record the reason and its effect on delivery, cost, or acceptance before continuing.
- Keep product, flow, page, API, data, permission, test, and release documents consistent with the implementation actually verified.
- When a result changes how later work should be done, update the nearest rule, contract, or automated check instead of starting a separate lessons log by default.
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
