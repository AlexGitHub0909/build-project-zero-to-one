# Project documentation

This directory contains the current product, engineering, test, and release contracts for {{PROJECT_NAME}}.

## Start here

1. Read the product spec.
2. Use `CODEX_DOC_ROUTER.md` to find documents for the task.
3. Check `../PLAN.md` for the active slice and current evidence.
4. Read the nearest `AGENTS.md` before changing code or documents.

## Fact boundaries

- Product and contract documents define approved behavior.
- Code, Git, tests, generated inventories, and runtime evidence prove current implementation.
- `PLAN.md` manages the gap between approved behavior and current implementation.
- `CHANGELOG.md` records completed capability changes.
- Derived summaries do not replace canonical contracts.

## Main areas

| Area | Purpose |
|---|---|
| `specs/` | Product, flow, interface, API, data, state, security, and traceability contracts |
| `architecture/decisions/` | Architecture decision records |
| `operations/` | Local setup, testing, evidence, release, backup, and rollback |

## Status labels

Use `IMPLEMENTED`, `PARTIAL`, `TODO / GAP`, `MANUAL_REQUIRED`, `BLOCKED`, and `FORBIDDEN / OUT_OF_SCOPE` consistently.
