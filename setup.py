from setuptools import setup, find_packages

setup(
    name="deepseek_cli",
    version="0.1.0",
    description="一个基于 DeepSeek API 的智能运维助手 CLI 工具",
    author="Shibo Li",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "openai",
        "rich",
        "pyperclip"
    ],
    entry_points={
        "console_scripts": [
            "deepseek_cli=cli:run_cli"   # 命令名=模块路径:函数
        ]
    },
    python_requires=">=3.8",
)
