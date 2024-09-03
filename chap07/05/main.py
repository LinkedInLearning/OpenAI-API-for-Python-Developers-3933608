# API Key を環境変数に読み込む
from dotenv import load_dotenv
load_dotenv()

#Const
MODEL_ENGINE = "gpt-4o-mini"
# モデルの作成
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model=MODEL_ENGINE)

# テンプレートの準備
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt_template = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="history"), # 会話履歴の挿入
        ("human", "{input}"),
    ]
)

# Runnableの準備
runnable = prompt_template | model

# from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
# 会話履歴（メモリ）を保存するにはRunnableWithMessageHistoryを使う

config = {
    "configurable": {
        "session_id": "abcd",
    }
}
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store: 
        #session_id は文字列で、どの会話か（セッションか）を判断するために用いる
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# LLM のモデルと、会話履歴を取り出す関数を渡すことで会話履歴を参照する
# Runnable が作られます
runnable_with_history = RunnableWithMessageHistory(
    runnable,   # Runnableをラップ
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

response = runnable_with_history.invoke(
    {"input": "こんにちは！私の名前は中村です。"},
    config=config,
)
print(response.content) 

response = runnable_with_history.invoke(
    {"input": "私の名前を覚えていますか？"},
    config=config,
)
print(response.content) 
print(store)
# はじめまして、中村さん！どうぞよろしくお願いします。何かお手伝いできることがあればお知らせくださいね。
# はい、覚えていますよ。中村さんですね。お話をしながら覚えていきますので、気軽に話しかけてくださいね。

# LCEL のチェイン機能
# chain = (prompt | model | parser)    # シェルのpipe機能のようなイメージ
# result = chain.invoke({
#     "messages": [
#         HumanMessage(content="こんにちは！"),
#         AIMessage(content="こんにちは！なにかお手伝いできますか？"),
#         HumanMessage(content="私は中村といいます。覚えておいてね"),
#     ]
# })
# print(result)

# 実行結果
# 了解しました、中村さんですね。何かお手伝いできることがあればいつでもお知らせくださいね。
# messages に渡した配列の最後が最終のインプットとなり、それに対するレスポンスが得られているのが分かる