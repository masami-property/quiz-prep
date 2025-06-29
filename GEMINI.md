# 地域限定旅行業務取扱管理者の過去問アプリ
- なるべく軽く作る！ index.htmlは14KB以下にこだわる
- https://github.com/masami-property/quiz-prep

## 情報元
- 過去問と回答 https://www.mlit.go.jp/kankocho/seisaku_seido/ryokogyoho/chiikigenteikanrisha.html
- 2024年解説 https://www.youtube.com/watch?v=SUa1vA8uxuA
- 2023年解説 https://www.youtube.com/watch?v=EMI9tlrnMhs
- "YouTube Summary with ChatGPT & Claude"で文字起こし → Geminiに下記プロンプトで変換しもらう → temp.txtに手動コピペ → pyでjsonに変換
  
## 使い方
1.  https://masami-property.github.io/quiz-prep/ をウェブブラウザで開いてください。
2.  クイズが10問ランダムで出題されます。
3.  解答を選択し、「解答する」ボタンをクリックすると、正解・不正解と解説が表示されます。

## クイズデータの更新方法

クイズデータは `data/quiz_data.json` に格納されています。
データを修正・追加する場合は、`temp/quiz_data_temp.txt` を編集し、以下のコマンドを実行して `quiz_data.json` を再生成してください。

## Todo(できれば)
- 2022年以前の問題を追加
- 解説ないとこ埋める
- リザルト画面に間違えた問題の一覧を表示
- 苦手な問題を優先して出すアルゴリズム
