import streamlit as st
from handlers import downloadFile, generate_image


st.title("OpenAI 画像生成")

with st.form("user_form", clear_on_submit=True):
    user_input = st.text_input("生成する画像のイメージを入力")
    submit_button = st.form_submit_button(label="生成")

if submit_button:
    with st.spinner("画像生成中..."):
        image = generate_image(user_input)
        st.image(image, use_column_width=True)  
        saved_image = downloadFile(user_input, image)
        st.success("imgフォルダに画像を保存しました")