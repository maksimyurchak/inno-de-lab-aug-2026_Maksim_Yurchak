-- Create function for calculating bonus
CREATE OR REPLACE FUNCTION CalculateAnnualBonus(employee_id INT, Salary NUMERIC)
RETURNS NUMERIC 
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN Salary * 1.10;
END;
$$

-- Using function to show bonus for employees
SELECT firstname, lastname, salary, CalculateAnnualBonus(employeeid, Salary) AS bonus
FROM Employees;

-- Create view showing EmployeeID, FirstName, LastName, Salary from IT department
CREATE OR REPLACE VIEW IT_Department_View AS 
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE department = 'IT';

-- Get data from the view IT_Department_View
SELECT * FROM IT_Department_View;