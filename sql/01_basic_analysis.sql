-- ============================================
-- STUDENT PERFORMANCE ANALYSIS
-- Basic SQL Analysis
-- ============================================


-- 1. Total number of students

SELECT COUNT(*) AS total_students
FROM students;


-- 2. Number of students by department

SELECT
    d.department_name,
    COUNT(*) AS student_count
FROM students s
JOIN departments d
    ON s.department_id = d.department_id
GROUP BY d.department_name
ORDER BY student_count DESC;


-- 3. Average marks by subject

SELECT
    sub.subject_name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM marks m
JOIN subjects sub
    ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
ORDER BY average_marks DESC;


-- 4. Average marks by department

SELECT
    d.department_name,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM marks m
JOIN students s
    ON m.student_id = s.student_id
JOIN departments d
    ON s.department_id = d.department_id
GROUP BY d.department_name
ORDER BY average_marks DESC;


-- 5. Semester-wise average marks

SELECT
    s.semester,
    ROUND(AVG(m.marks), 2) AS average_marks
FROM students s
JOIN marks m
    ON s.student_id = m.student_id
GROUP BY s.semester
ORDER BY average_marks DESC;


-- 6. Highest and lowest marks in each subject

SELECT
    sub.subject_name,
    MAX(m.marks) AS highest_marks,
    MIN(m.marks) AS lowest_marks
FROM marks m
JOIN subjects sub
    ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
ORDER BY highest_marks DESC;