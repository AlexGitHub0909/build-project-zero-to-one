# Lifecycle workflow

## Contents

- Modes
- Gates
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
| Planning | Vertical slices have dependencies, acceptance evidence, and stop or rollback conditions |
| Implementation | The current slice is implemented without claiming later work |
| Verification | Fresh checks support each completion claim; gaps stay visible |
| Release | Impact, environment, migration, backup, rollback, health, and post-release evidence are ready |
| Handoff | A new contributor can recover state from the repository without relying on chat history |

## Greenfield path

1. Read all product source material before choosing a stack.
2. Record assumptions and unresolved decisions. Ask only questions that materially change scope or architecture.
3. Prefer framework generators and installed dependencies over custom scaffolding.
4. Create the governance and documentation files from the supplied templates.
5. Define the smallest end-to-end slice that proves the architecture.
6. Implement and verify that slice before widening the backlog.

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
