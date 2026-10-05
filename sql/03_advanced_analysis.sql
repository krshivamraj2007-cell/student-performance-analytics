-- ============================================
-- STUDENT PERFORMANCE ANALYSIS
-- Advanced SQL Analysis
-- ============================================


-- 1. CTE: Student average performance

WITH student_average AS (
    SELECT
        s.student_id,
        s.name,
        d.department_name,
        ROUND(AVG(m.marks), 2) AS average_marks
    FROM students s
    JOIN departments d
        ON s.department_id = d.department_id
    JOIN marks m
        ON s.student_id = m.student_id
    GROUP BY
        s.student_id,
        s.name,
        d.department_name
)
SELECT *
FROM student_average
ORDER BY average_marks DESC;


-- 2. Department-wise student ranking

WITH student_average AS (
    SELECT
        s.student_id,
        s.name,
        d.department_name,
        ROUND(AVG(m.marks), 2) AS average_marks
    FROM students s
    JOIN departments d
        ON s.department_id = d.department_id
    JOIN marks m
        ON s.student_id = m.student_id
    GROUP BY
        s.student_id,
        s.name,
        d.department_name
)
SELECT
    student_id,
    name,
    department_name,
    average_marks,
    RANK() OVER (
        PARTITION BY department_name
        ORDER BY average_marks DESC
    ) AS department_rank
FROM student_average
ORDER BY department_name, department_rank;


-- 3. Top 3 students in each department

WITH student_average AS (
    SELECT
        s.student_id,
        s.name,
        d.department_name,
        ROUND(AVG(m.marks), 2) AS average_marks
    FROM students s
    JOIN departments d
        ON s.department_id = d.department_id
    JOIN marks m
        ON s.student_id = m.student_id
    GROUP BY
        s.student_id,
        s.name,
        d.department_name
),
ranked_students AS (
    SELECT
        student_id,
        name,
        department_name,
        average_marks,
        RANK() OVER (
            PARTITION BY department_name
            ORDER BY average_marks DESC
        ) AS department_rank
    FROM student_average
)
SELECT *
FROM ranked_students
WHERE department_rank <= 3
ORDER BY department_name, department_rank;


-- 4. Subject performance by department

SELECT
    d.department_name,
    sub.subject_name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN departments d
    ON s.department_id = d.department_id
JOIN marks m
    ON s.student_id = m.student_id
JOIN subjects sub
    ON m.subject_id = sub.subject_id
GROUP BY
    d.department_name,
    sub.subject_name
ORDER BY
    d.department_name,
    average_marks DESC;


-- 5. Subject ranking within each department

WITH department_subject_avg AS (
    SELECT
        d.department_name,
        sub.subject_name,
        ROUND(AVG(m.marks), 2) AS average_marks
    FROM students s
    JOIN departments d
        ON s.department_id = d.department_id
    JOIN marks m
        ON s.student_id = m.student_id
    JOIN subjects sub
        ON m.subject_id = sub.subject_id
    GROUP BY
        d.department_name,
        sub.subject_name
),
ranked_subjects AS (
    SELECT
        department_name,
        subject_name,
        average_marks,
        RANK() OVER (
            PARTITION BY department_name
            ORDER BY average_marks DESC
        ) AS subject_rank
    FROM department_subject_avg
)
SELECT
    department_name,
    subject_name,
    average_marks,
    subject_rank
FROM ranked_subjects
ORDER BY department_name, subject_rank;


-- 6. Subject failure rate

SELECT
    sub.subject_name,
    COUNT(*) AS total_students,
    COUNT(*) FILTER (WHERE m.marks < 40) AS failed_students,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE m.marks < 40) / COUNT(*),
        2
    ) AS failure_rate
FROM marks m
JOIN subjects sub
    ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
ORDER BY failure_rate DESC;


-- 7. Student performance consistency

WITH student_variation AS (
    SELECT
        s.student_id,
        s.name,
        ROUND(AVG(m.marks), 2) AS average_marks,
        ROUND(STDDEV(m.marks)::numeric, 2) AS marks_stddev
    FROM students s
    JOIN marks m
        ON s.student_id = m.student_id
    GROUP BY s.student_id, s.name
)
SELECT
    student_id,
    name,
    average_marks,
    marks_stddev
FROM student_variation
ORDER BY marks_stddev ASC
LIMIT 10;


-- 8. Subject score distribution

SELECT
    sub.subject_name,
    COUNT(*) AS student_count,
    ROUND(AVG(m.marks), 2) AS average_marks,
    ROUND(
        PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY m.marks)::numeric,
        2
    ) AS median_marks,
    ROUND(STDDEV(m.marks)::numeric, 2) AS marks_stddev
FROM marks m
JOIN subjects sub
    ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
ORDER BY average_marks DESC;


-- 9. Department + semester performance

SELECT
    d.department_name,
    s.semester,
    COUNT(DISTINCT s.student_id) AS student_count,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN departments d
    ON s.department_id = d.department_id
JOIN marks m
    ON s.student_id = m.student_id
GROUP BY
    d.department_name,
    s.semester
ORDER BY
    d.department_name,
    s.semester;


-- 10. Semester-wise pass rate

SELECT
    s.semester,
    COUNT(*) AS total_subject_attempts,
    COUNT(*) FILTER (WHERE m.marks >= 40) AS passed_attempts,
    COUNT(*) FILTER (WHERE m.marks < 40) AS failed_attempts,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE m.marks >= 40) / COUNT(*),
        2
    ) AS pass_rate
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
GROUP BY s.semester
ORDER BY s.semester;


-- 11. Attendance and marks correlation

WITH student_performance AS (
    SELECT
        s.student_id,
        AVG(m.marks) AS average_marks,
        a.attendance
    FROM students s
    JOIN marks m
        ON s.student_id = m.student_id
    JOIN attendance a
        ON s.student_id = a.student_id
    GROUP BY s.student_id, a.attendance
)
SELECT
    ROUND(
        CORR(attendance, average_marks)::numeric,
        3
    ) AS attendance_marks_correlation
FROM student_performance;


-- 12. Subject difficulty ranking

WITH subject_average AS (
    SELECT
        sub.subject_name,
        AVG(m.marks) AS average_marks
    FROM marks m
    JOIN subjects sub
        ON m.subject_id = sub.subject_id
    GROUP BY sub.subject_name
)
SELECT
    subject_name,
    ROUND(average_marks, 2) AS average_marks,
    RANK() OVER (
        ORDER BY average_marks ASC
    ) AS difficulty_rank
FROM subject_average
ORDER BY difficulty_rank;