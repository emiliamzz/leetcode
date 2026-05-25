# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP '^[:alpha:][a-z|A-Z|0-9|_|.|-]*@(?-i)leetcode[.]com$'