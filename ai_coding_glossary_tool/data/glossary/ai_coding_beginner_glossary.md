# AI 编程工具小白词库 v0.1

生成日期：2026-06-01  
用途：作为 Windows 桌面小工具 / 浏览器解释助手 / Codex 可维护词库的初版底稿。  
适用对象：刚开始使用 AI 工具、Codex、GitHub、命令行、域名、服务器和常见开发工具的非程序员用户。  

## 维护原则

1. 每个词条都用“小白能懂”的解释，不追求教科书式定义。  
2. 优先解释“看到这个词时我该不该点、该不该执行、有没有风险”。  
3. 不保存 API Key、密码、服务器登录信息、个人隐私、公司机密。  
4. 后续新增词条时，保持同一表格结构，方便 Codex 或桌面小工具解析。  

## 推荐文件路径

```txt
data/glossary/ai_coding_beginner_glossary.md
```

## 推荐字段说明

| 字段 | 含义 |
|---|---|
| 词条 | 用户可能选中的词 |
| 别名 / 英文 | 同义词、英文名、常见写法 |
| 分类 | 便于工具筛选和分组 |
| 小白解释 | 一句话说明它是什么 |
| 你通常在哪里看到 | 常见软件、界面、命令或报错场景 |
| 操作 / 风险提醒 | 看到它时该怎么处理，哪些情况不要乱点 |

---

# 词库正文

