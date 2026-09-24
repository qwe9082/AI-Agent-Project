import json
import os
from typing import Sequence

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import messages_from_dict, message_to_dict, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory


# message_to_dict: 单个消息对象（BaseMessage实例）->字典
# messages_from_dict: [字典,字典,...] -> [消息,消息,...]


class FileChatMessageHistory(BaseChatMessageHistory):
    storage_path: str
    session_id: str
    def __init__(self, session_id: str, storage_path: str):
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path, self.session_id)

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    @property # @property装饰器将messages方法变成成员属性用
    def messages(self) -> list[BaseMessage]:
        """获取消息"""
        try:
            with open(
                    os.path.join(self.storage_path, self.session_id),
                    "r",
                    encoding="utf-8",
            ) as f:
                messages_data = json.load(f)
            return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        """添加消息"""
        all_messages = list(self.messages)  # Existing messages
        all_messages.extend(messages)  # Add new messages

        serialized = [message_to_dict(message) for message in all_messages]
        file_path = os.path.join(self.storage_path, self.session_id)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def clear(self) -> None:
        """清空消息"""
        file_path = os.path.join(self.storage_path, self.session_id)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f)
model = ChatTongyi(model="qwen-max3")
prompt = PromptTemplate.from_template(
    "你需要根据会话历史消息回应用户问题。对话历史消息{chat_history}，用户提问：{input}，请回答"
)

str_parser = StrOutputParser()

base_chain = prompt | model | str_parser

store = {}
def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")

# 创建一个新的链，对原有链增强功能，附加历史消息
conversation_chain = RunnableWithMessageHistory(
    base_chain, # 被增强的原有链
    get_history, # 通过会话id或获取InMemoryChatMessageHistory
    input_messages_key="input", # 表示用户输入在模板中的占位符
    history_messages_key="chat_history" # 表示用户输入在模板中的占位符
)

if __name__ == '__name__':
    # 固定格式，添加langchain的配置。为当前程序配置所属的session_id
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    res = conversation_chain.invoke({"input": "小明有两只猫"}, session_config)
    print("第一次执行", res)

    res = conversation_chain.invoke({"input": "小红有一只狗"}, session_config)
    print("第二次执行", res)

    # res = conversation_chain.invoke({"input": "总共有几只宠物"}, session_config)
    # print("第三次执行", res)