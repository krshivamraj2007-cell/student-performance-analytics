import psycopg

connection = psycopg.connect(
    "dbname=student_performance user=shivamraj"
)

print("Database connected successfully!")

connection.close()