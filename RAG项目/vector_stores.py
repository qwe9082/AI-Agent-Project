from langchain_chroma import Chroma
import config_data as config

# 向量存储服务
class VectorStoresService:
    def __init__(self, embedding):
        self.embedding = embedding
        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        ) # 向量数据库的实例
    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})

if __name__ == '__main__':
    from langchain_community.embeddings import DashScopeEmbeddings
    services = VectorStoresService(DashScopeEmbeddings(model="text-embedding-v4"))

    result = services.get_retriever().invoke("我的体重180斤，尺码推荐")

    print(result)