-- Create new user hr_user
CREATE USER hr_user WITH PASSWORD 'not123';

-- Give permission to hr_user on SELECT in table Employess
GRANT SELECT ON Employees TO hr_user;

-- Give permission to hr_user on INSERT and UPDATE in table Employess
GRANT INSERT, UPDATE ON Employees TO hr_user;
-- Give permission to hr_user on auto increment in table Employess
GRANT USAGE, SELECT ON SEQUENCE employees_employeeid_seq TO hr_user;