# Write your MySQL query statement below
SELECT user_id, COUNT(follower_id) AS followers_count FROM Followers GROUP By user_id ORDER BY user_id