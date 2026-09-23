# langchain 是围绕大模型语言建立的一个框架 核心理念是为大模型语言实现通用接口
# langchain 是一个开发LLM相关业务的集大成者，本质是Python的第三方库，提供各类功能的API
"""
主要包含
Prompts 优化提示词（提示词工程）
Models 调用各类模型
History 管理会话历史记录
Indexs 管理和分析各类文档
Chain 构建功能的执行链条
Agent 构建智能体
"""

"""
pip install langchian langchain-community langchain-ollama dashscope langchain-chroma chromadb
langchain:核心包
langchain-community:社区支持包，提供了更多第三方调用模型（例如：阿里云千问）
langchain-ollama: Ollama支持包，支持调用ollama托管部署的本地模型
dashscope: 阿里云通义千问的Python SDK
langchain-chroma 外部向量存储
chromadb: 轻量向量数据库--后续使用
"""
