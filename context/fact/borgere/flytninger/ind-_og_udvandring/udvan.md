table: fact.udvan
description: Udvandringer efter køn, alder, statsborgerskab, udvandringsland og tid
measure: indhold (unit Antal)
columns:
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- statsb: values [DANSK=Dansk, UDLAND=Udenlandsk ]
- udvland: join dim.lande_psd on udvland=kode; levels [3]
- tid: date range 1980-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- Emigration mirror of indvan. Longest annual emigration series (1980–present) but no regional breakdown, no detailed citizenship (statsb only DANSK or UDLAND).
- kon uses M/K (not 1/2). alder individual ages only (0–103), no total.
- udvland only uses niveau 3 (233 individual countries). ColumnValues("lande_psd", "titel", for_table="udvan") for full list.
- For emigration with regional breakdown or detailed citizenship use van2aar or van2kvt instead.