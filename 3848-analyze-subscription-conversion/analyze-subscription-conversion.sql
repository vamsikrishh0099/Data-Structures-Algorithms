-- Write your PostgreSQL query statement below
WITH PAID_USERS AS (
SELECT 
distinct USER_ID AS USER_ID
FROM USERACTIVITY UA WHERE ACTIVITY_TYPE = 'paid'
)
SELECT 
PU.USER_ID,
round(avg(CASE WHEN ACTIVITY_TYPE = 'free_trial' then activity_duration else null end ),2) as trial_avg_duration,
round(avg(CASE WHEN ACTIVITY_TYPE = 'paid' then activity_duration else null end ),2) as paid_avg_duration
FROM PAID_USERS PU INNER JOIN USERACTIVITY UA ON 
PU.USER_ID = UA.USER_ID 
GROUP BY PU.USER_ID 
