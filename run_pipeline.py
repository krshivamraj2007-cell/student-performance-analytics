
import subprocess
import sys


def run_step(description, command):
    print(f"\n{'=' * 50}")
    print(f"RUNNING: {description}")
    print("=" * 50)

    result = subprocess.run(command)

    if result.returncode != 0:
        print(f"\nFAILED: {description}")
        sys.exit(result.returncode)

    print(f"SUCCESS: {description}")


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

    print("\nDATA PIPELINE COMPLETED SUCCESSFULLY!")
