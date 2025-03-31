import os
import re
from openai import OpenAI
from core.config import load_config
from utils.logger import logger

PROMPT_DIR = os.path.join(os.path.dirname(__file__), "..", "prompts")

def load_prompt(filename):
    path = os.path.join(PROMPT_DIR, filename)
    with open(path, encoding="utf-8") as f:
        return f.read()

class DeepSeekClient:
    def __init__(self):
        config = load_config()
        self.client = OpenAI(
            base_url=config["base_url"],
            api_key=config["api_key"]
        )
        self.model = config.get("default_model", "deepseek-model")

    def ask(self, messages):
        logger.info("调用 API，模型: %s", self.model)
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            raw_content = response.choices[0].message.content.strip()
            logger.info("API 响应成功")
            cleaned = self._clean_response(raw_content)
            return cleaned
        except Exception as e:
            logger.error("API 调用失败: %s", e)
            raise

    def _clean_response(self, content: str) -> str:
        match = re.search(r"```(?:bash)?\s*(.+?)\s*```", content, re.DOTALL)
        if match:
            cleaned = match.group(1).strip()
            logger.info("提取命令成功（清洗 Markdown）: %s", cleaned)
            return cleaned
        else:
            return content.strip()

    def generate_command(self, os_type, user_input, context=None):
        prompt_template = load_prompt("command.txt")
        prompt = prompt_template.format(os=os_type, user_input=user_input)

        messages = context.get_context() if context else []
        messages = messages + [{"role": "user", "content": prompt}]

        return self.ask(messages)

    def generate_command_with_explanation(self, os_type, user_input, context=None):
        prompt_template = load_prompt("command_explain.txt")
        prompt = prompt_template.format(os=os_type, user_input=user_input)

        messages = context.get_context() if context else []
        messages = messages + [{"role": "user", "content": prompt}]

        return self.ask(messages)

    def analyze_error(self, error_message):
        prompt_template = load_prompt("error_analysis.txt")
        prompt = prompt_template.format(error_message=error_message)
        return self.ask([{"role": "user", "content": prompt}])
