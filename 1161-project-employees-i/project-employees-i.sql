# Write your MySQL query statement below

select p.project_id, round(sum(IFNULL(e.experience_years,0))/count(distinct(p.employee_id)),2) as average_years from project p 
left join employee e on p.employee_id = e.employee_id where e.experience_years is not null
group by p.project_id