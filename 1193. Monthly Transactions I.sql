-- Write your PostgreSQL query statement below
SELECT to_char(trans_date, 'YYYY-MM') AS month,
    country,
    COUNT(id) AS trans_count,
    COUNT(CASE state WHEN 'approved' THEN 1 ELSE NULL END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE state WHEN 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month,
    country