-- Create a sample database table
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE,
    age INT
);
-- Insert sample data
INSERT INTO employees
VALUES (
        1,
        'John',
        'Doe',
        'IT',
        75000.00,
        '2020-01-15',
        30
    ),
    (
        2,
        'Jane',
        'Smith',
        'HR',
        65000.00,
        '2019-03-20',
        28
    ),
    (
        3,
        'Mike',
        'Johnson',
        'IT',
        85000.00,
        '2018-06-10',
        35
    ),
    (
        4,
        'Sarah',
        'Williams',
        'Sales',
        70000.00,
        '2021-02-28',
        26
    ),
    (
        5,
        'Tom',
        'Brown',
        'Sales',
        72000.00,
        '2020-08-05',
        32
    ),
    (
        6,
        'Emily',
        'Davis',
        'HR',
        68000.00,
        '2019-11-12',
        29
    );
-- Example 1: Find minimum and maximum salary
SELECT MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM employees;
-- Example 2: Find MIN and MAX by department
SELECT department,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    MAX(salary) - MIN(salary) AS salary_range
FROM employees
GROUP BY department;
-- Example 3: Find earliest and latest hire dates
SELECT MIN(hire_date) AS earliest_hire,
    MAX(hire_date) AS latest_hire
FROM employees;
-- Example 4: Find youngest and oldest employee ages
SELECT MIN(age) AS youngest_age,
    MAX(age) AS oldest_age,
    MAX(age) - MIN(age) AS age_difference
FROM employees;
-- Example 5: Employee with minimum salary
SELECT *
FROM employees
WHERE salary = (
        SELECT MIN(salary)
        FROM employees
    );
-- Example 6: Employee with maximum salary
SELECT *
FROM employees
WHERE salary = (
        SELECT MAX(salary)
        FROM employees
    );
-- Example 7: MIN and MAX with multiple conditions
SELECT department,
    COUNT(*) AS employee_count,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    AVG(salary) AS avg_salary
FROM employees
WHERE hire_date >= '2019-01-01'
GROUP BY department
HAVING COUNT(*) > 1
ORDER BY max_salary DESC;