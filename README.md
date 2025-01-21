# OpenAI API for Python Developers
This is the repository for the LinkedIn Learning course `OpenAI API for Python Developers`. The full course is available from [LinkedIn Learning][lil-course-url].

![lil-thumbnail-url]

生成AIを使う以前のプログラミングでは、答えを導くのは常にシステムエンジニアでありプログラマでした。しかし生成AIのAPIを利用するとAIが答えを出すようになります。このコースではOpenAIのAPIをPythonのプログラムから呼び出す方法について学びます。アプリケーションプログラミングインターフェイスをPythonのプログラムで使う方法や生成AIのフレームワークであるLangChainを使い、複雑な処理を簡単なコードで実現する方法を解説します。このコースで学習すれば、従来のプログラミングでは難しかった非定型データである通常の文章を読み込みや定型データに落とし込むような処理が簡単に作成できるようになります。

_See the readme file in the main branch for updated instructions and information._
## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"

## Installing
- エクササイズファイルを使うにはOpenAI API keyが必要です。次のサイト取得してください。[platform.openai.com](https://platform.openai.com)
## GitHub Codespacesdで実行するには
1. CodeボタンをクリックしてCodespacesを選んでください。
3. 新規Codespaceを作成するか既存のCodespaceを選んでください。
4. .envファイルをrootフォルダに作成してください。
5. OPENAI_API_KEY=に続けて取得したOpenAI API keyを.envに記入してください。
6. .envファイルをGitHub上ではなく、Codespaceだけに置くことでOpenAI API keyの誤使用、盗用を避けます。
## Windowsで実行するには
- PowerShellで次のコマンドを実行する。
setx OPENAI_API_KEY "your_api_key_here"
- もしくはエクササイズファイル内のコードファイルと同じフォルダに.envファイルを配置してください。
- 詳細は次のページを参照してください。https://platform.openai.com/docs/quickstart

## インストラクター

金宏和實

株式会社イーザー副社長、テクニカルライター


[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/openai-api-for-python-developers-23957123
[lil-thumbnail-url]: https://media.licdn.com/dms/image/v2/D4E0DAQG8PvS0nDMD4g/learning-public-crop_675_1200/learning-public-crop_675_1200/0/1734980145981?e=2147483647&v=beta&t=VUHQ-0pq2rkHH472d1S-dvk4ctGbMiq5ypN1e9QZ3g4

