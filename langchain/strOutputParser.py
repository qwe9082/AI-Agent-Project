# StrOutputParser
# AIMessage -> str
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字,仅告知名字，无需其他内容"
)

model = ChatTongyi(model="qwen3-max")
parser = StrOutputParser()
chain = prompt_template | model | parser | model # PromptTemplate -> AImessage -> str -> AIMessage
res:AIMessage = chain.invoke({"lastname": "张", "gender": "女儿"})
print(type(res))