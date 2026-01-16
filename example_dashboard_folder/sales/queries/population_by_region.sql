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