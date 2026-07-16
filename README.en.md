<p align="center"><samp>PRODUCT DEFINITION → PLAN → IMPLEMENTATION → EVIDENCE → HANDOFF</samp></p>

<h1 align="center">SpecToDelivery</h1>

<p align="center"><strong>From product definition to verified delivery</strong></p>

<p align="center">Connect the PRD, execution plan, engineering rules, implementation, and verification evidence in one delivery workflow.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2f855a.svg?style=flat-square"></a>
  <img alt="Open Agent Skill" src="https://img.shields.io/badge/Agent-Skill-2563eb.svg?style=flat-square">
  <img alt="Workflow: PLAN and AGENTS" src="https://img.shields.io/badge/workflow-PLAN%20%2B%20AGENTS-7c3aed.svg?style=flat-square">
  <img alt="Helper scripts: Python standard library only" src="https://img.shields.io/badge/helpers-Python%20stdlib-3776ab.svg?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <a href="README.md">🇨🇳 中文</a> · <a href="README.en.md">🇺🇸 English</a>
</p>

SpecToDelivery is for product owners and developers who work with an AI coding agent. It follows the open [Agent Skills specification](https://agentskills.io/specification). It can establish a project from product material, recover the current state of an existing repository before implementation continues, or produce an implementation-ready specification without changing code.

It is not tied to one agent and does not prescribe a programming language, framework, database, or deployment platform. It keeps existing technical choices when they are settled. When they are open, it recommends one preferred approach from the product and delivery constraints. The user still confirms decisions that are expensive to reverse unless they explicitly delegate that authority to the active agent.

## Quick start

1. [Download the latest ZIP](https://github.com/AlexGitHub0909/SpecToDelivery/archive/refs/heads/main.zip).
2. Extract it and rename `SpecToDelivery-main` to `spec-to-delivery`.
3. Move the folder into a supported Skill directory. Most tools use `~/.agents/skills/spec-to-delivery`; Claude Code uses `~/.claude/skills/spec-to-delivery`.

See [Compatibility](#compatibility) and [Installation and updates](#installation-and-updates) for other entry points. After installation, give the active agent a PRD, requirements document, or target repository:

```text
Use spec-to-delivery to audit the current material, establish or recover PLAN.md, the root AGENTS.md,
and any necessary scoped AGENTS.md files,
then implement the next piece of work with current verification evidence.
```

Codex accepts `$spec-to-delivery`. Platforms with a slash-command menu or Skill picker can invoke it there. The natural-language form does not depend on platform-specific syntax.

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
| Human review | Confirm unresolved product decisions through a prototype, example, or flow | `PLAN.md` and the review artifact |
| Specify and implement | Split requirements into observable, testable end-to-end slices | Product specs, flow specs, traceability, and code |
| Verify and hand off | Run current checks and update facts, status, rollback, and the next task | `PLAN.md`, test evidence, and `CHANGELOG.md` |

Each cycle advances one active slice. Finishing a slice does not mean the project is complete, and passing tests does not prove deployment.

## Human and agent responsibilities

SpecToDelivery does not let the agent replace human product acceptance. The user or named owner decides the goal, scope, material trade-offs, prototype direction, and final acceptance. The agent organizes source material, recommends an approach, prepares review artifacts, implements code, runs checks, and records evidence. A decision that changes scope, workflow, visual direction, data ownership, cost, or release risk needs an explicit result; silence is not approval.

### When to prototype first

A prototype is not required for every project. Prepare a confirmation artifact when text leaves a material ambiguity and direct implementation would create avoidable rework:

| Product surface | Suitable confirmation artifact |
|---|---|
| Website, web app, mobile app, or desktop interface | Sitemap, user flow, wireframe, visual screen, or clickable prototype |
| CLI | Command syntax, input and output examples, interaction transcript, and error behavior |
| API or system integration | Request and response examples, schema mock, webhook fixture, or sequence diagram |
| Backend workflow, automation, or data product | State diagram, decision table, dry-run output, field sample, or report mock |

The agent uses the lowest fidelity that can settle the decision. A flow or wireframe comes before a high-fidelity prototype unless visual, responsive, or complex interaction details require more. Record the result as `APPROVED`, `CHANGES_REQUESTED`, `REVIEW_REQUIRED`, or `NOT_REQUIRED`. Prototype approval confirms intended direction; it does not prove implementation or deployment.

## Core rules

- Keep `PLAN.md` as the current execution record. Update it when the task, result, evidence, blocker, or next step changes.
- Give the active slice an expected outcome or value signal, an acceptance owner, and a next checkpoint when it affects progress. Do not invent a KPI to fill a template.
- Track only material risks that can affect the current delivery, with their impact, response, owner, and trigger. Do not create a separate risk register by default.
- Give every project a root `AGENTS.md`. Add a scoped file when a directory has its own stack, application boundary, data boundary, validation commands, or release process.
- The agent may recommend and implement, but it may not approve its own material product decision. Do not start expensive or hard-to-reverse work while a required review artifact remains unapproved.
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
Use spec-to-delivery to turn this PRD into a GREENFIELD project.
Infer the applicable engineering work areas and ask only about unresolved choices that change scope or architecture.
Then establish PLAN, scoped AGENTS, specifications, and traceability before completing the first working slice.
```

Prepare a specification-only handoff:

```text
Use spec-to-delivery in SPEC_ONLY mode.
Produce product contracts, implementation slices, acceptance evidence, and release considerations without changing application code.
```

## Compatibility

SpecToDelivery follows the open Agent Skills specification. Every platform uses the same `SKILL.md`, references, templates, and scripts. `agents/openai.yaml` only supplies UI metadata for OpenAI products; other platforms ignore it.

| Platform | Official discovery or import path |
|---|---|
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `~/.agents/skills`, project `.agents/skills` |
| [Claude Code](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | `~/.claude/skills`, project `.claude/skills` |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | `~/.agents/skills`, `~/.copilot/skills`; project `.agents/skills`, `.github/skills`, or `.claude/skills` |
| [Cursor](https://cursor.com/docs/skills) | `~/.agents/skills`, `~/.cursor/skills`; project `.agents/skills` or `.cursor/skills` |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `~/.agents/skills`, `~/.gemini/skills`; project `.agents/skills` or `.gemini/skills` |
| [OpenCode](https://opencode.ai/docs/skills) | `~/.agents/skills`, `~/.config/opencode/skills`; project `.agents/skills`, `.opencode/skills`, or `.claude/skills` |
| [TRAE](https://www.trae.ai/blog/trae_tutorial_0115) | [TRAE IDE 3.5.44+](https://www.trae.ai/ja/changelog) can use project `.agents/skills`; UI import is also available under Settings → Rule & Skills → Skills |

The Skill can be loaded through the paths above. Available shell, browser, network, MCP, subagent, and external-system capabilities depend on the product version and workspace policy. SpecToDelivery adjusts its execution path to the available environment without lowering the requested outcome, acceptance criteria, safety boundary, or evidence standard. It uses an alternative method when that method produces equivalent evidence; otherwise the item remains `MANUAL_REQUIRED` or `BLOCKED_EXTERNAL`.

## Installation and updates

Use a Skill directory officially supported by the active platform. Codex, GitHub Copilot, Cursor, Gemini CLI, OpenCode, and TRAE IDE 3.5.44+ can use `.agents/skills`, making it the preferred shared location across tools. Claude Code uses `.claude/skills`. Do not install the same skill name in several discovered locations.

### Direct download (recommended)

[Download the latest ZIP](https://github.com/AlexGitHub0909/SpecToDelivery/archive/refs/heads/main.zip), extract it, rename the folder to `spec-to-delivery`, and move it to the appropriate location:

| Use | Target directory |
|---|---|
| Personal installation for several tools | `~/.agents/skills/spec-to-delivery` |
| Personal Claude Code installation | `~/.claude/skills/spec-to-delivery` |
| Shared inside a project | `<project-root>/.agents/skills/spec-to-delivery` |

A Claude Code-only project may use `.claude/skills/spec-to-delivery`; a Cursor-only project may use `.cursor/skills/spec-to-delivery`. To update, download the ZIP again and replace the old folder. Preserve any local changes before replacing it.

Codex users may also ask `$skill-installer` to install the repository root from `https://github.com/AlexGitHub0909/SpecToDelivery` with the Skill name `spec-to-delivery`.

<details>
<summary>Install and update with Git</summary>

Git is useful when you update often or contribute to the repository:

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git \
  "$HOME/.agents/skills/spec-to-delivery"
git -C "$HOME/.agents/skills/spec-to-delivery" pull --ff-only
```

Claude Code users can change the target to `~/.claude/skills/spec-to-delivery`. Teams may also use a Git submodule, but Git is not required to use the Skill.

</details>

For personal or repository use, this skill has no required MCP server or plugin. A project may still use capabilities that have already been approved for that environment. If the active session does not discover the Skill, refresh the Skill list or start a new agent session, then check the directory, filename, YAML frontmatter, and platform permissions.

## Initialization and audit scripts

The helper scripts use only the Python 3 standard library. They do not constrain the application project's language or stack. The commands below assume the current directory is this Skill's installation directory. When an agent invokes them from a target project, it should resolve the directory containing `SKILL.md` and use the script's full path.

Preview the files that would be created:

```bash
python3 scripts/init_project.py /path/to/project \
  --name "Project name" \
  --mode greenfield \
  --profile delivery \
  --dry-run
```

Use `--profile core` for only README, PLAN, and root AGENTS; `delivery` adds specifications, traceability, and test evidence; `release` adds release and architecture-decision material. Add `--prototype` when the project needs a separate human review record. Add `--scoped path/to/directory` only when the directory has a real local engineering boundary. The initializer creates missing files and leaves existing files unchanged.

Audit the initialized layout:

```bash
python3 scripts/audit_project.py /path/to/project
```

Before handoff, run the strict audit:

```bash
python3 scripts/audit_project.py /path/to/project --strict
```

Initialization creates a file skeleton, not finished project documentation. Strict mode checks structure, status values, human review gates, and basic consistency between requirements, traceability, and test evidence. It does not replace product review, code tests, or runtime verification.

## Readiness and boundaries

The skill reports `SPEC_READY`, `IMPLEMENTED_LOCAL`, `VERIFIED_LOCAL`, `RELEASE_READY`, `DEPLOYED_VERIFIED`, or `BLOCKED_EXTERNAL` according to the evidence currently available.

Product documents do not prove that code exists, and local tests do not prove that production works. Every completion claim needs current evidence. Checks that were not run, steps that need manual confirmation, external blockers, and prohibited actions remain visible in the plan and handoff.

## Repository layout

```text
spec-to-delivery/
├── SKILL.md                 # Platform-neutral core execution rules
├── README.md                # Chinese, shown by default on GitHub
├── README.en.md             # English
├── agents/openai.yaml       # Optional UI metadata for OpenAI products
├── references/              # Core rules, capability routing, and on-demand work-area rules
├── assets/templates/project # Project governance templates
├── scripts/                 # Initialization and audit helpers
├── tests/                   # Script regression tests
└── LICENSE                  # MIT
```

## License

This project is available under the [MIT License](LICENSE). You may use, copy, modify, and distribute it as long as you retain the original copyright and license notice. The work is provided without warranty.
