table: fact.ene1ht
description: Energiregnskab i specifikke enheder (detaljeret) efter tilgang, energitype og tid
measure: indhold (unit -)
columns:
- tilgang: values [ETIL=Tilgang i alt, EIMPORT=Import, ETILAFF=Tilgang af affald mv. som energi, ETILVE=Tilgang af vedvarende energi, EPRODI=Produktion i alt ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- energi1: values [EMRO=Råolie (ton), EMHFBK=Halvfabrikata (ton), EMRAFF=Raffinaderigas (ton), EMLPG=LPG (ton), EMLPGTR=LPG_transport (ton) ... EMBIOOIL=Biodiesel, bioethanol og bioolie (ton), EMVMP=Omgivelsesvarme indvundet med varmepumper (TJ), EMEL=El (GWh), EMFJV=Fjernvarme (TJ), EMGVG=Bygas (1000 Nm3)]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- energi1 encodes fuel type AND native unit (e.g. EMEL=El (GWh), EMFJV=Fjernvarme (TJ)). Do NOT sum across energy types — units are incompatible. Use ene2ht for cross-fuel GJ comparisons.
- tilgang mixes macro supply categories with sector-level production (same structure as ene2ht). Filter to one level.
- This is the supply/tilgang-side detail. Counterpart: ene1ha (use side).