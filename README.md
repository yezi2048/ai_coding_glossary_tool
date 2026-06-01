# 码词急救包

码词急救包是一个 Windows 本地术语解释小工具，面向刚开始接触 AI 编程、Git、命令行、域名、部署和常见开发工具的非程序员用户。

它的目标很简单：看到陌生术语时，选中文字，按快捷键，就能得到“小白能懂”的解释和操作风险提醒。

## 功能

- 全局快捷键：选中文字后按 `Ctrl+Shift+E`
- 本地 Markdown 词库：不联网，不需要 API Key
- 支持手动搜索和解释剪贴板
- 输出包含：小白解释、常见出现位置、操作/风险提醒
- 词库可直接用 Markdown 表格维护

## 安装

1. 安装 Python 3.10 或更新版本。
2. 下载本仓库。
3. 在 PowerShell 里进入项目目录。
4. 执行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\ai_coding_glossary_tool\install.ps1
```

安装后会创建：

- 开始菜单快捷方式：`码词急救包`
- 开机自启快捷方式
- 本地安装目录：`%LOCALAPPDATA%\CodexTools\AICodingGlossary`

## 使用

1. 在任意 App 或浏览器里选中术语，例如 `push origin`、`DNS`、`API Key`。
2. 按 `Ctrl+Shift+E`。
3. 查看弹窗解释。

如果某些软件不允许自动读取选中文字，可以先按 `Ctrl+C`，再在工具窗口点击“解释剪贴板”。

## 词库

默认词库在：

```txt
ai_coding_glossary_tool\data\glossary\ai_coding_beginner_glossary.md
```

维护词库时保持表格字段一致：

- 词条
- 别名 / 英文
- 分类
- 小白解释
- 你通常在哪里看到
- 操作 / 风险提醒

修改词库后，在工具窗口点击“重载词库”即可生效。

## 隐私

当前版本是本地词典版，不接入 AI API，不会主动上传选中文字或剪贴板内容。

它通过临时模拟 `Ctrl+C` 读取当前选中文字，并尽量恢复原来的文本剪贴板。请避免在密码、密钥、内部文档原文等敏感内容上触发解释。

## 卸载

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\CodexTools\AICodingGlossary\uninstall.ps1"
```

## 许可证

MIT License
