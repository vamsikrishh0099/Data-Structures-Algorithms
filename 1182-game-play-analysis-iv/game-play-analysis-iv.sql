-- Write your PostgreSQL query statement below
WITH TT AS (
    SELECT 
        a.player_id, 
        A.EVENT_DATE,
        B.EVENT_DATE AS NEXT_DATE,
        RANK() OVER(PARTITION BY A.PLAYER_ID ORDER BY A.EVENT_DATE) AS RNK
    FROM ACTIVITY A left JOIN ACTIVITY B 
    ON A.PLAYER_ID = B.PLAYER_ID AND A.EVENT_DATE = B.EVENT_DATE - 1
)
SELECT 
    round((sum(case when next_date is null then 0 else 1 end)*1.0)/(select count(distinct player_id) from activity),2) as fraction
FROM TT WHERE RNK = 1