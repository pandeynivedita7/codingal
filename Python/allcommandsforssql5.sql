CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Country VARCHAR(50),
    Age INT
);
INSERT INTO Customers (CustomerID, Name, Country, Age)
VALUES (1, 'Amit', 'India', 25),
    (2, 'John', 'USA', 30),
    (3, 'Priya', 'India', 28),
    (4, 'Emma', 'UK', 32),
    (5, 'Ali', 'UAE', 26),
    (6, 'Sara', 'India', 22),
    (17, 'Amit23', 'India', 25),
    (7, 'Tom', 'USA', 29);
SELECT *
FROM Customers;
SELECT Name,
    Country
FROM Customers;
SELECT Age
FROM Customers;
SELECT DISTINCT Country
FROM Customers;
---Shows only unique countries.
SELECT COUNT(CustomerID) AS IndianCustomers
FROM Customers
WHERE Country = 'UK';
----Counts customers from India.
SELECT AVG(Age) AS AverageAge
FROM Customers;
----Finds the average age.5 subject add all 5 subject/5(no of subject)
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    Country VARCHAR(50),
    OrderAmount DECIMAL(10, 2)
);
---SUM() Function (using another table) avg me add all marks and /by no of marks