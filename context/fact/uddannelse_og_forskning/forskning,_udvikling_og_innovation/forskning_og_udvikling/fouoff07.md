table: fact.fouoff07
description: FoU-omkostninger i den offentlige sektor efter fag, omkostningstyper og tid
measure: indhold (unit -)
columns:
- faget: values [0=Alle fag i alt, 400=Naturvidenskab i alt, 405=Matematik, 410=Datalogi, 415=Fysik (inkl. biofysik) ... 930=Teologi, 935=Musik- og teatervidenskab, 940=Kunst- og arkitekturvidenskab, 945=Film- og medievidenskab, 950=Øvrig humanistisk videnskab]
- drift1: values [0=FoU årsværk i alt, 200=Driftsomkostninger Mio. kr. , 210=Øvrige omkostninger  Mio. kr. , 220=Omkostninger i alt  Mio. kr. ]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- CRITICAL: drift1 mixes two incompatible units in a single column — never aggregate across all drift1 values:
  - drift1='0' → indhold is FoU årsværk (count), not mio. kr.
  - drift1='200' → Driftsomkostninger (mio. kr.)
  - drift1='210' → Øvrige omkostninger (mio. kr.)
  - drift1='220' → Omkostninger i alt (mio. kr.) = 200 + 210
- Always filter to a single drift1 value. For total costs: drift1='220'. For årsværk counts: drift1='0'.
- faget='0' = Alle fag i alt (total). All other faget codes are specific scientific fields — the field list is long (~50 codes at various levels of aggregation). Use ColumnValues("fouoff07", "faget") to browse.
- The unit column says "-" reflecting this mixed-unit design.
