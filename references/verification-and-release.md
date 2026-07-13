# Verification and release

## Risk-based verification

Select checks from the actual change, repository rules, and failure modes. Do not run a large generic suite as a substitute for understanding scope.

| Change | Minimum evidence |
|---|---|
| Documentation or copy | Targeted fact review, link/path check, formatting check, secret scan where relevant |
| Low-risk code | Targeted test, type/lint/build check required by the scoped rules |
| Defect | Failing evidence, first divergence, regression evidence, minimal fix, fresh pass |
| Interface, schema, permission, state, high-impact data, or external integration | Contract update, focused tests, broader regression, migration or compatibility review, rollback condition |
| Release tooling or production incident | Current environment evidence, adjacent-path audit, dry run, failure logging, verify path, rollback path, repeatability |

## Evidence rules

- Read current output before reporting a pass.
- Do not reuse a result from before the change.
- State which checks were not run and why.
- Keep manual evidence separate from automated evidence.
- A backend test does not prove a browser flow.
- A local build does not prove production deployment.
- A health endpoint does not prove authenticated or stateful user paths.
- A completed form does not prove release approval.

## Test and evidence matrix

Track at least:

- requirement or risk ID;
- priority;
- environment;
- automated or manual type;
- command, test, or procedure;
- expected result;
- current status;
- evidence location;
- owner and blocker when incomplete.

Do not treat `TODO`, `PARTIAL`, or `MANUAL_REQUIRED` as a release pass.

## Release readiness

Before `RELEASE_READY`, confirm:

- Git and artifact source are known;
- environment and secret requirements are documented without exposing values;
- release impact is understood;
- pending migrations and compatibility are reviewed;
- backups and rollback targets are usable;
- queues, schedulers, workers, or background jobs are included when relevant;
- health and version evidence identify the deployed revision;
- post-release checks cover the changed path;
- manual, external, and owner decisions are recorded;
- no `NO_GO` or technical blocker remains.

## Production actions

Treat production writes, destructive migrations, third-party side effects, paid services, external messages, remote document writes, and Git pushes as separate authorities. A request to build or verify does not automatically authorize them.

When an action is authorized, preserve:

- the target and expected revision;
- preflight output;
- backup or rollback evidence;
- the exact execution result;
- post-release health and affected-flow checks;
- unresolved risks and owner decisions.

## Readiness levels

| Level | Evidence |
|---|---|
| `SPEC_READY` | Contracts, traceability, slices, acceptance, and unresolved decisions are usable |
| `IMPLEMENTED_LOCAL` | The current scope exists in code, but verification is incomplete |
| `VERIFIED_LOCAL` | Current local checks support the implemented claims |
| `RELEASE_READY` | Impact, environment, backup, rollback, and release gates are ready |
| `DEPLOYED_VERIFIED` | The expected revision is live and the affected paths were checked in the target environment |
| `BLOCKED_EXTERNAL` | A named external dependency prevents the next level |
