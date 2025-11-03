-- ============================================
-- SQL OPERATORS - COMPLETE GUIDE
-- ============================================
-- Create sample tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade CHAR(1),
    marks INT,
    city VARCHAR(50),
    fees_paid DECIMAL(10, 2)
);
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    credits INT,
    student_id INT
);
-- Insert sample data
INSERT INTO students
VALUES (
        1,
        'Alice Johnson',
        20,
        'A',
        95,
        'New York',
        5000.00
    ),
    (2, 'Bob Smith', 22, 'B', 85, 'Boston', 4500.00),
    (
        3,
        'Charlie Brown',
        21,
        'A',
        92,
        'New York',
        5000.00
    ),
    (4, 'David Lee', 23, 'C', 75, 'Chicago', 4000.00),
    (5, 'Emma Davis', 20, 'B', 88, 'Boston', NULL),
    (
        6,
        'Frank Wilson',
        24,
        'D',
        65,
        'Chicago',
        3500.00
    );
INSERT INTO courses
VALUES (101, 'Mathematics', 4, 1),
    (102, 'Physics', 3, 2),
    (103, 'Chemistry', 3, 1),
    (104, 'Biology', 4, 3);
-- ============================================
-- 1. ARITHMETIC OPERATORS (+, -, *, /, %)
-- ============================================
-- Addition
SELECT name,
    marks,
    marks + 5 AS bonus_marks
FROM students;
-- Subtraction
SELECT name,
    age,
    age - 18 AS years_over_18
FROM students;
-- Multiplication
SELECT name,
    marks,
    marks * 1.1 AS marks_with_bonus
FROM students;
-- Division
SELECT name,
    marks,
    marks / 10.0 AS grade_points
FROM students;
-- Modulus (remainder)
SELECT name,
    marks,
    marks % 10 AS last_digit
FROM students;
-- Combined arithmetic
SELECT name,
    fees_paid,
    fees_paid * 0.10 AS discount,
    fees_paid - (fees_paid * 0.10) AS final_amount
FROM students
WHERE fees_paid IS NOT NULL;
-- ============================================
-- 2. COMPARISON OPERATORS (=, !=, <>, <, >, <=, >=)
-- ============================================
-- Equal to
SELECT *
FROM students
WHERE grade = 'A';
-- Not equal to (two ways)
SELECT *
FROM students
WHERE grade != 'A';
SELECT *
FROM students
WHERE grade <> 'A';
-- Less than
SELECT name,
    marks
FROM students
WHERE marks < 80;
-- Greater than
SELECT name,
    age
FROM students
WHERE age > 21;
-- Less than or equal to
SELECT name,
    marks
FROM students
WHERE marks <= 85;
-- Greater than or equal to
SELECT name,
    age
FROM students
WHERE age >= 22;
-- ============================================
-- 3. LOGICAL OPERATORS (AND, OR, NOT)
-- ============================================
-- AND operator (both conditions must be true)
SELECT *
FROM students
WHERE grade = 'A'
    AND city = 'New York';
-- OR operator (at least one condition must be true)
SELECT *
FROM students
WHERE grade = 'A'
    OR grade = 'B';
-- NOT operator (negates condition)
SELECT *
FROM students
WHERE NOT city = 'Chicago';
-- Combining logical operators
SELECT *
FROM students
WHERE (
        grade = 'A'
        OR grade = 'B'
    )
    AND marks > 85;
-- Complex logical expressions
SELECT name,
    marks,
    city
FROM students
WHERE (
        city = 'New York'
        OR city = 'Boston'
    )
    AND marks >= 85
    AND age <= 21;
-- ============================================
-- 4. BETWEEN OPERATOR
-- ============================================
-- BETWEEN (inclusive range)
SELECT *
FROM students
WHERE marks BETWEEN 80 AND 90;
-- NOT BETWEEN
SELECT *
FROM students
WHERE age NOT BETWEEN 20 AND 22;
-- BETWEEN with dates (example structure)
-- SELECT * FROM students WHERE enrollment_date BETWEEN '2023-01-01' AND '2023-12-31';
-- ============================================
-- 5. IN OPERATOR
-- ============================================
-- IN operator (match any value in list)
SELECT *
FROM students
WHERE city IN ('New York', 'Boston');
-- NOT IN operator
SELECT *
FROM students
WHERE grade NOT IN ('A', 'B');
-- IN with numbers
SELECT *
FROM students
WHERE marks IN (85, 92, 95);
-- ============================================
-- 6. LIKE OPERATOR (Pattern Matching)
-- ============================================
-- Starts with 'B'
SELECT *
FROM students
WHERE name LIKE 'B%';
-- Ends with 'son'
SELECT *
FROM students
WHERE name LIKE '%son';
-- Contains 'li'
SELECT *
FROM students
WHERE name LIKE '%li%';
-- Second character is 'a'
SELECT *
FROM students
WHERE name LIKE '_a%';
-- NOT LIKE
SELECT *
FROM students
WHERE name NOT LIKE 'A%';
-- ============================================
-- 7. IS NULL / IS NOT NULL
-- ============================================
-- Check for NULL values
SELECT *
FROM students
WHERE fees_paid IS NULL;
-- Check for NOT NULL values
SELECT *
FROM students
WHERE fees_paid IS NOT NULL;
-- ============================================
-- 8. ALL, ANY, SOME OPERATORS
-- ============================================
-- ANY operator (compare with any value returned by subquery)
SELECT *
FROM students
WHERE marks > ANY (
        SELECT marks
        FROM students
        WHERE city = 'Chicago'
    );
