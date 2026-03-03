table: fact.neetdiag
description: Sygehusbenyttelse i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, hoveddiagnosegruppe, bopæl, køn og tid
measure: indhold (unit -)
columns:
- statusneet: values [0=Aktive og ikke-aktive i alt, 5=Aktive, 10=Ikke-aktive (NEET)]
- bnogle: values [1080=Personer med hoveddiagnose (antal), 1090=Personer med hoveddiagnose (procent)]
- diagnosehoved: values [TOTH=Hoveddiagnosegrupper i alt, 001=Infektions- og parasitære sygdomme, 002=Ondartede svulster, 003=Godartede svulster, 004=Endokrine, ernærings- og stofskiftesygdomme, 005=Sygdomme i blod og bloddannende organer, 006=Psykiske lidelser, 007=Sygdomme i nervesystem og sanseorganer, 008=Sygdomme i kredsløbsorganer, 009=Sygdomme i åndedrætsorganer, 010=Sygdomme i fordøjelsesorganer, 011=Sygdomme i urin- og kønsorganer, 012=Sygdomme i svangerskab, under fødsel og i barselsseng, 013=Sygdomme i hud og underhud, 014=Sygdomme i knogler, bevægesystem og bindevæv, 015=Medfødte misdannelser, 016=Sygdomme i perinatalperiode, 017=Symptomer og mangelfuldt definerede tilstande, 018=Traumer, forgiftninger og anden legemsbeskadigelse, 019=Forebyggende foranstaltninger]
- bop: join dim.nuts on bop=kode; levels [1, 2]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- bnogle is a measurement selector — every other dimension combination appears 2 times (only 2 bnogle values here, unlike other NEET tables). Always filter to exactly one: bnogle=1080 (antal personer med diagnose) or bnogle=1090 (procent med diagnose).
- diagnosehoved categories (001–019) are NOT mutually exclusive — one person can receive multiple diagnosis groups in a year. Sum of individual groups (358k) far exceeds TOTH (231k). Use diagnosehoved='TOTH' for unduplicated person counts; never SUM across individual diagnosis codes.
- diagnosehoved code 016 (Sygdomme i perinatalperiode) is absent from the data — expected for a 16–24 year age group.
- statusneet=0 is the aggregate total. Filter statusneet IN (5, 10) to compare NEET vs active; never sum alongside statusneet=0.
- bop=0 is national total, not in dim.nuts. JOIN dim.nuts ON bop=kode WHERE d.niveau=1 for 5 regions, d.niveau=2 for 11 landsdele.
- kon=MOK is the both-genders total — never sum all three kon values.
- Use ColumnValues("neetdiag", "diagnosehoved") for the full list of ICD chapter names before filtering.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on bop=dim_kode. Exclude bop=0.