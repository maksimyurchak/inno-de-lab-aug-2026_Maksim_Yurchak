-- Select customers with at least 2 orders and delivery status = 'Delivered'
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    COUNT(o.customer_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM Customers AS c
INNER JOIN Shippings AS s
	ON c.customer_id = s.customer
INNER JOIN Orders AS o 
	ON c.customer_id = o.customer_id
WHERE s.status = 'Delivered'
GROUP BY c.first_name, c.last_name, c.country
HAVING COUNT(o.customer_id) > 1;