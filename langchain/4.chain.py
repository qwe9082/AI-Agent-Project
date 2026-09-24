# chain 将组件串联，上一个组件的输出作为下一个组件的输入。是langchain链的核心工作原理，也是链式调用的核心价值
# 实现数据的自动化流转和组件的协调工作
# chain = prompt_template | model
# 支持注入任意数量的历史会话信息
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableSerializable

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个唐朝边塞诗人，可以写诗"),
        MessagesPlaceholder("history"),
        ("human", "请再来一首唐诗")
    ]
)

history_data = [
    ("human", "你来写一首唐诗"),
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human", "好诗再来一个"),
    ("system", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。"),
]

model = ChatTongyi(model="qwen3-max", streaming=True)

# 组成链，要求每一个组件都是Runnable接口的子类
chain:RunnableSerializable =  chat_prompt_template | model

# 通过链去调用invoke或者stream
res1 = chain.invoke({"history": history_data})
print(res1.content)
res2 = chain.stream({"history": history_data})
for chunk in res2:
    print(chunk.content, end="", flush=True)