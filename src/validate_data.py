
import pandas as pd


def validate_student_data(file_path):
    df = pd.read_csv(file_path)

    errors = []

    # Check for duplicate student IDs
    if df["student_id"].duplicated().any():
        errors.append("Duplicate student IDs found.")

    # Check for missing values
    if df.isnull().any().any():
        errors.append("Missing values found.")

    # Check that marks are within the valid range
    mark_columns = [
        "maths_marks",
        "programming_marks",
        "dbms_marks",
        "communication_marks",
    ]

    for column in mark_columns:
        if column in df.columns:
            if not df[column].between(0, 100).all():
                errors.append(
                    f"Invalid marks found in {column}."
                )

    # Check attendance range
    if "attendance" in df.columns:
        if not df["attendance"].between(0, 100).all():
            errors.append("Invalid attendance values found.")

    if errors:
        print("DATA VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
    else:
        print("DATA VALIDATION PASSED")
        print(f"Total records validated: {len(df)}")


if __name__ == "__main__":
    validate_student_data("data/processed_students.csv")
