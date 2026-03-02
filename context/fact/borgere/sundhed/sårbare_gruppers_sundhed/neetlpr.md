table: fact.neetlpr
description: Sygehusbenyttelse i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, kontakttype, bopæl, køn og tid
measure: indhold (unit -)
columns:
- statusneet: values [0=Aktive og ikke-aktive i alt, 5=Aktive, 10=Ikke-aktive (NEET)]
- bnogle: values [1000=Kontakter (antal pr. person), 1005=Personer med kontakt (antal), 1010=Personer med kontakt (procent)]
- ktype: values [TOTAL3=Kontakttype i alt, 10=Indlæggelse, 20=Ambulant kontakt, 30=Akut-ambulant kontakt]
- bop: join dim.nuts on bop=kode; levels [1, 2]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- bnogle is a measurement selector — every other dimension combination appears 3 times. Always filter to exactly one: bnogle=1000 (kontakter pr. person), bnogle=1005 (antal personer med kontakt), or bnogle=1010 (procent med kontakt).
- ktype contact categories (10=indlæggelse, 20=ambulant, 30=akut-ambulant) are NOT mutually exclusive for persons — one person can have both an indlæggelse and an ambulant contact in the same year. Sum of ktype parts (301k) exceeds TOTAL3 (231k). Use ktype='TOTAL3' for unduplicated person counts; never SUM across ktype 10/20/30.
- statusneet=0 is the aggregate total. Filter statusneet IN (5, 10) to compare NEET vs active; never sum alongside statusneet=0.
- bop=0 is national total, not in dim.nuts. JOIN dim.nuts ON bop=kode WHERE d.niveau=1 for 5 regions, d.niveau=2 for 11 landsdele.
- kon=MOK is the both-genders total — never sum all three kon values.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on bop=dim_kode. Exclude bop=0.