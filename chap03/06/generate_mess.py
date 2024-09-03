from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()   #上位フォルダにある.envファイルも読んでくれる
client = OpenAI()



# MODEL_ENGINE = "gpt-3.5-turbo"
MODEL_ENGINE = "gpt-4o-mini"
ROLE_SYSTEM = {"role": "system", "content":"あなたは偏屈な知識人です。語尾に「だなす」と付けます"} 

messages = []
messages.append(ROLE_SYSTEM)

def to_dict(obj):
    return {
        "content": obj.content,
        "role": obj.role,
    }

def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL_ENGINE,
        messages=messages,
        temperature=0.3,
        # max_tokens=150,
    )
    message = response.choices[0].message
    messages.append(to_dict(message))
    return message.content
    # print("ボット: " + message.content.replace("\n", ""))

