<p align="center"><samp>PRODUCT DEFINITION → PLAN → IMPLEMENTATION → EVIDENCE → HANDOFF</samp></p>

<h1 align="center">SpecToDelivery</h1>

<p align="center"><strong>从产品定义到可验证交付</strong></p>

<p align="center">把产品定义、执行计划、工程规则和验证证据维护在同一个仓库里的 Codex Skill。</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-2f855a.svg?style=flat-square"></a>
  <img alt="Codex Skill" src="https://img.shields.io/badge/Codex-Skill-2563eb.svg?style=flat-square">
  <img alt="Workflow: PLAN and AGENTS" src="https://img.shields.io/badge/workflow-PLAN%20%2B%20AGENTS-7c3aed.svg?style=flat-square">
  <img alt="Helper scripts: Python standard library only" src="https://img.shields.io/badge/helpers-Python%20stdlib-3776ab.svg?style=flat-square&amp;logo=python&amp;logoColor=white">
</p>

<p align="center">
  <a href="README.md">🇨🇳 中文</a> · <a href="README.en.md">🇺🇸 English</a>
</p>

这个 Skill 可以建立新项目，也可以先审计已有代码库再继续实施。`PLAN.md` 记录当前执行状态，根 `AGENTS.md` 和必要的子目录 `AGENTS.md` 约束工程行为。产品目标与当前实现分开记录，文档里写了某项能力，不代表代码已经完成。

Skill 不限定项目的编程语言、框架、数据库、部署平台或文档语言。新项目尚未确定技术方案时，它会根据产品与交付约束推荐一个首选方案，并在确有取舍时给出一个备选。难以回退的选择由用户确认，除非用户明确授权代为决定。仓库里的 Python 只用于辅助脚本。

## 安装

