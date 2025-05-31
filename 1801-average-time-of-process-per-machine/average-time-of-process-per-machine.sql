-- Write your PostgreSQL query statement below

-- SELECT
-- A1.MACHINE_ID,
-- ROUND(AVG(A2.TIMESTAMP - A1.TIMESTAMP)::DECIMAL, 3) AS PROCESSING_TIME
-- FROM ACTIVITY A1 JOIN ACTIVITY A2 
-- ON A1.MACHINE_ID = A2.MACHINE_ID AND A1.PROCESS_ID = A2.PROCESS_ID AND A1.ACTIVITY_TYPE = 'start'
-- AND A2.ACTIVITY_TYPE = 'end'
-- group by A1.MACHINE_ID


SELECT
MACHINE_ID,
round((SUM(CASE WHEN ACTIVITY_TYPE='start' then -timestamp else timestamp end)/(count(distinct process_id)))::decimal,3) as processing_time
FROM ACTIVITY 
GROUP BY MACHINE_ID