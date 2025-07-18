-- Write your PostgreSQL query statement below
SELECT
    P.PRODUCT_ID,
    P.PRODUCT_NAME
FROM SALES S JOIN PRODUCT P ON S.PRODUCT_ID = P.PRODUCT_ID
    GROUP BY P.PRODUCT_ID, P.PRODUCT_NAME
    HAVING MIN(SALE_DATE) BETWEEN '2019-01-01' AND '2019-03-31' AND 
    MAX(SALE_DATE) BETWEEN '2019-01-01' AND '2019-03-31'