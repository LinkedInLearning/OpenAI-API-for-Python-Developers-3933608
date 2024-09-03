# from pathlib import Path
from openai import OpenAI


client = OpenAI()

audio_file= open("speech.mp3", "rb")
# audio_file= open(Path(__file__).parent / "speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)