import os
import json

CONFIG_PATH = os.path.expanduser("~/.deepseek_cli/config.json")
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "default_config.json")

def ensure_config_exists():
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(DEFAULT_CONFIG_PATH, 'r') as src, open(CONFIG_PATH, 'w') as dst:
            dst.write(src.read())

def load_config():
    ensure_config_exists()
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=4)

def update_config(**kwargs):
    config = load_config()
    config.update(kwargs)
    save_config(config)

def interactive_config_setup():
    print("欢迎使用 deepseek_cli，请输入以下配置：")
    api_key = input("请输入 DeepSeek API Key: ").strip()
    model = input("默认模型 (默认: deepseek-model): ").strip() or "deepseek-model"
    update_config(api_key=api_key, default_model=model)
    print("✅ 配置已保存！")

def reset_config_to_default():
    """重置配置为默认值"""
    with open(DEFAULT_CONFIG_PATH, 'r') as src, open(CONFIG_PATH, 'w') as dst:
        dst.write(src.read())
    print("✅ 配置已重置为默认值")
