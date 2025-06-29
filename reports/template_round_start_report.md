from pathlib import Path

# テンプレートの内容
template_text = """\
# 開始報告書：{開発名} - 第{ラウンド番号}ラウンド

- **提出者**：熊谷義行、ChatGPT
- **提出先**：Gemini
- **作成日**：{日付}

---

## 🔧 今回の開発概要

- **対象モジュール**：例）PhaseManager、CLI、Notifier
- **目的**：ラウンドの目的や目標を記述

---

## ✅ 達成したいこと

- [ ] 項目1
- [ ] 項目2
- [ ] 項目3

---

## 📝 感想・気づき

- 例）CLIからの操作性が安定してきた
- 例）phase_managerの通知条件の明示化が進んだ

---

## 🛠 改善提案・技術的考察

- 例）状態遷移時にWebhook通知が欲しい
- 例）設定ファイルの動的再読込対応
- 例）CLIをサブコマンド式にリファクタリング

---

## 📬 Geminiに提供してほしい情報

- [ ] 
- [ ] 
- [ ] 

---

## 🤝 共有しておきたい内部情報

- コマンド使用履歴やテスト成功回数
- フェーズ設定ミスの再現例と修正例 など

---

## 🔜 次のステップ提案

- [ ] 
- [ ] 
- [ ] 

"""

# ファイル保存先
report_path = Path("reports/template_round_final_report.md")
report_path.parent.mkdir(exist_ok=True)
report_path.write_text(template_text, encoding="utf-8")

report_path.name
