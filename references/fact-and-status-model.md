# Fact and status model

## Two kinds of truth

Keep target behavior and current implementation separate.

| Question | Primary evidence |
|---|---|
| What should the product do? | Approved product and contract documents |
| What does the project do now? | Current code, Git diff and history, tests, routes, schemas, and runtime evidence |
| What is being worked on? | `PLAN.md` |
| What changed in a released or completed capability? | `CHANGELOG.md` and Git history |
| Why was a major technical choice made? | ADRs |

When these disagree, do not silently pick one. Record the mismatch, decide whether the contract or implementation is wrong, and repair the affected sources together.

## Implementation fact order

Use this order when deciding what is currently implemented:

1. Current code, Git state, generated inventories, and runtime evidence.
2. Fresh tests and validation output.
3. `PLAN.md`.
4. `CHANGELOG.md`.
5. Canonical contracts and architecture documents.
6. Derived summaries and external collaboration copies.
7. Conversation history and memory, which are search hints only.

This order does not let code override approved product intent. It only answers what the system does now.

## Status vocabulary

Use the same labels across plans, specs, traceability, tests, and release records.

| Status | Meaning |
|---|---|
| `IMPLEMENTED` | Current code and direct evidence support the claim |
| `PARTIAL` | Some required behavior exists, but material work or evidence is missing |
| `TODO / GAP` | Approved or necessary behavior is not implemented |
| `MANUAL_REQUIRED` | A person must perform or confirm the step |
| `BLOCKED` | Work cannot proceed without a named dependency, decision, permission, or environment change |
| `FORBIDDEN / OUT_OF_SCOPE` | The project explicitly excludes the behavior |

Never use vague equivalents such as "basically done" or "should work" in evidence fields.

## Canonical and derived documents

Canonical documents define current intent or execution. Examples include product scope, contracts, `PLAN.md`, `AGENTS.md`, test standards, and the release runbook.

Derived documents summarize canonical facts for a different reader. Examples include project overviews, manuals, sales material, or remote collaboration copies.

Update canonical sources first. Refresh derived documents afterward. A derived document must not become a second plan or a competing contract.

## Claims

Every claim such as "implemented", "fixed", "covered", "ready", or "deployed" must point to current evidence. If the evidence is partial, narrow the claim.

Useful evidence includes:

- a file and line-level implementation;
- a route, schema, migration, or generated inventory;
- a named test or validation command with current output;
- a browser or API result from the target environment;
- a release marker, health response, backup record, or rollback target;
- a signed or named manual acceptance record.
