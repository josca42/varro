table: fact.ani11
description: Samlede værdier og indeks for animalske landbrugsprodukter (kvartal) efter indekstype og tid
measure: indhold (unit -)
columns:
- indekstype: values [1=Salgsværdi i alt (mio.kr), 15=Mængdeindeks 2015=100, 25=Prisindeks 2015=100]
- tid: date range 2015-01-01 to 2025-04-01

notes:
- `indekstype` is a measurement selector — filter to exactly one value per query. The 3 series are: 1=Salgsværdi i alt (actual value in mio.kr), 15=Mængdeindeks 2015=100, 25=Prisindeks 2015=100. Summing across indekstype is meaningless.
- Quarterly data from 2015. For annual data or longer series, use ani2.