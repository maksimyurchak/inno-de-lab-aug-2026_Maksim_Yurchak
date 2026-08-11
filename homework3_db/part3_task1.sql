-- Select number of customers by country
SELECT
	country,
	count(*) AS number_of_customers
FROM
	Customers
GROUP BY country;