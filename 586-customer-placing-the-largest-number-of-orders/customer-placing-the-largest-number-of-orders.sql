

-- Write your PostgreSQL query statement below


select 
customer_number 
from orders o 
group by customer_number order by count(*) desc limit 1 