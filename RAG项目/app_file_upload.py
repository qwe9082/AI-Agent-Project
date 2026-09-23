# 知识库更新主程序（streamlit）
import time

import streamlit as st
from knowledge_base import KnowledgeBaseService
st.title("文件知识库更新服务")

# 文件上次
result = st.file_uploader(
    "请上传文件",
    type=["txt"],
    accept_multiple_files=False,
)

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if result is not None:
    file_name = result.name
    file_size = result.size
    file_type = int(result.size) / 1024
    st.subheader(f"文件名：{file_name}")
    st.write(f"格式: {file_type}，文件大小:{file_size:.2f}KB")

    text = result.getvalue().decode("utf-8")
    with st.spinner("载入知识库中.."):
        time.sleep(1)
        res = st.session_state["service"].upload_by_str(text, file_name)
        st.write(res)
