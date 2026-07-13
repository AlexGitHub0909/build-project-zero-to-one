# Documentation dictionary

| Document | Audience | Responsibility | Update when | Does not prove |
|---|---|---|---|---|
| `README.md` | Contributors and Codex | Documentation entry and fact boundaries | Document structure changes | Implementation status |
| `CODEX_DOC_ROUTER.md` | Codex and contributors | Maps task types to required documents | Task routing or document responsibility changes | Task completion |
| `specs/product-spec.md` | Product and engineering | Approved users, scope, capabilities, and boundaries | Product behavior changes | That code is implemented |
| `specs/business-flow-spec.md` | Product, engineering, QA | User and system flows, decisions, failures, and outcomes | Flow or state behavior changes | Current runtime behavior |
| `specs/traceability-matrix.md` | Product, engineering, QA | Requirement-to-implementation-and-evidence map | Requirements, code, tests, or evidence change | Release approval by itself |
| `operations/testing-and-acceptance.md` | Engineering and QA | Test strategy and required commands | Test policy or stack commands change | That checks were run |
| `operations/test-evidence-matrix.md` | Engineering, QA, owners | Current automated and manual evidence | Evidence or status changes | That manual items passed |
| `operations/release-runbook.md` | Engineering and operations | Release, verification, backup, and rollback procedure | Environments or release flow change | Authority to deploy |
| `architecture/decisions/*.md` | Engineering | Why a major technical choice was made | A new decision or supersession occurs | Current implementation unless verified |
