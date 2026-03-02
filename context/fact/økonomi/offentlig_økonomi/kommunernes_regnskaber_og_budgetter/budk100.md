table: fact.budk100
description: Kommunernes budgetter, grupperinger uden tekst - efter område, funktion, dranst, ejerforhold, gruppering, art, prisenhed og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- funktion: values [2201=0.22.01 Fælles formål (jordforsyning), 2202=0.22.02 Boligformål (jordforsyning), 2203=0.22.03 Erhvervsformål (jordforsyning), 2204=0.22.04 Offentlige formål (jordforsyning), 2205=0.22.05 Ubestemte formål (jordforsyning) ... 86200=8.62.00 Immaterielle anlægsaktiver, 86500=8.65.00 Omsætningsaktiver - Varebeholdninger, 86800=8.68.00 Omsætningsaktiver - Fysiske anlæg til salg, 87200=8.72.00 Hensatte forpligtelser, 87500=8.75.00 Egenkapital]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 5=5 Finansforskydninger, 6=6 Afdrag på lån, 7=7 Finansiering]
- ejer: values [1=Egne, 2=Selvejende/private, 3=Andre offentlige myndigheder, 4=Private leverandører af ikke-momsbelagte tjenesteydelser, 0=Ikke angivet]
- gruppering: values [1=001, 2=002, 3=003, 4=004, 5=005 ... 126=126, 127=127, 128=128, 200=200, 999=999 Ikke-autoriserede grupperinger]
- art: values [TOT=I alt (netto), UE=Bruttoudgifter, I=Indtægter, S0=0 Beregnede omkostninger, S1=1 Lønninger ... 89=8.9 Øvrige finansindtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2017-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- Geography column is omrade (same as regk100). Join: JOIN dim.nuts ON omrade=kode. niveau=1 gives 5 regioner, niveau=3 gives kommuner. Same extra codes: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings).
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value.
- art: TOT=netto (UE minus I). Do not sum TOT with UE or I.
- ejer has no aggregate code — sum across all ejer values to get combined totals.
- gruppering=999 = sum of non-authorised groupings. No total-gruppering code exists.
- Budget (budgetter) not actuals, starts from 2017. For historical budget data before 2017 or at function level without ownership use budk32. For actuals use regk100.
- budkc is the "with text" version using the composite dranst1 key, starting from 2019.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
