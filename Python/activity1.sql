--  CREATE TABLE Salesman(
--   Salesman_id INT PRIMARY KEY,
--   name TEXT,
--   city TEXT,
--   Comission TEXT
-- );
-- INSERT INTO Salesman(Salesman_id,name,city,Comission)
-- VALUES
--   ("5001","James Hoog","New York","0.15"),
--   ("5002","Nail Knite","Paris","0.13"),
--   ("5005","Pit Alex","London","0.11"),
--   ("5006","Mc Lyon","Paris","0.14"),
--   ("5007","Paul Adam","Rome","0.13"),
--   ("5003","Lauson Hen","San Jose","0.12");
-- SELECT * FROM Salesman;
-- CREATE TABLE IF NOT EXISTS Orders(
--   ord_no TEXT PRIMARY KEY,
--   purch_amt TEXT,
--   ord_date TEXT,
--   customer_id TEXT,
--   Salesman_id TEXT
-- );
-- INSERT INTO Orders(ord_no,purch_amt,ord_date,customer_id,Salesman_id)
-- VALUES
--   ("70001","150.5","2012-10-05","3005","5002"),
--   ("70009","270.65","2012-09-10","3001","5001"),
--   ("70002","65.26","2012-10-05","3002","5003"),
--   ("70004","110.5","2012-08-17","3009","5007"),
--   ("70007","948.5","2012-09-10","3005","5005"),
--   ("70005","2400.6","2012-07-27","3007","5006");
-- SELECT * FROM Orders;
--   SELECT * FROM Orders
-- WHERE Salesman_id= (SELECT Salesman_id FROM Salesman WHERE city = 'London')
-- Creating tables
CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT,
    Commission REAL
);
CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    ord_date DATE,
    customer_id TEXT,
    Salesman_id INTEGER,
    FOREIGN KEY (Salesman_id) REFERENCES Salesman(Salesman_id)
);
-- Inserting data into Salesman
INSERT INTO Salesman
VALUES (5001, 'James Hoog', 'New York', 0.15),
    (5002, 'Nail Knite', 'Paris', 0.13),
    (5005, 'Pit Alex', 'London', 0.11),
    (5006, 'Mc Lyon', 'Paris', 0.14),
    (5007, 'Paul Adam', 'Rome', 0.13),
    (5003, 'Lauson Hen', 'San Jose', 0.12);
-- Inserting data into Orders
INSERT INTO Orders
VALUES ('70001', 150.5, '2012-10-05', '3005', 5002),
    ('70009', 270.65, '2012-09-10', '3001', 5001),
    ('70002', 65.26, '2012-10-05', '3002', 5003),
    ('70004', 110.5, '2012-08-17', '3009', 5007),
    ('70007', 948.5, '2012-09-10', '3005', 5005),
    ('70005', 2400.6, '2012-07-27', '3007', 5006);
-- Query to display Salesman
SELECT *
FROM Salesman;
-- Query to display Orders
SELECT *
FROM Orders;
-- Query to find Orders from Salesman in London
SELECT *
FROM Orders
WHERE Salesman_id IN (
        SELECT Salesman_id
        FROM Salesman
        WHERE city = 'London'
    );