import psycopg


def get_connection():
    return psycopg.connect(
        "dbname=student_performance user=shivamraj"
    )