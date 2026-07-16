---
name: spec-to-delivery
description: Turn a product brief, PRD, requirements document, or partial software repository into a planned, traceable project with current verification evidence. Use when an AI coding agent must establish a new software project, recover and continue an existing repository, produce a spec-only handoff, establish PLAN.md and root/scoped AGENTS.md rules, select only the website, frontend, backend, API, database, or operations rules that apply, implement end-to-end slices, reconcile code with approved intent, or prepare evidence-backed release and rollback work.
---

# SpecToDelivery

Use this skill to keep approved intent, implementation evidence, and handoff state consistent inside the repository. Fit the files, stack, and checks to the project in front of you.

## Non-negotiable rules

- Treat `PLAN.md` as the current execution record. Read it before work and update it when the current task, actual result, evidence, blocker, or next step changes.
- Require a root `AGENTS.md`. Add scoped `AGENTS.md` files wherever a directory has its own stack, functional surface, security boundary, data boundary, validation commands, or release process.
- Read the root rules and every scoped rule on the path to the file being changed. A child rule adds local detail; it does not silently weaken a root safety boundary.
- Separate approved target behavior from current implementation facts. Product and contract documents describe what should exist. Code, Git, tests, and runtime evidence describe what exists now.
- Label gaps and boundaries plainly. Never turn `PARTIAL`, `TODO / GAP`, `MANUAL_REQUIRED`, `BLOCKED`, or `FORBIDDEN / OUT_OF_SCOPE` into `IMPLEMENTED` without current evidence.
- Reuse the repository's existing facts, frameworks, commands, and document structure before adding new ones. Do not create a parallel planning or specification system.
- Preserve explicit user and repository choices for implementation language, framework, data store, architecture, hosting, tooling, and documentation language. Do not replace them with a preferred stack without approval.
- For open `GREENFIELD` choices, gather constraints and recommend one preferred option. Add one alternative only when it exposes a material trade-off. Get confirmation before scaffolding around a hard-to-reverse choice unless the user explicitly delegates the decision. Record the choice, rationale, assumptions, and revisit conditions in `PLAN.md` or an ADR. Use recorded defaults only for low-risk, reversible choices.
- Preserve unrelated user changes. Check Git status before editing and keep commits scoped.
- Do not deploy, push, buy services, create external accounts, write to remote collaboration systems, use real credentials, or run destructive data changes without clear authority.

## Load the right references

Always read:

- [fact-and-status-model.md](references/fact-and-status-model.md)
- [plan-governance.md](references/plan-governance.md)
- [agent-rules-governance.md](references/agent-rules-governance.md)

Read [lifecycle-workflow.md](references/lifecycle-workflow.md) when starting, recovering, or handing off a project.

Read [human-review-and-prototyping.md](references/human-review-and-prototyping.md) when product intent, workflow, interaction, visual direction, or another material decision needs human confirmation before implementation.

Read [work-area-discovery.md](references/work-area-discovery.md) when establishing or revisiting project scope. Then load only the rules needed for confirmed work areas or an open decision:

- [website-rules.md](references/website-rules.md) for public, discoverable, content-led, or marketing sites;
- [frontend-rules.md](references/frontend-rules.md) for interactive web, mobile, or desktop interfaces;
- [backend-rules.md](references/backend-rules.md) for server-side behavior, jobs, or integrations;
- [api-rules.md](references/api-rules.md) for programmatic interfaces between systems or clients;
- [database-rules.md](references/database-rules.md) for durable structured data or stateful storage;
- [operations-rules.md](references/operations-rules.md) for deployment, release, runtime, monitoring, or recovery.

Do not load all work-area references by default.

Read [specification-and-traceability.md](references/specification-and-traceability.md) when turning product documents into requirements, flows, contracts, or implementation slices.

Read [verification-and-release.md](references/verification-and-release.md) before declaring work complete, changing a high-risk subsystem, or preparing a release.

Read [capability-routing.md](references/capability-routing.md) when the task may need a specialized Skill, plugin, connector, external service, or artifact tool beyond the repository's existing commands. Load it only when the capability changes how the work can be completed or verified.

## Classify the project first

Choose one mode and record it in `PLAN.md`:

