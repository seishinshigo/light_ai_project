# config_loader.py

import yaml
from pathlib import Path

CONFIG_PATH = Path("config/workflow.yaml")

def load_workflow_config() -> dict:
    """
    Load the workflow configuration from config/workflow.yaml.
    Returns a dictionary with all workflow settings.
    """
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Workflow config file not found: {CONFIG_PATH}")

    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # fallback defaults
    config.setdefault("workflow", {})
    wf = config["workflow"]
    wf.setdefault("auto_advance", False)
    wf.setdefault("confirm_on_edit", [])
    wf.setdefault("notify_on", [])
    wf.setdefault("loop_detection", {
        "check_interval": 3,
        "max_no_change": 3,
        "pattern_similarity_threshold": 0.95
    })
    wf.setdefault("messages", {
        "phase_end": "✅ フェーズ終了：評価・承認待ち状態に移行しました。",
        "test_fail": "❌ テスト失敗：手動確認をお願いします。",
        "loop_detected": "⚠️ 思考のループが検出されました。処理を中断します。"
    })

    return config
