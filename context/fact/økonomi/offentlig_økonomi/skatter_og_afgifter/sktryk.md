table: fact.sktryk
description: Skattetryk efter nationalregnskabsgrupper og tid
measure: indhold (unit Pct.)
columns:
- natgrup: values [1=Skatter og afgifter i alt, 2=Produktions- og importskatter, 3=Løbende indkomst- og formueskatter, 4=Obligatoriske bidrag til sociale ordninger, 5=Kapitalskatter, 6=Korrigeret skattetryk, 7=Modificeret skattetryk, 8=Faktorskattetryk]
- tid: date range 1971-01-01 to 2024-01-01

notes:
- Each natgrup is an independent tax burden measure as % of GDP. Never sum across natgrup — they are different ways of measuring the same thing, not additive components.
- natgrup=1 (45.6% in 2024) is the standard total tax-to-GDP ratio. natgrup=2+3+4+5 are the four national accounts components that approximately decompose natgrup=1. natgrup=6/7/8 are alternative methodological adjustments (corrigeret, modificeret, faktorskattetryk) — report these individually only.
- For simple "what is the Danish tax burden" question: WHERE natgrup='1'. For composition breakdown: WHERE natgrup IN ('2','3','4','5').
