-- Last updated: 9/12/2026, 10:20:47 AM
SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;