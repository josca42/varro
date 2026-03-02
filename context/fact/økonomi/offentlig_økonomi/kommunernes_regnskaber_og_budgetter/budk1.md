table: fact.budk1
description: Kommunernes budgetter, hovedkonti efter kommune, hovedkonto, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- regi07a: join dim.nuts on regi07a=kode [approx]; levels [1, 3]
- funk1: values [0=0 Byudvikling, bolig- og miljøforanstaltninger, 1=1 Forsyningsvirksomheder m.v., 2=2 Transport og infrastruktur, 3=3 Undervisning og kultur, 4=4 Sundhedsområdet, 5=5 Sociale opgaver og beskæftigelse, 6=6 Fællesudgifter og administration, 7=7 Renter, tilskud, udligning og skatter, 8=8 Balanceforskydninger, X=I alt hovedkonto 0-8]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 5=5 Finansforskydninger, 6=6 Afdrag på lån, 7=7 Finansiering]
- art: values [UE=Bruttoudgifter, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger, 00=0.0 Statuskonteringer ... 79=7.9 Øvrige indtægter, S8=8 Finansindtægter, 86=8.6 Statstilskud, 89=8.9 Øvrige finansindtægter, S9=9 Interne udgifter og indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- Geography column is regi07a (not omrade like in the regnskab tables). Join: JOIN dim.nuts ON regi07a=kode. niveau=1 gives 5 regioner, niveau=3 gives kommuner. Same extra codes as regnskab tables: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings).
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value.
- funk1='X' is the aggregate of funk1 values 0–8. Do not sum with individual funk1 codes.
- art: TOT=netto (UE minus I). Do not sum TOT with UE or I.
- Budget table (budgetter), not actuals. For actual expenditure use regk11. tid goes to 2025-01-01 (one year ahead of regk11 which ends 2024).
- Budget tables (budk1/budk32) use regi07a; regnskab tables (regk11/regk31) use omrade. The two column names refer to the same dim.nuts join.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on regi07a=dim_kode. Exclude regi07a=0.
