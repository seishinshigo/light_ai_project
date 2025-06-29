import os
import json
import shutil
import pytest
from unittest.mock import patch

from phase_manager import PhaseManager, STATE_FILE, save_phase_status

@pytest.fixture(autouse=True)
def setup_and_cleanup_state():
    # テスト前：バックアップ
    backup_path = STATE_FILE.with_suffix(".bak")
    if STATE_FILE.exists():
        shutil.copy(STATE_FILE, backup_path)

    # テスト用初期状態
    save_phase_status({
        "current_phase": "会議",
        "completed_phases": [],
        "status": "in_progress"
    })

    yield  # テスト実行

    # テスト後：復元
    if backup_path.exists():
        shutil.move(backup_path, STATE_FILE)
    else:
        STATE_FILE.unlink(missing_ok=True)

def test_phase_progression():
    manager = PhaseManager()
    assert manager.phase_status["current_phase"] == "会議"

    manager.advance_phase()
    assert manager.phase_status["current_phase"] == "開発"

    manager.advance_phase()
    assert manager.phase_status["current_phase"] == "テスト"

    manager.advance_phase()
    assert manager.phase_status["current_phase"] == "完了"
    assert manager.phase_status["status"] == "done"

def test_notify_called_on_advance():
    with patch("phase_manager.notify") as mock_notify:
        manager = PhaseManager()
        manager.advance_phase()
        mock_notify.assert_called_once()
        args, _ = mock_notify.call_args
        assert "✅" in args[0]  # 通知メッセージに ✅ が含まれていること
