# CSVLoader JSONLoader PyPDFLoader TextLoader
from langchain_community.document_loaders import CSVLoader
loader = CSVLoader(
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
