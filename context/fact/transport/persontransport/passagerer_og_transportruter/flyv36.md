table: fact.flyv36
description: Persontransportarbejde med fly efter transporttype og tid
measure: indhold (unit Mio. personkm)
columns:
- transport: values [15=National, 25=International]
- tid: date range 1990-01-01 to 2024-01-01

notes:
- Simplest fly table: only transport type (National/International) and time. No airport dimension, no flight type breakdown.
- transport has NO total code — sum transport IN (15, 25) to get total air transport work. Neither value is a superset of the other.
- Annual data from 1990. Use for long-run trends in aviation transport work (Mio. personkm).
