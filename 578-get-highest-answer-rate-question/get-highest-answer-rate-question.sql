# Write your MySQL query statement below
select 
question_id as survey_log
from surveylog group by question_id 
order by (sum(case when action = 'answer' then 1 else 0 end)*1.0)/sum(case when action = 'show' then 1 else 0 end)
 desc, question_id asc limit 1;