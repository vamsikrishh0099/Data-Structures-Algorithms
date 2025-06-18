WITH add_rank AS (
    SELECT id, company, salary,
           ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary) AS rnk,
           COUNT(id) OVER (PARTITION BY company) AS total_ppl
    FROM Employee
)
SELECT id, company, salary
FROM add_rank
WHERE rnk IN (
    FLOOR((total_ppl + 1)::float / 2)::integer,
    CEIL((total_ppl + 1)::float / 2)::integer
);