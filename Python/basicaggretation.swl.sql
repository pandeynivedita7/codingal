-- Count all rows
SELECT COUNT(*)
FROM employees;
-- Count non-null values in a specific column
SELECT COUNT(email)
FROM employees;
-- Count distinct values
SELECT COUNT(DISTINCT department)
FROM employees;
-- Total salary expenditure
SELECT SUM(salary)
FROM employees;
-- Sum with condition
SELECT SUM(salary)
FROM employees
WHERE department = 'Sales';
-- Average salary
SELECT AVG(salary)
FROM employees;
-- Round the average
SELECT ROUND(AVG(salary), 2)
FROM employees;
-- Highest and lowest salaries
SELECT MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employees;
-- Average salary by department
SELECT department,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
-- Count employees in each department
SELECT department,
    COUNT(*) AS employee_count
FROM employees
GROUP BY department;
-- Multiple grouping columns
SELECT department,
    job_title,
    AVG(salary)
FROM employees
GROUP BY department,
    job_title;
-- Departments with more than 5 employees
SELECT department,
    COUNT(*) AS emp_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
-- Departments with average salary over $60,000
SELECT department,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;