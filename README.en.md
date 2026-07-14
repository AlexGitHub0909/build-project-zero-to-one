<p align="center"><samp>PRODUCT DEFINITION → PLAN → IMPLEMENTATION → EVIDENCE → HANDOFF</samp></p>

<h1 align="center">From product definition to verified delivery</h1>

<p align="center">A Codex Skill that keeps product intent, execution plans, engineering rules, and verification evidence in one repository.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2f855a.svg?style=flat-square"></a>
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-2563eb.svg?style=flat-square">
  <img alt="Workflow: PLAN and AGENTS" src="https://img.shields.io/badge/workflow-PLAN%20%2B%20AGENTS-7c3aed.svg?style=flat-square">
  <img alt="Python standard library only" src="https://img.shields.io/badge/Python-stdlib%20only-3776ab.svg?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <a href="README.md">🇨🇳 中文</a> · <a href="README.en.md">🇺🇸 English</a>
</p>

The skill can establish a new project or audit an existing codebase before implementation continues. `PLAN.md` records the current execution state. The root `AGENTS.md` and any necessary scoped files define engineering rules. Approved intent stays separate from implementation evidence, so a written requirement does not pass as finished code.

## Installation

You need Git and a Codex App, CLI, or IDE Extension version that supports Skills. The current [public Codex documentation](https://developers.openai.com/codex/concepts/customization) places personal skills in `$HOME/.agents/skills` and project-shared skills in `.agents/skills` inside the repository. The commands below follow that convention.

### Personal installation

A personal installation makes the skill available to all projects on the same machine.

macOS or Linux:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AlexGitHub0909/build-project-zero-to-one.git \
  "$HOME/.agents/skills/build-project-zero-to-one"
```

Windows PowerShell:

```powershell
$skillsDir = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
git clone https://github.com/AlexGitHub0909/build-project-zero-to-one.git `
  (Join-Path $skillsDir "build-project-zero-to-one")
```

Update a personal installation:

```bash
git -C "$HOME/.agents/skills/build-project-zero-to-one" pull --ff-only
```

In PowerShell, use:

```powershell
git -C (Join-Path $HOME ".agents\skills\build-project-zero-to-one") pull --ff-only
```

### Project-shared installation

To use the skill only in one repository, place it under that project's `.agents/skills` directory. A Git submodule keeps its version and upstream updates explicit:

```bash
git submodule add https://github.com/AlexGitHub0909/build-project-zero-to-one.git .agents/skills/build-project-zero-to-one
git commit -m "chore: add project delivery skill"
```

After cloning the project on another machine, run `git submodule update --init --recursive`. To move to a newer upstream version, run `git submodule update --remote .agents/skills/build-project-zero-to-one`, review the result, and commit the updated submodule pointer.

If the project does not use submodules, copy the skill into the same directory and commit it with the project, without retaining a nested `.git` directory.

Some installed versions and built-in tools still use `$CODEX_HOME/skills`, usually `~/.codex/skills` when `CODEX_HOME` is unset. If Codex already detects an existing installation, do not install a duplicate. Codex normally detects skill changes automatically; restart Codex if the skill does not appear.

The repository is self-contained. It does not require an MCP server or a separate plugin.

## Choose a working mode

| Your situation | Mode | What the skill does first |
|---|---|---|
| You have a PRD or requirements but little or no code | `GREENFIELD` | Establish the plan, scoped rules, specifications, and traceability before completing the first verifiable slice |
| Code and project documents already exist | `BROWNFIELD` | Audit Git, plans, documents, code, and tests before acting on confirmed gaps |
| You only need specifications and handoff material | `SPEC_ONLY` | Produce contracts, implementation slices, and acceptance evidence without changing application code |

## Project governance

The supplied templates cover:

- project entry and local setup;
- root and scoped agent rules;
- current planning and change history;
- document routing and ownership;
- product scope, behavior, and system flows;
- requirement-to-code traceability;
- test and release evidence;
- architecture decisions and rollback.

The default initializer creates the full governance baseline. Use it for a new project, or for an existing repository that has deliberately adopted this layout. Otherwise, adapt individual templates to the repository's canonical files instead of creating a second documentation system.

## Use it

Invoke the skill with the product material or repository in scope:

```text
Use $build-project-zero-to-one to audit this repository, recover the current plan, and implement the next piece of work with current verification evidence.
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
├── README.md          # Chinese, shown by default on GitHub
├── README.en.md       # English
├── LICENSE            # MIT
├── agents/
├── references/
├── scripts/
└── assets/templates/project/
```

Codex follows `SKILL.md`. The two README files are for people who want to understand or maintain the skill.

## License

This project is available under the [MIT License](LICENSE). You may use, copy, modify, and distribute it as long as you retain the original copyright and license notice. The work is provided without warranty.
