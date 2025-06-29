"""
RoundReporter
――――――――――――――――――――――――――――――――――――――――
・Gemini-CLI から自動で呼ばれるのは create_final() だけ  
・開始報告書は copy_start_template() で “雛形をコピー” するだけ  
  └ 内容はユーザー + ChatGPT が編集してコミットする
"""

from datetime import date
from pathlib import Path
import shutil

from config_loader import get_project_name

# ---------------------------------------------------------------------
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

TPL_FINAL = REPORTS_DIR / "template_round_final_report.md"
TPL_START = REPORTS_DIR / "template_round_start_report.md"


def _fill(text: str, project: str, n: int) -> str:
    """テンプレプレースホルダを置換"""
    return (
        text.replace("{開発名}", project)
            .replace("{ラウンド番号}", str(n))
            .replace("{AIモデル名}", "GPT-4o")
            .replace("{日付}", date.today().strftime("%Y年%m月%d日"))
    )


# ------------------------------------------------------------------
# Gemini-CLI が自動で呼ぶ関数
# ------------------------------------------------------------------
def create_final(round_no: int, project: str | None = None) -> Path:
    """
    最終報告書を生成して返す。内容は自動で埋め込み。
    例: reports/round_final_03_light_ai.md
    """
    project = project or get_project_name()
    dst = REPORTS_DIR / f"round_final_{round_no:02d}_{project}.md"
    shutil.copy(TPL_FINAL, dst)
    dst.write_text(_fill(dst.read_text(encoding="utf-8"), project, round_no), encoding="utf-8")
    return dst


# ------------------------------------------------------------------
# ユーザーが手動編集するためにテンプレをコピーするだけの関数
# ------------------------------------------------------------------
def copy_start_template(round_no: int, project: str | None = None) -> Path:
    """
    開始報告書テンプレをコピーして返す（内容自動置換なし）。
    例: reports/round_start_04_light_ai.md
    """
    project = project or get_project_name()
    dst = REPORTS_DIR / f"round_start_{round_no:02d}_{project}.md"
    shutil.copy(TPL_START, dst)
    return dst
