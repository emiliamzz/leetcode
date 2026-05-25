# Write your MySQL query statement below
WITH t AS (
    SELECT salary,
        departmentId,
        name,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS ranking
    FROM Employee
)

SELECT d.name AS Department,
    t.name AS Employee,
    salary AS Salary
FROM t JOIN Department d
    ON departmentId = d.id
WHERE ranking <= 3