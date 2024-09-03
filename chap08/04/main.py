from langchain_community.document_loaders import PyPDFLoader

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

import re
import json
import csv

def extract_and_parse2json(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL) 
        json_string = match.group() if match else ""
        return json.loads(json_string)
    except (AttributeError, json.JSONDecodeError):
        return {}

def write2csv(delivery_slip):
    # CSVファイル名
    csv_file = "./data/deliverySlip.csv"

    # ヘッダーをJSONのキーから求める
    header = delivery_slip[0].keys()

    # CSVファイルを書き込みモードで開き、データを書き込む
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(delivery_slip)

MODEL_ENGINE = "gpt-4o-mini"

# モデルの作成
model = ChatOpenAI(model=MODEL_ENGINE, temperature=0.0)
   
file_path = "./data/2001_1.pdf"
loader = PyPDFLoader(file_path)
pages = loader.load_and_split()

contents = []

prompt = f"""
    以下に示すデータは、納品書のPDFデータをテキスト化したものです。
    納品書データを、下記のキーを持つJSON形式に変換してください。
    キーに該当するテキストが見つからなければ、値は空欄にしてください。

    また、下記は弊社の情報なので、JSONの出力に含めないでください。
    ・シーマアパレル株式会社
    ・〒 103-0002 東京都日本橋牛喰町1-10-8

    キー：
    ・伝票No
    ・日付
    ・得意先名
    ・担当
    ・小計
    ・消費税
    ・税込金額

    以下はある納品書のデータをJSON形式に変換した場合の例です。

    例：
    [(
        "伝票No": "1050123",
        "日付": "2018/9/11",
        "得意先名": "東京商事",
        "担当": "山本",
        "小計": "1,000,000",
        "消費税": "100,000",
        "税込金額": "1,100,000"
    )]

    データ：
    {pages[0].page_content}
    """

result = model.invoke([HumanMessage(content=prompt)])
contents.append(extract_and_parse2json(result.content))

print(contents)
write2csv(contents)