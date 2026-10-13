
import subprocess
import sys
import logging  

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def run_step(description, command):
    print(f"\n{'=' * 50}")
    print(f"RUNNING: {description}")
    print("=" * 50)

    logging.info("Starting: %s", description)

    result = subprocess.run(command)

    if result.returncode != 0:
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
