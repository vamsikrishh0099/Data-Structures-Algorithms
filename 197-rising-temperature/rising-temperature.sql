# Write your MySQL query statement below


select W1.id
from weather w1 join weather w2 
on w1.recordDate = W2.recordDate + INTERVAL 1 DAY where w1.temperature > w2.temperature