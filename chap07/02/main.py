# インストール
# pip install langchain # 0.2.11
# pip install langchain-community # 0.2.10
#  OpenAI の ChatGPT を利用するため
# pip install -qU langchain-openai # 0.1.17

# API Key を環境変数に読み込む
from dotenv import load_dotenv
load_dotenv()

#Const
MODEL_ENGINE = "gpt-4o-mini"
# モデルの作成
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model=MODEL_ENGINE)

# メッセージの準備
from langchain_core.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="次の発言を日本語からフランス語に翻訳してください。"),
    HumanMessage(content="コーヒーを二つお願いします")
]

# 実行する invoke()メソッド
result = model.invoke(messages)
# print(result)

#パースしてわかりやすくする
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
parsed_result = parser.invoke(result)

print(parsed_result)