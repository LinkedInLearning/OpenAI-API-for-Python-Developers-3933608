import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

st.title("OpenAI 音声文字要約")

# 音声ファイルのアップロード
audio_file = st.file_uploader("音声ファイルをアップロードしてください", type=["m4a", "mp3", "webm", "mp4", "mpga", "wav"])
# 音声ファイルがアップロードされていたら、
if audio_file is not None:
    st.audio(audio_file, format="audio/wav")
    if st.button("要約処理を実行する"):
        with st.spinner("文字起こし中です..."):
            transcription = client.audio.transcriptions.create(    # transcribe(文字に起こす)
                model="whisper-1", 
                file=audio_file, 
                # response_format="text"
            )
        st.success("文字起こしが完了しました！")
        st.text(transcription.text)
        with st.spinner("要約処理を実行中です..."):
            # GPTを使ってテキスト処理
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "あなたは優秀な編集者です"},
                    {"role": "user", "content": "次のテキストを要約してください。" + transcription.text}
                ]
            )
            processed_text = response.choices[0].message.content

            # 処理結果を表示
            st.write("要約結果:")
            st.write(processed_text)
