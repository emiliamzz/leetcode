-- Write your PostgreSQL query statement below
SELECT MAX(num) AS num
FROM (
    SELECT num,
    COUNT(num) AS count
    FROM MyNumbers
    GROUP BY num
) WHERE count = 1