table: fact.neet2
description: Befolkningen (16-24 år) efter NEET-status, bopælsområde, køn, alder og tid
measure: indhold (unit Antal)
columns:
- statusneet: values [0=Aktive og ikke-aktive i alt, 5=Aktive, 10=Ikke-aktive (NEET)]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [IALT=Alder i alt, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- statusneet: same as neet1 — values 0/5/10 where 0=total. Filter to statusneet='10' for NEET, statusneet='5' for active, or statusneet='0' for everyone.
- bopomr joins dim.nuts. bopomr='0' is the national total, not in dim.nuts. Three hierarchy levels via d.niveau: 1=5 regioner, 2=11 landsdele, 3=99 kommuner. Filter d.niveau to pick geographic granularity and avoid double-counting.
- alder: IALT=16-24 total, plus 9 individual ages (16, 17, …, 24). IALT = sum of individual ages. Filter to alder='IALT' for totals, individual ages for age breakdowns. Do not sum across both IALT and individual ages.
- kon: TOT=total, M=mænd, K=kvinder.
- neet2 differs from neet1: it has individual ages but no socioøkonomisk breakdown. Use neet2 when you need age granularity; use neet1 when you need socioøkonomisk status.
- Clean NEET count by age: filter statusneet='10', kon='TOT', bopomr='0' (national), group by alder (exclude IALT or individual ages depending on desired aggregation).
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.