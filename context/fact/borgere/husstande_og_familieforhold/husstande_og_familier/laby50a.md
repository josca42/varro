table: fact.laby50a
description: Husstandes afstand til nærmeste dagligvarebutik (andel i  pct.) efter kommunegruppe, afstand og tid
measure: indhold (unit Andel i pct.)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- afstand: values [600=Under 0,5 km, 605=0,5-1 km, 610=1-2 km, 615=2-3 km, 620=3-4 km, 625=4 km og derover, 630=Uoplyst]
- tid: date range 2009-01-01 to 2022-01-01
dim docs: /dim/kommunegrupper.md

notes:
- IMPORTANT: The percentages in this table are NOT "% of households in kommunegruppe X at each distance." They are "% of all households at distance band Y that belong to kommunegruppe X." komgrp='0' = 100 for every afstand confirms the denominator is the national total within each distance band.
- Concretely: laby50a WHERE komgrp='1' AND afstand='600' = 42.3% means 42.3% of all Danish households within 0.5km of a grocery store are in Hovedstadskommuner — NOT that 42.3% of Hovedstadskommuner households are within 0.5km.
- To find "what % of Landkommuner households are more than 4km from a grocery store", use laby50 (counts) and compute: count(komgrp=5, afstand=625) / SUM(count across all afstand for komgrp=5) * 100.
- Values do NOT sum to 100 within a komgrp row — that's expected. They sum to 100 within each afstand column across all komgrp values.