table: fact.folk1am
description: Befolkningen den 1. i måneden efter område, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- tid: date range 2021-10-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- Same geographic structure as folk1a: omrade='0' (Hele landet, not in dim.nuts), niveau=1 (5 regioner), niveau=3 (99 kommuner). Each person is counted at all three levels — always filter omrade to one level to avoid 3x inflation.
- No civilstand column. Use folk1a for marital status breakdown or for data before Oct 2021.
- Monthly granularity (tid increments by month) from Oct 2021 — finest time resolution for population snapshots.
- Filter non-target dims: kon='TOT', alder='IALT'.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.