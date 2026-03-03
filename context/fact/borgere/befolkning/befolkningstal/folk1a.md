table: fact.folk1a
description: Befolkningen den 1. i kvartalet efter område, køn, alder, civilstand og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0=0 år, 1=1 år, 2=2 år, 3=3 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- civilstand: values [TOT=I alt, U=Ugift, G=Gift/separeret, E=Enke/enkemand, F=Fraskilt]
- tid: date range 2008-01-01 to 2025-07-01
dim docs: /dim/nuts.md

notes:
- omrade has 3 hierarchy levels in the same column: omrade='0' (Hele landet, not in dim.nuts), niveau=1 (5 regioner), niveau=3 (99 kommuner). Every person is counted at all three levels — summing without filtering inflates by 3x (verified: no-filter SUM = 17.98M vs correct 5.99M for Jan 2025).
- For national total: omrade='0'. For regions: JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=1. For municipalities: WHERE d.niveau=3. Never mix levels in the same query.
- This table has 5 dimension columns (omrade, kon, alder, civilstand, tid). Filter all non-target dimensions to their total: kon='TOT', alder='IALT', civilstand='TOT'. Forgetting any one inflates the sum.
- alder has 126 individual ages (0–125) plus IALT. For age groups, aggregate in SQL with CASE expressions — there is no pre-aggregated age-group dimension.
- civilstand G=Gift/separeret covers both married and legally separated in one code.
- omrade=0 (Hele landet) is not in dim.nuts — it exists in the fact table but has no dim row. Use it as a literal filter, not via the dim join.
- ColumnValues("nuts", "titel", for_table="folk1a") shows the 104 geographic codes present in this table.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.