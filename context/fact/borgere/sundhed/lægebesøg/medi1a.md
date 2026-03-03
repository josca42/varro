table: fact.medi1a
description: Salg af receptpligtig medicin (eksperimentel statistik) efter region, medicintype, nøgletal, køn, alder og tid
measure: indhold (unit Antal)
columns:
- region: join dim.nuts on region=kode; levels [1]
- medicintype: values [TOT=MEDICINTYPE I ALT, A=A FORDØJELSESORGANER OG STOFSKIFTE, A01=A01 Midler mod sygdomme i mundhulen, A02=A02 Midler mod syrerelaterede forstyrrelser, A03=A03 Midler mod funktionelle gastrointestinale forstyrrelser ... V07=V07 Alle andre non-terapeutiske produkter, V08=V08 Kontrastmidler, V09=V09 Radiofarmaka til diagnostisk brug, V10=V10 Radiofarmaka til terapeutisk brug, V20=V20 Surgical dressings]
- bnogle: values [2000=Personer, 2005=Indløste recepter]
- kon: values [0=Køn i alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- tid: date range 2016-01-01 to 2021-01-01
dim docs: /dim/nuts.md
notes:
- Experimental statistics (eksperimentel). region column (not omrade) joins dim.nuts niveau 1 only (5 regioner, kode 81-85). region=0 is national total — exclude when joining. No commune breakdown.
- bnogle is a measurement selector (2000=persons, 2005=prescriptions filled). Never aggregate across bnogle values.
- medicintype has a two-level hierarchy: letter codes (A, B, C...) are major ATC groups; letter+2-digit codes (A01, A02...) are sub-groups. TOT=grand total. Pick one level — do not sum both.
- alder has single-year ages (1-99-) plus IALT. cf. medi1b which has 10-year groups but also commune breakdown.
- kon uses 0=køn i alt, 1=mænd, 2=kvinder (not TOT/M/K). Data only through 2021.
- Map: /geo/regioner.parquet — merge on region=dim_kode. Exclude region=0.
