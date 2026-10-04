import pandas as pd
import psycopg

df = pd.read_csv("data/students.csv")

connection = psycopg.connect(
    "dbname=student_performance user=shivamraj"
)

print("CSV loaded and database connected!")


cursor = connection.cursor()

cursor.execute(
    "SELECT subject_id, subject_name FROM subjects"
)

subject_map = {
    name: subject_id
    for subject_id, name in cursor.fetchall()
}

print(subject_map)

subject_columns = {
    "maths_marks": "Mathematics",
    "programming_marks": "Programming",
    "dbms_marks": "DBMS",
    "communication_marks": "Communication"
}

for _, row in df.iterrows():

    for csv_subject, db_subject in subject_columns.items():

        subject_id = subject_map[db_subject]
        marks = row[csv_subject]

        cursor.execute(
            """
            INSERT INTO marks
            (student_id, subject_id, marks)
            VALUES (%s, %s, %s)
            """,
            (
                row["student_id"],
                subject_id,
                marks
            )
        )

connection.commit()

print("Marks inserted successfully!")