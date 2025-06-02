-- Write your PostgreSQL query statement below
delete from person 
where id in (
    select id from (
    select id, rank() over(partition by email order by id) as rnk 
    from person
    ) where rnk > 1
)