WITH reaction_counts AS (
    SELECT
        user_id,
        reaction,
        COUNT(*) AS cnt
    FROM reactions
    GROUP BY user_id, reaction
),
user_stats AS (
    SELECT
        user_id,
        MAX(cnt) AS max_cnt,
        SUM(cnt) AS total_cnt
    FROM reaction_counts
    GROUP BY user_id
    HAVING SUM(cnt) >= 5
)
SELECT
    rc.user_id,
    rc.reaction AS dominant_reaction,
    ROUND(rc.cnt / us.total_cnt, 2) AS reaction_ratio
FROM reaction_counts rc
JOIN user_stats us
    ON rc.user_id = us.user_id
WHERE rc.cnt = us.max_cnt
  AND rc.cnt / us.total_cnt >= 0.60
ORDER BY reaction_ratio DESC, rc.user_id ASC;