# Write your MySQL query statement below





# SELECT PRODUCT_ID, YEAR AS FIRST_YEAR, QUANTITY, PRICE FROM SALES WHERE 
# (PRODUCT_ID,YEAR) IN (SELECT PRODUCT_ID, MIN(YEAR) AS FIRST_YEAR FROM SALES GROUP BY PRODUCT_ID
# )


SELECT TT.PRODUCT_ID, TT.YEAR AS FIRST_YEAR, TT.QUANTITY, TT.PRICE FROM (
SELECT *, RANK() OVER(PARTITION BY S1.PRODUCT_ID ORDER BY S1.YEAR) AS YEAR_RANK FROM SALES S1
) TT
WHERE TT.YEAR_RANK = 1;
