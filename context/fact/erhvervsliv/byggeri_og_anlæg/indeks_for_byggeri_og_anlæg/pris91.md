table: fact.pris91
description: Producentprisindeks for renovering og vedligeholdelse efter arbejdets art, enhed og tid
measure: indhold (unit -)
columns:
- arbart: values [500=Renovering og vedligeholdelse i alt, 510=Elinstallation, 520=VVS- og blikkenslager, 530=Tømrer, 540=Bygningsfærdiggørelse, 550=Tagdækker, 560=Murer]
- tal: values [100=Indeks, 315=Ændring i forhold til året før (pct.)]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- `tal` is a measurement selector — every arbart×tid combination appears twice (100=Indeks, 315=år-over-år pct). Always filter to `tal = 100` or `tal = 315`.
- Annual frequency (month 1 only). Covers renovation and maintenance — distinct from the byg tables which cover new construction.
- `arbart`: 500=Renovering og vedligeholdelse i alt (total aggregate). 510–560 are individual trade specialisms. Do not sum across arbart — 500 already contains all trades.
- Data ends 2024.