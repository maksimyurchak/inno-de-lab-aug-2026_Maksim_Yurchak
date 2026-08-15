--Find all projects where Bob Johnson worked more than 150 hours
SELECT projectname 
FROM projects AS p
	INNER JOIN employeeprojects AS ep
	ON p.projectid = ep.projectid 
    INNER JOIN employees AS e 
	ON ep.employeeid = e.employeeid
WHERE 
	e.firstname = 'Bob'
	AND e.lastname = 'Johnson'
	AND ep.hoursworked > 150;
	
-- Increase budget of project if at least one of the employees from IT
UPDATE projects
SET budget = budget * 1.10
FROM employeeprojects AS ep
	INNER JOIN employees AS e
	ON ep.employeeid  = e.employeeid
WHERE
	projects.projectid = ep.projectid 
	AND 
	e.department IN ('Senior IT');

-- For every EndDate without date set EndDate = StartDate + 1 year
UPDATE projects 
SET enddate = (startdate + INTERVAL '1 year')::date 
WHERE enddate IS NULL 




/* Create a transaction where we add new employee and assing them
 to Website Redesign project with 80 worked hours
*/

BEGIN; 

WITH inserted AS (
  INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
  ('Susan', 'Garsia', 'IT', 80000.00)
  RETURNING EmployeeID
)

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT
	EmployeeID,
	1,
	80
FROM inserted;

COMMIT; 
