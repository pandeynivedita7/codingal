CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT,
    Grade CHAR(2),
    City VARCHAR(50)
);
INSERT INTO Students (StudentID, Name, Age, Grade, City)
VALUES (1, 'Aarav', 15, 'A', 'Mumbai'),
    (2, 'Riya', 14, 'B', 'Delhi'),
    (3, 'Kabir', 13, 'A', 'Pune'),
    (4, 'Simran', 15, 'C', 'Kolkata'),
    (5, 'Arjun', 14, 'B', 'Chennai');
SELECT *
FROM Students;
SELECT *
FROM Students
WHERE City = 'Delhi';
SELECT Name,
    City
FROM Students
WHERE Age > 14;
SELECT *
FROM Students
WHERE Grade = 'A'
    AND City = 'Pune';