
import subprocess
import sys
import logging  
import time
from datetime import datetime
import json 
from datetime import datetime

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

pipeline_start_time = time.time()
pipeline_status = "SUCCESS"

def run_step(description, command):
    print(f"\n{'=' * 50}")
    print(f"RUNNING: {description}")
    print("=" * 50)

    logging.info("Starting: %s", description)
    step_start_time = time.time() 
    result = subprocess.run(command)
    step_duration = time.time() - step_start_time

    print(f"Step execution time: {step_duration:.2f} seconds")
    logging.info(
    "Execution time for %s: %.2f seconds",
    description,
    step_duration
)
    #result = subprocess.run(["python3", "invalid_script.py"])
    if result.returncode != 0:
        global pipeline_status
        pipeline_status = "FAILED"
        logging.error("Step status: FAILED - %s", description)
        print(f"\nFAILED: {description}")
        logging.error(
            "Failed: %s (exit code: %s)",
            description,
            result.returncode
        )
        sys.exit(result.returncode)

    print(f"SUCCESS: {description}")
    logging.info("Success: %s", description)
    logging.info("Step status: SUCCESS - %s", description)



if __name__ == "__main__":
    run_step(
        "Generate Student Data",
        [sys.executable, "src/generate_data.py"]
    )

    run_step(
        "Clean Student Data",
        [sys.executable, "src/clean_data.py"]
    )

    run_step(
        "Transform Student Data",
        [sys.executable, "src/transform_data.py"]
    )

    run_step(
        "Validate Student Data",
        [sys.executable, "src/validate_data.py"]
    )

    run_step(
        "Load Students into PostgreSQL",
        [sys.executable, "src/load_students.py"]
    )

    run_step(
        "Load Marks into PostgreSQL",
        [sys.executable, "src/load_marks.py"]
    )

    run_step(
        "Load Attendance into PostgreSQL",
        [sys.executable, "src/load_attendance.py"]
    )


    print("\nDATA PIPELINE COMPLETED SUCCESSFULLY!")

    pipeline_end_time = time.time()
print(f"Total pipeline execution time: {pipeline_end_time - pipeline_start_time:.2f} seconds")
logging.info(
    "Total pipeline execution time: %.2f seconds",
    pipeline_end_time - pipeline_start_time
)
print("\n" + "=" * 50)
print("PIPELINE SUMMARY")
print("=" * 50)
print(f"status : {pipeline_status}")
print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Total execution time: {pipeline_end_time - pipeline_start_time:.2f} seconds")
print("=" * 50)


report = {
    "status": pipeline_status,
    "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "total_execution_time_seconds": round(
        pipeline_end_time - pipeline_start_time, 2
    )
}

with open("pipeline_report.json", "w") as report_file:
    json.dump(report, report_file, indent=4)

print("Pipeline report saved to pipeline_report.json")
