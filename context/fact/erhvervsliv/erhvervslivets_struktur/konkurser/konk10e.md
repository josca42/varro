table: fact.konk10e
description: Konkurser (eksperimentel statistik) efter nøgletal og tid
measure: indhold (unit Antal)
columns:
- bnogle: values [K01=Konkurser i alt, K02=Konkurser i aktive virksomheder, K03=Konkurser i nulvirksomheder, K04=Konkursbegæring]
- tid: date range 2009U01 to 2025U40

notes:
- tid is weekly format: '2009U01' = week 1 of 2009. This is the highest-frequency bankruptcy series — use when weekly trends or recency (last few weeks) matters.
- Experimental statistics — subject to revision and may differ from the official monthly konk9/konk11e figures.
- bnogle K04=Konkursbegæring (bankruptcy petition filed) is available here and in konk11e/konk12e but NOT in konk9 or konk3. This is a leading indicator — petitions precede formal declarations.
- K01 = K02 + K03. Always filter bnogle to one value.