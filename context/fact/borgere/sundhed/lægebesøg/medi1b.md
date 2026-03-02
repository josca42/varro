table: fact.medi1b
description: Salg af receptpligtig medicin (eksperimentel statistik) efter område, medicintype, nøgletal, køn, aldersgruppe og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- medicintype: values [TOT=MEDICINTYPE I ALT, A=A FORDØJELSESORGANER OG STOFSKIFTE, A01=A01 Midler mod sygdomme i mundhulen, A02=A02 Midler mod syrerelaterede forstyrrelser, A03=A03 Midler mod funktionelle gastrointestinale forstyrrelser ... V07=V07 Alle andre non-terapeutiske produkter, V08=V08 Kontrastmidler, V09=V09 Radiofarmaka til diagnostisk brug, V10=V10 Radiofarmaka til terapeutisk brug, V20=V20 Surgical dressings]
- bnogle: values [2000=Personer, 2005=Indløste recepter]
- kon: values [0=Køn i alt, 1=Mænd, 2=Kvinder]
- agebygroup: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9000=90 år og derover]
- tid: date range 2016-01-01 to 2021-01-01
dim docs: /dim/nuts.md
notes:
- Experimental statistics (eksperimentel). omrade joins dim.nuts with niveau 1 (5 regioner) and niveau 3 (98 kommuner). omrade=0 is national total — exclude when joining.
- bnogle is a measurement selector (2000=persons, 2005=prescriptions filled). Never aggregate across bnogle values.
- medicintype has two-level hierarchy: letter codes = major ATC groups, letter+2-digit = sub-groups. TOT=grand total. Do not sum across hierarchy levels.
- agebygroup uses 10-year groups (0009, 1019, ... 9000=90+) plus TOT. cf. medi1a for single-year ages (region-only).
- kon uses 0=køn i alt, 1=mænd, 2=kvinder. Data only through 2021.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
