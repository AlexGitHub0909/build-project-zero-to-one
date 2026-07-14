<p align="center"><samp>PRODUCT DEFINITION → PLAN → IMPLEMENTATION → EVIDENCE → HANDOFF</samp></p>

<h1 align="center">SpecToDelivery</h1>

<p align="center"><strong>从产品定义到可验证交付</strong></p>

<p align="center">把 PRD、执行计划、工程规则、项目实施和验证证据串成一条交付链。</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2f855a.svg?style=flat-square"></a>
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-2563eb.svg?style=flat-square">
  <img alt="Workflow: PLAN and AGENTS" src="https://img.shields.io/badge/workflow-PLAN%20%2B%20AGENTS-7c3aed.svg?style=flat-square">
  <img alt="Helper scripts: Python standard library only" src="https://img.shields.io/badge/helpers-Python%20stdlib-3776ab.svg?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <a href="README.md">🇨🇳 中文</a> · <a href="README.en.md">🇺🇸 English</a>
</p>

SpecToDelivery 是一个用于软件项目交付的单一 Codex Skill。它可以从产品文档建立新项目，也可以先恢复已有仓库的真实状态再接着实施；如果当前只需要规格和交接材料，它只产出可实施的规格，不修改代码。

它不预设编程语言、框架、数据库或部署平台。技术方案已经确定时沿用现有选择；尚未确定时，根据产品和交付约束给出一个首选建议。难以回退的决定仍由用户确认，除非用户明确授权 Codex 代为决定。

## 快速开始

在 Codex 中安装：

```text
使用 $skill-installer 安装 https://github.com/AlexGitHub0909/SpecToDelivery
仓库根目录的 Skill，名称设为 spec-to-delivery。
```

安装后，把 PRD、需求文档或目标仓库交给 Codex：

```text
使用 $spec-to-delivery 审计当前材料，建立或恢复 PLAN.md、根级 AGENTS.md
和必要的子目录 AGENTS.md，
然后实施下一项有完整验证证据的工作。
```

