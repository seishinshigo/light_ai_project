# tests/test_report_service.py

import os
import shutil
from app.report_service import ReportService

def setup_function():
    os.makedirs("report", exist_ok=True)

def teardown_function():
    shutil.rmtree("report", ignore_errors=True)

def test_save_and_load_report():
    filename = "test_report.txt"
    content = "これはテストレポートです。"
    ReportService.save_report(filename, content)
    loaded = ReportService.load_report(filename)
    assert loaded == content

def test_list_reports():
    ReportService.save_report("r1.txt", "a")
    ReportService.save_report("r2.txt", "b")
    reports = ReportService.list_reports()
    assert "r1.txt" in reports
    assert "r2.txt" in reports
