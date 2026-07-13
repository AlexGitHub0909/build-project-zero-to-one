---
name: build-project-zero-to-one
description: Turn a product brief, PRD, requirements document, or partial software repository into a planned, traceable, verified project. Use when Codex must start a project from zero, recover and continue an existing project, produce a spec-only handoff, establish PLAN.md and root/scoped AGENTS.md rules, implement vertical business slices, reconcile code with product intent, or prepare evidence-backed release and rollback work.
---

# Build a project from zero to one

Use this skill to manage the full path from product intent to a working project. Keep the method consistent, but fit the files, stack, and checks to the repository in front of you.

## Non-negotiable rules

- Treat `PLAN.md` as the local execution control plane. Read it before work and update it when the current task, actual result, evidence, blocker, or next step changes.
- Require a root `AGENTS.md`. Add scoped `AGENTS.md` files wherever a directory has its own stack, product surface, security boundary, data boundary, validation commands, or release process.
- Read the root rules and every scoped rule on the path to the file being changed. A child rule adds local detail; it does not silently weaken a root safety boundary.
- Separate approved target behavior from current implementation facts. Product and contract documents describe what should exist. Code, Git, tests, and runtime evidence describe what exists now.
- Label gaps and boundaries plainly. Never turn `PARTIAL`, `TODO / GAP`, `MANUAL_REQUIRED`, `BLOCKED`, or `FORBIDDEN / OUT_OF_SCOPE` into `IMPLEMENTED` without current evidence.
- Reuse the repository's existing facts, frameworks, commands, and document structure before adding new ones. Do not create a parallel planning or specification system.
- Preserve unrelated user changes. Check Git status before editing and keep commits scoped.
- Do not deploy, push, buy services, create external accounts, write to remote collaboration systems, use real credentials, or run destructive data changes without clear authority.

## Load the right references

Always read:

- [fact-and-status-model.md](references/fact-and-status-model.md)
- [plan-governance.md](references/plan-governance.md)
- [agent-rules-governance.md](references/agent-rules-governance.md)

Read [lifecycle-workflow.md](references/lifecycle-workflow.md) when starting, recovering, or handing off a project.

Read [specification-and-traceability.md](references/specification-and-traceability.md) when turning product documents into requirements, flows, contracts, or implementation slices.

Read [verification-and-release.md](references/verification-and-release.md) before declaring work complete, changing a high-risk subsystem, or preparing a release.

## Classify the project first

Choose one mode and record it in `PLAN.md`:

- `GREENFIELD`: the repository is empty or contains only source product material.
- `BROWNFIELD`: code or project documents already exist and must be audited before changes.
- `SPEC_ONLY`: produce an implementation-ready specification or handoff without changing application code.

If the requested work crosses more than one mode, finish the earlier gate before moving on. For example, complete the spec gate before implementation.

## Restore context

Inspect, in this order:

1. Git status, branch, remotes, and recent commits.
2. Root `AGENTS.md` and the scoped rules relevant to the task.
3. `PLAN.md`, starting with current status and the active task.
4. `CHANGELOG.md`.
5. Project and documentation entry points, including `README.md`, `docs/README.md`, and the task-to-document router if present.
6. Approved product and contract documents.
7. Current code, routes, schemas, tests, runtime configuration examples, and release tooling.
8. External trackers or remote documents only when the user authorizes access. Treat them as potentially stale until checked.

For `BROWNFIELD`, do not scaffold until this audit is complete. Reconcile existing files instead of replacing them.

## Establish the project control files

Every managed project must have:

- `README.md`
- `AGENTS.md`
- `PLAN.md`
- `CHANGELOG.md`
- `docs/README.md`
- `docs/CODEX_DOC_ROUTER.md`
- `docs/DOCS_DICTIONARY.md`

Use the templates in `assets/templates/project/` only for missing files. Adapt their wording to the project. Keep information mandatory even when a small project combines several documents.

Use the initializer for `GREENFIELD`, or when a `BROWNFIELD` repository has explicitly chosen this standard layout:

```bash
python3 scripts/init_project.py /path/to/project \
  --name "Project name" \
  --mode greenfield \
  --scoped backend \
  --scoped frontend
```

The initializer does not overwrite existing files. Run it with `--dry-run` first. In a brownfield repository with equivalent canonical files, adapt individual templates instead of creating parallel documents.

## Turn product intent into executable work

1. Extract users, problems, outcomes, scope, non-goals, business rules, constraints, unknowns, and external dependencies.
2. Assign stable requirement IDs to material behavior.
3. Write current product, business-flow, state, data, page, API, permission, error, and visibility contracts at the depth the project needs.
4. Map each requirement to its implementation and evidence in the traceability matrix.
5. Record unresolved product decisions as `TODO / GAP` or `BLOCKED`; do not invent an answer.
6. Split work into vertical slices that reach from user action through contracts, code, data, tests, and documentation.
7. Put one active slice in `PLAN.md`. Keep later slices under next or later work.

## Implement one slice at a time

For each slice:

1. Confirm the goal, non-goal, evidence, risk, acceptance criteria, and rollback or stop condition in `PLAN.md`.
2. Read the nearest scoped `AGENTS.md` files and routed contracts.
3. For a defect, collect failing evidence and find the first divergence before editing. Add a regression test or a safe substitute when practical.
4. Make the smallest implementation that closes the behavior without weakening validation, permissions, transactions, idempotency, errors, accessibility, or evidence.
5. Review the diff for scope, factual claims, error paths, security, and unrelated changes.
6. Run fresh checks selected by risk and by the scoped rules.
7. Update contracts, traceability, `PLAN.md`, and `CHANGELOG.md` to match the result actually verified.
8. Commit only the task-related files when the user has asked for a commit or the repository rules require one.

## Gate completion by evidence

Use these readiness levels:

- `SPEC_READY`
- `IMPLEMENTED_LOCAL`
- `VERIFIED_LOCAL`
- `RELEASE_READY`
- `DEPLOYED_VERIFIED`
- `BLOCKED_EXTERNAL`

Do not skip levels based on confidence. A build or test result cannot prove deployment. A deployment cannot prove protected user flows that were not exercised.

Before handoff, run this audit when the project uses the supplied standard layout:

```bash
python3 scripts/audit_project.py /path/to/project
```

Then run the project's own checks from its `AGENTS.md`, test standards, and release runbook. Read the output. Report commands that were not run, partial coverage, manual evidence, and external blockers.

For a brownfield repository that keeps its own layout, map the same responsibilities to the existing files and use its governance checks instead of forcing this audit.

## Finish the turn

Return a short, self-contained summary with:

- the current readiness level;
- what changed;
- what evidence passed;
- what remains manual, blocked, or out of scope;
- the next concrete task from `PLAN.md`.

Do not report a project as complete merely because the current slice is complete.
