table: fact.ene2ht
description: Energiregnskab i GJ (detaljeret) efter tilgang, energitype og tid
measure: indhold (unit GJ (gigajoule))
columns:
- tilgang: values [ETIL=Tilgang i alt, EIMPORT=Import, ETILAFF=Tilgang af affald mv. som energi, ETILVE=Tilgang af vedvarende energi, EPRODI=Produktion i alt ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- tilgang mixes supply-side macro categories (ETIL, EIMPORT, ETILVE, ETILAFF, EPRODI) with sector-level production codes (VA, VC, V{NACE}...). ETIL=total of all. Summing components with aggregates double-counts.
- energi1 is in GJ (all energy types). ETOT is total; sub-codes are fuel components. Filter to one.
- Counterpart to ene2ha (use/application side). ene2ho covers both sides in a single overview table (less granular on sectors).
- For sector-level production breakdowns, use ene2ht; for consumption/use breakdowns, use ene2ha.