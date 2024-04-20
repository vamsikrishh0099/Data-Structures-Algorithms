# Write your MySQL query statement below

-- select 
-- s.user_id, sum(case when c.user_id = 'confirmed' then 1 else 0 end)/count(*) as confirmation_rate
-- from CONFIRMATIONS c right outer join signups s 
-- on c.user_id = s.user_id 
-- group by s.user_id

select s.user_id, IFNULL(TT.CR,0) AS CONFIRMATION_RATE from signups s left join (
select 
c.user_id, ROUND(sum(case when c.action = 'confirmed' then 1 else 0 end)/count(*),2) as cr 
from CONFIRMATIONS c 
group by c.user_id 
) tt on s.user_id = tt.user_id 


# select tt.user_id,sum(case when tt.action = 'confirmed' then 1 else 0 end)/count(*) as 'confirmation_rate'
# from 
# (SELECT c.user_id, c.action,
# (CASE WHEN c.ACTION = 'confirmed' then 1 else 0 end ) as 'rate'
# FROM CONFIRMATIONS c right join signups on signups.user_id = c.user_id ORDER BY c.USER_ID,c.TIME_STAMP) tt group by tt.user_id;


-- select tt.user_id,round(sum(case when tt.action = 'confirmed' then 1 else 0 end)/count(*),2) as 'confirmation_rate'
--  from 
-- (SELECT signups.user_id, c.action,
-- (CASE WHEN c.ACTION = 'confirmed' then 1 else 0 end ) as 'rate'
-- FROM signups left join CONFIRMATIONS c on signups.user_id = c.user_id ORDER BY c.USER_ID,c.TIME_STAMP) tt group by tt.user_id;