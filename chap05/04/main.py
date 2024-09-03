from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    input="サンドイッチは食べやすい",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)