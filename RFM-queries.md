WITH rfm AS (
SELECT customer_id ,
C U R R E N T _ D A T E- MAX ( or de r_d at e ) :: date AS recency_days ,
COUNT ( DISTINCT order_id ) AS frequency ,
SUM ( amount ) AS monetary
FROM orders
GROUP BY c u s t o m e r _ i d
) , scored AS (
SELECT * ,
NTILE (5) OVER ( ORDER BY r e c e n c y _ d a y s DESC ) AS r ,
NTILE (5) OVER ( ORDER BY frequency ) AS f ,
NTILE (5) OVER ( ORDER BY monetary ) AS m
FROM rfm
)
SELECT customer_id , r , f , m ,
CASE WHEN r >= 4 AND f >= 4 AND m >= 4 THEN ’ Champion ’
WHEN r <= 2 AND f >= 3 THEN ’ At risk ’
WHEN r <= 2 AND f <= 2 THEN ’ H i b e r n a t i n g ’
ELSE ’ Other ’ END AS segment
FROM scored
