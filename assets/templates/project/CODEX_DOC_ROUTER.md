# Codex document router

Read `../AGENTS.md`, `../PLAN.md`, and the nearest scoped `AGENTS.md` for every task. Then use this table.

| Task | Required documents |
|---|---|
| Product scope or requirements | `specs/product-spec.md`, `specs/business-flow-spec.md`, `specs/traceability-matrix.md` |
| Page or user interaction | Product spec, flow spec, page/interface contract, design and accessibility rules |
| API or backend behavior | Product spec, flow spec, API contract, state/data contract, security contract |
| Database or migration | State/data contract, migration rules, API contract, backup and rollback rules |
| Permissions or sensitive data | Security contract, API/interface contract, state/data ownership rules |
| Defect investigation | Relevant contract, current tests, test evidence, `../PLAN.md` |
| Testing or acceptance | `operations/testing-and-acceptance.md`, `operations/test-evidence-matrix.md`, traceability matrix |
| Release or rollback | `operations/release-runbook.md`, test evidence, affected contracts, `../PLAN.md` |
| Documentation structure | `README.md`, `DOCS_DICTIONARY.md`, this router, root and docs-scoped rules |

Add project-specific routes when new document responsibilities appear. Remove stale routes when documents move.
