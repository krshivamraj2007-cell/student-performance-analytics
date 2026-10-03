import pandas as pd

INPUT_FILE = "data/students.csv"
OUTPUT_FILE = "data/cleaned_students.csv"

# Load raw data
df = pd.read_csv(INPUT_FILE)

print("Original rows:", len(df))

# Remove duplicate rows
df = df.drop_duplicates()

# Clean names
df["name"] = df["name"].str.strip()

# Standardize department names
df["department"] = df["department"].str.upper().str.strip()

# Remove records with missing student IDs
df = df.dropna(subset=["student_id"])

# Make sure student IDs are unique
df = df.drop_duplicates(subset=["student_id"])

# Save cleaned data
df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned rows:", len(df))
print(f"Cleaned data saved to: {OUTPUT_FILE}")