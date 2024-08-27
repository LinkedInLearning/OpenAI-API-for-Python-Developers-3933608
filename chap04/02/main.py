from openai import OpenAI
client = OpenAI()

speech_file_path = "speech.mp3"
with client.audio.speech.with_streaming_response.create(
  model="tts-1",
  voice="alloy",
  # input="Today is a wonderful day to build something people love!"
  # input="Aujourd’hui est une journée merveilleuse pour construire quelque chose que les gens aiment!"
  input="今日は、人々に愛されるものを構築するには素晴らしい日です。"
) as response:
  response.stream_to_file(speech_file_path)