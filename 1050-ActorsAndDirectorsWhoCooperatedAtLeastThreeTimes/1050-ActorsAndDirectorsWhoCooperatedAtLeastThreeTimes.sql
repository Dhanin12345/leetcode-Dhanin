-- Last updated: 9/12/2026, 10:23:11 AM
SELECT
    actor_id,
    director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;