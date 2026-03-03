table: fact.budk32
description: Kommunernes budgetter, funktioner efter kommune, funktion, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- regi07a: join dim.nuts on regi07a=kode [approx]; levels [1, 3]
- funktion: values [2201.0=0.22.01 Fælles formål (jordforsyning), 2202.0=0.22.02 Boligformål (jordforsyning), 2203.0=0.22.03 Erhvervsformål (jordforsyning), 2204.0=0.22.04 Offentlige formål (jordforsyning), 2205.0=0.22.05 Ubestemte formål (jordforsyning) ... 86200.0=8.62.00 Immaterielle anlægsaktiver, 86500.0=8.65.00 Omsætningsaktiver - Varebeholdninger, 86800.0=8.68.00 Omsætningsaktiver - Fysiske anlæg til salg, 87200.0=8.72.00 Hensatte forpligtelser, 87500.0=8.75.00 Egenkapital]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 5=5 Finansforskydninger, 6=6 Afdrag på lån, 7=7 Finansiering]
- art: values [UE=Bruttoudgifter, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger, 00=0.0 Statuskonteringer ... 79=7.9 Øvrige indtægter, S8=8 Finansindtægter, 86=8.6 Statstilskud, 89=8.9 Øvrige finansindtægter, S9=9 Interne udgifter og indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- Geography column is regi07a (same as budk1, not omrade). Join: JOIN dim.nuts ON regi07a=kode. niveau=1 gives 5 regioner, niveau=3 gives kommuner. Same extra codes as regnskab tables: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings).
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value.
- funktion codes are stored as floats with .0 suffix (e.g., 2201.0). Use WHERE funktion=2201 or CAST(funktion AS int)=2201 in SQL. The underlying values are the same 4–5 digit account codes as regk31.
- art: TOT=netto (UE minus I). Do not sum TOT with UE or I.
- Budget table (budgetter), not actuals. For actual expenditure at function level use regk31.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on regi07a=dim_kode. Exclude regi07a=0.
