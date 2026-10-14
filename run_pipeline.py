
import subprocess
import sys
import logging  
import time
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

    result = subprocess.run(command)
    #result = subprocess.run(["python3", "invalid_script.py"])
    if result.returncode != 0:
        global pipeline_status
        pipeline_status = "FAILED"
        print(f"\nFAILED: {description}")
        logging.error(
            "Failed: %s (exit code: %s)",
            description,
            result.returncode
        )
        sys.exit(result.returncode)

    print(f"SUCCESS: {description}")
    logging.info("Success: %s", description)



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