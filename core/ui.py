from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.rule import Rule

console = Console()


def show_result(title: str, content: str):
    panel = Panel.fit(content, title=title, title_align="left", border_style="green", padding=(1, 2))
    console.print(panel)


def show_error(message: str):
    panel = Panel.fit(message, title="❌ 出错啦", title_align="left", border_style="red", padding=(1, 2))
    console.print(panel)


def print_menu_options():
    console.print("\n[bold cyan]可用操作：[/bold cyan]")
    console.print("[green]1.[/green] 复制命令")
    console.print("[green]2.[/green] 执行命令")
    console.print("[green]3.[/green] 查看命令解释")
    console.print("[green]4.[/green] 取消")


def show_menu():
    return Prompt.ask("请选择操作", choices=["1", "2", "3", "4"], default="1")


def show_welcome():
    console.print(Rule(style="bold green"))

    welcome_text = Text()
    welcome_text.append("\n🤖 deepseek_cli\n", style="bold magenta")
    welcome_text.append("一个基于 DeepSeek API 的智能运维助手\n", style="dim")
    welcome_text.append("轻松生成命令、分析错误、复制/执行一步到位\n\n", style="italic white")
    welcome_text.append("💡 输入 'exit' 可随时退出程序\n", style="bold yellow")

    panel = Panel.fit(welcome_text, title="欢迎使用", border_style="blue", padding=(1, 2))
    console.print(panel)

    console.print(Rule(style="bold green"))
