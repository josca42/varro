table: fact.afg3
description: Bedrifter og arealer med udvalgte afgrøder efter område, areal med afgrøden, enhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.landbrugslandsdele on omrade=kode [approx]
- arealafg: values [10250=Uden rug, 10255=0,1-4,9 ha med rug, 10260=5,0-9,9 ha med rug, 10265=10,0-14,9 ha med rug, 10270=15,0-19,9 ha med rug ... 10485=15,0-19,9 ha med kartofler, 10490=20,0-29,9 ha med kartofler, 10495=30,0-49,9 ha med kartofler, 10500=50,0 ha med kartofler og over, 10505=Alle bedrifter med kartofler]
- enhed: values [200=Ha med afgrøden, 400=Bedrifter ]
- tid: date range 1982-01-01 to 2024-01-01
dim docs: /dim/landbrugslandsdele.md
notes:
- omrade does NOT join to dim.landbrugslandsdele. Only 3 values: 000=Hele landet, L3=Jylland, L4=Øerne. Very coarse 2-way regional split. Use ColumnValues("afg3","omrade") directly for labels — no dim join needed or useful.
- enhed is a measurement selector: 200=Ha med afgrøden, 400=Bedrifter. Every omrade × arealafg combination appears twice. Always filter to one enhed.
- arealafg encodes both crop type and farm-size class (same structure as afg207). Each crop has its own range of ~7–9 codes. The highest code in each range is the total for that crop (e.g. 10290="Alle bedrifter med rug", 10390="Alle bedrifter med havre"). Use ColumnValues("afg3","arealafg") to browse all 52 codes covering rug, havre, kartofler, raps, frø, and others.
- afg3 covers crops not in afg207 (rug, havre, kartofler, raps, frø mv.) and goes back to 1982, but only has the coarse 3-value regional split. For more regional detail use afg207 (from 2006, regioner + landsdele).
