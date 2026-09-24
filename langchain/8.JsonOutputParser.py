# JsonOutputParser
# AIMessage -> dict
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser


first_prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字,仅告知名字，无需其他内容"
    "并封装为JSON格式返回给我，要求key是name，value就是你起的名字，请严格遵守格式要求"
)

second_prompt_template = PromptTemplate.from_template(
    "姓名{name},帮我解释其含义"
)

model = ChatTongyi(model="qwen3-max")
str_parser = StrOutputParser()
json_parser = JsonOutputParser()
chain = first_prompt_template | model | json_parser | second_prompt_template | model | str_parser # PromptTemplate -> AImessage -> str -> AIMessage
res = chain.invoke({"lastname": "张", "gender": "女儿"})
print(res)

"""
模型输入要求：PromptValue或者字符串或者序列(BaseMessage,list,tuple,str,dict)
模型输出:AIMessage
提示词模板输入：字典
提示词模板输出：PromptValue对象
StrOutputParser: AIMessage输入，str输出
JsonOutputParser: AIMessage输入，dict输出
"""