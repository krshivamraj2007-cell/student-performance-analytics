
# def test_pipeline_status_is_success():
#     status = "SUCCESS"

#     assert status == "SUCCESS"



import json
from pathlib import Path


def test_pipeline_report_exists():
    report_path = Path("pipeline_report.json")

    assert report_path.exists(), "Pipeline report file is missing"


def test_pipeline_report_has_required_fields():
    with open("pipeline_report.json", "r") as file:
        report = json.load(file)

    assert "status" in report
    assert "completed_at" in report
    assert "total_execution_time_seconds" in report


def test_pipeline_report_status_is_valid():
    with open("pipeline_report.json", "r") as file:
        report = json.load(file)

    assert report["status"] in ["SUCCESS", "FAILED"]


def test_pipeline_execution_time_is_non_negative():
    with open("pipeline_report.json", "r") as file:
        report = json.load(file)

    assert report["total_execution_time_seconds"] >= 0

