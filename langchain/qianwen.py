# openai访问通义千问
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://ws-tr3rxxzfoq5hsbxg.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

response = client.chat.completions.create(
    model="qwen3.7-plus",
    messages=[ # 多个可附带历史消息
        {"role": "system", "content": "你是一个前端初级程序员"},
        {"role": "user", "content": "输出一段hello world的代码"},
    ],
    stream=True,
)

for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end="", # 每一段之间以空格区分
        flush=True, # 立刻刷新缓冲区
    )