# 📚 星辰詩語システム・技術資料（docs/）

このディレクトリは、Gemini CLI／ChatGPT／人間開発者が  
星辰詩語システムの内部構造を素早く理解・参照するための技術文書を含みます。

---

## 📄 資料一覧

| ファイル名                                      | 説明                                   |
|------------------------------------------------|----------------------------------------|
| `system_overview/starling_system_overview.md` | システム構成・通信チャネル・フローの全体図解     |
| `system_overview/prm_concept.md`              | PRM（詩的共鳴モデル）の概念と階層構造の説明     |

---

## 🧭 使用方法

- Gemini CLI で会議／開発フェーズを実行する際、以下のように `docs/` を context に追加：

```bash
python cli/main.py --phase meeting --context docs/
