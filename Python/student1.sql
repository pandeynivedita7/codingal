CREATE TABLE IF NOT EXISTS STUDENT1 (
    YEAR INTEGER,
    SUBJECT TEXT,
    Address TEXT,
    COUNTRY TEXT,
    city TEXT,
    age INTEGER
);
INSERT INTO STUDENT1 (YEAR, SUBJECT, Address, COUNTRY, city, age)
VALUES (
        2024,
        'Computer Science',
        '123 MG Road',
        'India',
        'Mumbai',
        20
    );
INSERT INTO STUDENT1 (YEAR, SUBJECT, Address, COUNTRY, city, age)
VALUES (
        2024,
        'Computer Science',
        '123 MG Road',
        'India',
        'Mumbai',
        20
    );
SELECT *
FROM STUDENT1;