-- Last updated: 9/12/2026, 10:23:08 AM
SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales s
JOIN Product p
ON s.product_id = p.product_id;