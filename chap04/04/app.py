import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("OpenAI 音声翻訳")

# 音声ファイルのアップロード
audio_file = st.file_uploader("音声ファイルをアップロードしてください", type=["m4a", "mp3", "webm", "mp4", "mpga", "wav"])


# 音声ファイルがアップロードされていたら、
if audio_file is not None:
    st.audio(audio_file, format="audio/wav")
    if st.button("音声翻訳を実行する"):
        with st.spinner("音声翻訳中です..."):
            translation = client.audio.translations.create(    
                model="whisper-1", 
                file=audio_file
            )
        st.success("音声翻訳が完了しました！")
        st.write(translation.text) 