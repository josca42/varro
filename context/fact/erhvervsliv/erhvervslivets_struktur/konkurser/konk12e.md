table: fact.konk12e
description: Konkurser (eksperimentel statistik) efter nøgletal og tid
measure: indhold (unit Antal)
columns:
- bnogle: values [K01=Konkurser i alt, K02=Konkurser i aktive virksomheder, K03=Konkurser i nulvirksomheder, K04=Konkursbegæring]
- tid: date range 2009-01-01 to 2025-01-01

notes:
- Annual experimental statistics. The least current of the experimental series (only to 2025-01-01 = year 2025). Use konk11e for monthly or konk10e for weekly if recency matters.
- Includes K04=Konkursbegæring (petition) as a leading indicator alongside the three standard measures.
- K01 = K02 + K03. Always filter bnogle to one value.