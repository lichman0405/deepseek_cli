import os
import json
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")

def ensure_history_file():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_history():
    ensure_history_file()
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_history(data):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_history(user_input, command, os_type):
    ensure_history_file()
    history = load_history()
    history.append({
        "time": datetime.now().isoformat(timespec="seconds"),
        "os": os_type,
        "input": user_input,
        "command": command
    })
    save_history(history)

def print_history():
    history = load_history()
    if not history:
        print("暂无历史记录。")
        return

    print("📜 命令历史记录：")
    for item in history[-10:]:  # 最近10条
        print(f"[{item['time']}] ({item['os']})")
        print(f"  需求：{item['input']}")
        print(f"  命令：{item['command']}")
        print("-" * 40)
