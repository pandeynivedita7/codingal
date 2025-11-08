CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    Country VARCHAR(50),
    OrderAmount DECIMAL(10, 2)
);
---Create another table:
INSERT INTO Orders (OrderID, CustomerID, Country, OrderAmount)
VALUES (101, 1, 'India', 5000),
    (102, 2, 'USA', 7000),
    (103, 3, 'India', 6000),
    (104, 4, 'UK', 8000),
    (105, 5, 'UAE', 3000),
    (106, 6, 'India', 4000),
    (107, 7, 'USA', 5000);
----Insert records:
SELECT *
FROM Orders;
---View the Orders Table
SELECT OrderID
FROM Orders;
SELECT SUM(OrderAmount) AS TotalSales
FROM Orders;
----SUM() Example
SELECT AVG(OrderAmount) AS AverageOrder
FROM Orders;
---AVG() on Orders
SELECT COUNT(DISTINCT Country) AS UniqueCountries
FROM Orders;
SELECT COUNT(OrderID) AS TotalOrders,
    SUM(OrderAmount) AS TotalSales,
    AVG(OrderAmount) AS AverageSale
FROM Orders;