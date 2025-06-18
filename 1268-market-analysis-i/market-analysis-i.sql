-- Write your PostgreSQL query statement below
SELECT
    U.USER_ID AS BUYER_ID,
    U.JOIN_DATE,
    COALESCE(COUNT(case when extract(year from o.order_date) = 2019 then 1 else null end), 0) AS orders_in_2019
FROM USERS U LEFT JOIN ORDERS O ON U.USER_ID = O.BUYER_ID 
GROUP BY U.USER_ID, U.JOIN_DATE
