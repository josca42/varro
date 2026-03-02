table: fact.ligedb2
description: Opstillede og valgte kandidater til kommunalvalg efter kandidater, køn, alder, kommune og tid
measure: indhold (unit Antal)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, U20=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 70OV=70 år og derover]
- komk: join dim.nuts on komk=kode; levels [1, 2, 3]
- tid: date range 2005-01-01 to 2021-01-01
dim docs: /dim/nuts.md

notes:
- Five dimension columns (kandidat, kon, alder, komk, tid). To get a simple count, filter all non-target dims to their total: kon='TOT', alder='TOT', komk by niveau. Forgetting any one inflates the sum.
- komk joins dim.nuts at three levels: niveau 1 (5 regioner), niveau 2 (11 landsdele), niveau 3 (98 kommuner), plus '0' = national aggregate not in dim. Filter to one niveau at a time to avoid double-counting.
- kandidat distinguishes OK (nominated) vs VK (elected). These are separate counts — never sum OK+VK together.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on komk=dim_kode. Exclude komk=0.
- Sample — female share of elected candidates by municipality 2021:
  SELECT d.titel, SUM(CASE WHEN f.kon='K' THEN f.indhold ELSE 0 END) * 100.0 / SUM(CASE WHEN f.kon='TOT' THEN f.indhold ELSE NULL END) as pct_women FROM fact.ligedb2 f JOIN dim.nuts d ON f.komk=d.kode WHERE f.kandidat='VK' AND f.alder='TOT' AND f.tid='2021-01-01' AND d.niveau=3 GROUP BY d.titel ORDER BY pct_women;