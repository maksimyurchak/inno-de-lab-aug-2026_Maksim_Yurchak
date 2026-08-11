-- Select total amount of orders for each customer
SELECT
	customer_id,
	order_id,
	item,
	amount,
	sum(amount) OVER (PARTITION BY customer_id) AS total_by_customer
FROM
	Orders;