-- Write your PostgreSQL query statement below
with first_year as (
    select
    product_id,
    min(year) as yr
    from sales 
    group by product_id
)
select
    s.product_id,
    s.year as first_year,
    quantity as quantity,
    price as price
from sales s join first_year a 
on s.product_id = a.product_id and s.year = a.yr
