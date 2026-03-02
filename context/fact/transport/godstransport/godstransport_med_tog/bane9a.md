table: fact.bane9a
description: Jernbanetransport af gods efter enhed, transporttype og tid
measure: indhold (unit -)
columns:
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- transport: values [1000=KØRSEL I ALT, 1500=National kørsel, 1600=International kørsel , 8000=Transit kørsel]
- tid: date range 2013-01-01 to 2025-04-01

notes:
- Simplest table in this subject: only enhed and transport as dimensions.
- enhed is a measurement selector: 75=1000 ton, 76=Mio. tonkm. Always filter to one.
- transport: 1000=total, 1500=national, 1600=international, 8000=transit. Same aggregate/detail pattern as other bane tables.
- This is the most up-to-date table (quarterly data to 2025 Q1 vs annual 2024 in other tables). Use for recent trends. For data before 2013 use bane1.
- tid increments quarterly (Jan/Apr/Jul/Oct). When comparing to annual tables, aggregate with SUM or filter to a specific quarter.