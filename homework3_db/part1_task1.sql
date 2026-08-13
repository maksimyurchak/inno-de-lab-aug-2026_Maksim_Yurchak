-- Select all customers from USA and older 25 years old
SELECT
	first_name,
	last_name,
	age,
	country
FROM
	Customers
WHERE
	country = 'USA' AND age > 25;