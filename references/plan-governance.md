# PLAN.md governance

## Purpose

`PLAN.md` is the durable record of current execution. It lets a new session recover the active phase, the current task, the evidence already gathered, and the next action without relying on conversation history.

## Required sections

Keep these sections near the top:

- Current status
- Current task
- Goal and non-goals
- Expected outcome or value signal
- Current evidence
- Implementation approach
- Risks and boundaries
- Human decisions and review gates
- Acceptance evidence
- Rollback or stop conditions
- Now, next, and later work
- Recent completions
- Blockers and external actions
- Validation baseline

For `GREENFIELD`, a material architecture change, or a change in product responsibility, add an applicable-work-areas table near current status. Record only areas that apply, remain open, are deferred, or would surprise a new contributor if omitted. Keep detailed rules in contracts and `AGENTS.md`.

Add a capability-decisions table only when a specialized Skill, plugin, connector, external service, or artifact tool affects delivery, permissions, acceptance evidence, or fallback. Record the need, selected capability, whether it is required, current availability and authority, and the fallback or blocker. Do not inventory routine repository commands.

Name the acceptance owner for the active task. Add a next checkpoint only when a date, decision, review, dependency, or release gate changes how the work should proceed. For material risks, record the likely impact, response, owner, and trigger or stop condition inside the current task; do not create a separate risk register by default.

Add a human-review row when a product decision, prototype, mock, transcript, API example, diagram, or dry run must be reviewed before implementation. Record the artifact, whether review is required, reviewer, status, and evidence. Do not treat agent output or user silence as approval.

## Update rules

Update `PLAN.md`:

- before a multi-step or high-risk change;
- when the active task changes;
- when evidence invalidates the planned approach;
- when implementation changes approved behavior;
- when approved scope or approach changes, with the reason and effect on delivery, cost, or acceptance;
- when the user confirms or delegates a material technology or documentation language decision;
- when a work area becomes applicable, deferred, not applicable, or unresolved;
- when a required capability, permission, or fallback changes;
- when a human review artifact is requested, approved, rejected, waived, or superseded;
- when a blocker or manual action appears or clears;
- after verification, with actual commands and results;
- after completion, with the next concrete task.

If the plan says A and implementation becomes B, change the plan before calling the work complete. Record the reason when it affects future implementation or rollback.

## Keep the plan readable

- Put current status first.
- Keep one active task.
- Move old detail into a compact recent-completions table or an archive when it obscures current work.
- Link to contracts and evidence rather than copying them.
- Do not use the plan as an API contract, design system, test case library, or changelog.
- When a completed task produces a lesson that changes future work, update the relevant `AGENTS.md`, contract, or automated check instead of keeping a separate lessons log by default.

## Existing trackers

When a project uses an external tracker, keep `PLAN.md` as the local execution snapshot. Link to external items without copying the full backlog. Do not write to the external system unless the user authorizes it.

## High-risk change package

For work that crosses subsystems or changes APIs, schemas, permissions, state machines, data integrity, external integration behavior, or release flow, record a lightweight change package inside `PLAN.md` and the affected contracts:

- goal and non-goal;
- current evidence;
- behavior added, modified, or removed;
- implementation path and dependencies;
- risk and rollback;
- acceptance evidence;
- stop conditions.

Do not create a second long-lived proposal system for ordinary changes.
