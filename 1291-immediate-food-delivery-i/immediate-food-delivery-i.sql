-- Write your PostgreSQL query statement below
with tt as (
select *,
    case when order_date = customer_pref_delivery_date then 'immediate' else 'scheduled' end as order_type
    from delivery
)
SELECT 
ROUND((SUM(CASE WHEN ORDER_TYPE = 'immediate' THEN 1 ELSE 0 END)*100.0)/COUNT(*), 2) AS immediate_percentage
FROM TT