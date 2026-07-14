<p align="center"><samp>PRODUCT DEFINITION → PLAN → IMPLEMENTATION → EVIDENCE → HANDOFF</samp></p>

<h1 align="center">SpecToDelivery</h1>

<p align="center"><strong>From product definition to verified delivery</strong></p>

<p align="center">Connect the PRD, execution plan, engineering rules, implementation, and verification evidence in one delivery workflow.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2f855a.svg?style=flat-square"></a>
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-2563eb.svg?style=flat-square">
  <img alt="Workflow: PLAN and AGENTS" src="https://img.shields.io/badge/workflow-PLAN%20%2B%20AGENTS-7c3aed.svg?style=flat-square">
  <img alt="Helper scripts: Python standard library only" src="https://img.shields.io/badge/helpers-Python%20stdlib-3776ab.svg?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <a href="README.md">🇨🇳 中文</a> · <a href="README.en.md">🇺🇸 English</a>
</p>

SpecToDelivery is a single Codex Skill for software project delivery. It can establish a project from product material, recover the current state of an existing repository before implementation continues, or produce an implementation-ready specification without changing code.

It does not prescribe a programming language, framework, database, or deployment platform. It keeps existing technical choices when they are settled. When they are open, it recommends one preferred approach from the product and delivery constraints. The user still confirms decisions that are expensive to reverse unless they explicitly delegate that authority to Codex.

## Quick start

Install from Codex:

```text
Use $skill-installer to install the skill at the repository root of
https://github.com/AlexGitHub0909/SpecToDelivery and name it spec-to-delivery.
```

Then give Codex a PRD, requirements document, or target repository:

```text
Use $spec-to-delivery to audit the current material, establish or recover PLAN.md, the root AGENTS.md,
and any necessary scoped AGENTS.md files,
then implement the next piece of work with current verification evidence.
```

