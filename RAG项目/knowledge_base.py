# 知识库更新服务
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
import config_data as config
import hashlib
from datetime import datetime
def check_md5(md5_str: str):
    """检查传入的md5字符串是否已经处理过了
        reutnr False(md5未处理过) True(md5已处理过，已有记录)
    """
    if not os.path.exists(config.md5_path):
        open(config.md5_path, "w", encoding="utf-8").close()
        return False
    else:
        for line in open(config.md5_path, "r", encoding="utf-8").readlines():
            line = line.strip()
            if line == md5_str:
                return True
        return False

def save_md5(md5_str: str):
    with open(config.md5_path, "a", encoding="utf-8") as f:
        f.write(md5_str + "\n")
    """将传入的md5字符串，记录到文件内保存"""
    pass

def get_string_md5(input_str:str, encoding="utf-8"):
    """将传入的字符串转换为md5字符串"""
    # 将字符串转换为bytes字节数组
    str_bytes = input_str.encode(encoding=encoding)

    hash_obj = hashlib.md5()
    hash_obj.update(str_bytes)
    hash_md5 = hash_obj.hexdigest()
    return hash_md5

class KnowledgeBaseService(object):
    def __init__(self):
        os.makedirs(config.persist_directory, exist_ok=True)
        self.chroma = Chroma(
            collection_name=config.collection_name,
            embedding_function=DashScopeEmbeddings(model="text-embedding-v4"),
            persist_directory=config.persist_directory,
        ) # 向量数据库的实例
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size, # 分割后的文本段最大长度
            chunk_overlap=config.chunk_overlap, # 连续文本段之间的字符重叠数量
            separators=config.separators, # 自然段落划分的符号
            length_function=len, # 使用Python自带的len函数做长度统计的依赖
        ) # 文本分割器
    def upload_by_str(self, data, filename):
        """将传入的字符串，进行向量化，存入向量数据库中"""
        md5_hex = get_string_md5(data)
        if check_md5(md5_hex):
            return "【跳过】内容已存在知识库中"
        if len(data) > config.max_split_char_numer:
            knowledge_chunks:list[str] = self.spliter.split_text(data)
        else:
            knowledge_chunks = [data]
            pass

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "wk"
        }

        self.chroma.add_texts(
            knowledge_chunks,
            metadatas=[metadata for _ in knowledge_chunks]
        )

        save_md5(md5_hex)
        return "【成功】内容已成功载入向量库"

if __name__ == "__main__":
    service = KnowledgeBaseService()

    print(service.upload_by_str("周杰伦", "testfile"))