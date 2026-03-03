table: fact.postnr1
description: Befolkningen 1. januar efter postnumre, køn, alder og tid
measure: indhold (unit Antal)
columns:
- pnr20: values [1=Hele landet, 1050=1050 København K (Københavns Kommune), 1051=1051 København K (Københavns Kommune), 1052=1052 København K (Københavns Kommune), 1053=1053 København K (Københavns Kommune) ... 9970=9970 Strandby (Frederikshavn Kommune), 9981=9981 Jerup (Frederikshavn Kommune), 9982=9982 Ålbæk (Frederikshavn Kommune, Hjørring Kommune), 9990=9990 Skagen (Frederikshavn Kommune), 9999=9999 Ukendt]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- pnr20=1 is the national total ("Hele landet") — unusual code (1 not a real postal code). 1061 distinct pnr20 codes.
- Has TOT totals for kon and IALT for alder. Filter: kon='TOT', alder='IALT' for simple postal code population counts.
- alder is in 5-year groups (0-4, 5-9, ..., 100OV), not individual years.
- postnr1 has one row per postal code (unique codes). postnr2 has municipality-postal code combos (1465 codes) — use postnr2 when a postal code spans multiple municipalities and you need the municipality split.
- Map: /geo/postnumre.parquet — merge on pnr20=dim_kode. Exclude pnr20 IN (1, 9999).