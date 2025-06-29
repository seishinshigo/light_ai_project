import argparse
from phase_manager import PhaseManager
from config_loader import get_project_name
from app.round_reporter import copy_start_template


def main() -> None:
    parser = argparse.ArgumentParser(description="フェーズ管理 CLI")
    parser.add_argument("--status", action="store_true", help="現在フェーズを表示")
    parser.add_argument("--advance", action="store_true", help="次のフェーズへ進行")
    parser.add_argument("--set", metavar="フェーズ名", help="指定フェーズに手動変更")
    parser.add_argument("--list", action="store_true", help="利用可能フェーズを一覧表示")
    parser.add_argument("--auto", action="store_true", help="auto_advance が True なら自動進行")
    parser.add_argument(
        "--copy-start-template",
        action="store_true",
        help="次ラウンド開始報告書テンプレを reports/ にコピー（内容は手動編集）",
    )

    args = parser.parse_args()
    mgr = PhaseManager()

    if args.status:
        mgr.status_report()

    elif args.advance:
        mgr.advance_phase()

    elif args.set:
        mgr.set_phase(args.set)

    elif args.list:
        mgr.list_phases()

    elif args.auto:
        if mgr.auto_advance_enabled():
            mgr.advance_phase()
        else:
            print("⚠️ auto_advance は無効です。config/workflow.yaml を確認してください。")

    elif args.copy_start_template:
        new_round = len(mgr.phase_status["completed_phases"]) + 1
        path = copy_start_template(new_round, get_project_name())
        print(f"📝 開始報告書テンプレをコピーしました: {path}")
        print("内容を編集後、git add / commit してください。")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
