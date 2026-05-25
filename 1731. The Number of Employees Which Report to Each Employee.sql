# Write your MySQL query statement below
WITH t AS (
    SELECT reports_to AS id,
        COUNT(reports_to) AS reports_count,
        ROUND(AVG(age), 0) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)

SELECT employee_id,
    name,
    reports_count,
    average_age
FROM Employees e
    JOIN t ON e.employee_id = t.id
GROUP BY employee_id
ORDER BY employee_id ASC