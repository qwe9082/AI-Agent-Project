# 1.通过community包访问
from langchain_community.llms.tongyi import Tongyi
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from langchain_core.chat_history import BaseChatMessageHistory
# llm = Tongyi(model="qwen-max")
# res = llm.invoke(input="你是谁")
# print(res)

"""
流式输出
res = llm.stream(input="你是谁")
for chunk in res:
    print(chunk, end="", flush=True)
"""

# 2.通过ollama访问
# from langchain_ollama import OllamaLLM
# model = OllamaLLM(model="qwen3:4b")
# res2 = model.invoke(input="你好！")
# print(res2)

# 聊天消息
# AIMessage
# HumanMessage
# SystemMessage
chat_models = ChatTongyi(model="qwen3-max", streaming=True)
messages = [
    SystemMessage(content="你是一名来自边塞的诗人"), # 简写 ("system", "...")
    AIMessage(content="一首描述山水的诗"), # 简写 ("ai", "...")
    HumanMessage(content="给我写一首唐诗") # 简写 ("human", "...")
]
res = chat_models.stream(input=messages)
for chunk in res:
    print(chunk.content, end="", flush=True)