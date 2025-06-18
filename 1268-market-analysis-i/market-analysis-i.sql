-- Write your PostgreSQL query statement below
SELECT
    U.USER_ID AS BUYER_ID,
    u.JOIN_DATE,
    COALESCE(COUNT(o.order_id), 0) AS orders_in_2019
FROM USERS U LEFT JOIN ORDERS O ON U.USER_ID = O.BUYER_ID 
and EXTRACT(YEAR FROM O.ORDER_DATE) = '2019' 
GROUP BY U.USER_ID,u.join_date