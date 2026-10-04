import pandas as pd
import psycopg

df = pd.read_csv("data/students.csv")

connection = psycopg.connect(
    "dbname=student_performance user=shivamraj"
)

print("CSV loaded and database connected!")


cursor = connection.cursor()

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO attendance
        (student_id, attendance)
        VALUES (%s, %s)
        """,
        (
            row["student_id"],
            row["attendance"]
        )
    )

connection.commit()

print("Attendance inserted successfully!")