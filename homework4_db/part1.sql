-- Insert two new employees
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Rick', 'Brown', 'Finance', 37000.00),
('Lara', 'Simpson', 'Engineering', 105000.00);

-- Select all employees from table Employees
SELECT * FROM Employees;

-- Select first and last name of employees from IT department
SELECT FirstName, LastName
FROM Employees
WHERE Department = 'IT';

-- Update Salary for Alice Smith to 65000.00
UPDATE Employees 
SET salary = 65000.00
WHERE firstname = 'Alice' AND lastname = 'Smith';

-- Delete employee Eve Davis
DELETE from Employees 
WHERE firstname = 'Eve' AND lastname = 'Davis';

-- Check final changes
SELECT * FROM Employees;

