
with tt as (
    select machine_id, process_id, activity_type,
    round(timestamp - lag(timestamp) over(partition by machine_id, process_id order by timestamp),3)  as dif,
    count( process_id) over(partition by machine_id,process_id) as num_processes
from
    activity 
)
 select 
machine_id, round(sum(dif)/count(*),3) as processing_time 
from tt 
where tt.activity_type='end'
group by machine_id;
