# rag核心服务
from vector_stores import VectorStoresService
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from file_history_store import get_history
import config_data as config
class RagService:
    def __init__(self):
        self.vectors = VectorStoresService(
            embedding=DashScopeEmbeddings(model=config.embedding_model_name)
        )
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "以我提供的已知参考资料为主,简介和专业的回答用户的提问。参考资料{context}."),
                ("system", "并且我提供用户的历史记录如下{history}"),
                MessagesPlaceholder("history"),
                ("user", "回答用户提问{input}")
            ]
        )
        self.chat_model = ChatTongyi(model=config.chat_model_name)

        self.chain = self.__get_chain()

    def __get_chain(self):
        """获取最终的执行链"""
        retriever = self.vectors.get_retriever()

        def format_function(docs: list[Document]):
            if not docs:
                return "无相关参考资料"
            docs_str = ""
            for doc in docs:
                docs_str += f"文档片段：{doc.page_content}, 文档元数据{doc.metadata}"
            return docs_str
        def formate_for_retriever(value:dict) -> str:
            return value["input"]
        def formate_for_prompt_template(value:dict) -> dict:
            new_value = {"input": value["input"]["input"], "history": value["input"]["history"], "context": value["context"]}
            return new_value
        chain = (
            {
                "input": RunnablePassthrough(),
                "context": RunnableLambda(formate_for_retriever) | retriever | format_function
            } |RunnableLambda(formate_for_prompt_template) | self.prompt_template | self.chat_model | StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,  # 被增强的原有链
            get_history,  # 通过会话id或获取InMemoryChatMessageHistory
            input_messages_key="input",  # 表示用户输入在模板中的占位符
            history_messages_key="history"  # 表示用户输入在模板中的占位符
        )

        return conversation_chain

if __name__ == '__main__':
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    service = RagService()

    chain = service.chain
    
    print(chain.invoke({"input": "我的体重180斤，尺码推荐"}, session_config))