-- Increase salary of HR department by 10%
UPDATE Employees
SET salary = salary * 1.10
WHERE department = 'HR';

-- Change department of emloyee to Senior IT if salary more than 70000
UPDATE Employees
SET department = 'Senior IT'
WHERE salary > 70000.00;

-- Delete employee if they do not have any project in table EmployeeProjects
DELETE FROM Employees AS e
WHERE NOT EXISTS (
    SELECT *
    FROM EmployeeProjects AS ep 
    WHERE e.employeeid = ep.employeeid
);

/* 
Create transaction where we add one new project and assign
two existing employees to it
*/
BEGIN;

WITH inserted AS (
	INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate) VALUES
	('Database support', 10000.99, '2026-07-01', '2026-08-01')
	RETURNING ProjectID
)

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
	SELECT 1, ProjectID, 101 FROM inserted
	UNION ALL
	SELECT 4, ProjectID, 99 FROM inserted;

COMMIT; 
