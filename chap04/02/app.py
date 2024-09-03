import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.title("OpenAI TTS(音声合成)")
user_input = st.text_area("音声にするテキストを入力してください", "")

# 利用可能な声のトーン
tones = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
selected_tone = st.radio("トーンを選択してください", tones)

# 結果をファイルに保存
speech_file = "speech.mp3"

if st.button('開始'):
    if user_input:
        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice=selected_tone,
            input=user_input,
        ) as response:
            response.stream_to_file(speech_file)

        # audioプレイヤー表示
        st.audio(speech_file)
    else:
        # 警告メッセージ
        st.warning("音声にするテキストを入力してください。")