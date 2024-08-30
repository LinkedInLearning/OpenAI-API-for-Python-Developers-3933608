from langchain_community.document_loaders import PyPDFLoader
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

import re
import json
import csv
import os 

from const import PROMPT_STRING

MODEL_ENGINE = "gpt-4o-mini"

def extract_and_parse2json(text):
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL) 
        json_string = match.group() if match else ""
        return json.loads(json_string)
    except (AttributeError, json.JSONDecodeError):
        return {}

def write2csv(delivery_slip):
    csv_file = "./data/deliverySlip.csv"

    header = delivery_slip[0].keys()

    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(delivery_slip)

def handle_all_files(folder):

    model = ChatOpenAI(model=MODEL_ENGINE, temperature=0.0)
   
    pdf_files = [f for f in os.listdir(folder) if f.endswith(".pdf")]

    contents = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(os.path.join(folder,pdf_file))
        pages = loader.load_and_split()

        prompt = f"""
            {PROMPT_STRING}
            データ：
            {pages[0].page_content}
            """

        result = model.invoke([HumanMessage(content=prompt)])
        contents.append(extract_and_parse2json(result.content))

    print(contents)
    return(contents)
    
def main():
    slip = handle_all_files('data')
    print("JSONファイルに変換しました")
    write2csv(slip)
    print("CSVファイルに保存しました")

if __name__ == "__main__":
    main()