# Write your MySQL query statement below


-- select tt.id, ifnull((case when tt.id%2 = 1 then tt.nextname 
--                 when tt.id%2 = 0 then tt.prevname 
--                 else tt.student end
--                 ),tt.student) as student from 
-- (select s1.id, s1.student, s2.id as nextid, s2.student as nextname, s3.id as previd, s3.student as prevname
-- from seat s1 left join seat s2 on s1.id = s2.id-1 left join seat s3 on s1.id = s3.id+1) tt

# select 
# s1.id, (case when s1.id%2 = 1 then )
# from seat s1

SELECT 
ID,
CASE WHEN ID%2 = 1 THEN IFNULL(LEAD(STUDENT) OVER(ORDER BY ID),STUDENT) 
ELSE LAG(STUDENT) OVER(ORDER BY ID) 
END AS STUDENT
 FROM SEAT