# Human review and prototyping

## Purpose

The human user owns product intent, material trade-offs, and acceptance. The agent prepares options, artifacts, implementation, and evidence. Do not turn silence into approval when a decision would change scope, workflow, visual direction, data responsibility, cost, or release risk.

## Choose the smallest useful confirmation artifact

Use a confirmation artifact before implementation when words alone leave a material ambiguity that would be expensive to discover in code.

| Product surface | Useful confirmation artifact |
|---|---|
| Website or visual interface | Sitemap, user flow, wireframe, high-fidelity screen, or clickable prototype |
| Mobile or desktop application | Screen map, navigation flow, state prototype, or device-specific interaction demo |
| CLI | Command synopsis, example transcript, prompts, errors, and exit behavior |
| API or integration | Request and response examples, schema mock, webhook fixture, or sequence diagram |
| Backend workflow or automation | State diagram, decision table, dry-run output, or operator workflow |
| Data or reporting product | Data sample, field dictionary, calculation example, or report mock |

A prototype is not mandatory for a text-only change, a well-defined low-risk adjustment, or a non-visual task whose contract already settles the behavior. Record why it is not needed when skipping it could surprise the user.

## Select prototype fidelity

- Use a flow or low-fidelity wireframe to settle scope, navigation, hierarchy, and missing states.
- Use a high-fidelity or clickable prototype only when visual direction, responsive behavior, interaction detail, or stakeholder review needs it.
- Reuse supplied designs and the project's existing design system before creating a new visual direction.
- Keep prototype effort proportional to the decision. Do not build production code merely to ask whether the layout is acceptable.
- Choose the tool from the active environment. Figma, HTML, images, diagrams, and Markdown are possible formats, not required dependencies.

## Review gate

Before asking for approval, show:

- the decision being requested;
- the artifact and the flows or states it covers;
- assumptions, alternatives, and known omissions;
- the acceptance points the human should inspect;
- what implementation will begin after approval.

Record the result as `DRAFT`, `REVIEW_REQUIRED`, `APPROVED`, `CHANGES_REQUESTED`, or `NOT_REQUIRED`. Name the reviewer and evidence location. Approval applies only to the stated scope and version of the artifact.

Do not begin an expensive or hard-to-reverse implementation while the required prototype remains `REVIEW_REQUIRED` or `CHANGES_REQUESTED`. A user may explicitly authorize implementation before approval; record that exception and the rework risk in `PLAN.md`.

## Fact boundary

A prototype confirms intended behavior or direction. It is not evidence that the product has been implemented, tested, released, or deployed. After implementation, verify the real artifact against the approved prototype and record intentional differences.
