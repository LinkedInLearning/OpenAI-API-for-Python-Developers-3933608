from openai import OpenAI
# from PIL import Image
import os
import requests
import ssl
from dotenv import load_dotenv


# Specify the folder path
folder_path = "img"


load_dotenv()
client = OpenAI()

def generate_image(user_input):
    response = client.images.generate(
        model="dall-e-3",
        prompt=user_input,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    return response.data[0].url

def downloadFile(user_input, url):
    #ファイルをurlからダウンロードして、imgフォルダに保存する

    try:
        # sslエラーを避けて、ssl検証を行わない指定
        ssl._create_default_https_context = ssl._create_unverified_context
        # HTTPのGETメソッド
        r = requests.get(url, allow_redirects=True)
        """
            raise_for_status()メソッドでHTTPステータスコードを確認し200番台であれば
            try:部分が実行、HTTPステータスコードが200番台以外であれば
            例外が発生したと判断しexcept:部分を実行
        """
        r.raise_for_status()

        # imgフォルダにダウンロード
        file_path = os.path.join(
            "img", os.path.basename("img_" + user_input.replace(" ", "_")) + ".png"
        )

        with open(file_path, "wb") as f:
            f.write(r.content)
        # return f"File downloaded successfully and saved to {file_path}"

    except requests.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")