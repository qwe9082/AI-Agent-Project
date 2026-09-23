from langchain_community.chat_models import ChatTongyi
from langchain_core.documents import Document
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatTongyi(model="qwen3-max")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
        ("user", "用户提问:{input}")
    ]
)

vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings(model="text-embedding-v4")
)

vector_store.add_texts(["减肥就是要少吃多练", "在减肥期间吃东西很重要，清淡少油控制卡路里摄入并运动起来", "跑步是很好的运动哦"])
prompt_text="怎么减肥?"

retriever = vector_store.as_retriever(search_key={"k": 2})

def prompt_print(prompt):
    print(prompt.to_string())
    print("="*20)
    return prompt

def format_function (docs:list[Document]):
    if not docs:
        return "无相关参考资料"
    docs_str = "["
    for doc in docs:
        docs_str += doc.page_content
    docs += "]"
    return docs_str

chain = {"input": RunnablePassthrough(), "context": retriever | format_function} | prompt | prompt_print | model | StrOutputParser()

res = chain.invoke(prompt_text)

print(res)




