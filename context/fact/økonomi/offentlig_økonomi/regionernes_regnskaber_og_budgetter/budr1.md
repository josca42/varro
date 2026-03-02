table: fact.budr1
description: Region budgetter (1000 kr.) efter region, hovedkonto, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- regi07: join dim.nuts on regi07=kode; levels [1]
- funk1: values [X=I alt hovedkonto 0-5, 1=1 Sundhed, 2=2 Social og specialundervisning, 3=3 Regional udvikling, 4=4 Fælles formål og administration, 5=5 Renter m.v.]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 7=7 Finansiering]
- art: values [UE=Udgifter excl. beregnede omkostninger, UI=Udgifter incl. beregnede omkostninger, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger ... 81=8.1 Finansindtægter, 85=8.5 Tilskud fra kommuner, 86=8.6 Statstilskud, 89=8.9 Øvrige finansindtægter, S9=9 Interne udgifter og indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- Budget counterpart to regr11, but uses regi07 (not omrade). regi07 joins dim.nuts (code 0=national, 81-85=5 regions). Covers through 2025; regr11 through 2024.
- funk1 has 6 high-level sector codes (X=all, 1-5). Same as regr11.
- prisenhed is a measurement selector: LOBM=1.000 kr., INDL=per inhabitant. Always filter to one.
- art has 42 values (TOT, UE, UI, I, S0-S9, numeric codes). Filter to one aggregate value.
- dranst: 5 account types (1=drift, 2=statsrefusion, 3=anlæg, 4=renter, 7=finansiering).
- Use this table for a quick budget overview by sector and region. For detailed function-level budgets, use budr32.
- Map: context/geo/regioner.parquet — merge on regi07=dim_kode. Exclude regi07=0.