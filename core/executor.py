import subprocess
import pyperclip
from core.ui import show_result, show_error
from utils.logger import logger

def copy_to_clipboard(command):
    try:
        pyperclip.copy(command)
        logger.info("已复制命令到剪贴板: %s", command)
        show_result("✅ 命令已复制到剪贴板", command)
    except Exception as e:
        logger.error("复制命令失败: %s", e)
        show_error(f"复制失败：{e}")

def execute_command(command):
    try:
        logger.info("执行命令: %s", command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if result.returncode == 0:
            if stdout:
                show_result("✅ 命令执行结果", stdout)
            else:
                show_result("✅ 命令执行成功，但无输出结果。")
            if stderr:
                show_result("⚠️ 命令警告输出", stderr)
        else:
            logger.error("命令执行失败: %s", stderr or "未知错误")
            show_error(stderr or "命令执行失败，未知错误")
    except Exception as e:
        logger.error("命令执行异常: %s", e)
        show_error(f"命令执行异常：{e}")
