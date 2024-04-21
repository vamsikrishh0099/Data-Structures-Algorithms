# Write your MySQL query statement below



select tt.id, sum(tt.friends) as num from
(
select
r1.requester_id as id, count(distinct r1.accepter_id) as friends
from requestaccepted r1 group by r1.requester_id
union all
select
r1.accepter_id as id, count(distinct r1.requester_id) as friends
from requestaccepted r1 group by r1.accepter_id
) tt group by tt.id order by sum(tt.friends) desc limit 1;


