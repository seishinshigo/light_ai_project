"""
フェーズ進行管理クラス

・フェーズ: 会議 → 開発 → テスト → 完了
・完了到達時に RoundReporter.create_final() を自動呼び出し
・auto_advance 設定は CLI 側でチェックして advance_phase() を呼ぶ
"""

import json
from pathlib import Path
import subprocess

from config_loader import load_workflow_config, get_project_name
from notifier import notify
from app.round_reporter import create_final

STATE_FILE = Path("state/phase_status.json")


# ---------------------------------------------------------------------
def load_phase_status() -> dict:
    if not STATE_FILE.exists():
        return {
            "current_phase": "会議",
            "completed_phases": [],
            "status": "in_progress",
        }
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def save_phase_status(data: dict):
    STATE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------
class PhaseManager:
    def __init__(self):
        cfg = load_workflow_config()
        self.workflow_cfg = cfg["workflow"]
        self.phase_status = load_phase_status()

        # 固定フェーズ順
        self.phases = ["会議", "開発", "テスト"]
        self.messages = self.workflow_cfg.get("messages", {})

    # -------------------------------------------------- public helpers
    def auto_advance_enabled(self) -> bool:
        return bool(self.workflow_cfg.get("auto_advance", False))

    # -------------------------------------------------- core actions
    def advance_phase(self):
        current = self.phase_status["current_phase"]

        # ① すでに完了
        if current == "完了":
            notify("⚠️ すでに全フェーズが完了しています。これ以上は進めません。")
            return

        # ② 次フェーズ計算
        try:
            idx = self.phases.index(current)
        except ValueError:
            notify(f"⚠️ 不明なフェーズ: {current}")
            return

        # ③ 通常進行 or 完了
        if idx + 1 < len(self.phases):
            next_phase = self.phases[idx + 1]
            self._update_status(next_phase, done=False)
            notify(self.messages.get("phase_end", "✅ フェーズ終了：評価・承認待ち状態に移行しました。"))
        else:
            # 最終フェーズ → 完了へ
            self._update_status("完了", done=True)

    # -------------------------------------------------- utilities
    def set_phase(self, name: str):
        if name not in self.phases:
            notify(f"⚠️ 無効なフェーズ指定: {name}")
            return
        self._update_status(name, done=False)
        notify(f"🚀 フェーズを手動で『{name}』に設定しました。")

    def status_report(self):
        cur = self.phase_status["current_phase"]
        done = len(self.phase_status["completed_phases"])
        total = len(self.phases)
        percent = int(done / total * 100)
        print(f"🔎 現在のフェーズ: {cur}\n📊 進行状況: {done}/{total} ({percent}%)\n🏁 状態: {self.phase_status['status']}")

    def list_phases(self):
        print("📋 利用可能フェーズ:")
        for i, p in enumerate(self.phases, 1):
            print(f"  {i}. {p}")

    def save(self):
        save_phase_status(self.phase_status)

    # -------------------------------------------------- internal
    def _update_status(self, new_phase: str, *, done: bool):
        cur = self.phase_status["current_phase"]
        if cur not in self.phase_status["completed_phases"]:
            self.phase_status["completed_phases"].append(cur)

        self.phase_status["current_phase"] = new_phase
        self.phase_status["status"] = "done" if done else "in_progress"
        save_phase_status(self.phase_status)

        # 完了時は最終報告書を作成
        if done:
            round_no = len(self.phase_status["completed_phases"])
            project = get_project_name()
            path = create_final(round_no, project)
            notify(self.messages.get("phase_done", "🎉 全てのフェーズが完了しました。お疲れさまでした！"))
            notify(f"📄 最終報告書を生成 → {path}")

            # 自動コミット
            subprocess.run(["git", "add", str(path)], check=False)
            subprocess.run(["git", "commit", "-m", f"Add {path.stem}"], check=False)
