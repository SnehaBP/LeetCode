# Write your MySQL query statement below
SELECT Employee.name, Bonus.bonus FROM Employee left join Bonus ON Employee.empId=Bonus.empId WHERE Bonus.bonus<1000 or Bonus.bonus IS NULL