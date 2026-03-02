table: fact.bil93
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, bystørrelse, rådighedsmønster og tid
measure: indhold (unit Pct.)
columns:
- maengde4: values [50=Procentfordelingen, 70=Andel af den totale bilrådighed]
- byst: values [TOT=I alt, HOVEDS=Hovedstadsområdet, 100000=100.000 indbyggere og derover, 50000=50.000-99.999 indbyggere, 40000=40.000-49.999 indbyggere, 30000=30.000-39.999 indbyggere, 29000=20.000-29.999 indbyggere, 10000=10.000-19.999 indbyggere, 5000=5.000-9.999 indbyggere, 2000=2.000-4.999 indbyggere, 1000=1.000-1.999 indbyggere, 500=500-999 indbyggere, 201=200-499 indbyggere, LAND=Landdistrikter, UOPBY=Uoplyst bystørrelse]
- raadmoens: values [10000=Familier i alt, 10200=Familier uden bil i alt, 10210=Familier med bil i alt, 10220=Familier med 1 bil i alt, 10230=Familier med personbil, 10240=Familier med firmabil, 10250=Familier med varebil, 10260=Familier med 2 biler i alt, 10270=Familier med 2 personbiler, 10280=Familier med 2 firmabiler, 10290=Familier med 2 varebiler, 10300=Familier med 1 personbil og 1 firmabil, 10310=Familier med 1 personbil og en varebil, 10320=Familier med 1 firmabil og 1 varebil, 10330=Familier med 3 biler i alt, 10340=Familier med flere end 3 biler]
- tid: date range 2013-01-01 to 2025-01-01
notes:
- maengde4 doubles all rows — always filter to one value: 50=Procentfordelingen, 70=Andel af den totale bilrådighed. Values are Pct.; do not SUM.
- byst is flat and mutually exclusive (HOVEDS is a named area at the same level as size bands). See bil92 notes.
- raadmoens is hierarchical — pick one level.
- Only available from 2013.
