-- ============================================
-- STUDENT PERFORMANCE ANALYSIS
-- Performance Analysis
-- ============================================


-- 1. Top 10 students

SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks DESC
LIMIT 10;


-- 2. Bottom 10 students

SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks ASC
LIMIT 10;


-- 3. Students with attendance below 75%

SELECT
    s.student_id,
    s.name,
    a.attendance
FROM students s
JOIN attendance a
    ON s.student_id = a.student_id
WHERE a.attendance < 75
ORDER BY a.attendance;


-- 4. Students with attendance above 90%

SELECT
    s.student_id,
    s.name,
    a.attendance
FROM students s
JOIN attendance a
    ON s.student_id = a.student_id
WHERE a.attendance > 90
ORDER BY a.attendance DESC;


-- 5. Students with high marks but low attendance

SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks,
    a.attendance
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
JOIN attendance a
    ON s.student_id = a.student_id
GROUP BY s.student_id, s.name, a.attendance
HAVING AVG(m.marks) >= 75
   AND a.attendance < 75
ORDER BY average_marks DESC;


-- 6. Students with high attendance but low marks

SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks,
    a.attendance
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
JOIN attendance a
    ON s.student_id = a.student_id
GROUP BY s.student_id, s.name, a.attendance
HAVING AVG(m.marks) < 60
   AND a.attendance >= 85
ORDER BY average_marks ASC;


-- 7. Department-wise average attendance

SELECT
    d.department_name,
    ROUND(AVG(a.attendance), 2) AS average_attendance
FROM students s
JOIN departments d
    ON s.department_id = d.department_id
JOIN attendance a
    ON s.student_id = a.student_id
GROUP BY d.department_name
ORDER BY average_attendance DESC;


-- 8. Performance category of each student

SELECT
    s.student_id,
    s.name,
    ROUND(AVG(m.marks), 2) AS average_marks,
    CASE
        WHEN AVG(m.marks) >= 90 THEN 'Excellent'
        WHEN AVG(m.marks) >= 75 THEN 'Good'
        WHEN AVG(m.marks) >= 60 THEN 'Average'
        WHEN AVG(m.marks) >= 40 THEN 'Below Average'
        ELSE 'Poor'
    END AS performance_category
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
GROUP BY s.student_id, s.name
ORDER BY average_marks DESC;


-- 9. Count students by performance category

SELECT
    performance_category,
    COUNT(*) AS student_count
FROM (
    SELECT
        s.student_id,
        CASE
            WHEN AVG(m.marks) >= 90 THEN 'Excellent'
            WHEN AVG(m.marks) >= 75 THEN 'Good'
            WHEN AVG(m.marks) >= 60 THEN 'Average'
            WHEN AVG(m.marks) >= 40 THEN 'Below Average'
            ELSE 'Poor'
        END AS performance_category
    FROM students s
    JOIN marks m
        ON s.student_id = m.student_id
    GROUP BY s.student_id
) AS student_performance
GROUP BY performance_category
ORDER BY student_count DESC;