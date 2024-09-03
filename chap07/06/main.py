# API Key を環境変数に読み込む
from dotenv import load_dotenv
load_dotenv()

#Const
MODEL_ENGINE = "gpt-4o-mini"
from langchain_openai import ChatOpenAI

# モデルの作成
model = ChatOpenAI(model=MODEL_ENGINE)

from langchain_core.output_parsers import StrOutputParser
# parserの作成
parser = StrOutputParser()

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
# テンプレートの準備
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

store = {}
# 会話履歴を取り出す関数
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store: 
        #session_id は文字列で、どの会話か（セッションか）を判断するために用いる
        store[session_id] = ChatMessageHistory()
    return store[session_id]

system_prompt = "あなたは有能なアシスタントです。"
while True:
    user_input = input("質問をどうぞ。終了は end\n")

    if user_input.lower() == "end":
        print("Goodbye!")
        break

    if user_input is None:
        continue
    prompt_template = ChatPromptTemplate.from_messages(
        messages=[
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="history"),   # 会話履歴の挿入
            HumanMessagePromptTemplate.from_template("{user_input}"),
        ]
    )

    # Runnableの準備
    chains = prompt_template | model | parser

    with_message_history = RunnableWithMessageHistory(
        chains,
        get_session_history,
        input_messages_key="user_input",
        history_messages_key="history",
    )
    result = with_message_history.invoke(
            {"user_input": user_input},
            config={
                "configurable": {
                    "session_id": "abcd",
                }
            },
        )
    print("ボット: " + result)