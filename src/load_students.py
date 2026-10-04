import pandas as pd
import psycopg

df = pd.read_csv("data/students.csv")

connection = psycopg.connect(
    "dbname=student_performance user=shivamraj"
)

print("CSV loaded and database connected!")


cursor = connection.cursor()

cursor.execute("SELECT department_id, department_name FROM departments")

department_map = {
    name: department_id
    for department_id, name in cursor.fetchall()
}

print(department_map)

for _, row in df.iterrows():

    department_id = department_map[row["department"]]

    cursor.execute(
        """
        INSERT INTO students
        (student_id, name, department_id, semester, gender, age)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            row["student_id"],
            row["name"],
            department_id,
            row["semester"],
            row["gender"],
            row["age"]
        )
    )

connection.commit()

print("Students inserted successfully!")