| 词条                    | 别名 / 英文                            | 分类         | 小白解释                               | 你通常在哪里看到                                      | 操作 / 风险提醒                    |
| --------------------- | ---------------------------------- | ---------- | ---------------------------------- | --------------------------------------------- | ---------------------------- |
| AI                    | Artificial Intelligence            | AI基础       | 让软件像助手一样理解材料、生成内容或执行任务。            | ChatGPT、Codex、飞书 Aily。                        | AI 会出错，法律、财务、服务器操作必须人工复核。    |
| 大模型                   | LLM                                | AI基础       | 能理解和生成文字的 AI 引擎。                   | 模型选择、API 文档、AI 工具设置。                          | 复杂任务用强模型，简单整理不必用高消耗模型。       |
| GPT                   | Generative Pre-trained Transformer | AI基础       | ChatGPT 背后常见的一类大模型技术。              | ChatGPT、OpenAI、模型名称。                          | 不要把 GPT 当成所有 AI 的统称。         |
| ChatGPT               | ChatGPT                            | AI工具       | 对话式 AI 助手，可写作、分析、解释、生成 Codex 指令。   | 网页端、桌面端、手机 App。                               | 结果要核对，尤其是重要决策、代码、部署。        |
| Prompt                | 提示词 / 指令                           | AI基础       | 你给 AI 的任务说明。                       | ChatGPT 输入框、Agent 配置、Prompt星图。                | 写清目标、背景、限制、输出格式，减少跑偏。        |
| System Prompt         | 系统提示词                              | AI基础       | 给 AI 设定长期角色、边界和工作规则的底层说明。          | 自定义 GPT、Agent 文件、Project 设置。                  | 规则不要互相矛盾，也不要超长堆叠。            |
| User Prompt           | 用户提示词                              | AI基础       | 你每次发给 AI 的具体任务。                    | ChatGPT、Codex 任务输入框。                          | 一次任务目标要明确，不要混入冲突要求。          |
| Agent                 | 智能体                                | AI工具       | 设定好角色、流程和规则的 AI 助手。                | 文档整理 Agent、数据分析 Agent、飞书 Aily。                | Agent 不是自动正确，规则更新后要测试。       |
| Skill                 | 技能                                 | AI工具       | 给 AI 或工具增加的一套专门能力。                 | 术语解释技能、文档整理技能、图片审核技能。                         | 要定义清楚触发场景和边界。                |
| Project               | 项目                                 | AI工具       | 同一主题的对话、文件、指令集合。                   | ChatGPT Project、学习项目、个人工具项目。                 | 不同业务规则尽量分项目维护。               |
| GPTs                  | 自定义 GPT                            | AI工具       | 可配置角色、知识和能力的定制版 ChatGPT。           | ChatGPT 的 GPTs 页面。                            | 不要上传不适合外部化的敏感材料。             |
| Token                 | 用量单位                               | AI基础       | AI 处理文字时的计量单位，可粗略理解为消耗额度。          | Codex 周额度、API 费用、上下文长度。                       | 文件越多、输出越长，消耗越高。              |
| 上下文                   | Context                            | AI基础       | AI 当前能看到并参考的信息。                    | 对话、上传文件、项目规则。                                 | 上下文太长时，AI 可能忽略早期信息。          |
| 上下文窗口                 | Context Window                     | AI基础       | AI 一次最多能读进去的信息容量。                  | 长文档分析、Codex 大任务。                              | 大任务要拆分，减少无关材料。               |
| 推理强度                  | Reasoning Effort                   | AI基础       | AI 在回答前“想得多不多”的设置。                 | Codex、ChatGPT 模型设置。                           | 高推理通常更慢、更耗额度。                |
| API                   | Application Programming Interface  | 接口         | 系统之间按规则沟通的接口。                      | OpenAI API、后端接口、网页请求。                        | 看清地址、方法、参数、返回结果。             |
| API Key               | 密钥                                 | 安全         | 调用 API 的钥匙。                        | OpenAI API、云服务、第三方接口。                         | 不要写进公开代码、截图或发给别人。            |
| OpenAI API            | OpenAI 接口                          | AI接口       | 让自己的程序调用 OpenAI 模型。                | AI 增强版工具、后端服务。                                | 会联网且可能计费，敏感内容要谨慎。            |
| API 调用                | Call API                           | 接口         | 程序向接口发一次请求并等待结果。                   | 后端日志、浏览器 Network、接口请求。                       | 循环调用可能产生费用或服务器压力。            |
| Quota                 | 额度 / 配额                            | AI用量       | 平台允许使用的次数、金额、Token 或资源上限。          | Codex 周额度、API 控制台。                            | 额度低时不要启动大重构。                 |
| Rate Limit            | 限流                                 | 接口         | 平台限制短时间内请求频率。                      | 429、Too many requests。                        | 降低频率或稍后重试，不要硬刷。              |
| Vibe Coding           | AI 辅助编程                            | 开发方式       | 用自然语言指挥 AI 写、改、排查代码。               | Codex、Cursor、ChatGPT 辅助开发。                    | 你负责需求和验收，AI 负责实现但需复核。        |
| Codex                 | 代码代理                               | 开发工具       | 能读取项目、修改代码、运行检查的 AI 编程工具。          | 本地项目开发、GitHub 项目。                             | 明确可改范围、禁止事项、自检方式。            |
| 代码代理                  | Coding Agent                       | 开发工具       | 能替你在项目里动代码的 AI。                    | Codex、Cursor Agent。                           | 涉及数据库、服务器、密钥时必须限制。           |
| 一键粘贴指令                | Single Prompt                      | AI工作流      | 一段可直接复制给 Codex 的完整任务说明。            | Codex 开发任务、修复任务。                              | 要写目标、路径、限制、自检、完成后回复格式。       |
| 工作区                   | Workspace                          | 开发基础       | 当前工具打开并操作的项目环境。                    | Codex、VS Code、GitHub Desktop。                 | 开错工作区会改错项目。                  |
| 项目文件夹                 | Project Folder                     | 开发基础       | 一个应用或工具的所有代码、配置、素材所在文件夹。           | 本地磁盘、VS Code、Codex 路径。                        | 不要随意移动根目录配置文件。               |
| Diff                  | 差异 / 变更对比                          | Git        | 显示文件被改了哪里。                         | GitHub Desktop、Codex 修改结果。                    | 提交前看 Diff，防止误删误改。            |
| Patch                 | 补丁                                 | 开发基础       | 一次局部代码修改方案。                        | Codex 输出、Git 补丁。                              | 来源不明的 Patch 不要直接套用。          |
| Build                 | 构建 / 打包                            | 开发基础       | 把源码处理成可运行或可发布的文件。                  | npm run build、Vite build。                     | Build 成功不等于功能一定正确。           |
| Compile               | 编译                                 | 开发基础       | 把代码转换成平台能运行的形式。                    | 本地开发工具、构建日志。                                  | 看第一条关键错误，不要只看最后一行。           |
| Test                  | 测试                                 | 开发基础       | 检查功能是否真的可用。                        | 本地测试、浏览器测试、接口测试。                               | 至少测正常路径和一个异常路径。              |
| Lint                  | 代码规范检查                             | 开发基础       | 检查格式、潜在错误和不规范写法。                   | npm run lint、CI。                              | 不要为通过 Lint 盲目删除关键代码。         |
| 自检                    | Self-check                         | AI工作流      | 让 Codex 完成后列出检查结果。                 | Codex 完成回复。                                   | 仍需人工抽查。                      |
| 备份                    | Backup                             | 通用         | 修改前保留原始文件或状态。                      | 文档模板、配置、数据库、服务器。                              | 大改前必须备份，密钥不要备份进公开仓库。         |
| 回滚                    | Rollback                           | 通用         | 恢复到修改前状态。                          | Git、部署、数据库。                                   | 数据库回滚风险高，不能随便做。              |
| Git                   | 版本控制工具                             | Git        | 记录文件修改历史，方便撤回和协作。                  | GitHub Desktop、命令行、项目开发。                      | 不懂时不要乱用 reset、force push。    |
| GitHub                | 代码托管平台                             | Git        | 放代码项目的网站，也可做版本备份。                  | GitHub Desktop、浏览器仓库页。                        | 公开仓库不要放密钥、客户资料、内部资料。         |
| GitHub Desktop        | Git 图形界面                           | Git        | 不用敲命令也能提交、拉取、推送代码。                 | Changes、History、Fetch origin、Push origin。     | 看到冲突、Discard、Reset 时不要乱点。    |
| Repository            | Repo / 仓库                          | Git        | 被 Git 管理的项目文件夹。                    | GitHub 仓库、GitHub Desktop 左上角。                 | 确认当前仓库是要改的项目。                |
| Local Repo            | 本地仓库                               | Git        | 你电脑上的那份 Git 项目。                    | GitHub Desktop、VS Code。                       | 本地没 push，远程还没有这些修改。          |
| Remote Repo           | 远程仓库                               | Git        | 放在 GitHub 等平台上的项目。                 | origin、GitHub 页面、Push/Pull。                   | 远程被别人改过时直接 push 可能失败。        |
| Origin                | 默认远程仓库名                            | Git        | 通常代表 GitHub 那边的项目地址。               | Fetch origin、Push origin。                     | origin 地址错了会推到错误项目。          |
| Branch                | 分支                                 | Git        | 同一项目的不同开发线。                        | main、feature、Current Branch。                  | 改错分支会导致变更进错地方。               |
| Main                  | 主分支 / master                       | Git        | 项目最主要、通常最稳定的分支。                    | main、master。                                  | 未经测试的大改不要直接进 main。           |
| Commit                | 提交                                 | Git        | 把当前修改保存成一个版本记录。                    | GitHub Desktop 左下角 Commit。                    | Commit 只保存本地，不等于已上传 GitHub。  |
| Commit Message        | 提交说明                               | Git        | 描述这次提交改了什么。                        | GitHub Desktop Summary。                       | 不要只写 update，要写具体修改点。         |
| Staged Changes        | 暂存区                                | Git        | 准备放进下一次 Commit 的修改。                | VS Code Source Control。                       | 不要把 .env、密钥文件一起暂存。           |
| Changes               | 变更                                 | Git        | 当前文件和上次提交相比的修改。                    | GitHub Desktop Changes 面板。                    | 提交前逐个看文件。                    |
| Discard Changes       | 丢弃修改                               | Git        | 把未提交修改直接扔掉。                        | GitHub Desktop、VS Code。                       | 点了可能找不回未提交内容。                |
| Fetch                 | 获取远程更新                             | Git        | 查看远程有没有新变化，但不改本地文件。                | Fetch origin。                                 | 相对安全，但 Fetch 不等于 Pull。       |
| Fetch origin          | 获取远程仓库更新                           | Git        | 让 GitHub Desktop 看 GitHub 上有没有新版本。 | GitHub Desktop 顶部按钮。                          | 后续变成 Pull/Push 时再谨慎判断。       |
| Pull                  | 拉取                                 | Git        | 把远程新修改下载并合并到本地。                    | Pull origin、git pull。                         | 可能产生冲突。                      |
| Push                  | 推送                                 | Git        | 把本地已 Commit 的修改上传远程。               | Push origin、git push。                         | 确认 Diff、Build、自检后再 Push。     |
| Push origin           | 推送到远程仓库                            | Git        | 把本地提交上传到 GitHub 对应仓库。              | GitHub Desktop 顶部按钮。                          | Push 后别人或部署流程可能看到这些代码。       |
| Merge                 | 合并                                 | Git        | 把一个分支修改合到另一个分支。                    | GitHub Desktop、Pull Request。                  | 不懂冲突时不要强行合并。                 |
| Conflict              | 冲突                                 | Git        | 两边都改了同一处，Git 不知道保留谁。               | merge conflict、pull conflict。                 | 需要人工选择保留内容。                  |
| Clone                 | 克隆                                 | Git        | 把远程仓库完整下载到本地。                      | Clone repository、git clone。                   | 确认下载路径，避免覆盖已有项目。             |
| Checkout              | 切换                                 | Git        | 切换到某个分支或版本。                        | checkout branch、Current Branch。               | 切换前保存或提交当前修改。                |
| Stash                 | 暂存当前修改                             | Git        | 把未提交修改临时收起来。                       | git stash、VS Code。                            | Stash 多了容易忘记内容。              |
| Revert                | 反做一次提交                             | Git        | 新增一个提交来撤销之前提交。                     | GitHub、git revert。                            | 已 push 后通常比 reset 更安全。       |
| Reset                 | 重置                                 | Git        | 把仓库状态退回某个版本。                       | git reset。                                    | 小白不建议自行使用，hard reset 可能丢数据。  |
| Pull Request          | PR / 合并请求                          | Git        | 请求把一个分支合并到另一个分支。                   | GitHub 网页。                                    | 没看 Diff 和检查结果不要 Merge。       |
| Release               | 版本发布                               | Git/部署     | 给稳定版本打包或标记。                        | GitHub Releases、软件版本号。                        | 不要把测试版误发成正式版。                |
| 命令行                   | Command Line / CLI                 | 命令行        | 通过文字命令操作电脑或服务器的窗口。                 | PowerShell、CMD、Linux 终端。                      | 复制命令前先确认它做什么、在哪执行。           |
| Terminal              | 终端                                 | 命令行        | 输入命令的窗口。                           | Windows Terminal、VS Code Terminal、服务器。        | 本地终端和服务器终端不要混淆。              |
| PowerShell            | Windows PowerShell                 | 命令行        | Windows 自带的现代命令行工具。                | 开始菜单、VS Code 终端。                              | 从网上复制脚本前要确认安全。               |
| CMD                   | 命令提示符                              | 命令行        | Windows 早期命令行工具。                   | cmd.exe。                                      | 不要混用 Linux 命令和 CMD 命令。       |
| Shell                 | 外壳                                 | 命令行        | 负责解释你输入命令的程序。                      | bash、zsh、PowerShell。                          | 同一命令在 Windows 和 Linux 可能不同。  |
| 当前目录                  | Current Directory                  | 命令行        | 命令行现在所在的文件夹。                       | 终端提示符、pwd、cd。                                 | 很多命令必须在项目根目录执行。              |
| 路径                    | Path                               | 文件/命令行     | 文件或文件夹的位置。                         | C:\Projects\demo-app、/var/www/demo、src/main.ts。 | 有空格、中文、括号时命令里可能要加引号。         |
| 绝对路径                  | Absolute Path                      | 文件/命令行     | 从磁盘或根目录开始的完整路径。                    | D:\...、/www/...。                              | 不同电脑上的绝对路径可能不同。              |
| 相对路径                  | Relative Path                      | 文件/命令行     | 相对于当前目录的位置。                        | src/index.js、../config。                       | 当前目录变了，相对路径含义也变。             |
| cd                    | Change Directory                   | 命令行        | 切换命令行所在文件夹。                        | cd project-folder。                            | 执行项目前先 cd 到正确目录。             |
| dir                   | 列出文件                               | 命令行        | 查看当前文件夹里有什么。                       | Windows CMD / PowerShell。                     | 只读查看，通常安全。                   |
| ls                    | list                               | 命令行        | 查看当前文件夹里有什么。                       | Linux、Git Bash、macOS。                         | 只读查看，通常安全。                   |
| mkdir                 | Make Directory                     | 命令行        | 新建文件夹。                             | mkdir logs、mkdir backup。                      | 确认路径，避免建错位置。                 |
| pwd                   | Print Working Directory            | 命令行        | 显示当前命令行所在路径。                       | Linux、Git Bash。                               | 只读查看，通常安全。                   |
| Ctrl + C              | 中断命令                               | 命令行        | 停止当前正在运行的命令或程序。                    | 终端卡住、开发服务运行中。                                 | 数据库迁移、部署写入时不要随便中断。           |
| curl                  | 命令行请求工具                            | 命令行/网络     | 用命令行访问网址或接口。                       | curl http://...、curl -4 ifconfig.me。          | 不要执行来源不明的 curl ｜ bash。       |
| ping                  | 网络连通测试                             | 命令行/网络     | 测试能不能连到某个域名或 IP。                   | ping assets.example.com。                      | ping 不通不一定代表网站不能访问。          |
| nslookup              | DNS 查询                             | 命令行/域名     | 查询域名解析到了哪个 IP。                     | nslookup assets.example.com。                  | 不同网络可能有缓存差异。                 |
| ipconfig              | Windows 网络配置查看                     | 命令行/网络     | 查看本机网络信息。                          | PowerShell / CMD。                             | 不要随便改系统网络设置。                 |
| 管理员权限                 | Run as Administrator               | Windows    | 以更高权限运行程序。                         | 安装软件、改端口、防火墙。                                 | 管理员权限下误操作影响更大。               |
| 环境变量                  | Environment Variable               | 系统/配置      | 程序运行时读取的配置值。                       | API_KEY、DATABASE_URL、NODE_ENV、.env。           | 密钥不要提交到 GitHub。              |
| PATH                  | 系统路径变量                             | 系统/命令行     | 系统寻找命令程序的位置清单。                     | Node、Git、Python 安装配置。                         | 不要随便删除 PATH 原有内容。            |
| Log                   | 日志                                 | 开发/服务器     | 程序运行过程留下的记录。                       | Nginx log、后端日志、Codex 输出。                      | 日志可能含敏感信息，不要公开。              |
| 域名                    | Domain                             | 域名         | 网站的人类可读地址。                         | example.com、域名控制台、浏览器地址栏。                     | 域名要解析到服务器 IP 才能访问服务。         |
| 子域名                   | Subdomain                          | 域名         | 主域名前面加一段的新地址。                      | assets.example.com、api.example.com。           | 拼写必须准确，少一个字母就是另一个域名。         |
| DNS                   | Domain Name System                 | 域名         | 把域名翻译成 IP 地址的系统。                   | 域名解析、DNS 控制台、nslookup。                        | 不要随便改 NS 记录。                 |
| 域名解析                  | DNS Resolution                     | 域名         | 配置域名应该指向哪个服务器 IP。                  | 腾讯云/阿里云/DNSPod。                               | 解析生效有延迟，不要频繁乱改。              |
| A 记录                  | A Record                           | 域名         | 把域名直接指向一个 IPv4 地址。                 | DNS 解析控制台。                                    | IP 写错会访问失败或访问错机器。            |
| CNAME                 | 别名记录                               | 域名         | 把一个域名指向另一个域名。                      | CDN、云服务自定义域名。                                 | 同一主机记录通常不能同时配 A 和 CNAME。     |
| NS 记录                 | Name Server                        | 域名         | 指定由哪组 DNS 服务器管理解析。                 | 域名注册商、DNS 服务商。                                | 改错会影响整个域名解析。                 |
| TTL                   | Time To Live                       | 域名         | DNS 解析结果被缓存多久。                     | DNS 解析记录设置。                                   | 刚改解析时各地生效可能不一致。              |
| IP 地址                 | IP Address                         | 网络         | 服务器或设备在网络中的数字地址。                   | 示例公网 IP、本机回环地址。                              | 不要公开敏感管理入口和登录信息。             |
| 公网 IP                 | Public IP                          | 服务器        | 外部网络可访问的服务器地址。                     | 腾讯云服务器、curl -4 ifconfig.me。                   | 公网服务要注意端口、防火墙、安全组。           |
| localhost             | 本机地址                               | 网络/开发      | 指当前这台电脑自己。                         | localhost:3000、127.0.0.1。                     | 手机访问 localhost 是访问手机自己，不是电脑。 |
| 127.0.0.1             | Loopback                           | 网络/开发      | 本机回环地址，基本等同 localhost。             | http://127.0.0.1:3000。                        | 不能作为正式外网地址。                  |
| 端口                    | Port                               | 网络/服务器     | 同一台服务器上不同服务的门牌号。                   | 3000、80、443。                                  | 不要把数据库端口暴露公网。                |
| 3000 端口               | Port 3000                          | 网络/开发      | 开发环境常用端口。                          | localhost:3000、Node/Express。                  | 正式服务通常用 Nginx 转发。            |
| 防火墙                   | Firewall                           | 网络/安全      | 控制哪些连接能进出服务器或电脑。                   | Windows 防火墙、腾讯云安全组。                           | 不要开放所有端口。                    |
| 安全组                   | Security Group                     | 云服务器       | 云服务器平台上的防火墙规则。                     | 腾讯云、阿里云控制台。                                   | 只开放必要端口。                     |
| HTTP                  | HyperText Transfer Protocol        | 网络         | 网页和接口传输数据的基础协议。                    | http:// 开头网址。                                 | 正式环境优先用 HTTPS。               |
| HTTPS                 | 安全 HTTP                            | 网络         | 加密版 HTTP。                          | https:// 开头网址、线上接口。                          | 证书过期会导致访问失败。                 |
| SSL 证书                | SSL/TLS Certificate                | 网络         | 让网站支持 HTTPS 的证书。                   | Nginx、宝塔、云服务器。                                | 证书到期或域名不匹配会报错。               |
| Nginx                 | Web 服务器 / 反向代理                     | 服务器        | 接收网页请求、返回静态文件或转发后端的服务。             | Nginx 配置、access.log、error.log。                | 改配置前备份并测试。                   |
| 反向代理                  | Reverse Proxy                      | 服务器        | 外部访问 Nginx，Nginx 再转给内部后端。          | proxy_pass、API 域名转发。                          | 路径配置错会导致 404、502。            |
| 代理                    | Proxy                              | 网络         | 网络请求先经过一个中间服务再出去。                  | Clash、VPN、系统代理。                               | 不要轻易关闭代理，可能影响 ChatGPT 连接。    |
| VPN                   | Virtual Private Network            | 网络         | 通过加密通道连接网络。                        | 系统代理、Clash、网络排查。                              | 正在用 ChatGPT 时不要随意断开。         |
| Clash                 | 代理工具                               | 网络         | 常见代理/VPN 客户端。                      | 系统托盘、代理设置。                                    | 优先用图形界面，不要直接改配置文件。           |
| CDN                   | 内容分发网络                             | 网络/静态资源    | 把图片等静态资源分发到更近节点。                   | 图片外链、静态资源加速。                                  | 缓存会导致更新不马上生效。                |
| 静态资源                  | Static Assets                      | 前端/服务器     | 图片、CSS、JS 等可直接访问文件。                | assets、public、头像图片。                           | 路径改错会导致加载失败。                 |
| 服务器                   | Server                             | 服务器        | 放网站、接口、数据库或资源的远程电脑。                | 腾讯云、Linux、Nginx、Docker。                       | 不要直接删除未知文件或重启不熟悉服务。          |
| Linux                 | Linux 系统                           | 服务器        | 服务器常用操作系统，多用命令行操作。                 | 腾讯云服务器、SSH 终端。                                | rm、chmod、systemctl 要谨慎。      |
| SSH                   | Secure Shell                       | 服务器        | 远程登录服务器的安全方式。                      | ssh root@服务器IP。                               | root 权限很高，误操作影响大。            |
| Docker                | 容器工具                               | 部署         | 把程序和运行环境打包在容器里。                    | Docker Desktop、服务器容器。                         | 不要随便删容器和 volume。             |
| Container             | 容器                                 | Docker     | Docker 运行起来的程序盒子。                  | math-profile-backend、docker ps。               | 重建前确认数据是否保存在 volume。         |
| Image                 | 镜像                                 | Docker     | 创建容器的模板。                           | docker images、构建镜像。                           | 代码更新后可能需要重建镜像。               |
| Docker Compose        | docker-compose                     | Docker     | 用一个配置文件管理多个容器。                     | docker-compose.yml。                           | down、rm、volume 相关命令要谨慎。      |
| Volume                | 数据卷                                | Docker/数据  | Docker 保存数据的地方。                    | 数据库容器、上传文件目录。                                 | 删除 volume 可能直接丢数据。           |
| Deploy                | 部署 / 上线                            | 部署         | 把项目放到服务器上运行。                       | Nginx、Docker、服务器。                             | 部署前确认 Build、环境变量、数据库、端口。     |
| CI                    | Continuous Integration             | 部署         | 代码提交后自动跑检查、测试、构建。                  | GitHub Actions、CI 验证。                         | CI 通过不等于业务功能完全正确。            |
| CD                    | Continuous Deployment              | 部署         | 代码通过检查后自动部署。                       | 自动发布、GitHub Actions。                          | 配置错可能把测试代码发到正式环境。            |
| GitHub Actions        | GitHub 自动化流程                       | 部署/Git     | GitHub 上的自动测试、构建、部署系统。             | Actions 标签页。                                  | 不要把密钥直接写进 workflow。          |
| Secrets               | 密钥变量                               | 安全/部署      | 平台安全保存密码、API Key、服务器密钥的位置。         | GitHub Secrets、云平台密钥管理。                       | 不要截图或公开 Secrets 内容。          |
| 前端                    | Frontend                           | 前端         | 用户看得见、点得到的界面部分。                    | 网页、管理后台、React、Vue。                             | 改完要看实际界面效果。                  |
| 后端                    | Backend                            | 后端         | 服务器上处理数据、接口、业务逻辑的部分。               | Express、Flask、API、数据库。                        | 后端改动可能影响所有用户和真实数据。           |
| 全栈                    | Full Stack                         | 开发         | 同时涉及前端、后端、数据库、部署。                  | 全栈项目、数据看板、管理后台。                               | 全栈任务消耗高，建议拆分。                |
| React                 | React.js                           | 前端         | 常见网页前端开发框架。                        | 管理后台、Vite、组件开发。                               | 改组件后要 Build 和页面测试。           |
| Vue                   | Vue.js                             | 前端         | 另一种常见前端框架。                         | 管理后台、Ruoyi 前端。                                | 先确认项目技术栈，不要混用 React 写法。      |
| 组件                    | Component                          | 前端         | 页面上的可复用小模块。                        | 按钮、卡片、表格。                                     | 一个组件可能影响多个页面。                |
| Node.js               | Node                               | 后端/前端工具    | 让 JavaScript 在电脑或服务器运行的环境。         | npm、Express、Vite。                             | Node 版本不一致可能构建失败。            |
| npm                   | Node Package Manager               | Node       | Node 项目安装依赖和运行脚本的工具。               | npm install、npm run build。                    | 不要装来源不明的依赖。                  |
| package.json          | Node 项目配置文件                        | Node       | 记录依赖、脚本命令和项目信息。                    | 项目根目录。                                        | 改依赖版本可能引发连锁问题。               |
| npm run build         | 构建命令                               | 前端/Node    | 运行 package.json 里的 build 脚本。       | Codex 自检、前端部署。                                | Build 失败不要继续部署。              |
| Vite                  | 前端构建工具                             | 前端         | 用于开发和打包前端项目。                       | Vite build、React 管理后台。                        | 配置错会导致页面启动或资源路径错误。           |
| Express               | Express.js                         | 后端/Node    | Node 常用后端框架。                       | backend/src/index.js、端口 3000。                 | 接口改动要确认前端是否同步适配。             |
| Flask                 | Python Flask                       | 后端/Python  | Python 轻量后端框架。                     | 本地小工具、后台管理系统。                                | 部署时关注 Python 版本、uwsgi、Nginx。 |
| Python                | Python                             | 编程语言       | 常用于脚本、数据处理、后端工具。                   | Flask、自动化、文件转换。                               | 先确认 Python 版本。               |
| JavaScript            | JS                                 | 编程语言       | 网页和 Node 后端常用语言。                   | .js 文件、React、Express。                         | JS 可能在前端也可能在后端。              |
| TypeScript            | TS                                 | 编程语言       | 带类型检查的 JavaScript。                 | .ts、.tsx 文件。                                  | 不要用 any 粗暴绕过所有类型检查。          |
| JSON                  | JavaScript Object Notation         | 数据格式       | 常见结构化数据格式。                         | API 返回、配置文件、网页接口。                            | 少逗号或引号会格式错误。                 |
| Request               | 请求                                 | 接口         | 前端向后端发出的动作。                        | Network、fetch、后端日志。                           | 提交类请求可能改变数据。                 |
| Response              | 响应                                 | 接口         | 后端收到请求后返回的结果。                      | JSON、接口测试、Network。                            | 看状态码和返回内容。                   |
| Endpoint              | 接口地址                               | 接口         | 某个 API 的具体访问路径。                    | /api/questions、/weapp/detail-report-requests。 | 测试接口和正式接口不要混用。               |
| GET                   | HTTP GET                           | 接口         | 从后端获取数据的请求方式。                      | 接口文档、浏览器地址访问。                                 | 不要用 GET 传敏感信息。               |
| POST                  | HTTP POST                          | 接口         | 向后端提交数据的请求方式。                      | 表单提交、登录、申请详细报告。                               | 重复点击可能重复提交。                  |
| Body                  | 请求体                                | 接口         | POST 请求里携带的数据内容。                   | 接口调试、JSON 提交。                                 | 不要放不该暴露的密钥。                  |
| Header                | 请求头                                | 接口         | 请求附带的说明信息。                         | Authorization、Content-Type。                   | Authorization 可能含登录凭证。       |
| 状态码                   | Status Code                        | 接口         | 服务器用数字说明请求结果。                      | 200、404、500、502、429。                          | 只看状态码不够，还要看日志。               |
| 200                   | OK                                 | 接口         | 请求成功。                              | curl 返回、Network、Nginx 日志。                     | 200 不等于业务数据一定正确。             |
| 404                   | Not Found                          | 接口         | 访问路径不存在。                           | 网页打不开、接口路径错误。                                 | 优先查路径、路由、Nginx，不要先改数据库。      |
| 500                   | Internal Server Error              | 接口         | 服务器内部报错。                           | API 返回、后端日志。                                  | 看后端 error log。               |
| 502                   | Bad Gateway                        | 服务器        | Nginx 找不到或连不上后端。                   | 网页 502、API 502。                               | 查后端服务、端口、proxy_pass。         |
| CORS                  | 跨域                                 | 前后端        | 浏览器限制网页随便请求其他域名的安全机制。              | Access-Control-Allow-Origin。                  | 正式环境不要无脑允许所有来源。              |
| 数据库                   | Database                           | 数据库        | 保存业务数据的地方。                         | MySQL、SQLite、Redis、Prisma。                    | 改数据库前必须备份。                   |
| MySQL                 | MySQL Database                     | 数据库        | 常见关系型数据库。                          | 后端项目、服务器部署、Prisma。                            | 不要把数据库端口暴露公网。                |
| SQLite                | 轻量数据库                              | 数据库        | 文件型小数据库，适合原型或本地工具。                 | Flask 小工具、本地数据。                               | 不一定适合多人高并发正式系统。              |
| Redis                 | 缓存数据库                              | 数据库/缓存     | 常用于缓存、队列、临时状态。                     | Docker Compose、后端部署。                          | Redis 暴露公网风险高。               |
| Prisma                | ORM 工具                             | 数据库        | 让后端更方便操作数据库的工具。                    | schema.prisma、migration。                      | Migration 会改数据库结构，必须谨慎。      |
| ORM                   | 对象关系映射                             | 数据库        | 把数据库表和代码对象连接起来的工具。                 | Prisma、Sequelize。                             | 配置错可能读写错表。                   |
| Migration             | 数据库迁移                              | 数据库        | 修改数据库结构的版本记录。                      | prisma/migrations。                            | 正式库 migration 前必须备份。         |
| Schema                | 结构定义                               | 数据库/数据     | 定义数据有哪些表、字段、类型。                    | schema.prisma、JSON schema。                    | 字段乱改会影响旧数据和接口。               |
| CRUD                  | 增删改查                               | 后台/数据库     | 新增、查询、修改、删除四类基础操作。                 | 后台管理、用户列表、内容管理。                               | 删除功能要有确认、权限和日志。              |
| Obsidian              | Obsidian                           | 知识库        | 基于 Markdown 文件的本地知识库工具。            | 个人知识库、模板、插件。                                  | 插件修改文件前要备份。                  |
| Vault                 | 库 / 仓库                             | Obsidian   | Obsidian 管理的一整个文件夹。                | D:\Notes、个人知识库目录。                              | 不要随意重命名或移动整个 Vault。          |
| Markdown              | MD                                 | 文档         | 用 #、-、表格等表示结构的纯文本格式。               | .md、README、审核报告。                              | 复杂排版不如 Word，但适合 AI 和 Git。    |
| README                | 说明文件                               | 文档/Git     | 项目说明书。                             | README.md、GitHub 首页。                          | README 更新不代表代码实际已更新。         |
| Frontmatter           | 文件头元数据                             | Markdown   | Markdown 顶部用 --- 包起来的信息。           | Obsidian 模板、文档属性。                             | 格式错可能影响插件识别。                 |
| 插件                    | Plugin                             | 工具         | 给软件增加额外功能的扩展模块。                    | Obsidian、浏览器、VS Code。                         | 插件可能读取或修改本地文件。               |
| manifest.json         | 插件清单                               | 插件         | 描述插件名称、版本、入口文件等信息。                 | Obsidian 插件目录。                                | 不要随便改 id 或入口文件。              |
| main.js               | 主脚本                                | 插件/JS      | 插件运行的主要代码文件。                       | Obsidian 插件目录。                                | 优先改源码再构建，不要手改压缩产物。           |
| 命令面板                  | Command Palette                    | 工具         | 通过搜索命令执行软件功能的面板。                   | Obsidian Ctrl+P、VS Code。                      | 批量命令前确认作用范围。                 |
| 快捷键                   | Hotkey                             | 工具         | 用键盘组合快速触发功能。                       | Ctrl+Shift+E、Obsidian、桌面助手。                   | 全局快捷键要避免冲突。                  |
| 文件监听                  | File Watcher                       | 自动化        | 程序观察文件夹，有新文件就自动处理。                 | Word/Excel 转 Markdown 插件。                     | 监听目录配置错会批量处理错误文件。            |
| .docx                 | Word 文档格式                          | 文档         | 新版 Word 文件格式。                      | 制度、报告、模板、说明文档。                                | 转 Markdown 可能丢复杂格式。          |
| .md                   | Markdown 文件                        | 文档         | Markdown 格式纯文本文件。                  | Obsidian、GitHub、Codex 指令。                     | 不是所有业务同事都习惯阅读。               |
| .env                  | 环境变量文件                             | 安全/配置      | 保存本地或服务器运行配置，常含密钥。                 | Node、Flask、后端项目。                              | 应加入 .gitignore，不要提交。         |
| .gitignore            | Git 忽略文件                           | Git/配置     | 告诉 Git 哪些文件不要纳入版本管理。               | 项目根目录。                                        | 配置错会漏提交或误提交敏感文件。             |
| node_modules          | Node 依赖目录                          | Node       | npm 安装的第三方依赖文件夹。                   | Node 项目根目录。                                   | 通常不提交到 Git。                  |
| 配置                    | Config                             | 通用         | 控制程序行为的设置项。                        | config.js、JSON、环境变量、后台配置中心。                   | 配置改错可能影响全局功能。                |
| 写死                    | Hardcode                           | 开发         | 把本应可配置的内容直接写进代码。                   | 域名、文案、图片地址、类型画像。                              | 后续每次改都要动代码。                  |
| 配置中心                  | Configuration Center               | 系统设计       | 集中管理文案、题库、报告、开关等配置的后台。             | 管理后台、内容后台、业务系统。                               | 要有版本、审核、回滚机制。                |
| 权限                    | Permission                         | 安全         | 谁能看、谁能改、谁能删除的规则。                   | 后台管理、飞书、数据库。                                  | 不要所有人都给管理员。                  |
| 角色                    | Role                               | 权限         | 按身份分配功能权限。                         | 管理员、运营、财务、普通用户。                               | 先设计角色，再配置权限。                 |
| 日志审计                  | Audit Log                          | 安全         | 记录谁在什么时候做了什么操作。                    | 后台管理、数据修改记录。                                  | 没有日志很难追责和回滚。                 |
| 版本号                   | Version                            | 发布         | 标记文件、功能或软件当前版本。                    | v0.1、v2.5、文档模板版本。                             | 版本混乱会导致业务拿错文件。               |
| 变更记录                  | Changelog                          | 文档/发布      | 记录每个版本改了什么。                        | README、发布说明、开发进度文档。                           | 不要只写“优化了”。                   |
| 缓存                    | Cache                              | 网络/系统      | 为了加速访问临时保存的旧数据。                    | 浏览器缓存、DNS 缓存、CDN 缓存。                          | 资源没更新可能是缓存，但要结合日志判断。         |
| 浏览器 Network           | Network 面板                         | 调试         | 浏览器开发者工具里查看请求和资源加载。                | F12、接口排查。                                     | 不要公开 Token、Cookie、接口敏感参数。    |
| Cookie                | Cookie                             | 登录/Web     | 浏览器保存的登录或状态信息。                     | 开发者工具、登录态。                                    | Cookie 可能代表你的登录身份。           |
| Session               | 会话                                 | 登录/Web     | 服务器记录当前登录状态的方式。                    | 登录系统、后台管理。                                    | 不要共享会话信息。                    |
| 登录 Token              | Auth Token                         | 安全/登录      | 证明已登录或有权限访问接口的一串字符。                | Authorization Header、Network。                 | 泄露后别人可能冒用身份。                 |
| 401                   | Unauthorized                       | 接口/权限      | 没有登录或认证失败。                         | 接口返回、Network。                                 | 不要为解决 401 直接关闭权限校验。          |
| 403                   | Forbidden                          | 接口/权限      | 已识别身份，但没有权限访问。                     | 后台接口、文件访问。                                    | 不要直接把所有权限开放。                 |
| 桌面小工具                 | Desktop App                        | 桌面工具       | 安装在电脑本地运行的小应用。                     | Windows 托盘、快捷键助手。                             | 要明确是否读取剪贴板、选中文字。             |
| 全局快捷键                 | Global Hotkey                      | 桌面工具       | 无论在哪个 App，按组合键就触发功能。               | Ctrl+Shift+E。                                 | 避免和常用软件冲突。                   |
| 剪贴板                   | Clipboard                          | 系统/隐私      | 复制内容后临时存放的地方。                      | 复制粘贴、全局解释工具。                                  | 可能含内部文档、密码、API Key，读取和保存要受控。 |
| 选中文字                  | Selected Text                      | 桌面工具       | 鼠标或键盘框选的一段文字。                      | 浏览器、GitHub Desktop、命令行、文档。                    | 不要默认把敏感长文本上传 AI。             |
| 本地词典                  | Local Dictionary                   | 桌面工具       | 词库保存在电脑本地，不联网也能查。                  | MVP 版解释助手。                                    | 解释范围受词库限制。                   |
| AI 增强版                | AI Enhanced Mode                   | 桌面工具/AI    | 本地查不到时交给 AI 解释。                    | 解释助手高级模式。                                     | 需要 API Key，敏感内容要确认再发送。       |
| 弹窗                    | Popup                              | 桌面工具/UI    | 按快捷键后出现的小窗口。                       | 选词解释、错误提示。                                    | 不要遮挡关键操作或默认抢焦点。              |
| 托盘                    | System Tray                        | Windows    | Windows 右下角后台应用图标区域。                | Clash、输入法、桌面助手。                               | 后台运行工具要能清楚退出。                |
| ERR_CONNECTION_CLOSED | 连接被关闭                              | 报错/网络      | 浏览器连接服务器时被中途断开。                    | Chrome 访问 API 或网页。                            | 查网络、代理、防火墙、Nginx、服务器日志。      |
| NXDOMAIN              | 域名不存在                              | 报错/DNS     | DNS 查不到这个域名。                       | nslookup server can't find。                   | 检查域名拼写和解析记录。                 |
| Connection refused    | 连接被拒绝                              | 报错/网络      | 目标机器到了，但端口没有服务接收。                  | curl、浏览器、后端连接。                                | 查服务是否启动、端口、防火墙。              |
| Timeout               | 超时                                 | 报错/网络      | 请求等太久没收到结果。                        | 接口调用、浏览器、API 日志。                              | 不要无限重试，可能造成压力。               |
| 不是内部或外部命令             | Command not recognized             | 报错/Windows | 系统找不到你输入的命令程序。                     | CMD、PowerShell。                               | 检查软件是否安装、PATH 是否配置。          |
| Permission denied     | 权限不足                               | 报错/服务器     | 当前用户没有权限执行或访问。                     | Linux、Git、服务器文件。                              | 不要无脑 chmod 777。              |
| Module not found      | 模块未找到                              | 报错/Node    | 代码引用了依赖或文件，但项目找不到。                 | npm run build、Vite、Node。                      | 先查依赖安装和路径，不要盲目装包。            |
| Build failed          | 构建失败                               | 报错/开发      | 项目打包或编译没有通过。                       | npm run build、Vite、Node 项目。                   | 失败时不要继续部署。                   |
| Cannot find module    | 找不到模块                              | 报错/Node    | Node 项目找不到要加载的包或文件。                | 启动后端、npm run build。                           | 先 npm install，再查 import 路径。  |
| Port already in use   | 端口被占用                              | 报错/开发      | 某个端口已经有程序在用了。                      | 启动本地服务、Node 后端。                               | 不要随便结束不认识的系统进程。              |
| Merge conflict        | 合并冲突                               | 报错/Git     | Git 合并时同一处被两边修改。                   | Pull、Merge、GitHub Desktop。                    | 暂停操作，人工选择保留内容。               |

