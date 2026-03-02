table: fact.folk1d
description: Befolkningen den 1. i kvartalet efter område, køn, alder, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- statsb: values [TOT=I alt, DANSK=Dansk statsborger, UDLAND=Udenlandsk statsborger]
- tid: date range 2008-01-01 to 2025-07-01
dim docs: /dim/nuts.md

notes:
- omrade=0 is the national total ("I alt") — not in dim.nuts. dim.nuts covers niveau=1 (5 regioner) and niveau=3 (99 kommuner).
- statsb is simplified (TOT/DANSK/UDLAND). Use folk1b for country-level statsb breakdown.
- alder has individual years (0–125) with IALT as total. No aggregate age bands.
- 4 dimension columns (omrade, kon, alder, statsb). Filter non-target dims: omrade=0, kon='TOT', alder='IALT', statsb='TOT'.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.