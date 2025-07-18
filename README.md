# 地域限定旅行業務取扱管理者試験 過去問クイズアプリ

これは、地域限定旅行業務取扱管理者試験の過去問を学習するためのクイズアプリです。

**📗 [クイズで遊ぶ](https://masami-property.github.io/quiz-prep/)**

### ✨ コンセプト

- なんか過去問アプリがない...じゃあ自分で作ってみるか！
- **通信速度が遅いスマホ回線でもサクサク快適に学習できるオンラインアプリ**を目指しました。
- なるべく軽く作る！(htmlは14KB以下)

- （プログラミングとかやったことないので）GEMINI CLI, Claude, ChatGPTの力を借りて作りました。AI様ありがとう！！！
- Githubも初心者なのでなんか使い方違ったらごめんなさい。

---

## 💡 使い方

- 過去問からランダムに10問出題されます
- 回答後に解説が表示され、最後に正解した数が表示されます

---

## ⚠️ 免責事項

このアプリは個人の趣味で制作したものです。  
問題や解説の内容について正確性を保証するものではありません。  
実際の試験対策には、必ず公式の資料や信頼できる教材をご確認ください。

---

## 📚 参考資料・謝辞

- 過去問と回答：[国土交通省 地域限定旅行業務取扱管理者試験](https://www.mlit.go.jp/kankocho/seisaku_seido/ryokogyoho/chiikigenteikanrisha.html)
- 解説動画：
  - [2024年度 試験解答速報](https://www.youtube.com/watch?v=SUa1vA8uxuA)
  - [2023年度 試験解答速報](https://www.youtube.com/watch?v=EMI9tlrnMhs)
  - 解説内容は上記動画を参考に作成しました。ありがとうございます！

- ファビコン: Twitter Twemoji (CC-BY 4.0)
  - Graphics Title: 1f4d7.svg
  - Graphics Author: Copyright 2020 Twitter, Inc and other contributors (https://github.com/twitter/twemoji)
  - Graphics Source: https://github.com/twitter/twemoji/blob/master/assets/svg/1f4d7.svg
  - Graphics License: CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/)

---

## 🛠 開発者向け情報

- このプロジェクトは [Gemini CLI](https://gemini-docs.dev/) を使って構築されています。

### クイズデータの更新方法

1. `src/quiz_data_source.yaml` に問題データを追記・編集します。
2. `python3 src/yaml_to_json.py` を実行します。
   - これにより、`data/quizzes/` ディレクトリ内に問題ごとのJSONファイル（`q001.json` など）と、それらのインデックスファイル（`index.json`）が生成されます。
   - （旧形式の `data/quiz_data.json` は、メインのアプリでは使用されなくなりました。）

<!-- ### デバッグ画面

開発者向けデバッグ画面（非公開推奨）
[デバッグ画面（開発者向け）](https://masami-property.github.io/quiz-prep/dev.html) -->

---

## 🧱 使用技術

- HTML / CSS / JavaScript
- Gemini CLI
- GitHub Pages

---

## 📄 ライセンス

MITライセンス  
（趣味で作ったものであり、商用利用等はご自身の判断でお願いします）

---

## 🕘 更新履歴

- `v0.1.3`（2025-07-02）2025年度の試験詳細が公開されたため追加。試験日までのカウントダウンと願書提出期限表示機能を追加
- `v0.1.2`（2025-07-02）選択肢のシャッフル機能を追加、ファイルサイズを最適化
- `v0.1.1`（2025-07-01）問題データを分割し、読み込みを高速化
- `v0.1.0`（2025-07-01）最低限遊べるようになったので公開

