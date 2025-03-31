import os
import json

DEFAULT_CONTEXT_PATH = os.path.expanduser("~/.deepseek_cli/context.json")

class ConversationContext:
    def __init__(self, path=DEFAULT_CONTEXT_PATH, max_length=10):
        self.path = path
        self.max_length = max_length
        self.history = []
        self.load()

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})
        self.history = self.history[-self.max_length:]
        self.save()  # 自动保存更新后的内容

    def get_context(self):
        return list(self.history)

    def clear(self):
        self.history = []
        self.save()

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.history, f, indent=2, ensure_ascii=False)

    def load(self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    self.history = json.load(f)
            except Exception:
                self.history = []
        else:
            self.history = []
