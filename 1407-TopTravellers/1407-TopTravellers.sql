-- Last updated: 9/12/2026, 10:21:49 AM
# Write your MySQL query statement below
SELECT
    u.name,
    IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY
    u.id,
    u.name
ORDER BY
    travelled_distance DESC,
    u.name ASC;