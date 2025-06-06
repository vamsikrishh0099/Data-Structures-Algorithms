-- Write your PostgreSQL query statement below
with first_login as (
    select
    *, rank() over(partition by user_id order by activity_date) as rnk 
    from traffic where activity = 'login'
)
SELECT
activity_date as login_date,
count(distinct user_id) as user_count
FROM first_login
WHERE rnk = 1
  AND '2019-06-30'::date - activity_date <= 90
  group by activity_date
