SELECT year, 
    COUNT(*) AS book_count,
    ROUND(AVG(
        CASE
            WHEN currency = '€' THEN price * 1.2
            ELSE price
        END), 2) AS avg_price_in_usd           
FROM books
GROUP BY year
ORDER BY year;
