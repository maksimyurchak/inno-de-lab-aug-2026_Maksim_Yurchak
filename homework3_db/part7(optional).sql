-- Select customers with at least 2 orders and delivery status = 'Delivered'
SELECT 
    CONCAT(c.first_name, ' ', c.last_name) AS full_name,
    c.country,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM Customers AS c
INNER JOIN Shippings AS s
	ON c.customer_id = s.customer
INNER JOIN Orders AS o 
	ON c.customer_id = o.customer_id
WHERE s.status = 'Delivered'
GROUP BY c.customer_id
HAVING COUNT(o.order_id) > 1;