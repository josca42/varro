table: fact.laby22
description: Ejendomssalg efter kommunegruppe, ejendomskategori, nøgletal og tid
measure: indhold (unit -)
columns:
- komgrp: join dim.kommunegrupper on komgrp=kode; levels [1]
- ejendomskate: join dim.ejendom on ejendomskate=kode; levels [1, 2]
- bnogle: values [25=Gennemsnitlig pris pr. ejendom (1.000 kr.), 26=Gennemsnitlig kvadratmeterpris  pr. ejendom (kr. pr. m2), 27=Gennemsnitsalder hvor hele køberkredsen er førstegangskøbere (alder), 28=Andelen af førstegangskøbere (pct.)]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/ejendom.md, /dim/kommunegrupper.md

notes:
- `bnogle` selects the key figure — always filter to one value: 25=Gennemsnitlig pris pr. ejendom (1000 kr), 26=Gennemsnitlig kvadratmeterpris (kr/m2), 27=Gennemsnitsalder førstegangskøbere (år), 28=Andel førstegangskøbere (pct.). These are completely different measures that cannot be summed.
- `komgrp` joins dim.kommunegrupper niveau 1 only (5 grupper: Hovedstads-, Storby-, Provinssby-, Opllands- og Landkommuner). Code 0 = "Hele landet" (not in dim). Use ColumnValues("kommunegrupper", "titel") for labels.
- `ejendomskate` only has 2 property types: 111=Enfamiliehuse and 2103=Ejerlejligheder. Code 111 appears at both niveau 1 and 2 in dim.ejendom with the same kode — filter `d.niveau = 1` to avoid getting duplicate rows.
- Only table in this subject with first-time buyer (førstegangskøbere) statistics. Annual, ends 2024. No transfer-type or overdrag breakdown — covers all sale types combined.