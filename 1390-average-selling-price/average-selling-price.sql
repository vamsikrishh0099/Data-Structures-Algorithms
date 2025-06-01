-- Write your PostgreSQL query statement below
WITH TT AS (
SELECT 
P.PRODUCT_ID, 
P.PRICE, 
US.UNITS AS UNITS
FROM PRICES P LEFT JOIN UNITSSOLD US 
    ON P.PRODUCT_ID = US.PRODUCT_ID AND US.PURCHASE_DATE BETWEEN P.START_DATE AND P.END_DATE
)
--select * from tt; 
SELECT 
    tt.product_id, 
    coalesce(round((sum(tt.units*tt.price)/(sum(tt.units)*1.0)),2), 0) as average_price
FROM TT 
    GROUP BY TT.PRODUCT_ID