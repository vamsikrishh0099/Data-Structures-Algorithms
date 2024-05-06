# Write your MySQL query statement below
WITH CTE1 AS (
select BUYER_ID,P.PRODUCT_ID,P.PRODUCT_NAME FROM SALES S JOIN PRODUCT P ON S.PRODUCT_ID = P.PRODUCT_ID
),
 cte2 as (
SELECT c1.BUYER_ID FROM CTE1 c1 WHERE c1.PRODUCT_NAME = 'S8'
),
cte3 as (
SELECT c1.BUYER_ID FROM CTE1 c1 WHERE c1.PRODUCT_NAME = 'iPhone'
)
select distinct cte2.buyer_id from cte2 left join cte3 
on cte2.BUYER_ID = cte3.BUYER_ID
where cte3.BUYER_ID is null;