也可以按下面的方式[手动安装](#安装与更新)。

## 适用场景

| 当前情况 | 模式 | 先做什么 |
|---|---|---|
| 已有 PRD 或需求材料，代码很少或还没有代码 | `GREENFIELD` | 建立计划、工程规则、规格和追溯关系，再完成第一个可验证切片 |
| 已有代码和项目文档 | `BROWNFIELD` | 审计 Git、计划、文档、代码与测试，确认真实缺口后继续实施 |
| 只需要规格和交接材料 | `SPEC_ONLY` | 输出可实施的契约、任务切片和验收依据，不修改应用代码 |

## 工作方式

| 阶段 | 处理内容 | 主要记录位置 |
|---|---|---|
| 恢复事实 | 检查 Git、现有规则、计划、文档、代码和测试 | 当前仓库证据 |
| 确认范围 | 选择工作模式，判断哪些工程工作区适用 | `PLAN.md` |
| 建立约束 | 写明当前任务、目录责任、验证命令和禁止事项 | 根级与子目录 `AGENTS.md` |
| 规格与实施 | 把需求拆成可观察、可测试的端到端切片 | 产品规格、流程规格、追溯矩阵和代码 |
| 验证与交接 | 运行当前检查，更新事实、状态、回滚和下一步 | `PLAN.md`、测试证据、`CHANGELOG.md` |

一轮工作只推进一个当前切片。切片完成不等于项目完成；测试通过也不等于已经上线。

## 核心规则

- `PLAN.md` 是当前执行记录，必须保留。任务、结果、证据、阻塞或下一步变化时，随实施一起更新。
- 当前切片要写明预期结果或价值信号、验收负责人，以及真正会影响推进的下一检查点。没有现成指标时，不为填表编造 KPI。
- 只跟踪会影响当前交付的重大风险，并写清影响、应对、负责人和触发条件；不默认建立独立风险登记册。
- 每个项目都有根 `AGENTS.md`。目录出现独立技术栈、应用边界、数据边界、验证命令或发布流程时，再增加就近的子目录 `AGENTS.md`。
- 产品和契约描述目标行为；代码、Git、测试和运行结果证明当前实现。两类事实不能混写。
- 已批准的范围或实施方式发生变化时，记录原因及其对交付、成本或验收的影响。真正会改变后续工作的经验，直接更新规则、契约或自动检查。
- 优先复用仓库已有的结构、依赖、组件、服务和文档，不为套用模板另建一套平行事实源。
- 没有明确授权时，不执行部署、外部系统写入、付费操作、真实凭证使用或破坏性数据变更。

## 按需加载工程规则

Skill 先根据产品材料和仓库证据判断需要哪些工作区。只有证据不足，而且答案会改变范围、架构、数据责任、发布责任或验收方式时，才向用户提问。需要确认时，一次最多集中三个相关问题，并使用产品语言，不把没有解释的技术选项直接丢给用户。

| 工作区 | 适用情况 |
|---|---|
| 官网 | 公开页面、内容传播、搜索发现、营销活动、文档站或公开表单 |
| 前端 | Web、移动端或桌面端的交互界面与用户流程 |
| 后端 | 服务端业务规则、认证、任务、队列或私有集成 |
| API | 客户端、合作方、自动化或系统之间的稳定程序接口 |
| 数据库 | 持久化业务状态、账户、历史、报表、搜索或审计数据 |
| 运维 | 部署、环境、域名、后台任务、监控、发布或恢复责任 |

这六类不是固定架构。库、CLI、数据管道、模型、嵌入式系统或其他独立责任可以增加项目专用工作区。工作区也不等于目录：一个目录可以承载多个工作区，一个工作区也可以跨多个目录。

## 按需使用 Skills 和插件

项目实施可以使用环境中已有的 Skill、插件、连接器或专业工具，但它们不是默认依赖。先确认项目需要什么结果，再选择能够完成并验证该结果的能力。

| 能力类型 | 处理方式 |
|---|---|
| 项目已有命令、脚本和依赖 | 优先使用，遵守当前目录的 `AGENTS.md` |
| 可选专业能力 | 有助于设计、浏览器验证或文档处理时按需使用，同时保留普通执行路径 |
| 交付必需能力 | 在 `PLAN.md` 记录可用性、权限、负责人和替代方案；缺失时明确阻塞 |
| 企业或项目专用集成 | 把凭证、账号、内部地址和操作规则留在项目仓库，不写入公共 Skill |

使用前需要读取对应说明，检查权限、费用、网络访问和外部副作用。没有明确授权时，不安装或启用插件，不创建外部账号，也不向远端系统写入。工具成功运行只能证明执行发生过，项目自己的验收规则仍要检查最终结果。

## 其他调用方式

从产品文档建立项目：

```text
使用 $spec-to-delivery 把这份 PRD 建成一个 GREENFIELD 项目。
先判断适用的工程工作区，只确认仍会改变范围或架构的问题；
再建立 PLAN、分层 AGENTS、规格和追溯关系，完成第一个可运行切片。
```

只做规格交接：

```text
使用 $spec-to-delivery 的 SPEC_ONLY 模式。
输出产品契约、实施切片、验收证据和发布注意事项，不修改应用代码。
```

## 安装与更新

[Codex Skills 文档](https://learn.chatgpt.com/docs/build-skills)使用 `$HOME/.agents/skills` 存放个人 Skill，项目共享 Skill 放在仓库的 `.agents/skills`。如果现有 Codex 已经能识别其他目录中的安装，不必重复安装。

<details>
<summary>macOS / Linux 个人安装</summary>

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git \
  "$HOME/.agents/skills/spec-to-delivery"
```

更新：

```bash
git -C "$HOME/.agents/skills/spec-to-delivery" pull --ff-only
```

</details>

<details>
<summary>Windows PowerShell 个人安装</summary>

```powershell
$skillsDir = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git `
  (Join-Path $skillsDir "spec-to-delivery")
```

更新：

```powershell
git -C (Join-Path $HOME ".agents\skills\spec-to-delivery") pull --ff-only
```

</details>

<details>
<summary>项目共享安装</summary>

把 Skill 作为 Submodule 放进项目仓库：

```bash
git submodule add https://github.com/AlexGitHub0909/SpecToDelivery.git \
  .agents/skills/spec-to-delivery
git commit -m "chore: add project delivery skill"
```

协作者克隆项目后运行：

```bash
git submodule update --init --recursive
```

也可以直接复制 Skill 内容，但不要保留嵌套的 `.git` 目录。

</details>

作为个人或项目内 Skill 使用时，本仓库没有必装的 MCP Server 或 Plugin。具体项目可以按需调用已经获准使用的能力。Codex 未发现 Skill 时，重启 Codex 后再检查。

## 初始化与审计脚本

辅助脚本只使用 Python 标准库，不限制应用项目的语言和技术栈。

先预览将创建的文件：

```bash
python3 scripts/init_project.py /path/to/project \
  --name "项目名称" \
  --mode greenfield \
  --dry-run
```

只有目录确实存在独立工程边界时，才追加 `--scoped path/to/directory`。脚本只创建缺失文件，不覆盖已有内容。

初始化完成后运行：

```bash
python3 scripts/audit_project.py /path/to/project
```

准备移交时运行严格审计：

```bash
python3 scripts/audit_project.py /path/to/project --strict
```

初始化得到的是文件骨架，不是完成后的项目文档。严格审计只能发现结构缺失、明显未填写的模板内容和关键空表，不能代替业务评审、代码测试或运行验证。

## 项目状态与边界

Skill 使用 `SPEC_READY`、`IMPLEMENTED_LOCAL`、`VERIFIED_LOCAL`、`RELEASE_READY`、`DEPLOYED_VERIFIED` 和 `BLOCKED_EXTERNAL` 表示当前证据能够支持到哪一步。

产品文档不能直接证明代码已经实现，本地测试也不能证明生产环境已经可用。所有完成声明都需要当前证据；未运行的检查、需要人工确认的步骤、外部阻塞和禁止事项会继续保留在计划与交接结果中。

## 仓库结构

```text
spec-to-delivery/
├── SKILL.md                 # Codex 执行规则
├── README.md                # 中文说明，GitHub 默认展示
├── README.en.md             # English
├── agents/openai.yaml       # Skill 列表元数据
├── references/              # 核心规则、能力路由与按需工作区规则
├── assets/templates/project # 项目治理模板
├── scripts/                 # 初始化与审计脚本
├── tests/                   # 脚本回归测试
└── LICENSE                  # MIT
```

## 许可证

本项目采用 [MIT License](LICENSE)。可以使用、复制、修改和分发，但必须保留原版权及许可证声明。本项目不提供任何担保。
