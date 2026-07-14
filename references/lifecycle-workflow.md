# Lifecycle workflow

## Contents

- Modes
- Gates
- Technology and language decisions
- Greenfield path
- Brownfield path
- Spec-only path
- Handoff

## Modes

Record one primary mode in `PLAN.md`.

| Mode | Starting point | First responsibility |
|---|---|---|
| `GREENFIELD` | Product material, little or no code | Establish facts, constraints, governance, and an implementable first slice |
| `BROWNFIELD` | Existing code or project records | Audit current truth and preserve user work before proposing changes |
| `SPEC_ONLY` | Product material or an existing system | Produce a traceable handoff without changing application code |

## Gates

Move through gates in order. A later gate may expose a defect in an earlier one; when that happens, repair the earlier fact source before continuing.

| Gate | Required result |
|---|---|
| Orientation | Project mode, repository state, authority, owners, constraints, and unknowns are recorded |
| Governance | Root/scoped `AGENTS.md`, `PLAN.md`, document routing, and fact-source order are usable |
| Specification | Scope, flows, contracts, status labels, and requirement IDs are clear enough to implement |
| Planning | Implementation slices have dependencies, acceptance evidence, and stop or rollback conditions |
| Implementation | The current slice is implemented without claiming later work |
| Verification | Fresh checks support each completion claim; gaps stay visible |
| Release | Impact, environment, migration, backup, rollback, health, and post-release evidence are ready |
| Handoff | A new contributor can recover state from the repository without relying on chat history |

## Technology and language decisions

- Treat user-approved choices and an existing repository's stack as project constraints. Recommend a change only when current evidence shows a material problem, and get approval before acting on it.
- In a new project, gather the product type, target platforms, team experience, delivery window, budget, deployment environment, integrations, compliance needs, and expected scale before recommending a stack.
- Recommend one preferred approach and explain why it fits. Include one alternative only when it reveals a material trade-off. Do not present an unranked catalogue of technologies.
- Get user confirmation before scaffolding around choices that are expensive to reverse, including the implementation language, primary framework or runtime, data store, architecture, hosting model, and identity approach. If the user delegates the decision, choose the simplest suitable option and record the rationale, assumptions, and revisit conditions in `PLAN.md` or an ADR.
- Use reasonable recorded defaults for low-risk choices that are easy to change. Do not interrupt the user for every formatting tool or directory detail.
- Keep the repository's established documentation language. For a new project, follow the user's requested language or the supplied product material, and confirm a different team standard when it affects handoff.

## Greenfield path

1. Read all product source material and collect the constraints needed for technology decisions.
2. Separate confirmed choices from open decisions. Ask only questions that materially change scope, architecture, cost, operations, or handoff.
3. Follow the technology decision rules above before scaffolding application code.
4. Prefer generators from the confirmed framework and installed dependencies over custom scaffolding.
5. Create the governance and documentation files from the supplied templates, using the project's chosen language.
6. Define the smallest end-to-end slice that proves the architecture.
7. Implement and verify that slice before widening the backlog.

## Brownfield path

1. Check Git status and preserve dirty files.
2. Locate root and scoped rules, plan, change history, contracts, tests, runtime examples, and release tools.
3. Compare intended behavior with current code and tests.
4. Classify drift as stale documentation, missing implementation, unintended behavior, or unresolved decision.
5. Repair the canonical source and direct dependants in one scoped change.
6. Avoid broad scaffolding and directory renames unless the project explicitly needs them.

## Spec-only path

1. State that application code is out of scope.
2. Build the product, flow, state, data, interface, permission, and error contracts needed for implementation.
3. Mark current evidence separately from target behavior.
4. Produce a traceability matrix, implementation slices, acceptance evidence, risks, and stop conditions.
5. Do not label the target behavior as implemented.

## Handoff

A handoff is ready when a new contributor can answer these questions from the repository:

- What is the product trying to do?
- What exists now?
- What should exist next?
- Which rules apply to the files I will change?
- What is the current task?
- Which contracts define it?
- How do I verify it?
- What is blocked, manual, or forbidden?
- How is the project released and rolled back?