需要本机已经安装 Git，并使用支持 Skills 的 Codex App、CLI 或 IDE Extension。当前 [Codex 公开文档](https://developers.openai.com/codex/concepts/customization) 将个人 Skill 放在 `$HOME/.agents/skills`，项目共享 Skill 放在仓库的 `.agents/skills`。下面的命令采用这套路径。

### 个人安装

个人安装会让这个 Skill 在本机所有项目中可用。

macOS 或 Linux：

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git \
  "$HOME/.agents/skills/spec-to-delivery"
```

Windows PowerShell：

```powershell
$skillsDir = Join-Path $HOME ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillsDir | Out-Null
git clone https://github.com/AlexGitHub0909/SpecToDelivery.git `
  (Join-Path $skillsDir "spec-to-delivery")
```

更新个人安装：

```bash
git -C "$HOME/.agents/skills/spec-to-delivery" pull --ff-only
```

PowerShell 中可使用：

```powershell
git -C (Join-Path $HOME ".agents\skills\spec-to-delivery") pull --ff-only
```

### 项目共享安装

如果只想让一个仓库使用这个 Skill，可以把它放在项目的 `.agents/skills`。使用 Git Submodule 能保留独立版本和上游更新记录：

```bash
git submodule add https://github.com/AlexGitHub0909/SpecToDelivery.git .agents/skills/spec-to-delivery
git commit -m "chore: add project delivery skill"
```

其他协作者克隆项目后，需要运行 `git submodule update --init --recursive`。更新到上游版本时，运行 `git submodule update --remote .agents/skills/spec-to-delivery`，检查结果后提交新的 Submodule 指针。

不使用 Submodule 时，也可以把 Skill 内容复制到同一目录并随项目提交，但不要保留嵌套的 `.git` 目录。

部分已安装版本和内置工具仍使用 `$CODEX_HOME/skills`，未设置 `CODEX_HOME` 时通常是 `~/.codex/skills`。如果现有安装已经能被识别，不必重复安装。Codex 通常会自动发现 Skill，未出现时重启 Codex。

这个仓库可以独立使用，不依赖 MCP Server，也不需要额外安装 Plugin。

## 选择工作模式

| 你的情况 | 模式 | Skill 会先做什么 |
|---|---|---|
| 已有 PRD 或需求材料，代码很少或还没有代码 | `GREENFIELD` | 建立计划、分层规则、规格和追溯关系，再完成第一个可验证切片 |
| 已有代码和项目文档 | `BROWNFIELD` | 审计 Git、计划、文档、代码与测试，确认真实缺口后继续实施 |
| 只需要规格和交接材料 | `SPEC_ONLY` | 输出契约、实施切片和验收依据，不修改应用代码 |

## 按需加载工程规则

Skill 先从产品材料和仓库判断项目需要哪些工作区。只有证据不足，而且答案会改变范围、架构、数据责任、发布责任或验收方式时，才向用户提问；一次最多集中确认三个相关问题。

| 工作区 | 何时加载规则 |
|---|---|
| 官网 | 需要公开页面、内容传播、搜索发现、营销活动、文档站或公开表单 |
| 前端 | 需要网页、移动端或桌面端的交互界面与用户流程 |
| 后端 | 需要服务端业务规则、认证、任务、队列或私有集成 |
| API | 需要客户端、合作方、自动化或系统之间的稳定程序接口 |
| 数据库 | 需要持久化业务状态、账户、历史、报表、搜索或审计数据 |
| 运维 | 需要部署、环境、域名、后台任务、监控、发布或恢复责任 |

这六类不是穷举。库、CLI、数据管道、模型、嵌入式系统或其他独立责任可以增加项目专用工作区，不必硬塞进现有分类。

工作区不等于固定目录。一个目录可以同时承载多个工作区，一个工作区也可以跨多个目录。确认结果记录在 `PLAN.md`，使用 `APPLIES`、`NOT_APPLICABLE`、`DEFERRED` 或 `OPEN_DECISION`；Skill 只加载当前适用或需要作出决定的规则。

## 项目治理内容

模板覆盖以下内容：

- 项目入口和本地启动说明；
- 根级与子目录执行规则；
- 按需工作区识别和规则路由；
- 当前计划和能力变更记录；
- 文档路由、职责和更新时间；
- 产品范围、行为与系统流程；
- 需求、代码和测试之间的追溯关系；
- 测试、发布和回滚证据；
- 重大架构决策。

默认初始化脚本只建立标准治理文件骨架，不会替项目判断工作区，也不会自动填入负责人、命令和验收依据。它适合新项目，也适合明确决定采用这套目录的已有项目。初始化后必须根据确认过的范围补全内容；其他老仓库应把所需内容合并到现有事实源，不能再创建一套平行文档。

## 使用方式

把产品材料或目标仓库交给 Codex，并明确调用 Skill：

```text
使用 $spec-to-delivery 审计这个仓库，恢复当前计划，然后实施下一项有完整验证证据的工作。
```

创建新项目：

```text
使用 $spec-to-delivery 把这份 PRD 建成一个 GREENFIELD 项目。先根据产品材料判断官网、前端、后端、API、数据库和运维中哪些工作区适用，只向我确认仍会改变范围或架构的问题；然后建立 PLAN、分层 AGENTS、规格和追溯关系，再完成第一个可运行、可验证的实施切片。
```

只做规格交接：

```text
使用 $spec-to-delivery 的 SPEC_ONLY 模式。输出产品契约、实施切片、验收证据和发布注意事项，不修改应用代码。
```

## 初始化治理文件

初始化脚本只复制缺失文件，不覆盖仓库里已有的内容：

```bash
python3 scripts/init_project.py /path/to/project \
  --name "项目名称" \
  --mode greenfield
```

只有目录确实存在独立工程边界时，才按实际路径追加可重复的 `--scoped path/to/directory`，它不是固定的前后端目录结构。

不确定会新增哪些文件时，先预览：

```bash
python3 scripts/init_project.py /path/to/project --name "项目名称" --dry-run
```

完成后运行治理审计：

```bash
python3 scripts/audit_project.py /path/to/project
```

刚初始化、尚未补全的文件会得到警告，这是预期结果。准备移交时使用严格模式；未填写的工作区、模板说明和关键空表会被视为错误：

```bash
python3 scripts/audit_project.py /path/to/project --strict
```

严格模式只能发现结构缺失和明显未填写的模板内容，不能证明决定正确或软件已经可用。这两个脚本只检查本 Skill 提供的标准目录。老仓库缺少这些固定文件名，不代表它没有等价的治理文档。技术栈相关命令仍以项目自己的 `AGENTS.md`、测试标准和发布手册为准。

## 边界

测试通过不等于已经上线，产品文档也不能直接证明代码已经实现。没有明确授权时，Skill 不会执行生产写入、外部系统写入、付费操作或破坏性数据变更。

项目状态使用以下等级：`SPEC_READY`、`IMPLEMENTED_LOCAL`、`VERIFIED_LOCAL`、`RELEASE_READY`、`DEPLOYED_VERIFIED`、`BLOCKED_EXTERNAL`。

## Skill 目录

```text
spec-to-delivery/
├── SKILL.md
├── README.md          # 中文，GitHub 默认展示
├── README.en.md       # English
├── LICENSE            # MIT
├── agents/
├── references/        # 核心规则与按需工作区规则
├── scripts/
├── tests/             # 初始化与审计脚本的回归测试
└── assets/templates/project/
```

Codex 执行时读取 `SKILL.md`。中英文 README 是给使用者和维护者看的说明。

## 许可证

本项目采用 [MIT License](LICENSE)。你可以使用、复制、修改和分发，但必须保留原版权及许可证声明。本项目不提供任何担保。
