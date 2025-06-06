-- Write your PostgreSQL query statement below
-- first filter rows with people >= 100.
-- create rank column order by id, visit date, 
-- find diff of id - rank 
-- this diff should be same for consecutive rows. 
-- group by diff column having count(*) > 2 and get distinct diffs 
-- filter for rwos with diff in (above result)

WITH RANKED_STADIUM AS (
SELECT
*, RANK() OVER(ORDER BY ID, VISIT_DATE) AS RNK
FROM STADIUM WHERE PEOPLE >= 100 
),
DIFFED AS (
SELECT
*, ID - RNK AS DIFF 
FROM RANKED_STADIUM
),
DIFFS_TO_INCLUDE AS (
SELECT 
DIFF
FROM DIFFED GROUP BY DIFF HAVING COUNT(DISTINCT ID) > 2
)
SELECT 
ID,VISIT_DATE,PEOPLE FROM DIFFED WHERE DIFF IN (SELECT DIFF FROM DIFFS_TO_INCLUDE)