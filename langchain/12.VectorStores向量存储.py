from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_chroma import Chroma

# Chroma 外部数据库向量存储 langchain-chroma chromadb
vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"
)

# 内存向量存储
vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings()
)

loader = CSVLoader(
    file_path="./info.csv",
    encoding="utf-8",
    source_column="source",
)

documents = loader.load()

# 添加文档
vector_store.add_documents(
    documents=documents,
    ids=["id" + str(i) for i in range(1, len(documents) + 1)],
)

# 删除文档
vector_store.delete(["id1", "id2"])

# 相似度检索
result = vector_store.similarity_search(
    "Python学起来简单吗",
    1
)

print(result)