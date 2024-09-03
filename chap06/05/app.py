import streamlit as st
from openai import OpenAI
import json
from dotenv import load_dotenv
from utils import get_postcode
load_dotenv()

client = OpenAI()

# Step 1: 呼び出す関数を定義
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_postcode", #関数の名前
            "description": "日本の郵便番号を住所から検索します",
            "parameters": {
                "type": "object",
                "properties": { 
                    "address": { 
                        "type": "string", #引数のデータ型
                        "description": "日本の住所, 例) 富山県高岡市末広町", 
                    },
                },
                "required": ["address"], 
            },
        },
    }
]
MODEL_ENGINE = "gpt-4o-mini"
messages = []
ROLE_SYSTEM = {"role": "system", "content":"あなたは優秀な教授です"} 
messages.append(ROLE_SYSTEM)

def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL_ENGINE,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    response_message = response.choices[0].message
    if response_message.tool_calls is None:
            return response_message.content
    else:
        tool_calls = response_message.tool_calls
        available_functions = {
            "get_postcode": get_postcode,
        }
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                address=function_args.get("address"),
            )
            postcode_str = ', '.join(function_response)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": postcode_str,
                }
            )
        print(messages)
        second_response = client.chat.completions.create(
            model=MODEL_ENGINE,
            messages=messages,
        )
        return second_response.choices[0].message.content #回答文


st.title("郵便番号に強いボット")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("〒〒〒"):

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_chat_completion(prompt)
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})