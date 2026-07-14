<p align="center"><samp>PRODUCT DEFINITION → PLAN → IMPLEMENTATION → EVIDENCE → HANDOFF</samp></p>

<h1 align="center">SpecToDelivery</h1>

<p align="center"><strong>From product definition to verified delivery</strong></p>

<p align="center">A Codex Skill that keeps product intent, execution plans, engineering rules, and verification evidence in one repository.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2f855a.svg?style=flat-square"></a>
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-2563eb.svg?style=flat-square">
  <img alt="Workflow: PLAN and AGENTS" src="https://img.shields.io/badge/workflow-PLAN%20%2B%20AGENTS-7c3aed.svg?style=flat-square">
  <img alt="Helper scripts: Python standard library only" src="https://img.shields.io/badge/helpers-Python%20stdlib-3776ab.svg?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <a href="README.md">🇨🇳 中文</a> · <a href="README.en.md">🇺🇸 English</a>
</p>

The skill can establish a new project or audit an existing codebase before implementation continues. `PLAN.md` records the current execution state. The root `AGENTS.md` and any necessary scoped files define engineering rules. Approved intent stays separate from implementation evidence, so a written requirement does not pass as finished code.

The skill does not prescribe the project's programming language, framework, database, deployment platform, or documentation language. When a new project has no technology decision yet, it recommends one preferred approach from the product and delivery constraints. It adds one alternative only when a material trade-off exists. The user confirms choices that are expensive to reverse unless they explicitly delegate the decision. Python is used only by the helper scripts in this repository.

## Installation

