# API Key を環境変数に読み込む
from dotenv import load_dotenv
load_dotenv()

#Const
MODEL_ENGINE = "gpt-4o-mini"
# モデルの作成
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model=MODEL_ENGINE)

# テンプレートの準備
from langchain_core.prompts import ChatPromptTemplate


# Pythonのf-stringのようにパラメータを埋め込むことができる
system_template = "次の内容を {language} に翻訳してください。"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}")
])

#パースしてわかりやすくする
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
# parsed_result = parser.invoke(result)

# LCEL のチェイン機能
chain = (prompt_template | model | parser)    # シェルのpipe機能のようなイメージ
llm_result = chain.invoke({
    "language": "フランス語",
    "text": "ルーブル美術館へようこそ。",
})
print(llm_result)

# 実行結果
# Bienvenue au Musée du Louvre.