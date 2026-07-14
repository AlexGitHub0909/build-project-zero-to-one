# AGENTS.md governance

## Rule hierarchy

Every managed project needs a root `AGENTS.md`. Add scoped files only where local rules materially differ.

For a file being changed, read:

1. the root `AGENTS.md`;
2. each scoped `AGENTS.md` between the root and that file;
3. the nearest scoped file last.

Child rules add local detail. They must not silently weaken a root safety, evidence, credential, or external-write boundary.

## When to add a scoped file

Add one when a directory has one or more of these:

- a different framework or language;
- a separate application or user surface;
- a distinct security, permission, data, or visibility boundary;
- its own architecture and reuse rules;
- different validation, build, or release commands;
- special documentation, script, database, or operations behavior.

Do not add an `AGENTS.md` to every folder. A rule file should resolve a real difference.

## Root file content

The root file should cover:

- product purpose and current stage;
- hard domain and capability boundaries;
- current technology facts;
- approved technology and documentation language choices, plus the owner of any open decision;
- fact sources and document routing;
- minimal implementation and reuse rules;
- defect and change-control workflow;
- Git, credential, external-write, and production rules;
- the scoped-rule routing table;
- project-wide verification and completion rules;
- clear counterexamples.

## Scoped file content

A scoped file should cover:

- scope and inherited rules;
- directory responsibility and structure;
- patterns and components to reuse;
- local security, data, and visibility boundaries;
- documents to read;
- implementation workflow;
- required commands;
- definition of done;
- actions that are not allowed.

Avoid copying long root sections. Keep the shared rule at the highest useful level.

## Rule changes

When a rule changes:

1. update the correct root or scoped file;
2. update document routing if responsibility changed;
3. map the rule to an automated check or a named manual review;
4. update `PLAN.md` and affected contracts;
5. run rule and documentation checks;
6. verify that narrower rules still inherit the root boundary.

A rule without a completion condition or check is guidance, not a reliable guardrail.
