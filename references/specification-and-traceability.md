# Specification and traceability

## Contents

- Required information
- Suggested document map
- Requirement IDs
- Implementation slices
- Change impact
- Scaling the package

## Required information

Capture what applies to the project. Mark an area as not applicable instead of inventing details. A small project may combine several areas in one file.

- project purpose, actors, problems, outcomes, scope, and non-goals;
- roles, permissions, visibility, and sensitive data boundaries;
- observable behavior, workflows, states, transitions, errors, and recovery paths;
- user interfaces, actions, loading, empty, error, and disabled states when present;
- programmatic interfaces, inputs, outputs, authentication, authorization, errors, and idempotency when present;
- entities, relationships, ownership, retention, migrations, units, and precision where relevant;
- external integrations, environments, credentials, timeouts, retries, and production-write boundaries;
- acceptance evidence and release impact.

## Suggested document map

Use as many files as the project needs, not as many as the template offers.

| Document | Responsibility |
|---|---|
| Product spec | Purpose, actors, scope, non-goals, capabilities, and boundaries |
| Behavior and flow spec | Observable behavior, system steps, decisions, failures, and outcomes |
| State and data contract | Entities, state transitions, invariants, ownership, units, and precision |
| Frontend or interface contract | Pages, fields, actions, states, visibility, and accessibility |
| API contract | Routes, requests, responses, permissions, errors, and examples |
| Security contract | Roles, credentials, data exposure, audit, and external effects |
| Traceability matrix | Requirement-to-code-and-evidence map |

## Requirement IDs

Give material behavior stable IDs. Choose labels that fit the project instead of assuming a particular product domain. Neutral examples:

```text
REQ-AREA-001
FLOW-JOURNEY-002
API-RESOURCE-003
TEST-BEHAVIOR-004
```

Do not renumber IDs just to make the list tidy. Retire or supersede them with a note so history remains traceable.

## Traceability

For each requirement, map:

```text
product intent
-> behavior or flow
-> interface or API contract
-> state and data rule
-> PLAN task
-> implementation
-> automated or manual evidence
-> CHANGELOG entry
-> release evidence
```

Use evidence IDs such as `EV-AREA-001` when the project maintains a test evidence matrix. Keep the referenced ID synchronized with that matrix; use a direct path or procedure only when a separate evidence row would add no value.

Use `PARTIAL`, `TODO / GAP`, `MANUAL_REQUIRED`, `BLOCKED`, and `FORBIDDEN / OUT_OF_SCOPE` when the chain is incomplete.

## Implementation slices

A useful slice starts with an observable trigger and ends with an observable result. It includes the contracts, code, data, errors, tests, and documentation needed for that result.

Avoid plans that finish all database work, then all APIs, then all pages without proving a working path. Shared infrastructure can come first when a slice cannot work without it, but keep that dependency explicit.

## Change impact

When product intent changes, inspect the affected:

- requirement IDs and product scope;
- flows and state transitions;
- pages, API contracts, data, permissions, and errors;
- plan and task order;
- implementation and migrations;
- tests and evidence matrix;
- manuals, release scope, and rollback.

Update the canonical contract first. Do not patch only the summary or the UI copy.

## Scale the package

For a small project, combine related contracts while keeping clear headings and ownership. Split documents when they have different audiences, update triggers, or evidence sources. Maintain `docs/README.md`, `docs/DOC_ROUTER.md`, and `docs/DOCS_DICTIONARY.md` once the project has more than a handful of documents or multiple work areas. Reuse an existing equivalent router instead of creating a parallel file.
