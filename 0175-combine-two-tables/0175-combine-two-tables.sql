# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state FROM Person as p lEFT JOIN Address as a ON p.personId=a.personId