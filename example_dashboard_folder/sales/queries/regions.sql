SELECT DISTINCT n.titel as region
FROM dim.nuts n
WHERE n.niveau = 1
ORDER BY n.titel;