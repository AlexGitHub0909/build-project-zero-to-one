# Build Project Zero to One

[简体中文](README.zh-CN.md)

This Codex skill turns a product brief or an existing repository into a project that can be planned, implemented, checked, and handed over without relying on chat history.

It is opinionated about project control: every managed project needs a current `PLAN.md`, a root `AGENTS.md`, and scoped `AGENTS.md` files where local engineering rules differ. It also keeps product intent separate from implementation evidence, so a written requirement never passes as finished code.

## Install from GitHub

Clone the repository into your personal Codex skills directory:

```bash
git clone https://github.com/AlexGitHub0909/build-project-zero-to-one.git \
  ~/.codex/skills/build-project-zero-to-one
```

If you already installed it with Git, update it in place:

```bash
git -C ~/.codex/skills/build-project-zero-to-one pull --ff-only
```

Start a new Codex task after installation so the skill list refreshes. The repository is self-contained; it does not require an MCP server or a separate plugin.

## When to use it

Use `$build-project-zero-to-one` when you want Codex to:

- start a software project from a PRD, brief, or set of requirements;
- recover the state of an existing repository and continue the work;
- produce an implementation-ready spec and handoff without writing application code;
- add or repair project planning, document routing, traceability, test evidence, and release rules;
- implement the next vertical slice and update the repository facts as it goes.

The skill supports three modes:

| Mode | Use it for |
|---|---|
| `GREENFIELD` | A new project with product material but little or no code |
| `BROWNFIELD` | An existing repository that must be audited before changes |
| `SPEC_ONLY` | A specification and handoff package with no application-code changes |

## What it puts in a project

The supplied templates cover:

- project entry and local setup;
- root and scoped agent rules;
- current planning and change history;
- document routing and ownership;
- product scope and business flows;
- requirement-to-code traceability;
- test and release evidence;
- architecture decisions and rollback.

The default initializer creates the full governance baseline. Use it for a new project, or for an existing repository that has deliberately adopted this layout. Otherwise, adapt individual templates to the repository's canonical files instead of creating a second documentation system.

## Use it

Invoke the skill with the product material or repository in scope:

```text
Use $build-project-zero-to-one to audit this repository, recover the current plan, and implement the next verified product slice.
```

For a new project:

```text
Use $build-project-zero-to-one to turn this PRD into a greenfield project. Set up the plan, agent rules, specs, traceability, and the first working slice.
```

For a spec-only handoff:

```text
Use $build-project-zero-to-one in SPEC_ONLY mode. Produce the contracts, implementation slices, acceptance evidence, and release considerations without changing application code.
```

## Initialize the governance files

The initializer copies missing templates and leaves existing files alone:

```bash
python3 scripts/init_project.py /path/to/project \
  --name "Project name" \
  --mode greenfield \
  --scoped backend \
  --scoped frontend
```

Preview the changes first:

```bash
python3 scripts/init_project.py /path/to/project --name "Project name" --dry-run
```

Audit the result:

```bash
python3 scripts/audit_project.py /path/to/project
```

These scripts check the standard layout supplied by this skill. Do not use missing standard filenames as proof that an older repository lacks equivalent governance. Its own `AGENTS.md`, test standards, and release runbook still decide which stack-specific commands to run.

## Boundaries

The skill does not treat a test pass as proof of deployment. It does not turn product text into an implementation claim, and it does not write to production or external systems without clear authority.

Readiness is reported as `SPEC_READY`, `IMPLEMENTED_LOCAL`, `VERIFIED_LOCAL`, `RELEASE_READY`, `DEPLOYED_VERIFIED`, or `BLOCKED_EXTERNAL`.

## Skill layout

```text
build-project-zero-to-one/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/
├── references/
├── scripts/
└── assets/templates/project/
```

Codex follows `SKILL.md`. The two README files are for people who want to understand or maintain the skill.

Before publishing a fork, review the templates, replace repository-specific examples, and choose a license that fits how you want others to use the work.
