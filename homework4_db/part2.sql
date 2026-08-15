-- Create table Departments 
CREATE TABLE Departments (
DepartmentID SERIAL PRIMARY KEY, 
DepartmentName VARCHAR(50) UNIQUE NOT NULL,
Location VARCHAR(50)
);

-- Add new column to table employees
ALTER TABLE employees ADD COLUMN Email VARCHAR(100);

-- Add email for all employees in table Employees
UPDATE employees
SET Email = 'Bob@gmail.com'
WHERE firstname = 'Bob';

UPDATE employees
SET Email = 'Charlie@gmail.com'
WHERE firstname = 'Charlie';

UPDATE employees
SET Email = 'Diana@gmail.com'
WHERE firstname = 'Diana';

UPDATE employees
SET Email = 'Rick@gmail.com'
WHERE firstname = 'Rick';

UPDATE employees
SET Email = 'Lara@gmail.com'
WHERE firstname = 'Lara';

UPDATE employees
SET Email = 'Alice@gmail.com'
WHERE firstname = 'Alice';

-- Add constraint UNIQUE for email in table Employees
ALTER TABLE employees ADD CONSTRAINT unique_email UNIQUE (email);

-- Rename column Location to OfficeLocation in table Departments
ALTER TABLE Departments RENAME COLUMN Location TO OfficeLocation;

