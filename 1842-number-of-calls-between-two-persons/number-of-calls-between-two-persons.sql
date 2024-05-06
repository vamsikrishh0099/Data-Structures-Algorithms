# Write your MySQL query statement below
with cte as (
select 
case when from_id < to_id then from_id 
else to_id 
end as first_user,
case when from_id > to_id then from_id 
else to_id 
end as to_user,
duration
from calls
)
select first_user as person1, to_user as person2, count(*) as call_count, sum(duration) as total_duration
from cte group by first_user,to_user;