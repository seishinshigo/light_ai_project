import os
os.environ["GEMINI_MODEL"]="gemini-2.5-flash"

from pathlib import Path
import subprocess

SCRIPT = Path(__file__).resolve().parents[1] / "run_gemini_api.py"

def test_basic_call():
    """Gemini へ簡単な問い合わせが出来るか確認"""
    result = subprocess.run(
        ["python", str(SCRIPT), "-p", "Say OK."],
        capture_output=True,
        text=True,
        timeout=30,
    )
    # プロセスが正常終了し、レスポンスが短いことを確認
    assert result.returncode == 0
    assert "OK" in result.stdout
    assert len(result.stdout) < 400
