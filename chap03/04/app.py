import streamlit as st

#
# https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps
#

st.title("Echo Bot")

# チャット履歴を初期化する
if "messages" not in st.session_state:
	# リストの中に辞書形式で保持する
    st.session_state["messages"] = []
# これまでのチャット履歴を全て表示する
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

print(st.session_state.messages)

# ユーザーの入力が送信された際に実行される処理
# ユーザーの入力を受け取るには、st.chat_inputを使用する。 
# st.chat_inputは第一引数にプロンプト文字列を指定できる。
if prompt := st.chat_input("最近どう?"):

    # ユーザの入力を表示する
    with st.chat_message("user"):
        st.markdown(prompt)
    # ユーザの入力をチャット履歴に追加する
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # ChatBotの返答を表示する
    with st.chat_message("assistant"):
        st.markdown(response)
    # ChatBotの返答をチャット履歴に追加する
    st.session_state.messages.append({"role": "assistant", "content": response})