table: fact.forp2
description: Bedrifter med forpagtning efter enhed, landmandens alder, forpagtning og tid
measure: indhold (unit -)
columns:
- enhed: values [ANTAL=Bedrifter (antal), AFP=Forpagtet areal (ha), AREAL=Samlet dyrket areal (ha)]
- bdfalder: values [IALT=Alder i alt, 25UN=Under 25 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75OV=75 år og derover, 999=Uoplyst alder]
- forp: values [4000=Alle bedrifter, 4010=Ingen forpagtning, 4015=Forpagtning 0,1-9,9 pct., 4020=Forpagtning 10,0-24,9 pct., 4025=Forpagtning 25,0-49,9 pct., 4030=Forpagtning 50,0-74,9 pct., 4035=Forpagtning 75,0-99,9 pct., 4040=Forpagtning 100 pct.]
- tid: date range 1982-01-01 to 2024-01-01

notes:
- enhed is a measure-type selector (ANTAL / AFP / AREAL). Same 3-way split as forp1. Always filter to one.
- forp: 4000=Alle bedrifter is total; 4010-4040 are forpagtning-pct brackets that sum to 4000.
- bdfalder: IALT = all ages. 999=Uoplyst alder is a real category. Filter to IALT unless doing age analysis.
- Sister table to forp1 — same time range and forpagtning structure but crossed by farmer age instead of farm size. National only.