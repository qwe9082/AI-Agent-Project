# 配置文件
from openai.types import embedding_model

md5_path = "./md5.text"

collection_name = "rag"
persist_directory = "./chroma_db"

chunk_size = 1000
chunk_overlap = 100
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_numer = 1000 # 文本分割的阈值

similarity_threshold = 1

embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"