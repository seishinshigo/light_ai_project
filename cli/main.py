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
        mgr.print_status()
    elif args.advance:
        mgr.advance_phase()
    elif args.set:
        mgr.set_phase(args.set)
    elif args.list:
        mgr.list_phases()
    elif args.auto:
        mgr.auto_advance()
    elif args.copy_start_template:
        project = get_project_name()
        copy_start_template(project)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
