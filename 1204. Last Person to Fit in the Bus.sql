# Write your MySQL query statement below
WITH t AS (
    SELECT person_name,
    SUM(weight) OVER (ORDER BY turn) AS w
    FROM Queue
)

SELECT person_name
FROM t
WHERE w <= 1000
ORDER BY w DESC
LIMIT 1