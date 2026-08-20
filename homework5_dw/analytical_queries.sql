-- Calculate revenue for July 2026
SELECT 
    SUM(f.line_total) AS total_revenue
FROM Fact_sales AS f
	JOIN dim_date AS d
	ON f.date_sk = d.date_sk
	WHERE d.year = 2026 
	AND d.month = 'July';


-- Calculate revenue for vet specialised in MRI for 2025
SELECT 
    SUM(f.line_total) AS total_revenue
FROM Fact_sales AS f
JOIN dim_vet AS v ON f.vet_sk = v.vet_sk
JOIN dim_specialisation AS s ON v.specialisation_sk = s.specialisation_sk
JOIN dim_date d ON f.date_sk = d.date_sk
WHERE s.specialisation_name = 'MRI'
  AND d.year = 2025;


--Select min and max price of an appointment in July 2026
WITH appointment_totals AS (
    SELECT 
        f.bill_sk,
        SUM(f.line_total) AS total_appointment_price
    FROM Fact_sales AS f
    JOIN dim_date AS d ON f.date_sk = d.date_sk
    WHERE d.year = 2026 
    AND d.month = 'July'
    GROUP BY f.bill_sk
)
SELECT 
    MIN(total_appointment_price) AS min_appointment_price,
    MAX(total_appointment_price) AS max_appointment_price
FROM appointment_totals;


--Select the most profitable day of the week in July 2026
SELECT 
    d.day_of_week,
    SUM(f.line_total) AS total_revenue
FROM Fact_sales AS f
    JOIN dim_date AS d ON f.date_sk = d.date_sk
    WHERE d.year = 2026 
    AND d.month = 'July' 
    GROUP BY d.day_of_week
    ORDER BY total_revenue DESC
    LIMIT 1;
