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
	JOIN dim_date AS d ON f.date_sk = d.date_sk
	WHERE d.year = 2025
	AND v.vet_specialisation = 'MRI';

--Select min and max price of an appointment in July 2026
WITH AppointmentPrices AS (
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
FROM AppointmentPrices;