-- Write your PostgreSQL query statement below
-- select
-- name as Customers
-- from customers 
-- where id not in (
--     select customerid from orders
-- )

select
c.name as "Customers"
from customers c left join orders o 
on c.id = o.customerid where o.customerid is null