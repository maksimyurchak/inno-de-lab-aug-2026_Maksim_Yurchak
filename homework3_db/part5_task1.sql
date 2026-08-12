-- Select customers with max orders amount
SELECT
	c.first_name,
	c.last_name , 
	o.amount AS max_amount
FROM Customers AS c
INNER JOIN Orders AS o
	ON c.customer_id = o.customer_id 
WHERE o.amount = (
	SELECT max(amount) FROM Orders
	WHERE c.customer_id = o.customer_id
);