You can also use the [manual installation](#installation-and-updates) instructions below.

## When to use it

| Current situation | Mode | First action |
|---|---|---|
| You have a PRD or requirements but little or no code | `GREENFIELD` | Establish the plan, engineering rules, specifications, and traceability before completing the first verifiable slice |
| Code and project documents already exist | `BROWNFIELD` | Audit Git, plans, documents, code, and tests before acting on confirmed gaps |
| You only need specifications and handoff material | `SPEC_ONLY` | Produce implementation-ready contracts, work slices, and acceptance evidence without changing application code |

## How it works

| Stage | What happens | Primary record |
|---|---|---|
| Recover facts | Inspect Git, existing rules, plans, documents, code, and tests | Current repository evidence |
| Confirm scope | Choose the project mode and determine which engineering work areas apply | `PLAN.md` |
| Establish constraints | Record the active task, directory ownership, validation commands, and prohibited actions | Root and scoped `AGENTS.md` files |
| Specify and implement | Split requirements into observable, testable end-to-end slices | Product specs, flow specs, traceability, and code |
| Verify and hand off | Run current checks and update facts, status, rollback, and the next task | `PLAN.md`, test evidence, and `CHANGELOG.md` |

Each cycle advances one active slice. Finishing a slice does not mean the project is complete, and passing tests does not prove deployment.

## Core rules

- Keep `PLAN.md` as the current execution record. Update it when the task, result, evidence, blocker, or next step changes.
- Give the active slice an expected outcome or value signal, an acceptance owner, and a next checkpoint when it affects progress. Do not invent a KPI to fill a template.
- Track only material risks that can affect the current delivery, with their impact, response, owner, and trigger. Do not create a separate risk register by default.
- Give every project a root `AGENTS.md`. Add a scoped file when a directory has its own stack, application boundary, data boundary, validation commands, or release process.
- Keep intended product behavior separate from implementation facts. Contracts define the target; code, Git, tests, and runtime results show the current implementation.
- When approved scope or approach changes, record the reason and its effect on delivery, cost, or acceptance. Put reusable lessons into the relevant rule, contract, or automated check.
- Reuse the repository's existing structure, dependencies, components, services, and documents before adding another abstraction or a parallel fact source.
- Do not deploy, write to external systems, buy services, use real credentials, or make destructive data changes without clear authority.

## Load engineering rules on demand

The skill infers needed work areas from product material and repository evidence. It asks the user only when the evidence is insufficient and the answer would change scope, architecture, data ownership, release responsibility, or acceptance. When confirmation is needed, it groups no more than three related questions and uses product language instead of presenting unexplained technology choices.

| Work area | Use it for |
|---|---|
| Website | Public pages, content distribution, search discovery, campaigns, documentation, or public forms |
| Frontend | Interactive web, mobile, or desktop interfaces and user flows |
| Backend | Server-side rules, authentication, jobs, queues, or private integrations |
| API | Stable programmatic interfaces for clients, partners, automation, or other systems |
| Database | Durable business state, accounts, history, reporting, search, or audit data |
| Operations | Deployment, environments, domains, background runtime, monitoring, release, or recovery ownership |

These six areas are not a fixed architecture. A library, CLI, data pipeline, model, embedded system, or another distinct responsibility can use a project-specific work area. A work area is not a directory: one directory may serve several areas, and one area may span several directories.

## Use Skills and plugins when needed

A project may use Skills, plugins, connectors, or specialist tools already available in the environment, but they are not default dependencies. Define the result first, then choose a capability that can produce and verify it.

| Capability type | Treatment |
|---|---|
| Existing project commands, scripts, and dependencies | Prefer them and follow the nearest `AGENTS.md` |
| Optional specialist capability | Use it for work such as design, browser verification, or document handling while keeping a normal fallback |
| Required delivery capability | Record availability, authority, owner, and fallback in `PLAN.md`; mark a missing dependency as a blocker |
| Organization- or project-specific integration | Keep credentials, accounts, internal addresses, and operating rules in the project repository |

Read the capability's instructions before use and check permissions, cost, network access, and external side effects. Do not install or enable a plugin, create an external account, or write to a remote system without clear authority. A successful tool run proves that the tool ran; the project still has to validate the resulting artifact or system state.

## Other prompts

Start from product material:

```text
Use $spec-to-delivery to turn this PRD into a GREENFIELD project.
Infer the applicable engineering work areas and ask only about unresolved choices that change scope or architecture.
Then establish PLAN, scoped AGENTS, specifications, and traceability before completing the first working slice.
```

Prepare a specification-only handoff:

```text
Use $spec-to-delivery in SPEC_ONLY mode.
Produce product contracts, implementation slices, acceptance evidence, and release considerations without changing application code.
```

## Installation and updates

The [Codex Skills documentation](https://learn.chatgpt.com/docs/build-skills) uses `$HOME/.agents/skills` for personal skills and `.agents/skills` inside a repository for shared skills. If your Codex installation already discovers this skill from another supported location, do not install a duplicate.

<details>
<summary>Personal installation on macOS or Linux</summary>

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git \
  "$HOME/.agents/skills/spec-to-delivery"
```

Update:

```bash
git -C "$HOME/.agents/skills/spec-to-delivery" pull --ff-only
```

</details>

<details>
<summary>Personal installation on Windows PowerShell</summary>

```powershell
$skillsDir = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git `
  (Join-Path $skillsDir "spec-to-delivery")
```

Update:

```powershell
git -C (Join-Path $HOME ".agents\skills\spec-to-delivery") pull --ff-only
```

</details>

<details>
<summary>Project-shared installation</summary>

Add the skill to a project as a Git submodule:

```bash
git submodule add https://github.com/AlexGitHub0909/SpecToDelivery.git \
  .agents/skills/spec-to-delivery
git commit -m "chore: add project delivery skill"
```

After cloning the project, collaborators run:

```bash
git submodule update --init --recursive
```

You may copy the skill instead, but do not keep a nested `.git` directory.

</details>

For personal or repository use, this skill has no required MCP server or plugin. A project may still use capabilities that have already been approved for that environment. Restart Codex if the skill does not appear after installation.

## Initialization and audit scripts

The helper scripts use only the Python standard library. They do not constrain the application project's language or stack.

Preview the files that would be created:

```bash
python3 scripts/init_project.py /path/to/project \
  --name "Project name" \
  --mode greenfield \
  --dry-run
```

Add `--scoped path/to/directory` only when the directory has a real local engineering boundary. The initializer creates missing files and leaves existing files unchanged.

Audit the initialized layout:

```bash
python3 scripts/audit_project.py /path/to/project
```

Before handoff, run the strict audit:

```bash
python3 scripts/audit_project.py /path/to/project --strict
```

Initialization creates a file skeleton, not finished project documentation. Strict mode catches structural gaps, obvious unfinished starter content, and key empty tables. It does not replace product review, code tests, or runtime verification.

## Readiness and boundaries

The skill reports `SPEC_READY`, `IMPLEMENTED_LOCAL`, `VERIFIED_LOCAL`, `RELEASE_READY`, `DEPLOYED_VERIFIED`, or `BLOCKED_EXTERNAL` according to the evidence currently available.

Product documents do not prove that code exists, and local tests do not prove that production works. Every completion claim needs current evidence. Checks that were not run, steps that need manual confirmation, external blockers, and prohibited actions remain visible in the plan and handoff.

## Repository layout

```text
spec-to-delivery/
├── SKILL.md                 # Codex execution rules
├── README.md                # Chinese, shown by default on GitHub
├── README.en.md             # English
├── agents/openai.yaml       # Skill list metadata
├── references/              # Core rules, capability routing, and on-demand work-area rules
├── assets/templates/project # Project governance templates
├── scripts/                 # Initialization and audit helpers
├── tests/                   # Script regression tests
└── LICENSE                  # MIT
```

## License

This project is available under the [MIT License](LICENSE). You may use, copy, modify, and distribute it as long as you retain the original copyright and license notice. The work is provided without warranty.
