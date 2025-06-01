-- Write your PostgreSQL query statement below

SELECT 
name, bonus as bonus
FROM EMPLOYEE E LEFT JOIN BONUS B 
ON E.EMPID = B.EMPID 
WHERE bonus < 1000 or bonus is null