- `GREENFIELD`: the repository is empty or contains only source product material.
- `BROWNFIELD`: code or project documents already exist and must be audited before changes.
- `SPEC_ONLY`: produce an implementation-ready specification or handoff without changing application code.

If the requested work crosses more than one mode, finish the earlier gate before moving on. For example, complete the spec gate before implementation.

## Classify applicable work areas

Use the product material, repository evidence, and [work-area-discovery.md](references/work-area-discovery.md) before asking questions. Record confirmed or unresolved areas in `PLAN.md` as `APPLIES`, `NOT_APPLICABLE`, `DEFERRED`, or `OPEN_DECISION` when the distinction matters.

Ask no more than three related questions at a time, and ask only when the answer changes product scope, architecture, data ownership, release responsibility, or acceptance evidence. Phrase questions in product terms instead of asking the user to choose from unexplained technologies.

A work area is not a directory. Multiple areas may share one scoped `AGENTS.md`, and one area may span several directories. Create scoped rules only where a real local boundary exists.

## Keep the human in control

Treat the user as the product decision and acceptance owner unless another owner is named. The agent may analyze, recommend, draft, implement, and verify within its authority; it must not silently approve its own material product decisions.

Choose the smallest confirmation artifact that lets the human judge an unresolved decision. For a website or interactive interface, this may be a flow, wireframe, visual screen, or clickable prototype. For a CLI, API, automation, data product, or backend workflow, prefer transcripts, examples, diagrams, decision tables, or dry-run output when they communicate the behavior better than a UI mock.

Require human review before expensive or hard-to-reverse implementation when the artifact settles scope, navigation, visual direction, workflow, data responsibility, cost, or release risk. Record the artifact, reviewer, decision, requested changes, and evidence in `PLAN.md` or `docs/specs/prototype-review.md`. Keep prototype approval separate from implementation and release evidence.

## Route specialized capabilities

Describe the needed outcome before choosing a tool. Prefer approved repository commands and already available capabilities. Treat a Skill or plugin as optional unless the acceptance criteria cannot be met without it.

Record a capability decision in `PLAN.md` only when it affects delivery, permissions, external writes, acceptance evidence, or the fallback path. Do not install, enable, authorize, or write through an external capability without clear user authority. If a required capability is unavailable, use a safe fallback or mark the dependency `BLOCKED_EXTERNAL` instead of pretending the evidence exists.

## Adapt to the active agent runtime

Treat file access, shell execution, Python, web or browser access, plugins, MCP, subagents, and external-system access as runtime capabilities, not assumptions.

- Do not lower the requested outcome, acceptance criteria, safety boundary, or evidence standard because the active platform lacks a feature. Use an equivalent path or record the task as manual or blocked.
- Resolve bundled references, templates, and scripts relative to this `SKILL.md`; do not assume the target project contains this Skill's `scripts/` directory.
- Read root and scoped `AGENTS.md` files explicitly when the active platform does not load them automatically.
- Use subagents or parallel work only when the platform provides them and the task benefits. Otherwise perform the same checks sequentially.
- If shell or Python is unavailable, create or review the governance files directly and mark the helper-script audit `MANUAL_REQUIRED`.
- If browser, network, plugin, MCP, deployment, or external-system access is unavailable, use the strongest local substitute and narrow the readiness claim to the evidence actually obtained.
- Treat platform-specific metadata and invocation syntax as optional adapters. They must not change the core workflow or become project requirements.

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

Choose a governance profile before using the initializer:

- `core`: `README.md`, root `AGENTS.md`, and `PLAN.md` for a small or already documented project;
- `delivery`: add product, flow, traceability, testing, evidence, changelog, and documentation routing for normal implementation or spec handoff;
- `release`: add the release runbook and ADR template when deployment, migration, recovery, or major architecture decisions apply.

Add `docs/specs/prototype-review.md` only when a human confirmation artifact is useful. Accept existing equivalent files instead of creating duplicates. Keep the responsibilities covered when a small project combines them.

Use the templates in `assets/templates/project/` only for missing files. Adapt their wording and documentation language to the project.

Use the initializer for `GREENFIELD`, or when a `BROWNFIELD` repository has explicitly chosen this standard layout:

```bash
python3 /path/to/spec-to-delivery/scripts/init_project.py /path/to/project \
  --name "Project name" \
  --mode greenfield \
  --profile delivery
```

