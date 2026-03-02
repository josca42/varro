table: fact.bil53
description: Nyregistrerede motorkøretøjer efter område, køretøjstype, brugerforhold, drivmiddel og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- biltype: values [4000100001=Køretøjer i alt, 4000101002=Personbiler i alt, 4000102000=Varebiler i alt, 4000103000=Lastbiler i alt, 4000103030=Sættevognstrækkere i alt]
- brug: values [1000=I alt, 1100=I husholdningerne, 1200=I erhvervene]
- driv: values [20200=Drivmidler i alt, 20205=Benzin, 20210=Diesel, 20215=F-gas, 20220=N-gas, 20225=El, 20230=Petroleum, 20231=Brint, 20256=Metanol, 20258=Ætanol, 20232=Pluginhybrid, 20235=Øvrige drivmidler]
- tid: date range 2018-01-01 to 2025-10-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at 3 levels: niveau=1 (5 regioner, koder 81-85), niveau=2 (11 landsdele, koder 1-11), niveau=3 (99 kommuner). Filter d.niveau to pick granularity and avoid mixing levels (which would double-count).
- Two omrade codes not in dim.nuts: 0=Hele landet (national total), 99=Uoplyst (unknown municipality). Use omrade='0' for national totals without joining dim.nuts.
- Use ColumnValues("nuts", "titel", for_table="bil53") to see the available regions/kommuner — there are 115 matched codes so for_table filtering is useful.
- This table has 5 dimension columns: omrade, biltype, brug, driv, tid. For a simple count, fix the non-target columns: biltype='4000100001' (alle køretøjer), brug='1000' (I alt), driv='20200' (alle drivmidler). Forgetting any one inflates the result.
- biltype and driv both have I alt totals. brug also has I alt (1000). Always anchor non-target dims to their total.
- Sample: new registrations by region 2024: JOIN dim.nuts d ON f.omrade=d.kode WHERE d.niveau=1 AND biltype='4000100001' AND brug='1000' AND driv='20200' AND tid='2024-01-01'
- Only table in this subject with regional breakdown. Covers from 2018-01-01 only.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 99).
