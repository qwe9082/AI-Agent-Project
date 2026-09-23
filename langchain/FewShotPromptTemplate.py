# 支持基于模板注入任意数量的示例信息
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 示例的模板
example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")

# 示例的动态数据注入，list内部嵌套字典
example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]

few_short_template = FewShotPromptTemplate(
    example_template=example_template,
    example_data=example_data,
    prefix="告知我单词的反义词，我提供如下的实例：", # 示例之前的提示词
    suffix="基于前面的实例告知我,{input_word}的反义词是？", # 示例之后的提示词
    input_variables=['input_word'] # 声明在前缀和后缀中需要注入的变量名
)

prompt_text = few_short_template.invoke(input={"input_word": "左"}).to_string()

model=Tongyi(model="qwen-max")

model.invoke(input=prompt_text)
