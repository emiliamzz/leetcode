# Write your MySQL query statement below
WITH s AS (
    SELECT machine_id,
        process_id,
        timestamp AS start
    FROM Activity
    WHERE activity_type = 'start'
    GROUP BY machine_id,
        process_id
),

e AS (
    SELECT machine_id,
        process_id,
        timestamp AS end
    FROM Activity
    WHERE activity_type = 'end'
    GROUP BY machine_id,
        process_id
)

SELECT s.machine_id,
    ROUND(AVG(end - start), 3) AS processing_time
FROM s JOIN e
    ON s.machine_id = e.machine_id AND
        s.process_id = e.process_id
GROUP BY s.machine_id