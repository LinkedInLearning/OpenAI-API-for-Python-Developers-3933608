from openai import OpenAI
import json
from dotenv import load_dotenv

from utils import get_current_weather

load_dotenv()


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "指定された都市の現在の天気を取得する",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "英語表記の都市名と国名もしくは州名, e.g. tokyo, JP",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

# Constants
MODEL_ENGINE = "gpt-3.5-turbo"
messages = []
ROLE_SYSTEM = {"role": "system", "content":"あなたは優秀な教授です"} 
messages.append(ROLE_SYSTEM)

client = OpenAI()

def generate_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    messages.append(
        response.choices[0].message
    )  # extend conversation with assistant's reply
    return response.choices[0].message

available_functions = {
    "get_current_weather": get_current_weather,
}  # only one function in this example, but you can have multiple

def call_function(tool_calls):
    if tool_calls:
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location")
            )

            print(function_response)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response

def main():
    print("ボット: 何でも聞いてください。お天気には詳しいよ end で終了")

    while True:
        user_input = input("あなた: ")

        if user_input == "end":
            break

        # Step 1: send the conversation and available functions to GPT
        message_response = generate_response(user_input)
        print(message_response)

        # Step 2: check if GPT wanted to call a function and generate an extended response
        if message_response.tool_calls is None:
            print("ボット: " + message_response.content)
            continue

        # Step 3: call the function
        call_function(message_response.tool_calls)

        # Step 4: send the info on the function call and function response to GPT
        # extend conversation with assistant's reply
        second_response = client.chat.completions.create(
            model=MODEL_ENGINE,
            messages=messages,
        )  # get a new response from the model where it can see the function response
        print("ボット: " + second_response.choices[0].message.content)


if __name__ == "__main__":
    main()