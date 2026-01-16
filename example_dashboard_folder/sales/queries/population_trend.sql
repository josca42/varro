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