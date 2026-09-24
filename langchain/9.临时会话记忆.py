from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from prompt_toolkit.history import InMemoryHistory

model = ChatTongyi(model="qwen-max3")
prompt = PromptTemplate.from_template(
    "你需要根据会话历史消息回应用户问题。对话历史消息{chat_history}，用户提问：{input}，请回答"
)

str_parser = StrOutputParser()

base_chain = prompt | model | str_parser

store = {}
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
        return store[session_id]

# 创建一个新的链，对原有链增强功能，附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain, # 被增强的原有链
    get_history, # 通过会话id或获取InMemoryChatMessageHistory
    input_messages_key="input", # 表示用户输入在模板中的占位符
    history_messages_key="chat_history" # 表示用户输入在模板中的占位符
)

if __name__ == '__main__':
    # 固定格式，添加langchain的配置。为当前程序配置所属的session_id
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    conversation_chain.invoke({"input": "小明有两只猫"}, session_config)


