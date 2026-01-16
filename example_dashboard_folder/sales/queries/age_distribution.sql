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