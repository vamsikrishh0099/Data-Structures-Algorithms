-- Write your PostgreSQL query statement below
-- WITH LAST_6_DAYS AS (
--     SELECT DISTINCT VISITED_ON AS DT
--     FROM CUSTOMER ORDER BY VISITED_ON OFFSET 6
-- )
-- SELECT
-- A.DT AS VISITED_ON, 
-- SUM(B.AMOUNT) AS AMOUNT,
-- ROUND((SUM(B.AMOUNT)*1.0)/(7),2) AS AVERAGE_AMOUNT
-- FROM LAST_6_DAYS A JOIN CUSTOMER B ON 
--   B.VISITED_ON between a.dt -6 and a.dt
-- GROUP BY A.DT

with day_sum as (
    select
    visited_on, 
    sum(amount) as total
    from customer group by visited_on 
    order by visited_on
)
select
visited_on, 
sum(total) over(rows between 6 preceding and current row) as amount,
round(avg(total) over(rows between 6 preceding and current row),2) as average_amount
from day_sum 
order by visited_on offset 6