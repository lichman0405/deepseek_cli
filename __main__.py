from core.config import interactive_config_setup
from core.api import DeepSeekClient
from core.context import ConversationContext
from core.executor import copy_to_clipboard, execute_command
from core.ui import show_result, show_error, show_menu, print_menu_options
from utils.os_detector import get_os_type
from utils.logger import logger
from utils.history import add_history
import sys

def start_interactive_mode(os_type):
    client = DeepSeekClient()
    context = ConversationContext()

    logger.info("进入交互模式，系统: %s", os_type)
    print("请选择使用模式：")
    print("1. 命令生成模式")
    print("2. 错误分析模式")
    mode = input("输入 1 或 2：").strip()

    if mode == "1":
        user_input = input("请输入运维需求：").strip()
        logger.info("用户输入需求: %s", user_input)
        context.add_message("user", user_input)

        try:
            command = client.generate_command(os_type, user_input)
            logger.info("生成命令成功: %s", command)
            context.add_message("assistant", command)

            # ✅ 添加到历史记录
            add_history(user_input, command, os_type)

            show_result("生成的命令", command)
            print_menu_options()
            choice = show_menu()

            if choice == "1":
                copy_to_clipboard(command)
            elif choice == "2":
                execute_command(command)
            elif choice == "3":
                explanation = client.generate_command_with_explanation(os_type, user_input)
                logger.info("生成解释成功")
                show_result("命令解释", explanation)
            elif choice == "4":
                print("操作已取消。")
                logger.info("用户取消操作")
        except Exception as e:
            logger.error("命令生成或处理失败: %s", e)
            show_error(f"发生错误：{e}")

    elif mode == "2":
        error_input = input("请输入错误信息：").strip()
        logger.info("用户输入错误日志: %s", error_input)
        show_result("正在分析错误...", "")
        try:
            result = client.analyze_error(error_input)
            logger.info("错误分析完成")
            show_result("错误分析结果", result)
        except Exception as e:
            logger.error("错误分析失败: %s", e)
            show_error(f"分析失败：{e}")
    else:
        print("无效的选择。")
        logger.warning("用户输入了无效模式: %s", mode)
        sys.exit(1)

if __name__ == "__main__":
    interactive_config_setup()

    os_type = get_os_type()
    print(f"检测到操作系统：{os_type}")
    start_interactive_mode(os_type)
