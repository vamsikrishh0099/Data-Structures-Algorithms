# Write your MySQL query statement below

with cte as (
select product_id, new_price, rank() over(partition by product_id order by change_date desc) as rnk 
 from PRODUCTS 
WHERE change_date <= '2019-08-16'
)
select product_id, new_price as price from cte where rnk = 1 
union
select product_id, 10 as price from products 
group by product_id having min(change_date) > '2019-08-16'
# select ttt3.product_id, ifnull(tt2.new_price,10) as price from 
# (
# select tt.product_id, tt.new_price, tt.change_date, tt.rnk
# from(
# select *,rank() over(partition by product_id order by change_date desc) as rnk from products where datediff(change_date,"2019-08-16") <=0
# ) tt 
#  where tt.rnk = 1
# ) tt2
# right join (select distinct product_id  from products) ttt3
# on ttt3.product_id = tt2.product_id;










-- select x2.product_id, ifnull(tt.price,10) as price
-- from (select distinct product_id from products) x2
-- left join
-- (
--  SELECT DISTINCT
--       product_id,
--       FIRST_VALUE (new_price) OVER (
--         PARTITION BY
--           product_id
--         ORDER BY
--           change_date DESC
--       ) AS price
--     FROM
--       Products
--        WHERE
--       change_date <= '2019-08-16'
-- ) tt
-- on tt.product_id = x2.product_id;
