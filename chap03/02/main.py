from openai import OpenAI
client = OpenAI()

# MODEL_ENGINE = "gpt-3.5-turbo"
MODEL_ENGINE = "gpt-4o-mini"
ROLE_SYSTEM = {"role": "system", "content":"あなたは優秀な教授です"} 

messages = []
messages.append(ROLE_SYSTEM)

def generate_chat_completion(user_input=""):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model=MODEL_ENGINE,
        messages=messages,
        temperature=0.8,
        max_tokens=100,
    )
    message = response.choices[0].message
    messages.append(message)
    print("ボット: " + message.content.replace("\n", ""))
    print()
    print(messages)

def main():
    while True:
        print("\n----------------------------------------\n")
        print(" こんにちは AI-CHATBOT です\n")
        print("選択してください\n")
        print("1 -> チャット開始")
        print("2 -> 終了")
        choice = input("1か2を押してください: ")
        if choice == "1":
            start_chat()
        elif choice == "2":
            exit()
        else:
            print("正しく入力してください")


def start_chat():
    print("チャットを終わるには End と入力してください")
    print("\n      新規チャット       ")
    print("---------------------")

    while True:
        user_input = input("あなた: ")

        if user_input.lower() == "end":
            break
        else:
            generate_chat_completion(user_input)


if __name__ == "__main__":
    main()