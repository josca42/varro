table: fact.inn21
description: Erhvervslivets innovationsudgifter efter branche og størrelsesgruppe, region, udgiftstype og tid
measure: indhold (unit 1.000 kr.)
columns:
- innbranche: values [1000=ALLE BRANCHER (DB07), 1010=Industri, 1015=Bygge og anlæg, 1020=Handel, 1025=Transport, 1030=Hotel, restauration, 1035=Information og kommunikation, 1040=Finansiering og forsikring, 1045=Erhvervsservice, 1050=Øvrige brancher, 1055=STØRRELSESGRUPPER I ALT (årsværk), 1060=Under 10 årsværk, 1065=10-49 årsværk, 1070=50-249 årsværk, 1075=250 årsværk og derover]
- region: join dim.nuts on region=kode; levels [1]
- udgtyp: values [380=Løn og sociale udgifter vedr. innovation, ekskl. FoU, 390=Øvrige driftsudgifter vedr. innovation, ekskl. FoU, 400=Køb af maskinel, udstyr og software til innovation, 410=Køb af eksterne rettigheder, 420=Køb af anden ekstern viden, 430=Køb af konsulentydelser]
- tid: date range 2020-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- innbranche mixes two independent hierarchies: branch view (1000=ALLE BRANCHER total, 1010-1050=individual branches) and size group view (1055=STØRRELSESGRUPPER I ALT total, 1060-1075=individual size groups). Choose one view per query. The totals 1000 and 1055 cover the same firms — never sum rows from both hierarchies.
- region joins dim.nuts at niveau=1 only (the 5 regions: 81=Nordjylland, 82=Midtjylland, 83=Syddanmark, 84=Hovedstaden, 85=Sjælland). Code 0 = national total, not in dim.nuts — use WHERE f.region = '0' for national totals or LEFT JOIN and handle NULLs.
- udgtyp has no total code — the 6 cost categories (380-430) are additive components of total innovation expenditure. SUM across all udgtyp values to get the full expenditure figure.
- indhold is in 1.000 kr. (thousands DKK). Multiply by 1000 for absolute figures.
- Map: context/geo/regioner.parquet — merge on region=dim_kode. Exclude region='0'.