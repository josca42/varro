table: fact.ene3h
description: Bruttoenergiforbrug i GJ efter branche, energitype og tid
measure: indhold (unit GJ (gigajoule))
columns:
- branche: values [ETOT=Brancher og husholdninger, EHUSHOLD=Husholdninger, EV=Brancher i alt, VA=A Landbrug, skovbrug og fiskeri, V01000=01000 Landbrug og gartneri ... V96000=96000 Frisører, vaskerier og andre serviceydelser, V960000=960000 Frisører, vaskerier og andre serviceydelser, VSB=SB Private husholdninger med ansat medhjælp, V97000=97000 Private husholdninger med ansat medhjælp, V970000=970000 Private husholdninger med ansat medhjælp]
- energi1: values [ETOT=I ALT, EROOL=RÅOLIE OG HALVFABRIKATA, ERO=Råolie, EHFBK=Halvfabrikata, EOIL=OLIEPRODUKTER ... EVMP=Omgivelsesvarme indvundet med varmepumper, EKONV=KONVERTEREDE ENERGIARTER, EEL=El, EFJV=Fjernvarme, EGVG=Bygas]
- tid: date range 1966-01-01 to 2024-01-01

notes:
- branche is inline-coded with a V-prefix convention (no dim join). Totals: ETOT=all sectors+households, EV=all sectors, EHUSHOLD=households. Individual sectors follow the V{NACE-code} pattern (VA=agriculture, VC=industry, etc.). Multiple hierarchy levels coexist — filter to one level to avoid double-counting.
- energi1 has ETOT (grand total) plus many fuel-type sub-codes. Summing sub-codes while ETOT is present causes double-counts. For total consumption, filter energi1='ETOT'.
- indhold is in GJ. Long series from 1966 — best table for sector-level gross energy consumption over time.