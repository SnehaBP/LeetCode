# Write your MySQL query statement below
SELECT u.name As NAME,SUM(t.amount) AS BALANCE FROM Users AS u JOIN Transactions AS t ON u.account=t.account GROUP BY u.account,u.name HAVING BALANCE>10000;