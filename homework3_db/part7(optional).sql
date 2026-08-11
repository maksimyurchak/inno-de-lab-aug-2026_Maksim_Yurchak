-- Select customers with at least 2 orders and delivery status = 'Delivered'
WITH pre_table AS (
SELECT 
	CONCAT(c.first_name, ' ', c.last_name) AS full_name,
	c.country,
	(SELECT count(*) AS total_orders
	FROM Orders AS o
	WHERE o.customer_id = c.customer_id),
	(SELECT sum(amount) AS total_amount
	FROM Orders AS o
	WHERE o.customer_id = c.customer_id)
FROM Customers AS c
INNER JOIN Shippings AS s
	ON c.customer_id = s.customer 
WHERE s.status = 'Delivered'
)
SELECT *
FROM pre_table
WHERE total_orders > 1;
