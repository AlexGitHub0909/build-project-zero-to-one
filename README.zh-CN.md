# 项目 0 到 1

[English](README.md)

这个 Codex Skill 用来把产品文档或已有仓库推进成一个能继续实施、能验证、也能交接的项目。项目状态写在仓库里，不依赖聊天记录。

它有几个明确要求：项目必须维护当前 `PLAN.md`，根目录必须有 `AGENTS.md`，存在独立工程边界的子目录也要有自己的 `AGENTS.md`。产品目标和当前实现分开记录，文档里写了某项能力，不代表代码已经完成。

## 从 GitHub 安装

把仓库克隆到个人 Codex Skills 目录：

```bash
git clone https://github.com/AlexGitHub0909/build-project-zero-to-one.git \
  ~/.codex/skills/build-project-zero-to-one
```

如果已经通过 Git 安装，可以在原目录更新：

```bash
git -C ~/.codex/skills/build-project-zero-to-one pull --ff-only
```

安装完成后新建一个 Codex 任务，让 Skill 列表重新加载。这个仓库可以独立使用，不依赖 MCP Server，也不需要额外安装 Plugin。

## 适用场景

使用 `$build-project-zero-to-one` 可以完成这些工作：

- 根据 PRD、产品说明或需求清单创建新项目；
- 恢复已有仓库的真实状态，找出下一项应该实施的工作；
- 只输出可交接的规格包，不修改应用代码；
- 补齐或修正计划、文档路由、需求追溯、测试证据和发布规则；
- 按业务切片实施功能，并同步更新仓库中的事实记录。

Skill 支持三种模式：

| 模式 | 适用情况 |
|---|---|
| `GREENFIELD` | 新项目，已有产品材料，但代码很少或还没有代码 |
| `BROWNFIELD` | 已有仓库，必须先审计现状，再决定如何修改 |
| `SPEC_ONLY` | 只做规格和交接，不改应用代码 |

## 会为项目补充什么

模板覆盖以下内容：

- 项目入口和本地启动说明；
- 根级与子目录执行规则；
- 当前计划和能力变更记录；
- 文档路由、职责和更新时间；
- 产品范围与业务流程；
- 需求、代码和测试之间的追溯关系；
- 测试、发布和回滚证据；
- 重大架构决策。

默认初始化脚本会建立完整治理基线。它适合新项目，也适合明确决定采用这套目录的已有项目。其他老仓库应把模板内容合并到现有事实源，不能再创建一套平行文档。

## 使用方式

把产品材料或目标仓库交给 Codex，并明确调用 Skill：

```text
使用 $build-project-zero-to-one 审计这个仓库，恢复当前计划，然后实施下一项有完整验证证据的产品功能。
```

创建新项目：

```text
使用 $build-project-zero-to-one 把这份 PRD 建成一个 GREENFIELD 项目。先建立 PLAN、分层 AGENTS、规格和追溯关系，再完成第一个可运行的业务切片。
```

只做规格交接：

```text
使用 $build-project-zero-to-one 的 SPEC_ONLY 模式。输出产品契约、实施切片、验收证据和发布注意事项，不修改应用代码。
```

## 初始化治理文件

初始化脚本只复制缺失文件，不覆盖仓库里已有的内容：

```bash
python3 scripts/init_project.py /path/to/project \
  --name "项目名称" \
  --mode greenfield \
  --scoped backend \
  --scoped frontend
```

不确定会新增哪些文件时，先预览：

```bash
python3 scripts/init_project.py /path/to/project --name "项目名称" --dry-run
```

完成后运行治理审计：

```bash
python3 scripts/audit_project.py /path/to/project
```

这两个脚本只检查本 Skill 提供的标准目录。老仓库缺少这些固定文件名，不代表它没有等价的治理文档。技术栈相关命令仍以项目自己的 `AGENTS.md`、测试标准和发布手册为准。

## 边界

测试通过不等于已经上线，产品文档也不能直接证明代码已经实现。没有明确授权时，Skill 不会执行生产写入、外部系统写入、付费操作或破坏性数据变更。

项目状态使用以下等级：`SPEC_READY`、`IMPLEMENTED_LOCAL`、`VERIFIED_LOCAL`、`RELEASE_READY`、`DEPLOYED_VERIFIED`、`BLOCKED_EXTERNAL`。

## Skill 目录

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

Codex 执行时读取 `SKILL.md`。中英文 README 是给使用者和维护者看的说明。

公开自己的分支前，应重新检查模板里的示例，并根据预期的使用方式选择合适的开源许可证。
