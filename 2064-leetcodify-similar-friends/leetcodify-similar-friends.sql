WITH dedup AS (
  SELECT DISTINCT user_id, song_id, day
  FROM Listens
),
pair_day AS (
  SELECT f.user1_id, f.user2_id, d1.day
  FROM Friendship f
  JOIN dedup d1
    ON d1.user_id = f.user1_id
  JOIN dedup d2
    ON d2.user_id = f.user2_id
   AND d2.day = d1.day
   AND d2.song_id = d1.song_id
  GROUP BY f.user1_id, f.user2_id, d1.day
  HAVING COUNT(DISTINCT d1.song_id) >= 3
)
SELECT user1_id, user2_id
FROM pair_day
GROUP BY user1_id, user2_id;
