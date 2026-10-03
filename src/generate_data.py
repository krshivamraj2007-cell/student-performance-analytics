import csv
import random

# Number of students
NUM_STUDENTS = 500

# Departments
departments = ["CSE", "CSE-DS", "ISE", "ECE", "EEE", "ME", "CIVIL"]

# Names
first_names = [
    "Rahul", "Amit", "Priya", "Neha", "Rohan",
    "Ananya", "Arjun", "Sneha", "Vivek", "Kavya"
]

last_names = [
    "Kumar", "Sharma", "Singh", "Patel", "Verma",
    "Gupta", "Reddy", "Mehta", "Joshi", "Das"
]

# Output file
output_file = "data/students.csv"

students = []

for i in range(NUM_STUDENTS):

    student_id = f"STU{1001 + i}"

    name = random.choice(first_names) + " " + random.choice(last_names)

    department = random.choice(departments)

    semester = random.randint(1, 8)

    gender = random.choice(["Male", "Female"])

    age = random.randint(18, 23)

    maths_marks = random.randint(35, 100)
    programming_marks = random.randint(35, 100)
    dbms_marks = random.randint(35, 100)
    communication_marks = random.randint(35, 100)

    attendance = round(random.uniform(55, 100), 2)

    backlogs = random.randint(0, 3)

    students.append([
        student_id,
        name,
        department,
        semester,
        gender,
        age,
        maths_marks,
        programming_marks,
        dbms_marks,
        communication_marks,
        attendance,
        backlogs
    ])


# Write data to CSV
with open(output_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "student_id",
        "name",
        "department",
        "semester",
        "gender",
        "age",
        "maths_marks",
        "programming_marks",
        "dbms_marks",
        "communication_marks",
        "attendance",
        "backlogs"
    ])

    writer.writerows(students)

print(f"{NUM_STUDENTS} student records generated successfully.")
print(f"File saved to: {output_file}")