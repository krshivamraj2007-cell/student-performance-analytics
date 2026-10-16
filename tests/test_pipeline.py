
# def test_pipeline_status_is_success():
#     status = "SUCCESS"

#     assert status == "SUCCESS"



# import json
# from pathlib import Path


# def test_pipeline_report_exists():
#     report_path = Path("pipeline_report.json")

#     assert report_path.exists(), "Pipeline report file is missing"


# def test_pipeline_report_has_required_fields():
#     with open("pipeline_report.json", "r") as file:
#         report = json.load(file)

#     assert "status" in report
#     assert "completed_at" in report
#     assert "total_execution_time_seconds" in report


# def test_pipeline_report_status_is_valid():
#     with open("pipeline_report.json", "r") as file:
#         report = json.load(file)

#     assert report["status"] in ["SUCCESS", "FAILED"]


# def test_pipeline_execution_time_is_non_negative():
#     with open("pipeline_report.json", "r") as file:
#         report = json.load(file)

#     assert report["total_execution_time_seconds"] >= 0


import json
import subprocess


def test_pipeline_report_exists():
    from pathlib import Path

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


def test_temporary_pipeline_report(tmp_path):
    report_path = tmp_path / "pipeline_report.json"

    report = {
        "status": "SUCCESS",
        "completed_at": "2026-10-15 09:00:00",
        "total_execution_time_seconds": 2.5,
    }

    with open(report_path, "w") as file:
        json.dump(report, file)

    with open(report_path, "r") as file:
        loaded_report = json.load(file)

    assert loaded_report["status"] == "SUCCESS"
    assert loaded_report["total_execution_time_seconds"] == 2.5

import subprocess


def test_failed_command_returns_nonzero_exit_code():
    result = subprocess.run(
        ["python3", "-c", "import sys; sys.exit(1)"],
        capture_output=True,
        text=True
    )

    assert result.returncode != 0

import run_pipeline
import pytest


def test_run_step_exits_when_command_fails(monkeypatch):
    monkeypatch.setattr(
        run_pipeline.subprocess,
        "run",
        lambda command: type("Result", (), {"returncode": 1})()
    )

    with pytest.raises(SystemExit) as error:
        run_pipeline.run_step(
            "Test failed step",
            ["fake-command"]
        )

    assert error.value.code == 1
    assert run_pipeline.pipeline_status == "FAILED"
