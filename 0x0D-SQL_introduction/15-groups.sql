-- counting the number of distinct scores
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
