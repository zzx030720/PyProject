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

system_prompt="""
你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。：
规则：
1.每次只回1条消息
2.禁止任何场景或状态描述性文字
3.匹配用户的语言
4.回复简短，像微信聊天一样
5.有需要的话可以用❤等emoji表情
6.用符合伴侣性格的方式对话
7.回复的内容，要充分体现伴侣的性格特征
伴侣性格：
-%s
你必须严格遵守上述规则来回复用户。
"""
# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

#昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小美"

#性格
if "personality" not in st.session_state:
    st.session_state.personality = "娇小可爱的四川姑娘"

#展示聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])

    # st.chat_message(message["role"]).write(message["content"])


#logo
st.logo("👨‍💻")

#侧边栏,with语句块
with st.sidebar:
    st.subheader("伴侣信息")
    #伴侣名称
    nick_name = st.text_input("伴侣名称",placeholder="请输入伴侣名称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    #性格
    personality = st.text_area("伴侣性格",placeholder="请输入伴侣性格",value=st.session_state.personality)
    if personality:
        st.session_state.personality = personality

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
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.personality)},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

# 打印AI大模型的回复,非流式输出
#     print("------------->AI大模型回复:",response.choices[0].message.content)
#     st.chat_message("assistant").write(response.choices[0].message.content)
#     # 添加AI大模型回复到会话状态
#     st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

# 流式输出AI大模型的回复

    # 创建一个空的st.empty()对象用于显示AI大模型的回复
    response_message = st.empty()
    full_result = ""
    for chunk in response:
        delta = chunk.choices[0].delta
        # 思考内容:可能为None,做兜底后再累加
        # reasoning = delta.reasoning_content
        # if reasoning:
        #     print("------------->AI大模型思考:", reasoning)
        #     full_result += reasoning
        # 正式回答内容:同样可能为None,做兜底后再累加
        content = delta.content
        if content:
            # print("------------->AI大模型回复:", content)
            full_result += content
        response_message.chat_message("assistant").write(full_result)
    # 流式输出结束后,把完整回复存入会话状态,保留聊天记录
    st.session_state.messages.append({"role": "assistant", "content": full_result})