Add `--prototype` when the project needs a dedicated human-review artifact. Add repeatable `--scoped path/to/directory` arguments only for directories with real local rule boundaries. The Python helpers manage governance files; they do not select or constrain the application's language or stack.

The initializer does not overwrite existing files. Run it with `--dry-run` first. In a brownfield repository with equivalent canonical files, adapt individual templates instead of creating parallel documents.

After classification, replace template instructions with the confirmed work-area rows, rule routes, owners, and concrete commands. Do not hand off an empty routing table or generic scoped `AGENTS.md` as finished governance.

## Turn product intent into executable work

1. Extract actors or systems, problems, desired outcomes, observable value signals, scope, non-goals, domain rules, constraints, unknowns, and external dependencies. Do not invent a KPI when an observable outcome is enough.
2. Assign stable requirement IDs to material behavior.
3. Write the relevant behavior, flow, state, data, interface, API, permission, error, and visibility contracts at the depth the project needs.
4. Produce a confirmation artifact when unresolved behavior, interaction, or visual direction would otherwise create material rework. Record human approval or requested changes before crossing the review gate.
5. Map each requirement to its implementation and evidence in the traceability matrix.
6. Record unresolved product decisions as `TODO / GAP` or `BLOCKED`; do not invent an answer.
7. Split work into end-to-end slices that connect observable behavior with contracts, code, data, tests, and documentation.
8. Put one active slice in `PLAN.md`. Keep later slices under next or later work.

## Implement one slice at a time

For each slice:

1. Confirm the goal, non-goal, expected outcome or value signal, acceptance owner, next checkpoint when one matters, evidence, material risks, acceptance criteria, and rollback or stop condition in `PLAN.md`.
2. Confirm that every required human review gate is `APPROVED`, `NOT_REQUIRED`, or explicitly waived with its rework risk recorded.
3. Read the nearest scoped `AGENTS.md` files and routed contracts.
4. For a defect, collect failing evidence and find the first divergence before editing. Add a regression test or a safe substitute when practical.
5. Make the smallest implementation that closes the behavior without weakening validation, permissions, transactions, idempotency, errors, accessibility, or evidence.
6. Review the diff for scope, factual claims, error paths, security, and unrelated changes.
7. Run fresh checks selected by risk and by the scoped rules. For an approved prototype, compare the implemented artifact with it and record intentional differences.
8. Update contracts, traceability, `PLAN.md`, and `CHANGELOG.md` to match the result actually verified. If approved scope or approach changed, record the reason and its effect on delivery, cost, or acceptance.
9. When a result changes how later work should be done, update the nearest rule, contract, or automated check. Do not create a separate lessons log by default.
10. Commit only the task-related files when the user has asked for a commit or the repository rules require one.

## Gate completion by evidence

Use these readiness levels:

- `SPEC_READY`
- `IMPLEMENTED_LOCAL`
- `VERIFIED_LOCAL`
- `RELEASE_READY`
- `DEPLOYED_VERIFIED`
- `BLOCKED_EXTERNAL`

Do not skip levels based on confidence. A build or test result cannot prove deployment. A deployment cannot prove protected user flows that were not exercised.

Run the standard-layout audit while establishing the project. Warnings identify starter content that still needs a project-specific decision or command:

```bash
python3 /path/to/spec-to-delivery/scripts/audit_project.py /path/to/project
```

Before handoff, run it in strict mode. Do not hand off while it reports an empty work-area route, untouched starter text, or another error:

```bash
python3 /path/to/spec-to-delivery/scripts/audit_project.py /path/to/project --strict
```

This audit catches structural gaps and obvious unfinished starter content; a clean result does not prove that the decisions are correct or the software works. Then run the project's own checks from its `AGENTS.md`, test standards, and release runbook. Read the output. Report commands that were not run, partial coverage, manual evidence, and external blockers.

For a brownfield repository that keeps its own layout, map the same responsibilities to the existing files and use its governance checks instead of forcing this audit.

## Finish the turn

Return a short, self-contained summary with:

- the current readiness level;
- what changed;
- what evidence passed;
- what remains manual, blocked, or out of scope;
- the next concrete task from `PLAN.md`.

Do not report a project as complete merely because the current slice is complete.
