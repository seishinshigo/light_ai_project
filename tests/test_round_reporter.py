from app.round_reporter import create_final, copy_start_template, REPORTS_DIR
from pathlib import Path

def test_create_final(tmp_path, monkeypatch):
    # 出力先を一時ディレクトリに差し替え
    monkeypatch.setattr("app.round_reporter.REPORTS_DIR", tmp_path)
    path = create_final(99, project="demo")
    assert path.exists()
    assert "round_final_99_demo.md" in str(path)

def test_copy_start_template(tmp_path, monkeypatch):
    monkeypatch.setattr("app.round_reporter.REPORTS_DIR", tmp_path)
    path = copy_start_template(100, project="demo")
    assert path.exists()
    assert "round_start_100_demo.md" in str(path)
