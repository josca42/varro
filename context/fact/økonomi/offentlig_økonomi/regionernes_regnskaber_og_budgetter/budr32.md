table: fact.budr32
description: Region budgetter (1000 kr.) efter region, funktion, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- regi07: join dim.nuts on regi07=kode; levels [1]
- funktion: values [11001.0=1.10.01 Somatiske sygehuse, 11002.0=1.10.02 Psykiatriske sygehuse og afdelinger, 12010.0=1.20.10 Almen lægehjælp, 12011.0=1.20.11 Speciallægehjælp, 12012.0=1.20.12 Medicin ... 55200.0=5.52.00 Renter af kortfristet gæld i øvrigt, 55500.0=5.55.00 Renter af langfristet gæld, 57500.0=5.75.00 Kurstab og kursgevinster, 58000.0=5.80.00 Refusion af købsmoms, 59000.0=5.90.00 Overførsel til hovedkonto 1 og 3]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 7=7 Finansiering]
- art: values [UE=Udgifter excl. beregnede omkostninger, UI=Udgifter incl. beregnede omkostninger, TOT=I alt (netto), I=Indtægter, S0=0 Beregnede omkostninger ... 81=8.1 Finansindtægter, 85=8.5 Tilskud fra kommuner, 86=8.6 Statstilskud, 89=8.9 Øvrige finansindtægter, S9=9 Interne udgifter og indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- Budget counterpart to regr31. regi07 joins dim.nuts (code 0=national, 81-85=5 regions at niveau=1). Covers through 2025; regr31 through 2024.
- funktion has 86 detailed function codes (fewer than regr31's 110 — budgets have less line-item detail than accounts). No total/aggregate funktion code.
- prisenhed is a measurement selector: LOBM=1.000 kr., INDL=per inhabitant. Always filter to one — silently doubles sums.
- art has 42 values with the same aggregate/detail structure (TOT, UE, UI, I, S0-S9, numeric codes). Filter to one aggregate value.
- dranst: 5 account types. Same pitfall as regr31.
- To compare budget vs. actual: join budr32 with regr31 on regi07+funk1+dranst+art+prisenhed+tid (note: budr32 uses funktion, regr31 uses funk1 — same column, different name).
- Map: /geo/regioner.parquet — merge on regi07=dim_kode. Exclude regi07=0.