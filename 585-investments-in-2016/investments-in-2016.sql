# Write your MySQL query statement below



select round(sum(t.TIV_2016),2) as tiv_2016 from insurance t
where (lat,lon) not in (
select lat, lon from insurance where pid != t.pid 
) and 
t.tiv_2015 in (select tiv_2015 from insurance where pid != t.pid )


-- SELECT
--     SUM(TIV_2016) AS TIV_2016
-- FROM insurance
-- WHERE (LAT, LON) IN (SELECT
--                         LAT,
--                         LON
--                      FROM insurance
--                      GROUP BY LAT, LON
--                      HAVING COUNT(*) = 1) AND
--        TIV_2015 IN (SELECT TIV_2015 FROM insurance GROUP BY TIV_2015 HAVING COUNT(*) >= 2);


