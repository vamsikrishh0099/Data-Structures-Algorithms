-- Write your PostgreSQL query statement below
-- Write your PostgreSQL query statement below
-- Write your PostgreSQL query statement below
With cte as
(select
    policy_id,
    state,
    fraud_score,
    percent_rank() over(partition by state order by fraud_score desc) pct_rank
from Fraud)
select
    policy_id,
    state,
    fraud_score
from cte
where pct_rank<= 0.05
order by state, fraud_score desc, policy_id