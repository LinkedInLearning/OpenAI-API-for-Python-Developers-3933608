# OpenAI API for Python Developers
This is the repository for the LinkedIn Learning course `OpenAI API for Python Developers`. The full course is available from [LinkedIn Learning][lil-course-url].

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

[0]: # (Replace these placeholder URLs with actual course URLs)

[lil-course-url]: https://www.linkedin.com/learning/
[lil-thumbnail-url]: http://

