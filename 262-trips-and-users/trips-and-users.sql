-- Write your PostgreSQL query statement below


SELECT
    REQUEST_AT as "Day",
    round(COUNT(CASE WHEN T.STATUS ILIKE 'cancelled_%' then 1 else null end)::numeric/count(*),2) as 
    "Cancellation Rate"
FROM TRIPS T JOIN USERS UC
    ON T.CLIENT_ID = UC.USERS_ID
    JOIN USERS UD ON 
    T.DRIVER_ID = UD.USERS_ID 
WHERE 
    REQUEST_AT::DATE BETWEEN '2013-10-01' and '2013-10-03'
    AND UC.BANNED = 'No' AND UD.BANNED = 'No'
GROUP BY 
    REQUEST_AT 