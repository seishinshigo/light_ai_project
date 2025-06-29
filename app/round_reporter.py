import os
from datetime import datetime


def copy_start_template(project_name: str) -> None:
    """
    次のラウンド開始報告書テンプレートを reports/ にコピーする関数。
    ファイル名は `round_start_XX_<project_name>.md` 形式。
    """
    os.makedirs("reports", exist_ok=True)

    # 現在の reports ディレクトリ内の既存 round_start_XX_*.md を数えて連番を決定
    existing_files = [f for f in os.listdir("reports") if f.startswith("round_start_")]
    round_num = len(existing_files) + 1
    filename = f"round_start_{round_num:02d}_{project_name}.md"
    filepath = os.path.join("reports", filename)

    # テンプレートの中身
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template = f"""# 🌸 開発報告：ラウンド {round_num}

- プロジェクト名: {project_name}
- 開始時刻: {now}
- フェーズ: 会議（初期化済）

---

## 📌 このラウンドでの目標

（ここに目標を書く）

## 🧩 想定される作業分担

- ChatGPT:
- Gemini CLI:
- ユーザー:

---

## 🗒 備考

（自由記述）
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(template)

    print(f"✅ テンプレートを作成しました: {filepath}")
