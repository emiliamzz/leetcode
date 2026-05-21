# Write your MySQL query statement below
SELECT (
    SELECT salary
    FROM Employee
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary