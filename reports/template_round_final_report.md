from pathlib import Path

# テンプレートの内容（更新版）
template_text = """\
# 最終報告書：{開発名} - 第{ラウンド番号}ラウンド

- **提出者**：{AIモデル名}
- **提出先**：熊谷義行
- **作成日**：{日付}

---

## 🔧 今回の開発概要

- **対象モジュール**：例）PhaseManager、CLI、Notifier
- **目的**：ラウンドの目的や目標を記述

---

## ✅ 達成したこと

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

## 📬 ユーザーに提供してほしい情報

- [ ] 実運用時のログ例
- [ ] ステップ間のレビューコメント
- [ ] フィードバック内容（あれば）

---

## 🤝 共有しておきたい内部情報

- コマンド使用履歴やテスト成功回数
- フェーズ設定ミスの再現例と修正例 など

---

## 🔜 次のステップ提案

- [ ] ラウンド2の開始（どの範囲か？）
- [ ] 使用するモジュールの再確認
- [ ] Gemini CLI拡張の方向性検討

"""

# ファイル保存先
report_path = Path("reports/template_round_final_report.md")
report_path.parent.mkdir(exist_ok=True)
report_path.write_text(template_text, encoding="utf-8")

report_path.name
