# 通用提示词模板，支持动态注入消息
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},你帮我起个名字,简单回答"
)
prompt_text = prompt_template.format(lastname="张", gender="女儿")

model = Tongyi(model="qwen-plus")
res = model.invoke(input=prompt_text)
print(res)