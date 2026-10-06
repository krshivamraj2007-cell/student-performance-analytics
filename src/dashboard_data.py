import pandas as pd
#from src.db_connection import get_connection
from src.db_connection import get_connection


def get_student_performance():

    query = """
    SELECT
        s.student_id,
        s.name,
        d.department_name,
        s.semester,
        ROUND(AVG(m.marks), 2) AS average_marks,
        a.attendance
    FROM students s
    JOIN departments d
        ON s.department_id = d.department_id
    JOIN marks m
        ON s.student_id = m.student_id
    JOIN attendance a
        ON s.student_id = a.student_id
    GROUP BY
        s.student_id,
        s.name,
        d.department_name,
        s.semester,
        a.attendance
    ORDER BY average_marks DESC;
    """

    with get_connection() as connection:
        return pd.read_sql(query, connection)


def get_subject_performance():

    query = """
    SELECT
        sub.subject_name,
        ROUND(AVG(m.marks), 2) AS average_marks
    FROM marks m
    JOIN subjects sub
        ON m.subject_id = sub.subject_id
    GROUP BY sub.subject_name
    ORDER BY average_marks DESC;
    """

    with get_connection() as connection:
        return pd.read_sql(query, connection)