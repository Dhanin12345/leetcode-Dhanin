-- Last updated: 9/12/2026, 10:22:58 AM
SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;