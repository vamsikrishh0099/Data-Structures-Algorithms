-- Solution for 5 or more consecutive days
WITH DistinctLogins AS (
    -- Remove duplicate logins on the same day
    SELECT DISTINCT id, login_date
    FROM Logins
),
ConsecutiveLogins AS (
    -- Calculate the difference to identify consecutive dates
    SELECT 
        id,
        login_date,
        login_date - ROW_NUMBER() OVER (PARTITION BY id ORDER BY login_date)::integer AS group_id
    FROM DistinctLogins
),
ConsecutiveCounts AS (
    -- Count consecutive days per group
    SELECT 
        id,
        COUNT(*) AS consecutive_days
    FROM ConsecutiveLogins
    GROUP BY id, group_id
    HAVING COUNT(*) >= 5
)
SELECT 
    distinct a.id,
    a.name
FROM Accounts a
JOIN ConsecutiveCounts c ON a.id = c.id
ORDER BY a.id;
