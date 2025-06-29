# tests/test_phase_manager.py

from phase_manager import PhaseManager, Phase

def test_auto_advance():
    pm = PhaseManager()
    pm.auto_advance = True
    pm.current = Phase.MEETING
    pm.complete_phase(success=True)
    assert pm.current == Phase.DEVELOP
