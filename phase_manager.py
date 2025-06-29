# phase_manager.py

from enum import Enum, auto
from config_loader import get_workflow_setting

class Phase(Enum):
    MEETING = auto()
    DEVELOP = auto()
    TEST = auto()

class PhaseManager:
    def __init__(self):
        self.auto_advance = get_workflow_setting("auto_advance", False)
        self.messages = get_workflow_setting("messages", {})
        self.current = Phase.MEETING

    def notify(self, key: str):
        msg = self.messages.get(key)
        if msg:
            print(msg)

    def next_phase(self):
        next_map = {
            Phase.MEETING: Phase.DEVELOP,
            Phase.DEVELOP: Phase.TEST,
            Phase.TEST: None,
        }
        self.current = next_map.get(self.current)

    def complete_phase(self, success=True, loop=False):
        if loop:
            self.notify("loop_detected")
            return
        if not success:
            self.notify("test_fail")
            return

        self.notify("phase_end")
        if self.auto_advance and self.current:
            self.next_phase()
