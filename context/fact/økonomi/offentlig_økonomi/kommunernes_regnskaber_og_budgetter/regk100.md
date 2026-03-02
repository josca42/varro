table: fact.regk100
description: Kommunernes regnskaber på gruppering uden tekst efter område, funktion, dranst, ejerforhold, gruppering, art, prisenhed og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- funktion: values [2201=0.22.01 Fælles formål (jordforsyning), 2202=0.22.02 Boligformål (jordforsyning), 2203=0.22.03 Erhvervsformål (jordforsyning), 2204=0.22.04 Offentlige formål (jordforsyning), 2205=0.22.05 Ubestemte formål (jordforsyning) ... 87591=8.75.91 Modpost for takstfinansierede aktiver, 87592=8.75.92 Modpost for selvejende institutioners aktiver, 87593=8.75.93 Modpost for skattefinansierede aktiver, 87594=8.75.94 Reserve for opskrivninger, 87595=8.75.95 Modpost for donationer]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 5=5 Finansforskydninger, 6=6 Afdrag på lån, 7=7 Finansiering]
- ejer: values [1=Egne, 2=Selvejende/private, 3=Andre offentlige myndigheder, 4=Private leverandører af ikke-momsbelagte tjenesteydelser, 0=Ikke angivet]
- gruppering: values [1=001, 2=002, 3=003, 4=004, 5=005 ... 126=126, 127=127, 128=128, 200=200, 999=999 Ikke-autoriserede grupperinger]
- art: values [TOT=I alt (netto), UE=Bruttoudgifter, I=Indtægter, S0=0 Beregnede omkostninger, S1=1 Lønninger ... 89=8.9 Øvrige finansindtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts (same pattern as regk11): niveau=1 regioner, niveau=3 kommuner. Extra codes not in dim.nuts: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings).
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value.
- art has the same aggregate/detail structure as regk11 (art='TOT' for net, do not sum TOT with UE or I).
- ejer (ownership) adds a dimension: 1=Egne institutioner, 2=Selvejende/private, 3=Andre offentlige myndigheder, 4=Private leverandører, 0=Ikke angivet. No ejer='TOT' aggregate exists — sum across all ejer values to get combined totals.
- gruppering (001–200 plus 999) is the finest-granularity breakdown — specific expenditure sub-groups within each funktion. gruppering=999 = sum of non-authorised groupings.
- This is the most granular expenditure table (funktion × dranst × ejer × gruppering × art × prisenhed). Use only when you need ownership breakdown or specific gruppering detail. For standard expenditure questions use regk31 (by function) or regk11 (by main account).
- regkc covers the same granularity but encodes dranst+funktion+gruppering as a single composite key (dranst1) with human-readable labels. regkc starts from 2018 only.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
