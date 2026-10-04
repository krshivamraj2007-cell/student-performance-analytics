subject_columns = {
    "Maths": "Mathematics",
    "Programming": "Programming",
    "DBMS": "DBMS",
    "Communication": "Communication"
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