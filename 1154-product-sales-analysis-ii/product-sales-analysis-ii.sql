-- Write your PostgreSQL query statement below
WITH TT AS (
SELECT 
p.product_id, s.quantity
FROM PRODUCT P JOIN SALES S
    ON P.PRODUCT_ID = S.PRODUCT_ID 
)
select 
    product_id, coalesce(sum(quantity), 0) as total_quantity
from tt group by product_id

