table: fact.neetmed
description: Køb af receptpligtig medicin i befolkningen (16-24 år) (eksperimentel statistik) efter NEET-status, nøgletal, medicintype, bopæl, køn og tid
measure: indhold (unit -)
columns:
- statusneet: values [0=Aktive og ikke-aktive i alt, 5=Aktive, 10=Ikke-aktive (NEET)]
- bnogle: values [1050=Indløste recepter (antal pr. person), 1055=Personer med indløste recepter (antal), 1060=Personer med indløste recepter (procent)]
- medicintype: values [TOTAL2=Medicintype i alt, A=A Lægemidler til fordøjelse og stofskifte, B=B Lægemidler udvundet af blod og lægemidler til bloddannende organer, C=C Lægemidler til hjerte og kredsløb, D=D Hudmidler, G=G Kønshormoner, gynækologiske lægemidler og urinvejsmidler, H=H Hormoner til systemisk brug, J=J Systemiske lægemidler mod infektionssygdomme, L=L Cancermidler og lægemidler til immunsystemet, M=M Lægemidler til muskler, led og knogler, N=N Lægemidler til nervesystemet, P=P Lægemidler til parasitter, R=R Lægemidler til åndedrætsorganer, S=S Lægemidler til sanseorganer, V=V Diverse lægemidler]
- bop: join dim.nuts on bop=kode; levels [1, 2]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- tid: date range 2019-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- bnogle is a measurement selector — every other dimension combination appears 3 times. Always filter to exactly one: bnogle=1050 (indløste recepter pr. person), bnogle=1055 (antal personer med recepter), or bnogle=1060 (procent med recepter).
- medicintype categories (A–V, ATC groups) are NOT mutually exclusive for persons — a person can use multiple medicine types. Sum of individual ATC groups (844k) far exceeds TOTAL2 (406k). Use medicintype='TOTAL2' for unduplicated person counts; never SUM across individual ATC categories.
- statusneet=0 is the aggregate total. Filter statusneet IN (5, 10) to compare NEET vs active; never sum alongside statusneet=0.
- bop=0 is national total, not in dim.nuts. JOIN dim.nuts ON bop=kode WHERE d.niveau=1 for 5 regions, d.niveau=2 for 11 landsdele.
- kon=MOK is the both-genders total — never sum all three kon values.
- ATC category names are long; use ColumnValues("neetmed", "medicintype") to get the full mapping before writing SQL filters.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on bop=dim_kode. Exclude bop=0.