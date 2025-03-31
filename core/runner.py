from core.api import DeepSeekClient
from core.context import ConversationContext
from core.executor import copy_to_clipboard, execute_command
from core.ui import show_result, show_error, show_menu, print_menu_options
from utils.logger import logger
from utils.history import add_history
from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
from time import sleep
from core.ui import show_welcome


console = Console()

def start_interactive_mode(os_type):
    show_welcome()
    client = DeepSeekClient()
    context = ConversationContext()

    logger.info("进入交互模式，系统: %s", os_type)
    print(f"✅ 当前操作系统: {os_type}")
    print("请选择使用模式：")
    print("1. 命令生成模式")
    print("2. 错误分析模式")
    mode = input("输入 1 或 2：").strip()

    if mode == "1":
        # 🌀 多轮对话循环
        print("\n[命令生成模式] 输入 `exit` 可随时退出。\n")
        while True:
            user_input = input("🧠 请输入运维需求：").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("👋 已退出对话，会话历史已保存。")
                logger.info("用户退出多轮对话，保存上下文")
                break

            logger.info("用户输入需求: %s", user_input)
            context.add_message("user", user_input)

            try:
                with Live(Spinner("dots", text="🧠 正在生成命令，请稍候..."), refresh_per_second=8):
                    command = client.generate_command(os_type, user_input, context=context)
                    sleep(0.3)  # 稍作停顿，增强过渡感

                logger.info("生成命令成功: %s", command)
                context.add_message("assistant", command)
                add_history(user_input, command, os_type)

                show_result("✅ 生成的命令", command)
                print_menu_options()
                choice = show_menu()

                if choice == "1":
                    copy_to_clipboard(command)
                elif choice == "2":
                    execute_command(command)
                elif choice == "3":
                    with Live(Spinner("dots2", text="💡 正在生成解释，请稍候..."), refresh_per_second=8):
                        explanation = client.generate_command_with_explanation(os_type, user_input, context=context)
                        sleep(0.3)
                    logger.info("生成解释成功")
                    show_result("📘 命令解释", explanation)
                    context.add_message("assistant", explanation)
                elif choice == "4":
                    logger.info("用户跳过命令处理")
                    print("👌 跳过当前命令。")
            except Exception as e:
                logger.error("命令生成或处理失败: %s", e)
                show_error(f"发生错误：{e}")

    elif mode == "2":
        error_input = input("请输入错误信息：").strip()
        logger.info("用户输入错误日志: %s", error_input)
        try:
            with Live(Spinner("earth", text="🔍 正在分析错误，请稍候..."), refresh_per_second=8):
                result = client.analyze_error(error_input)
                sleep(0.3)
            logger.info("错误分析完成")
            show_result("🛠️ 错误分析结果", result)
        except Exception as e:
            logger.error("错误分析失败: %s", e)
            show_error(f"分析失败：{e}")
    else:
        print("❌ 无效的选择")
        logger.warning("用户输入了无效模式: %s", mode)
