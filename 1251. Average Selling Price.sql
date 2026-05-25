# Write your MySQL query statement below
WITH t AS (
    SELECT p.product_id,
        purchase_date,
        units,
        units * price AS profit
    FROM Prices p LEFT JOIN UnitsSold us
        ON p.product_id = us.product_id AND
        purchase_date BETWEEN start_date AND end_date
    UNION
    SELECT p.product_id,
        purchase_date,
        units,
        units * price AS profit
    FROM Prices p RIGHT JOIN UnitsSold us
        ON p.product_id = us.product_id AND
        purchase_date BETWEEN start_date AND end_date
)

SELECT product_id,
    IFNULL(ROUND(SUM(profit) / SUM(units), 2), 0) AS average_price
FROM t
GROUP BY product_id