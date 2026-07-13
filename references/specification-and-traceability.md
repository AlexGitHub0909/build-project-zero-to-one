# Specification and traceability

## Contents

- Required information
- Suggested document map
- Requirement IDs
- Vertical slices
- Change impact
- Scaling the package

## Required information

Capture this information even when a small project combines it into fewer files:

- product purpose, users, problems, outcomes, scope, and non-goals;
- roles, permissions, visibility, and sensitive data boundaries;
- business flows, states, transitions, errors, and recovery paths;
- pages or interfaces, user actions, loading, empty, error, and disabled states;
- APIs, inputs, outputs, authentication, authorization, errors, and idempotency;
- entities, relationships, ownership, retention, migrations, units, and precision where relevant;
- external integrations, environments, credentials, timeouts, retries, and production-write boundaries;
- acceptance evidence and release impact.

## Suggested document map

Use as many files as the project needs, not as many as the template offers.

| Document | Responsibility |
|---|---|
| Product spec | Purpose, users, scope, non-goals, capabilities, and boundaries |
| Business flow spec | User and system steps, decisions, failures, and outcomes |
| State and data contract | Entities, state transitions, invariants, ownership, and amounts |
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
-> business flow
-> interface or API contract
-> state and data rule
-> PLAN task
-> implementation
-> automated or manual evidence
-> CHANGELOG entry
-> release evidence
```

Use `PARTIAL`, `TODO / GAP`, `MANUAL_REQUIRED`, `BLOCKED`, and `FORBIDDEN / OUT_OF_SCOPE` when the chain is incomplete.

## Vertical slices

A useful slice starts with a user or operator action and ends with an observable result. It includes the contracts, code, data, errors, tests, and documentation needed for that result.

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

For a small project, combine related contracts while keeping clear headings and ownership. Split documents when they have different audiences, update triggers, or evidence sources. Maintain `docs/README.md`, `docs/CODEX_DOC_ROUTER.md`, and `docs/DOCS_DICTIONARY.md` once the project has more than a handful of documents or multiple work areas.
