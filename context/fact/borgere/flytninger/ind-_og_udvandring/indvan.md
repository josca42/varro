table: fact.indvan
description: Indvandringer efter køn, alder, statsborgerskab, indvandringsland og tid
measure: indhold (unit Antal)
columns:
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- statsb: values [DANSK=Dansk, UDLAND=Udenlandsk ]
- indvland: join dim.lande_psd on indvland=kode; levels [3]
- tid: date range 1980-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- No regional breakdown (no omrade column). For region/kommune level, use van1aar or van1kvt instead.
- statsb is very coarse: only DANSK or UDLAND (not individual countries). For detailed citizenship use van1aar/van1kvt.
- kon uses M/K (not 1/2 like van1kvt). No total row.
- indvland only uses niveau 3 (236 individual countries). ColumnValues("lande_psd", "titel", for_table="indvan") for the full list.
- alder is individual ages 0–103 only, no total. Aggregate in SQL.
- Longest annual immigration series: back to 1980. Use this when historical trend is more important than geographic or citizenship detail.