You need Git and a Codex App, CLI, or IDE Extension version that supports Skills. The current [public Codex documentation](https://developers.openai.com/codex/concepts/customization) places personal skills in `$HOME/.agents/skills` and project-shared skills in `.agents/skills` inside the repository. The commands below follow that convention.

### Personal installation

A personal installation makes the skill available to all projects on the same machine.

macOS or Linux:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git \
  "$HOME/.agents/skills/spec-to-delivery"
```

Windows PowerShell:

```powershell
$skillsDir = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git `
  (Join-Path $skillsDir "spec-to-delivery")
```

Update a personal installation:

```bash
git -C "$HOME/.agents/skills/spec-to-delivery" pull --ff-only
```

In PowerShell, use:

```powershell
git -C (Join-Path $HOME ".agents\skills\spec-to-delivery") pull --ff-only
```

### Project-shared installation

To use the skill only in one repository, place it under that project's `.agents/skills` directory. A Git submodule keeps its version and upstream updates explicit:

```bash
git submodule add https://github.com/AlexGitHub0909/SpecToDelivery.git .agents/skills/spec-to-delivery
git commit -m "chore: add project delivery skill"
```

After cloning the project on another machine, run `git submodule update --init --recursive`. To move to a newer upstream version, run `git submodule update --remote .agents/skills/spec-to-delivery`, review the result, and commit the updated submodule pointer.

If the project does not use submodules, copy the skill into the same directory and commit it with the project, without retaining a nested `.git` directory.

Some installed versions and built-in tools still use `$CODEX_HOME/skills`, usually `~/.codex/skills` when `CODEX_HOME` is unset. If Codex already detects an existing installation, do not install a duplicate. Codex normally detects skill changes automatically; restart Codex if the skill does not appear.

The repository is self-contained. It does not require an MCP server or a separate plugin.

## Choose a working mode

| Your situation | Mode | What the skill does first |
|---|---|---|
| You have a PRD or requirements but little or no code | `GREENFIELD` | Establish the plan, scoped rules, specifications, and traceability before completing the first verifiable slice |
| Code and project documents already exist | `BROWNFIELD` | Audit Git, plans, documents, code, and tests before acting on confirmed gaps |
| You only need specifications and handoff material | `SPEC_ONLY` | Produce contracts, implementation slices, and acceptance evidence without changing application code |

## Load engineering rules on demand

The skill first infers the needed work areas from product material and repository evidence. It asks the user only when the evidence is insufficient and the answer would change scope, architecture, data ownership, release responsibility, or acceptance. It groups no more than three related questions at a time.

| Work area | Load its rules when the project needs |
|---|---|
| Website | Public pages, content distribution, search discovery, campaigns, documentation, or public forms |
| Frontend | Interactive web, mobile, or desktop interfaces and user flows |
| Backend | Server-side rules, authentication, jobs, queues, or private integrations |
| API | Stable programmatic interfaces for clients, partners, automation, or other systems |
| Database | Durable business state, accounts, history, reporting, search, or audit data |
| Operations | Deployment, environments, domains, background runtime, monitoring, release, or recovery ownership |

These six areas are not exhaustive. A library, CLI, data pipeline, model, embedded system, or another distinct responsibility can use a project-specific work area instead of being forced into the nearest category.

A work area is not a fixed directory. One directory may serve several areas, and one area may span several directories. The result is recorded in `PLAN.md` as `APPLIES`, `NOT_APPLICABLE`, `DEFERRED`, or `OPEN_DECISION`. The skill loads rules only for areas that apply or need a decision.

## Project governance

The supplied templates cover:

- project entry and local setup;
- root and scoped agent rules;
- on-demand work-area discovery and rule routing;
- current planning and change history;
- document routing and ownership;
- product scope, behavior, and system flows;
- requirement-to-code traceability;
- test and release evidence;
- architecture decisions and rollback.

The initializer creates a standard governance file skeleton. It does not decide the project's work areas or fill in owners, commands, and acceptance evidence. Use it for a new project, or for an existing repository that has deliberately adopted this layout, then replace the starter content with confirmed project facts. Otherwise, adapt the needed content to the repository's canonical files instead of creating a second documentation system.

## Use it

Invoke the skill with the product material or repository in scope:

```text
Use $spec-to-delivery to audit this repository, recover the current plan, and implement the next piece of work with current verification evidence.
```

For a new project:

```text
Use $spec-to-delivery to turn this PRD into a greenfield project. Infer which website, frontend, backend, API, database, and operations work areas apply from the product material, and ask me only about unresolved choices that would change scope or architecture. Then set up the plan, scoped agent rules, specs, traceability, and the first working slice.
```

For a spec-only handoff:

```text
Use $spec-to-delivery in SPEC_ONLY mode. Produce the contracts, implementation slices, acceptance evidence, and release considerations without changing application code.
```

## Initialize the governance files

The initializer copies missing templates and leaves existing files alone:

```bash
python3 scripts/init_project.py /path/to/project \
  --name "Project name" \
  --mode greenfield
```

Add repeatable `--scoped path/to/directory` arguments only when real directory-level rule boundaries exist. They do not imply a fixed frontend and backend layout.

Preview the changes first:

```bash
python3 scripts/init_project.py /path/to/project --name "Project name" --dry-run
```

Audit the result:

```bash
python3 scripts/audit_project.py /path/to/project
```

Warnings are expected immediately after initialization because the starter content is not a finished handoff. Before handoff, use strict mode; empty work-area routes, untouched starter text, and key empty tables become errors:

```bash
python3 scripts/audit_project.py /path/to/project --strict
```

Strict mode catches structural gaps and obvious unfinished starter content. It does not prove that the decisions are correct or the software works. These scripts check the standard layout supplied by this skill. Do not use missing standard filenames as proof that an older repository lacks equivalent governance. Its own `AGENTS.md`, test standards, and release runbook still decide which stack-specific commands to run.

## Boundaries

The skill does not treat a test pass as proof of deployment. It does not turn product text into an implementation claim, and it does not write to production or external systems without clear authority.

Readiness is reported as `SPEC_READY`, `IMPLEMENTED_LOCAL`, `VERIFIED_LOCAL`, `RELEASE_READY`, `DEPLOYED_VERIFIED`, or `BLOCKED_EXTERNAL`.

## Skill layout

```text
spec-to-delivery/
├── SKILL.md
├── README.md          # Chinese, shown by default on GitHub
├── README.en.md       # English
├── LICENSE            # MIT
├── agents/
├── references/        # Core rules and on-demand work-area rules
├── scripts/
├── tests/             # Regression tests for the helper scripts
└── assets/templates/project/
```

Codex follows `SKILL.md`. The two README files are for people who want to understand or maintain the skill.

## License

This project is available under the [MIT License](LICENSE). You may use, copy, modify, and distribute it as long as you retain the original copyright and license notice. The work is provided without warranty.
