import yaml
import os

PHASE_STATUS_FILE = "phase_status.yaml"


class PhaseManager:
    def __init__(self):
        self.phases = ["会議", "開発", "テスト"]
        self.phase_status = self.load_phase_status()

    def load_phase_status(self):
        if not os.path.exists(PHASE_STATUS_FILE):
            # 初期状態を作成
            initial_status = {
                "current_phase": "会議",
                "progress": 0,
                "state": "in_progress"
            }
            self.save_phase_status(initial_status)
            return initial_status

        with open(PHASE_STATUS_FILE, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def save_phase_status(self, status):
        with open(PHASE_STATUS_FILE, "w", encoding="utf-8") as f:
            yaml.dump(status, f, allow_unicode=True)

    def print_status(self):
        phase = self.phase_status["current_phase"]
        progress = self.phase_status.get("progress", 0)
        state = self.phase_status.get("state", "unknown")
        print(f"🔎 現在のフェーズ: {phase}")
        print(f"📊 進行状況: {progress}/3 ({int(progress / 3 * 100)}%)")
        print(f"🏁 状態: {state}")

    def advance_phase(self):
        current_index = self.phases.index(self.phase_status["current_phase"])
        if current_index + 1 < len(self.phases):
            new_phase = self.phases[current_index + 1]
            self.phase_status["current_phase"] = new_phase
            self.phase_status["progress"] = 0
            self.phase_status["state"] = "in_progress"
            self.save_phase_status(self.phase_status)
            print(f"✅ フェーズを '{new_phase}' に進行しました。")
        else:
            print("🚩 すでに最終フェーズに到達しています。")

    def set_phase(self, phase_name):
        if phase_name not in self.phases:
            print(f"❌ フェーズ名 '{phase_name}' は無効です。")
            return
        self.phase_status["current_phase"] = phase_name
        self.phase_status["progress"] = 0
        self.phase_status["state"] = "in_progress"
        self.save_phase_status(self.phase_status)
        print(f"✅ フェーズを '{phase_name}' に設定しました。")

    def list_phases(self):
        print("📋 利用可能フェーズ一覧:")
        for i, p in enumerate(self.phases, 1):
            print(f"  {i}. {p}")

    def auto_advance(self):
        if self.phase_status.get("state") == "done":
            self.advance_phase()
        else:
            print("ℹ️ 現在のフェーズが完了状態ではないため、自動進行しません。")
