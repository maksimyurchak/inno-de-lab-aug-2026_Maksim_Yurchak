-- Select number of orders and average amount for item
SELECT
	item,
	count(*) AS number_of_orders,
	avg(amount) AS average_amount
FROM
	Orders
GROUP BY item;