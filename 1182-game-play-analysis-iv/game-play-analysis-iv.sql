-- Write your PostgreSQL query statement below
with first_login as (select * from (
select
*,
rank() over(partition by player_id order by event_date) as rnk
from activity 
) where rnk = 1
)
select round(count(distinct a.player_id)::numeric/(select count(distinct player_id) from activity),2) as fraction
 from first_login a 
join activity b on a.player_id = b.player_id and 
a.event_date = b.event_date - 1
