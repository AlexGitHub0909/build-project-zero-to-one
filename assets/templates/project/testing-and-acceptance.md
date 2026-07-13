# Testing and acceptance

## Test strategy

Define the project test layers, supported environments, fixtures, and evidence rules.

## Risk levels

| Risk | Examples | Required evidence |
|---|---|---|
| Low | Copy, documentation, isolated style | Targeted review and relevant static checks |
| Medium | Local behavior, API output, component state | Focused automated tests and scoped regression |
| High | Schema, permissions, state transitions, data integrity, external writes, release flow | Contract review, focused tests, broader regression, rollback and environment evidence |

## Commands

| Area | Command | What it checks | Constraints |
|---|---|---|---|

## Evidence rules

- Run checks after the final change.
- Read current output before reporting a pass.
- Record commands that were skipped or blocked.
- Do not use a lower test layer to claim a higher one passed.
- Keep manual evidence separate from automation.

## Completion

Link acceptance to `../specs/traceability-matrix.md` and `test-evidence-matrix.md`.
