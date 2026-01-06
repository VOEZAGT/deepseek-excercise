import os
from openai import OpenAI
import anthropic
"""
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)
if not api_key:
    raise ValueError("请设置环境变量 OPENAI_API_KEY")
"""
client = OpenAI(
    api_key="5dee70339ca043cfa643273100bfddcc.e48PRfsTXQnIILqV",
    base_url="https://open.bigmodel.cn/api/paas/v4/",
)
