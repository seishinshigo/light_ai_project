import yaml
import os


def get_project_name() -> str:
    """
    config.yaml からプロジェクト名を取得する関数。
    設定ファイルはプロジェクトルートに存在する必要がある。
    """
    config_path = "config.yaml"
    if not os.path.exists(config_path):
        raise FileNotFoundError("❌ config.yaml が見つかりません。プロジェクトルートに配置してください。")

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    project_name = config.get("project_name", "unknown_project")
    return project_name
