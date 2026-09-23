# 项目主程序（streamlit）,启动对话WEB页面
import time
import streamlit as st
from rag import RagService
import config_data as config

st.title("智能客服")
st.divider()
# 用户输入栏
prompt = st.chat_input()

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你好，有什么可以帮助你？"}]

if "rag" not in st.session_state:
    st.session_state["rag"] = RagService()

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])


chain = RagService().chain

if prompt is not None:
    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})
    ai_res_list = []
    with st.spinner("AI思考中.."):
        time.sleep(1)
        res = st.session_state["rag"].chain.stream({"input": prompt}, config.session_config)

        def capture(generator, cache_list):
            for chunk in generator:
                cache_list.append(chunk)
                yield chunk

        st.chat_message("assistant").write_stream(capture(res, ai_res_list))
        st.session_state["messages"].append({"role": "assistant", "content": "".join(ai_res_list)})