# PLAN.md governance

## Purpose

`PLAN.md` is the durable record of current execution. It lets a new session recover the active phase, the current task, the evidence already gathered, and the next action without relying on conversation history.

## Required sections

Keep these sections near the top:

- Current status
- Current task
- Goal and non-goals
- Current evidence
- Implementation approach
- Risks and boundaries
- Acceptance evidence
- Rollback or stop conditions
- Now, next, and later work
- Recent completions
- Blockers and external actions
- Validation baseline

## Update rules

Update `PLAN.md`:

- before a multi-step or high-risk change;
- when the active task changes;
- when evidence invalidates the planned approach;
- when implementation changes approved behavior;
- when the user confirms or delegates a material technology or documentation language decision;
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
