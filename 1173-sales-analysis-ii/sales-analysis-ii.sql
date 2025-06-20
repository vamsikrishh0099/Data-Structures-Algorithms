-- Write your PostgreSQL query statement below
WITH TT AS (
    SELECT
    P.PRODUCT_ID, 
    P.PRODUCT_NAME,
    S.BUYER_ID
    FROM SALES S JOIN PRODUCT P 
    ON S.PRODUCT_ID = P.PRODUCT_ID 
    WHERE P.PRODUCT_NAME IN ('S8', 'iPhone')
)
SELECT
    DISTINCT BUYER_ID
FROM TT WHERE PRODUCT_NAME = 'S8' 
 AND BUYER_ID NOT IN (
    SELECT BUYER_ID FROM TT WHERE PRODUCT_NAME = 'iPhone'
 )
