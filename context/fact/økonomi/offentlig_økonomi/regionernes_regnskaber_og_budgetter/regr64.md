table: fact.regr64
description: Regionernes likvide beholdninger (1000 kr.) efter funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- funktion: values [61000=6.10.00 Likvide aktiver i alt, 61001=6.10.01 Kontante beholdninger, 61005=6.10.05 Indskud i pengeinstitutter mv., 61007=6.10.07 Investerings- og placeringsforeninger , 61008=6.10.08 Realkreditobligationer, 61009=6.10.09 Kommunekredits obligationer, 61010=6.10.10 Statsobligationer mv., 61011=6.10.11 Udenlandske obligationer]
- tid: date range 2007-04-01 to 2025-04-01

notes:
- No region dimension — national totals only.
- Quarterly time series (same quarter encoding as regr63).
- funktion 61000 = Likvide aktiver i alt (total). Sub-codes 61001-61011 are types of liquid assets (cash, bank deposits, bonds, etc.). Do not sum all funktion rows — 61000 is already the aggregate.
- Subset of regr63 (61000 group only). Use regr63 if you also need other balance sheet items alongside liquid assets.