table: fact.ani2
description: Samlede værdier og indeks for animalske landbrugsprodukter (år) efter indekstype og tid
measure: indhold (unit Mio. kr.)
columns:
- indekstype: values [1=Salgsværdi i alt (mio.kr), 15=Mængdeindeks 2015=100, 23=Mængdeindeks 2010=100, 20=Mængdeindeks 2005=100, 4=Mængdeindeks 2000=100, 5=Mængdeindeks 1995=100, 25=Prisindeks 2015=100, 22=Prisindeks 2010=100, 21=Prisindeks 2005=100, 8=Prisindeks 2000=100, 10=Prisindeks 1995=100]
- tid: date range 1995-01-01 to 2024-01-01

notes:
- `indekstype` is a measurement selector — filter to exactly one value per query. Never sum across indekstype.
- indekstype=1 (Salgsværdi i alt) is the raw value in mio.kr. The remaining 10 values are index numbers with different base years: mængdeindeks in bases 1995/2000/2005/2010/2015 and prisindeks in the same bases. Pick one base year for a consistent index series — do not mix base years.
- The most current base-year indices are 15 (mængdeindeks 2015=100) and 25 (prisindeks 2015=100), but they only cover 2015-2024. Older base-year series go back to 1995.
- Annual data. For quarterly series from 2015, use ani11.