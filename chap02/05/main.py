from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "あなたは大学教授です"},
    {"role": "user", "content": "AIについて少し解説してください"}
  ],
  max_tokens=200
)
# Returns a chat completion object
print(completion)
print(completion.choices[0].message)