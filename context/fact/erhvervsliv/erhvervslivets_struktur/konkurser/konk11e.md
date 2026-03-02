table: fact.konk11e
description: Konkurser (eksperimentel statistik) efter nøgletal og tid
measure: indhold (unit Antal)
columns:
- bnogle: values [K01=Konkurser i alt, K02=Konkurser i aktive virksomheder, K03=Konkurser i nulvirksomheder, K04=Konkursbegæring]
- tid: date range 2009-01-01 to 2025-09-01

notes:
- Monthly experimental statistics. Similar to konk9 (which goes back to 1979) but experimental and includes K04=Konkursbegæring (bankruptcy petition) which konk9 lacks.
- Use konk9 for long historical monthly series (from 1979), use konk11e when you need Konkursbegæring alongside monthly counts.
- K01 = K02 + K03. Always filter bnogle to one value.