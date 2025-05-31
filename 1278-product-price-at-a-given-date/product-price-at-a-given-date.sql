-- Write your PostgreSQL query statement below
WITH TT AS (
SELECT 
PRODUCT_ID, new_price, rank() over (partition by product_id order by change_date desc) as rnk 
FROM PRODUCTS WHERE CHANGE_DATE <= '2019-08-16'
),
t2 as (
    select * from tt where rnk = 1
)
SELECT P.PRODUCT_ID, COALESCE(t2.NEW_PRICE, 10) AS PRICE FROM (select distinct product_id as product_id from PRODUCTS) P 
LEFT JOIN t2 ON P.PRODUCT_ID = t2.PRODUCT_ID
