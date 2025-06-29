# cli/main.py

from phase_manager import PhaseManager, Phase
import subprocess
import time


def execute_phase(phase: Phase) -> bool:
    print(f"\n🚀 実行中: {phase.name} フェーズ")

    if phase == Phase.MEETING:
        # 会議フェーズ（後でGemini CLI連携などを追加）
        print("🧠 会議を実行中...（ダミー処理）")
        time.sleep(1)

    elif phase == Phase.DEVELOP:
        print("🛠️ 開発を実行中...（ダミー処理）")
        # 将来的にコード生成コマンドをここに追加
        time.sleep(1)

    elif phase == Phase.TEST:
        print("🧪 テストを実行中...")
        result = subprocess.run(["pytest", "-q"], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print("❌ テストに失敗しました。")
            return False

    print(f"✅ {phase.name} フェーズが正常に完了しました。")
    return True


def main():
    pm = PhaseManager()

    while not pm.is_complete():
        success = execute_phase(pm.current)
        pm.complete_phase(success=success)

    print("\n🌟 全フェーズが完了しました。")


if __name__ == "__main__":
    main()
