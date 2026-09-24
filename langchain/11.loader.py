# CSVLoader JSONLoader PyPDFLoader TextLoader
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PDFLoader
loader = PDFLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",", # 指定分隔符
        "quotechar": '"',
    },
    encoding="utf-8",
)
documents = loader.load()
print(documents)
for document in documents:
    print(document)


# loader = JSONLoader(
#     file_path="./stu.json", # 文件名称和地址
#     jq_schema=".", # .(抽取整个json文件) .other.add(抽取字段) .[](抽取列表)
#     text_content=False, # 告知JSONLoader抽取内容非字符串，默认True
#     json_lines=True, // 告知JSONLoader 这是一个JSONlines文件（每一行都是单独json）
# )

# loader = TextLoader("./ppp.txt", encoding="utf-8")
# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=500, # 分段的最大字符数
#     chunk_overlap=50, # 分段之间允许重叠字符数
#     separator=["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""], # 文本自然段落分割的依据符号
#     length_function=len, # 统计字符的依据函数
# )
# spliter_docs = splitter.split_document(loader)
# for doc in spliter_docs:
#     print(doc)

# loader = PDFLoader(
#     file_path="./data/stu.pdf", # 文件路径，必填
#     mode="single", # 读取模式默认page single单个document  page按页面划分不同document
#     password="password", # 文件密码
# )
# for doc in loader.lazy_load():
#     print(doc)