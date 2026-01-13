-- @query: regions
SELECT DISTINCT n.titel as region
FROM dim.nuts n
WHERE n.niveau = 1
ORDER BY n.titel;

-- @query: population_trend
-- National data when no region selected (omrade=0), or regional when filter set
SELECT
  f.tid as quarter,
  f.indhold as population
FROM fact.folk1a f
LEFT JOIN dim.nuts n ON f.omrade::int = n.kode AND n.niveau = 1
WHERE f.kon = 'TOT'
  AND f.alder = 'IALT'
  AND f.civilstand = 'TOT'
  AND ((:region IS NULL AND f.omrade = 0) OR (:region IS NOT NULL AND n.titel = :region))
  AND (:period_from IS NULL OR f.tid >= :period_from)
  AND (:period_to IS NULL OR f.tid <= :period_to)
ORDER BY f.tid;

-- @query: population_by_region
SELECT
  n.titel as region,
  f.indhold as population
FROM fact.folk1a f
JOIN dim.nuts n ON f.omrade::int = n.kode
WHERE n.niveau = 1
  AND f.kon = 'TOT'
  AND f.alder = 'IALT'
  AND f.civilstand = 'TOT'
  AND f.tid = (SELECT MAX(tid) FROM fact.folk1a)
ORDER BY f.indhold DESC;

-- @query: age_distribution
SELECT
  CASE
    WHEN f.alder::int BETWEEN 0 AND 17 THEN '0-17'
    WHEN f.alder::int BETWEEN 18 AND 29 THEN '18-29'
    WHEN f.alder::int BETWEEN 30 AND 49 THEN '30-49'
    WHEN f.alder::int BETWEEN 50 AND 64 THEN '50-64'
    WHEN f.alder::int >= 65 THEN '65+'
  END as age_group,
  SUM(f.indhold) as population
FROM fact.folk1a f
LEFT JOIN dim.nuts n ON f.omrade::int = n.kode AND n.niveau = 1
WHERE f.kon = 'TOT'
  AND f.civilstand = 'TOT'
  AND f.alder != 'IALT'
  AND f.tid = (SELECT MAX(tid) FROM fact.folk1a)
  AND ((:region IS NULL AND f.omrade = 0) OR (:region IS NOT NULL AND n.titel = :region))
GROUP BY 1
ORDER BY 1;
