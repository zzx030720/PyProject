import streamlit as st

st.title("测试")

st.write("2026-10-10,streamlit测试")

#图片
st.image("./resource/jietu_20260608203846.jpg")

#表格
stb_data = {"name":["zzx1","zzx2","zzx3"],
            "age":[10,11,12],
            "gender":[1,0,1]}

st.table(stb_data)

title = st.text_input("请输入name")
st.write(f"输入的name是:{title}")

#单选
gender = st.radio("性别:",["男","女"],index=0)
st.write(f"选择的性别是:{gender}")
