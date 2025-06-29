# app/report_service.py

import os
from typing import List

REPORT_DIR = "report"

class ReportService:
    @staticmethod
    def save_report(filename: str, content: str) -> None:
        os.makedirs(REPORT_DIR, exist_ok=True)
        path = os.path.join(REPORT_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def load_report(filename: str) -> str:
        path = os.path.join(REPORT_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def list_reports() -> List[str]:
        if not os.path.exists(REPORT_DIR):
            return []
        return [f for f in os.listdir(REPORT_DIR) if os.path.isfile(os.path.join(REPORT_DIR, f))]
