table: fact.uheldk7
description: Færdselsuheld med personskade efter uheldsart, område, by/landområde, uheldssituation og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- byland: values [1=I byzone, 2=I landzone]
- uheldsit: values [0=Eneuheld, 100=Indhentningsuheld, 200=Mødeuheld, 300=Svingningsuheld mellem medkørende, 400=Svingningsuheld mellem modkørende, 500=Uheld mellem krydsende køretøjer, 600=Svingningsuheld mellem krydsende køretøjer, 700=Parkeringsuheld, 800=Fodgængeruheld, 900=Forhindringsuheld, 999=Uoplyst]
- tid: date range 1998-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts on omrade=kode. The fact table has niveau 1 (5 regioner) and niveau 3 (98 kommuner) — mix both levels in the same query without filtering d.niveau and you double-count.
- omrade='0' means Hele landet (national total) and is NOT in dim.nuts. Use it directly without a join; ColumnValues("uheldk7", "omrade") lists it as id=0/text="Hele landet".
- uhelda=0 (Alle uheld) is an aggregate — always filter.
- uheldsit=0 means Eneuheld (single-vehicle), NOT a total.
- byland has no total code (I byzone / I landzone only). Sum both for national counts.
- Sample query — accidents by kommune in 2024: SELECT d.titel, SUM(f.indhold) FROM fact.uheldk7 f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.tid='2024-01-01' AND d.niveau=3 AND f.uhelda='0' AND f.byland IN ('1','2') AND f.uheldsit IN ('0','100','200','300','400','500','600','700','800','900','999') GROUP BY d.titel ORDER BY SUM(f.indhold) DESC;
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
