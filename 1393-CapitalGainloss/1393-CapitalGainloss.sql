-- Last updated: 9/12/2026, 10:21:52 AM
# Write your MySQL query statement below
SELECT
    stock_name,
    SUM(
        CASE
            WHEN operation = 'Sell' THEN price
            ELSE -price
        END
    ) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;