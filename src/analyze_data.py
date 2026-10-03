import pandas as pd

# Load the student dataset
df = pd.read_csv("data/students.csv")

# Display basic information
print("\n===== DATASET OVERVIEW =====")

print("Number of students:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\n===== FIRST 5 RECORDS =====")
print(df.head())

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE RECORDS =====")
print("Duplicate rows:", df.duplicated().sum())


print("\n===== DATA VALIDATION =====")

# Check duplicate student IDs
print("Duplicate student IDs:",
      df["student_id"].duplicated().sum())

# Check invalid marks
marks_columns = [
    "maths_marks",
    "programming_marks",
    "dbms_marks",
    "communication_marks"
]

for column in marks_columns:
    invalid = ((df[column] < 0) | (df[column] > 100)).sum()
    print(f"Invalid {column}: {invalid}")

# Check invalid attendance
invalid_attendance = (
    (df["attendance"] < 0) |
    (df["attendance"] > 100)
).sum()

print("Invalid attendance:", invalid_attendance)

# Check invalid semester
invalid_semester = (
    (df["semester"] < 1) |
    (df["semester"] > 8)
).sum()

print("Invalid semester:", invalid_semester)

# Check negative backlogs
negative_backlogs = (df["backlogs"] < 0).sum()

print("Negative backlogs:", negative_backlogs)