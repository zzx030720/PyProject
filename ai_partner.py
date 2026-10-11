import streamlit as st
from openai import OpenAI

# 创建OpenAI客户端
client = OpenAI(
    api_key="sk-f376c75348fd4efdab6c5a74d4128df9",
    base_url="https://api.deepseek.com",
)
# 设置页面配置
st.set_page_config(
    page_title="AI智能聊天框",
    page_icon="🦸",

    #布局设置为wide铺满屏幕
    layout="wide",

    #初始侧边栏状态设置为expanded展开
    initial_sidebar_state="expanded",
    menu_items={}
)

#大标题
st.title("AI智能聊天框")

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#展示聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])


#logo
st.logo("👨‍💻")

#聊天消息输入框
prompt = st.chat_input("请输入您的问题")
if prompt:
    # 展示消息
    st.chat_message("user").write(prompt)
    print("----->调用AI大模型进行回复,提示词:", prompt)
    # 添加用户消息到会话状态
    st.session_state.messages.append({"role": "user", "content": prompt})

# 调用AI大模型进行回复
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            *st.session_state.messages
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

# 打印AI大模型的回复
    print("------------->AI大模型回复:",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 添加AI大模型回复到会话状态
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})




