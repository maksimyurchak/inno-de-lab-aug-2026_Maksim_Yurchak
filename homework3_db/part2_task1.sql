-- Select orders with name of customer
SELECT
	c.first_name,
	c.last_name ,
	o.item,
	o.amount
FROM
	Orders AS o
INNER JOIN Customers AS c
	ON o.customer_id = c.customer_id;