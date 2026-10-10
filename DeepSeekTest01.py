import os
from openai import OpenAI

# 创建api交互客户端
client = OpenAI(
    api_key="sk-f376c75348fd4efdab6c5a74d4128df9",
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "你是什么模型"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)