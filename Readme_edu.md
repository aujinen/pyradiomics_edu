## Untached Original area, but added educational items into new folder "workspace"
In this fork, the original files (source code, binary components and others) remain completely unmodified;<br>
instead, source code and data suitable for educational purposes are accumulated within a newly added `workspace` folder.


## Installing PyRadiomics (ver 3.1.1.dev111+g8ed579383)
As these materials are intended for students in Japan, the content in folder 'workspace' is primarily in Japanese.<br>
Please refer to the article at the Qiita URL below for instructions on how to install PyRadiomics (Japanese).<br>

=== 日本語版
## オリジナル領域は変更せず、教育用コンテンツを「workspace」フォルダに追加
このフォークでは、オリジナルのファイル（ソースコード、バイナリコンポーネントなど）は一切変更されていません。<br>
その代わりに、教育に適したソースコードやデータが、新たに追加された `workspace` フォルダに格納されています。

## PyRadiomics (ver 3.1.1.dev111+g8ed579383) のインストール
本教材は日本の学生を対象としているため、`workspace` フォルダ内のコンテンツは主に日本語で記述されています。<br>
PyRadiomicsのインストール手順については、以下のQiita記事をご参照ください。<br>
[uv で PyRadiomics を簡便にインストールする](https://qiita.com/aujinen/items/035674c54ce138aa7a80)<br>

## Installation Instructions
## インストール方法
### Software required before installation
### インストール前に必要なソフト類
+ uv<br>
[uvインストールとPATH設定のやさしい解説（PowerShellとCMD両対応）](https://note.com/youpapalife/n/na3bdb65e8d18)
+ git<br>
[Gitのインストール方法(Windows版)](https://qiita.com/takeru-hirai/items/4fbe6593d42f9a844b1c)
+ Build Tools for Visual Studio<br>
参考資料：[Visual Studio で C と C++ のサポートをインストールする](https://learn.microsoft.com/ja-jp/cpp/build/vscpp-step-0-installation?view=msvc-170)<br>
下記のサイトページ下方の「すべてのダウンロード」部分にあります<br>
[https://visualstudio.microsoft.com/ja/downloads/](https://visualstudio.microsoft.com/ja/downloads/)<br>
→　Tools For Visual Studio<br>
→　Build Tools for Visual Studio 2026<br>
→　【ダウンロード】後、インストーラー実行<br>
→　「C++によるデスクトップ開発」を選択し、「x64/x86 用 MSVC ビルドツール」、「Windows 11 SDK」、「Windows 用 C++ CMake ツール」の3つを最低限選択してインストール
### for windows11, PowerShell

```
git clone https://github.com/aujinen/pyradiomics_edu.git
cd .\pyradiomics_edu\
[System.Environment]::SetEnvironmentVariable('UV_MALWARE_CHECK',1)
uv sync
```
※上記手順で```pyradiomics 0.1.dev1340+g15a938dad```がインストールされます。
### add ipykernel for ipynb fiels used in VS-Code
### VS-Codeでipynbファイルを利用するために必要なライブラリ（ipykernel）の追加
```
uv add ipykernel
```
※python 3.13の場合、上記手順で```pyradiomics 0.1.dev1340+g15a938dad.d20260625```に変更されます。
