-- Write your PostgreSQL query statement below
WITH TT AS (
    SELECT 
        S.USER_ID, C.USER_ID AS C_USER_ID, C.ACTION
    FROM SIGNUPS S LEFT JOIN CONFIRMATIONS C 
        ON S.USER_ID = C.USER_ID 
)
SELECT 
    USER_ID, 
    coalesce(Round(SUM(CASE WHEN ACTION = 'confirmed' then 1 else 0 end)/(count(*)*1.0), 2), 0) as confirmation_rate
FROM TT GROUP BY USER_ID