# 事前準備
## pandocのインストール
- [ここ](https://github.com/jgm/pandoc/releases)からpandocのインストーラを取得する
  - pythonのpandocライブラリがpandocのバージョンチェックをしているみたいで  
  (python packageの)pandoc2.2の場合は[pandoc-2.18](https://github.com/jgm/pandoc/releases/download/2.18/pandoc-2.18-windows-x86_64.zip)をインストールする 
## python packageのpandocインストール
このプロジェクトのルートでターミナルを開いて以下のコマンドを実行。

```sh
  pip install -r requirements.txt
```
pandoc2.2を固定でインストールするようにしています。

# 実行
```sh
python main.py
```
ちゃんと動けば、sampleフォルダ以下にあるsample.mdをsample.txtに変換します。
