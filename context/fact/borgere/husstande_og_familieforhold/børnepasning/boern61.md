table: fact.boern61
description: Fuldtidsomregnet pædagogisk personale i kommunale skolefritidsordninger efter område, stillingskategori og tid
measure: indhold (unit Antal)
columns:
- amt: join dim.nuts on amt=kode; levels [3]
- stilkat: values [STOT=Stillingskategori i alt, 80=Ledelse, inspektør, 81=Sekretær, 82=Læge, psykolog, sygeplejerske, 83=Lærer, støttepædagog, 84=Socialrådgiver, 85=Fysio-, ergoterapeut, 86=Pædagog, omsorgsassistent, 87=Pædagogmedhjælper, 88=Social- og sundhedsassistent, 89=Økonoma, kok, 90=Rengørings- og køkkenhjælp, 91=Pedel, vicevært]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- amt contains kode 0 (national total, not in dim.nuts) and niveau 3 (98 kommuner) only — no regional breakdown.
- stilkat has STOT=Stillingskategori i alt as the aggregate. Filter to STOT for total FTE staff; filter to individual codes (80-91) for breakdown by role.
- Covers kommunale skolefritidsordninger (SFO) only. For all fritidsordninger staff including selvejende and private, no comparable table exists in this subject.
- Map: /geo/kommuner.parquet — merge on amt=dim_kode. Exclude amt=0.
