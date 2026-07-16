# Project document router

Read `../AGENTS.md`, `../PLAN.md`, and the nearest scoped `AGENTS.md` for every task. Then use this table.

| Task | Required documents |
|---|---|
| Product scope or requirements | `specs/product-spec.md`, `specs/behavior-and-flow-spec.md`, `specs/traceability-matrix.md` |
| Prototype, interaction, or human product review | `specs/prototype-review.md` when present, product spec, flow spec, interface or API contract, `../PLAN.md` |
| Public website, content, or discovery | Product spec, page/interface contract, approved content facts, SEO, accessibility, performance, and privacy rules |
| Interactive frontend behavior | Product spec, flow spec, interface contract, design system, accessibility, and request-state rules |
| Backend service, job, or integration | Product spec, flow spec, state/data contract, security contract, integration and failure rules |
| API or webhook behavior | API contract, authentication and authorization rules, state/data contract, compatibility and consumer evidence |
| Database or migration | State/data contract, migration rules, API contract, backup and rollback rules |
| Deployment, runtime, or incident | Release runbook, environment and observability rules, test evidence, backup and recovery evidence, `../PLAN.md` |
| Permissions or sensitive data | Security contract, API/interface contract, state/data ownership rules |
| Defect investigation | Relevant contract, current tests, test evidence, `../PLAN.md` |
| Testing or acceptance | `operations/testing-and-acceptance.md`, `operations/test-evidence-matrix.md`, traceability matrix |
| Release or rollback | `operations/release-runbook.md` when present, test evidence, affected contracts, `../PLAN.md`; create the runbook before `RELEASE_READY` |
| Documentation structure | `README.md`, `DOCS_DICTIONARY.md`, this router, root and docs-scoped rules |

Add project-specific routes when new document responsibilities appear. Remove stale routes when documents move.
