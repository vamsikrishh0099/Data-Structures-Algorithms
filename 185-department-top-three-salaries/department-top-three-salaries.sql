-- Write your PostgreSQL query statement below
with ranked as (select
e.id, 
e.name, 
e.departmentid,
e.salary,
d.name as dname,
dense_rank() over(partition by departmentid order by salary desc) as rnk
from employee e
join department d on e.departmentid = d.id
)
select
    dname as "Department",
    name as "Employee",
    salary
 from ranked where rnk <= 3