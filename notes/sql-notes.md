# SQL Notes

## What is SQL?
- SQL stands for Structured Query Language
- Used to manage databases
- Used to store, retrieve and update data

## Basic Commands
```sql
-- Create a table
CREATE TABLE students (
  id INT,
  name VARCHAR(50),
  age INT
);

-- Insert data
INSERT INTO students VALUES (1, 'Amalsha', 22);

-- Select all data
SELECT * FROM students;

-- Select specific columns
SELECT name, age FROM students;

-- Filter data
SELECT * FROM students WHERE age > 20;

-- Update data
UPDATE students SET age = 23 WHERE name = 'Amalsha';

-- Delete data
DELETE FROM students WHERE id = 1;

-- Sort data
SELECT * FROM students ORDER BY age DESC;

-- Count rows
SELECT COUNT(*) FROM students;
```

## Joins
```sql
-- Inner Join
SELECT * FROM students
INNER JOIN courses ON students.id = courses.student_id;

-- Left Join
SELECT * FROM students
LEFT JOIN courses ON students.id = courses.student_id;
```

## Useful Functions
- COUNT() → count rows
- SUM() → add values
- AVG() → average value
- MAX() → highest value
- MIN() → lowest value