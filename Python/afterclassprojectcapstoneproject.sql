CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT,
    JoinDate DATE
);
INSERT INTO Employees
VALUES (101, 'Amit Sharma', 'HR', 45000, '2021-04-12'),
    (102, 'Sara Khan', 'IT', 55000, '2020-11-22'),
    (
        103,
        'Rohan Verma',
        'Finance',
        60000,
        '2022-03-10'
    ),
    (104, 'Meha Singh', 'IT', 52000, '2023-01-05'),
    (105, 'Vikas Patel', 'HR', 47000, '2021-08-16');
UPDATE Employees
SET Salary = 58000
WHERE EmpID = 102;
SELECT *
FROM Employees
ORDER BY Salary DESC;
SELECT *
FROM Employees
ORDER BY Name ASC;
SELECT *
FROM Employees
WHERE Salary > 50000;
SELECT MAX(Salary) AS HighestSalary
FROM Employees;
SELECT Department,
    SUM(Salary) AS TotalDeptSalary
FROM Employees
GROUP BY Department;