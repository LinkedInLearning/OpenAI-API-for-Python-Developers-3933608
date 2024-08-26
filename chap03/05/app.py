import streamlit as st
from generate_mess import generate_chat_completion

st.title("Echo Bot")

# チャット履歴を初期化する
if "messages" not in st.session_state:
	# 辞書形式で定義
    st.session_state["messages"] = []

# これまでのチャット履歴を全て表示する
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ユーザーの入力が送信された際に実行される処理
if prompt := st.chat_input("何か質問はありませんか?"):

    # ユーザの入力を表示する
    with st.chat_message("user"):
        st.markdown(prompt)
    # ユーザの入力をチャット履歴に追加する
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_chat_completion(prompt)
    # ChatBotの返答を表示する
    with st.chat_message("assistant"):
        st.markdown(response)
    # ChatBotの返答をチャット履歴に追加する
    st.session_state.messages.append({"role": "assistant", "content": response})