---

# 推荐桌面工具解释输出格式

当用户选中一个词，建议桌面小工具按以下结构展示：

```md
【词条】Push origin

【一句话解释】
把你电脑上已经提交的代码上传到 GitHub 远程仓库。

【你现在看到它，通常意味着】
你本地有 Commit，但 GitHub 上还没有这些修改。

【小白操作建议】
先看 Changes / Diff，确认没有误改、没有密钥文件，再点 Push origin。

【不要乱点的情况】
如果你不确定当前仓库、分支、提交内容，或者 Build 没通过，先不要 Push。

【相关词】
Commit、Origin、Remote Repo、Fetch origin
```

# 后续版本建议

```txt
v0.1 初版：覆盖高频 AI / Git / 命令行 / 域名 / 服务器 / 前端开发术语。
v0.2 增补：根据用户实际选词记录补充新词。
v0.3 增补：加入更多常见报错解释。
v0.4 增补：加入命令安全等级。
v1.0 稳定版：支持本地词典检索 + AI 增强模式。
```

# 建议安全等级字段

后续可以给每个词条增加 `安全等级`：

```txt
低：只读、查看、解释类，如 dir、ls、Fetch。
中：会改变本地状态，如 Commit、npm install、Build。
高：会影响远程、服务器、数据库或公开结果，如 Push、Deploy、Migration。
禁止自动执行：rm、reset --hard、force push、删除数据库、公开 API Key。
```

# MVP 第一批优先匹配词

```txt
git
commit
push
push origin
fetch
fetch origin
pull
origin
branch
merge
conflict
repo
GitHub Desktop
domain
DNS
A record
CNAME
TTL
IP
port
localhost
Nginx
server
Docker
Docker Compose
container
API
API Key
JSON
GET
POST
status code
npm
npm run build
Node.js
Vite
React
backend
frontend
database
Prisma
migration
Obsidian
Markdown
plugin
manifest.json
.env
```

# 给 Codex 的维护口径

```txt
请把本文件作为桌面术语解释工具的初版词库。
维护时不要删除原词条；如需修改，优先补充“别名 / 英文”“你通常在哪里看到”“操作 / 风险提醒”。
新增词条必须保持统一字段结构，方便后续解析。
不得在词库中写入 API Key、密码、服务器登录凭据、内部文档原文、客户隐私或公司敏感信息。
如后续要用于程序检索，可按 Markdown 表格读取，或将表格转换为 JSON/YAML。
```
