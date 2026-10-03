import pandas as pd

INPUT_FILE = "data/cleaned_students.csv"
OUTPUT_FILE = "data/processed_students.csv"

# Load cleaned data
df = pd.read_csv(INPUT_FILE)

# Calculate total marks
marks_columns = [
    "maths_marks",
    "programming_marks",
    "dbms_marks",
    "communication_marks"
]

df["total_marks"] = df[marks_columns].sum(axis=1)

# Calculate average marks
df["average_marks"] = df["total_marks"] / len(marks_columns)

# Calculate percentage
df["percentage"] = df["average_marks"]

# Create performance category
def get_performance(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 75:
        return "Good"
    elif percentage >= 60:
        return "Average"
    elif percentage >= 40:
        return "Below Average"
    else:
        return "Poor"


df["performance_category"] = df["percentage"].apply(get_performance)


# Create risk status
def get_risk(row):
    if (
        row["attendance"] < 75
        or row["percentage"] < 40
        or row["backlogs"] >= 2
    ):
        return "High Risk"

    elif (
        row["attendance"] < 80
        or row["percentage"] < 60
        or row["backlogs"] == 1
    ):
        return "Medium Risk"

    else:
        return "Low Risk"


df["risk_status"] = df.apply(get_risk, axis=1)

# Save processed data
df.to_csv(OUTPUT_FILE, index=False)

print("Transformation completed successfully.")
print("Total students:", len(df))
print("New columns added:")
print("- total_marks")
print("- average_marks")
print("- percentage")
print("- performance_category")
print("- risk_status")
print(f"Processed data saved to: {OUTPUT_FILE}")