# Write your MySQL query statement below

select distinct l1.id,a.name from logins l1 inner join accounts a 
on l1.id = a.id 
inner join logins l2 on l1.id = l2.id and  datediff(l1.login_date, l2.login_date) between 1 and 4 
group by l1.id,l1.login_date
having count(distinct l2.login_date) >= 4