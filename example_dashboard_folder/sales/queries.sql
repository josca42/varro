-- @query: regions
SELECT DISTINCT region FROM sales ORDER BY region;

-- @query: monthly_revenue
SELECT
    date_trunc('month', date) as month,
    sum(revenue) as revenue
FROM sales
WHERE (:region IS NULL OR region = :region)
  AND (:period_from IS NULL OR date >= :period_from)
  AND (:period_to IS NULL OR date <= :period_to)
GROUP BY 1
ORDER BY 1;

-- @query: top_products
SELECT
    product_name,
    sum(revenue) as revenue,
    count(*) as orders
FROM sales
WHERE (:region IS NULL OR region = :region)
  AND (:period_from IS NULL OR date >= :period_from)
  AND (:period_to IS NULL OR date <= :period_to)
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;