-- ALL operator (compare with all values returned by subquery)
SELECT *
FROM students
WHERE marks > ALL (
        SELECT marks
        FROM students
        WHERE city = 'Chicago'
    );
-- SOME operator (same as ANY)
SELECT *
FROM students
WHERE marks = SOME (
        SELECT marks
        FROM students
        WHERE grade = 'A'
    );
-- ============================================
-- 9. EXISTS OPERATOR
-- ============================================
-- EXISTS (check if subquery returns any rows)
SELECT *
FROM students s
WHERE EXISTS (
        SELECT 1
        FROM courses c
        WHERE c.student_id = s.student_id
    );
-- NOT EXISTS
SELECT *
FROM students s
WHERE NOT EXISTS (
        SELECT 1
        FROM courses c
        WHERE c.student_id = s.student_id
    );
-- ============================================
-- 10. UNION, INTERSECT, EXCEPT (Set Operators)
-- ============================================
-- UNION (combine results, remove duplicates)
SELECT city
FROM students
WHERE grade = 'A'
UNION
SELECT city
FROM students
WHERE grade = 'B';
-- UNION ALL (combine results, keep duplicates)
SELECT city
FROM students
WHERE grade = 'A'
UNION ALL
SELECT city
FROM students
WHERE grade = 'B';
-- INTERSECT (common records)
-- Note: Not supported in MySQL, use INNER JOIN instead
SELECT city
FROM students
WHERE grade = 'A'
INTERSECT
SELECT city
FROM students
WHERE grade = 'B';
-- EXCEPT (records in first query but not in second)
-- Note: Not supported in MySQL, use LEFT JOIN with NULL check instead
SELECT city
FROM students
WHERE marks > 80
EXCEPT
SELECT city
FROM students
WHERE age > 22;
-- ============================================
-- 11. BITWISE OPERATORS (&, |, ^)
-- ============================================
-- Bitwise AND
SELECT marks,
    marks & 1 AS is_odd
FROM students;
-- Bitwise OR
SELECT marks,
    marks | 1 AS result
FROM students;
-- Bitwise XOR
SELECT marks,
    marks ^ 1 AS result
FROM students;
-- ============================================
-- 12. CASE OPERATOR (Conditional Logic)
-- ============================================
SELECT name,
    marks,
    CASE
        WHEN marks >= 90 THEN 'Excellent'
        WHEN marks >= 80 THEN 'Very Good'
        WHEN marks >= 70 THEN 'Good'
        ELSE 'Needs Improvement'
    END AS performance
FROM students;
-- CASE with multiple conditions
SELECT name,
    age,
    city,
    CASE
        WHEN city = 'New York'
        AND age < 21 THEN 'Young New Yorker'
        WHEN city = 'Boston'
        AND marks > 85 THEN 'Boston Scholar'
        WHEN city = 'Chicago' THEN 'Chicago Student'
        ELSE 'Other'
    END AS category
FROM students;
-- ============================================
-- 13. COMBINING MULTIPLE OPERATORS
-- ============================================
-- Complex query with multiple operator types
SELECT name,
    marks,
    age,
    city,
    fees_paid
FROM students
WHERE (
        marks > 80
        OR grade IN ('A', 'B')
    )
    AND city LIKE '%o%'
    AND age BETWEEN 20 AND 23
    AND fees_paid IS NOT NULL
    AND marks % 5 = 0
ORDER BY marks DESC;
-- Arithmetic + Comparison + Logical
SELECT name,
    marks,
    fees_paid,
    (fees_paid * 0.9) AS discounted_fees
FROM students
WHERE marks >= 85
    AND (fees_paid * 0.9) < 5000
    AND city IN ('New York', 'Boston');
-- ============================================
-- PRACTICE EXERCISES
-- ============================================
-- Exercise 1: Find students with marks divisible by 5
-- Exercise 2: Find students from cities starting with 'B' or 'N'
-- Exercise 3: Calculate scholarship (10% of fees) for students with marks > 90
-- Exercise 4: Find students who are not from Chicago and have paid fees
-- Exercise 5: Use CASE to assign letter grades based on marks