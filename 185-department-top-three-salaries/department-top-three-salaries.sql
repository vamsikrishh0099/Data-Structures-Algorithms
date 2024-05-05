# Write your MySQL query statement below

# select emp.departmentId,  from Employee emp 
# inner join Department dp on emp.departmentId = dp.id 
# group by emp.departmentId ;

-- SELECT 
-- D.NAME AS Department,  E1.NAME AS EMPLOYEE, E1.Salary
-- FROM EMPLOYEE E1 INNER JOIN EMPLOYEE E2 ON E1.Salary <= E2.Salary AND
--  E1.DepartmentID = E2.DepartmentID JOIN Department D ON D.ID = E1.DepartmentID
--  GROUP BY D.NAME,E1.NAME HAVING COUNT(distinct E2.SALARY) < 4 
# using dense RANK 
# with temp as (
# select  emp.name as employee_name, dp.name, emp.salary, dense_rank() 
# over(partition by emp.departmentId order by emp.salary desc) as dept_rank  
# from Employee emp inner join Department dp on emp.departmentId = dp.id
# )
# select temp.name as Department, temp.employee_name as Employee,temp.salary as Salary 
# from temp where dept_rank <4;

# select tt.departmentId,tt.name as Employee, tt.s1
# from (
# select emp1.id,emp1.name,emp1.salary as s1,emp2.salary as s2,emp1.departmentId from Employee emp1 inner join Employee emp2 on emp1.salary < emp2.salary and emp1.departmentId = emp2.departmentId
# ) tt
# where count(distinct s2) < 3;

SELECT D.NAME AS DEPARTMENT,E1.NAME AS EMPLOYEE,E1.SALARY FROM EMPLOYEE E1 INNER JOIN EMPLOYEE E2 
ON E1.SALARY <= E2.SALARY AND E1.DepartmentID = E2.DepartmentID
INNER JOIN Department D ON E1.DepartmentID = D.ID 
GROUP BY D.NAME, E1.NAME HAVING COUNT(DISTINCT (E2.SALARY)) < 4 ; 


-- select d.name as department, e1.name as Employee, e1.salary
-- from employee e1 inner join department d on d.id = e1.departmentId 
-- inner join employee e2 on e1.departmentId = e2.departmentId and 
-- e1.salary <= e2.salary group by e1.name, e1.departmentId 
-- having count(distinct e2.salary) <= 3;





# select d.name as Department ,e1.name as Employee,e1.salary as Salary
# from Employee e1 inner join Department d on d.id = e1.departmentId inner join Employee e2
# on e1.departmentId = e2.departmentId and e1.salary <= e2.salary group by e1.name,e1.departmentId having count(distinct e2.salary) <= 3;

