# Documentation dictionary

| Document | Audience | Responsibility | Update when | Does not prove |
|---|---|---|---|---|
| `README.md` | Contributors and delivery agents | Documentation entry and fact boundaries | Document structure changes | Implementation status |
| `DOC_ROUTER.md` | Delivery agents and contributors | Maps task types to required documents | Task routing or document responsibility changes | Task completion |
| `specs/product-spec.md` | Project owners and engineering | Approved actors, scope, capabilities, and boundaries | Intended behavior changes | That code is implemented |
| `specs/behavior-and-flow-spec.md` | Product, engineering, QA | Observable behavior, system flows, decisions, failures, and outcomes | Flow or state behavior changes | Current runtime behavior |
| `specs/prototype-review.md` when present | Product owner, design, engineering | Human review of visual, interaction, workflow, or contract direction | The reviewed artifact or decision changes | Implementation, testing, or release |
| `specs/traceability-matrix.md` | Product, engineering, QA | Requirement-to-implementation-and-evidence map | Requirements, code, tests, or evidence change | Release approval by itself |
| `operations/testing-and-acceptance.md` | Engineering and QA | Test strategy and required commands | Test policy or stack commands change | That checks were run |
| `operations/test-evidence-matrix.md` | Engineering, QA, owners | Current automated and manual evidence | Evidence or status changes | That manual items passed |
| `operations/release-runbook.md` when present | Engineering and operations | Release, verification, backup, and rollback procedure | Environments or release flow change | Authority to deploy |
| `architecture/decisions/*.md` | Engineering | Why a major technical choice was made | A new decision or supersession occurs | Current implementation unless verified |
