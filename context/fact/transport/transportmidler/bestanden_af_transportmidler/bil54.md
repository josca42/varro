table: fact.bil54
description: Bestand af motorkøretøjer efter område, køretøjstype, brugerforhold, drivmiddel og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- biltype: values [4000100001=Køretøjer i alt, 4000101002=Personbiler i alt, 4000102000=Varebiler i alt, 4000103000=Lastbiler i alt, 4000103030=Sættevognstrækkere i alt]
- brug: values [1000=I alt, 1100=I husholdningerne, 1200=I erhvervene]
- driv: values [20200=Drivmidler i alt, 20205=Benzin, 20210=Diesel, 20215=F-gas, 20220=N-gas, 20225=El, 20230=Petroleum, 20231=Brint, 20256=Metanol, 20258=Ætanol, 20232=Pluginhybrid, 20235=Øvrige drivmidler]
- tid: date range 2018-01-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts (both smallint). dim.nuts has 3 levels: niveau 1 = 5 regioner, niveau 2 = 11 landsdele, niveau 3 = 99 kommuner. Filter d.niveau to pick granularity.
- omrade=0 (Hele landet, national total) and omrade=99 (Uoplyst) are not in dim.nuts. Use WHERE f.omrade = 0 for national totals without joining dim.nuts.
- 4 dimension columns + omrade. For a simple national total, filter all non-target dims to their aggregate codes: omrade=0, brug=1000 (I alt), driv=20200 (Drivmidler i alt), biltype=4000100001 (Køretøjer i alt). Omitting any dimension inflates the sum.
- biltype=4000100001 is the overall total. biltype=4000101002 is personbiler, 4000102000 varebiler, 4000103000 lastbiler, 4000103030 sættevognstrækkere.
- tid is monthly (2018–2025-09), not annual. Use MAX(tid) or a specific month for point-in-time counts.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.