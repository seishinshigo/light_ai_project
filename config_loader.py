"""
設定ファイル（config/workflow.yaml）を読み込み、
プロジェクト共通で参照できる辞書を返すユーティリティ。
"""

import yaml
from pathlib import Path

DEFAULT_CONFIG_PATH = Path("config/workflow.yaml")


# ----------------------------------------------------------------------
# 基本読込
# ----------------------------------------------------------------------
def load_workflow_config(path: Path | str = DEFAULT_CONFIG_PATH) -> dict:
    """
    YAML を読み込み、`workflow` セクションにデフォルト値を補完して返す。
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"設定ファイルが見つかりません: {path}")

    with path.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}

    cfg.setdefault("workflow", {})
    wf = cfg["workflow"]

    # --- デフォルト各種 ---
    wf.setdefault("project_name", "light_ai")                 # ★プロジェクト名
    wf.setdefault("auto_advance", False)
    wf.setdefault("confirm_on_edit", [])
    wf.setdefault("notify_on", [])
    wf.setdefault(
        "loop_detection",
        {"check_interval": 3, "max_no_change": 3, "pattern_similarity_threshold": 0.95},
    )
    wf.setdefault(
        "messages",
        {
            "phase_end": "✅ フェーズ終了：評価・承認待ち状態に移行しました。",
            "phase_done": "🎉 全てのフェーズが完了しました。お疲れさまでした！",
            "test_fail": "❌ テスト失敗：手動確認をお願いします。",
            "loop_detected": "⚠️ 思考のループが検出されました。処理を中断します。",
        },
    )

    return cfg


# ----------------------------------------------------------------------
# 便利アクセサ
# ----------------------------------------------------------------------
def get_workflow_setting(key: str, default=None):
    """
    workflow セクションから任意キーを取得
    """
    return load_workflow_config()["workflow"].get(key, default)


def get_project_name() -> str:
    """
    プロジェクト名（workflow.project_name）を取得
    """
    return get_workflow_setting("project_name", "light_ai")


def auto_advance_enabled() -> bool:
    """
    auto_advance が True なら True を返す
    """
    return bool(get_workflow_setting("auto_advance", False))
