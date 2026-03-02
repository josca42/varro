table: fact.postnr2
description: Befolkningen 1. januar efter postnumre, køn, alder og tid
measure: indhold (unit Antal)
columns:
- pnr20: values [1=Hele landet, 1011050=101 København - 1050 København K, 1011051=101 København - 1051 København K, 1011052=101 København - 1052 København K, 1011053=101 København - 1053 København K ... 8609870=860 Hjørring - 9870 Sindal, 8609881=860 Hjørring - 9881 Bindslev, 8609900=860 Hjørring - 9900 Frederikshavn, 8609982=860 Hjørring - 9982 Ålbæk, 8609999=860 Hjørring - 9999 Ukendt]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- tid: date range 2010-01-01 to 2025-01-01

notes:
- pnr20 codes are compound: municipality code (3 digits) + postal code (4 digits), e.g., 1011050 = kommunekode 101 (København) + postnr 1050. pnr20=1 is national total.
- 1465 distinct codes vs 1061 in postnr1 — the extra codes come from postal areas that span multiple municipalities (each municipality's slice gets its own code).
- Do NOT sum all pnr20 codes — pnr20=1 (Hele landet) is a separate aggregate that overlaps with all other codes.
- Use postnr1 for simple "population by postal code". Use postnr2 when you need to split a cross-municipality postal area by municipality.
- Same age groupings (5-year bands) and kon totals as postnr1.
- Map: context/geo/postnumre.parquet — postal code is pnr20 % 10000; merge on (pnr20 % 10000)=dim_kode. Exclude pnr20=1 and rows where pnr20 % 10000 = 9999.