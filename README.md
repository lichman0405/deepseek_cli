# 🤖 deepseek_cli

一个基于 DeepSeek API 的智能运维助手，支持自然语言生成终端命令、错误分析、上下文对话、命令执行与历史记录等功能。

> 🚀 支持 Linux / macOS / Windows  
> 🎨 终端界面美观（基于 [rich](https://github.com/Textualize/rich)）  
> 🧠 内置上下文记忆、命令解释与剪贴板复制  

---

## ✨ 功能亮点

- 💡 自然语言生成命令（自动适配操作系统）
- ❌ 错误日志分析，生成解决建议
- 📋 命令历史记录（可查看、导出）
- 💬 上下文记忆，支持连续提问
- 🖥️ 美观 CLI UI（`rich.panel`, `rich.live`）
- ⚙️ 支持配置 API Key 和模型参数
- ✅ 支持终端命令补全（可选）

---

## 📦 安装方式

### 1. 克隆项目

```bash
git clone https://github.com/your-org/deepseek_cli.git
cd deepseek_cli
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

或使用：

```bash
pip install -e .
```

> ✅ 安装后可直接使用命令：`deepseek_cli`

---

## 🚀 快速上手

```bash
deepseek_cli
```

交互模式下示例：

```
🧠 请输入运维需求：查看 CPU 使用率
✅ 生成的命令：top -o cpu
```

---

## 🛠️ 可用参数

| 参数              | 说明                             |
|------------------|----------------------------------|
| `--config`       | 进入交互配置模式（设置 API Key） |
| `--clear-context`| 清除当前上下文对话               |
| `--history`      | 查看命令历史记录                 |
| `--version`      | 显示当前版本                     |
| `--os <系统>`    | 指定操作系统（Linux/Windows）    |
| `--help`         | 查看 CLI 帮助信息                 |

---

## ⚙️ 配置说明

首次运行会提示设置 API Key，也可手动配置：

配置文件路径：

```bash
~/.deepseek_cli/config.json
```

示例内容：

```json
{
  "base_url": "https://api.deepseek.com/v1",
  "api_key": "your-api-key",
  "default_model": "deepseek-chat"
}
```

---

## 📂 历史记录路径

命令历史自动保存在：

```bash
~/.deepseek_cli/history.json
```

上下文持久化文件：

```bash
~/.deepseek_cli/context.json
```

---

## 🎯 TODO / 计划中功能

- [ ] 多会话上下文支持（命名切换）
- [ ] 收藏命令 / 标签系统
- [ ] 命令导出为 Markdown
- [ ] PyPI 正式发布
- [ ] 子命令支持（analyze、favorite、debug）

---

## 🙏 感谢

本项目基于 [OpenAI](https://github.com/openai/openai-python)、[DeepSeek](https://deepseek.com)、[rich](https://github.com/Textualize/rich) 构建。

---

## 📄 License

MIT License