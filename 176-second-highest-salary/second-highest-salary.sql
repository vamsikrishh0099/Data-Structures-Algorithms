-- Write your PostgreSQL query statement below

-- SELECT 
-- MAX(E1.SALARY)
-- FROM EMPLOYEE E1 JOIN EMPLOYEE E2 
--     ON E1.SALARY < E2.SALARY 
    
SELECT
  (SELECT DISTINCT Salary
     FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1) AS SecondHighestSalary;
