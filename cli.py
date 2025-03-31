import argparse
from core.config import interactive_config_setup
from core.context import ConversationContext
from utils.os_detector import get_os_type
from utils.history import print_history
from core.runner import start_interactive_mode
from rich.console import Console
from rich.table import Table

VERSION = "0.1.0"

def print_help():
    console = Console()
    console.print("[bold cyan]\n🤖 deepseek_cli - 运维智能助手[/bold cyan]")

    table = Table(show_header=True, header_style="bold green")
    table.add_column("参数", style="yellow", no_wrap=True)
    table.add_column("功能说明", style="white")

    table.add_row("--config", "进入配置模式，设置 API Key 和模型")
    table.add_row("--clear-context", "清除上下文记录")
    table.add_row("--history", "查看命令历史记录")
    table.add_row("--version", "查看工具版本")
    table.add_row("--os <系统类型>", "指定目标系统（Linux / Windows / macOS）")
    table.add_row("--help", "显示本帮助信息")

    console.print(table)

def parse_cli_args():
    parser = argparse.ArgumentParser(add_help=False)  # 自定义 --help 样式
    parser.add_argument("--config", action="store_true")
    parser.add_argument("--clear-context", action="store_true")
    parser.add_argument("--history", action="store_true")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("--os", type=str)
    parser.add_argument("--help", action="store_true")
    return parser.parse_args()

def run_cli():
    args = parse_cli_args()

    if args.help:
        print_help()
        return

    if args.version:
        print(f"deepseek_cli version {VERSION}")
        return

    if args.config:
        interactive_config_setup()
        return

    if args.clear_context:
        ctx = ConversationContext()
        ctx.clear()
        print("✅ 上下文已清除")
        return

    if args.history:
        print_history()
        return

    os_type = args.os if args.os else get_os_type()
    start_interactive_mode(os_type)

if __name__ == "__main__":
    run_cli()
