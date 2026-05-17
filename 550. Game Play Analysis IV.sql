# Write your MySQL query statement below
WITH t AS (
    SELECT player_id,
    ADDDATE(MIN(event_date), INTERVAL 1 DAY) AS first_login
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(*) / (
    SELECT COUNT(DISTINCT Activity.player_id)
    FROM Activity
), 2) AS fraction
FROM Activity JOIN t ON (
    Activity.player_id = t.player_id AND
    Activity.event_date = t.first_login
)