table: fact.regk31
description: Kommunernes regnskaber på funktioner efter område, funktion, dranst, art, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- funktion: values [2201=0.22.01 Fælles formål (jordforsyning), 2202=0.22.02 Boligformål (jordforsyning), 2203=0.22.03 Erhvervsformål (jordforsyning), 2204=0.22.04 Offentlige formål (jordforsyning), 2205=0.22.05 Ubestemte formål (jordforsyning) ... 87591=8.75.91 Modpost for takstfinansierede aktiver, 87592=8.75.92 Modpost for selvejende institutioners aktiver, 87593=8.75.93 Modpost for skattefinansierede aktiver, 87594=8.75.94 Reserve for opskrivninger, 87595=8.75.95 Modpost for donationer]
- dranst: values [1=1 Driftskonti, 2=2 Statsrefusion, 3=3 Anlægskonti, 4=4 Renter, 5=5 Finansforskydninger, 6=6 Afdrag på lån, 7=7 Finansiering]
- art: values [TOT=I alt (netto), UE=Bruttoudgifter, I=Indtægter, S0=0 Beregnede omkostninger, S1=1 Lønninger ... 89=8.9 Øvrige finansindtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts (same pattern as regk11): niveau=1 regioner, niveau=3 kommuner. Extra codes not in dim.nuts: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings). See regk11 notes for details.
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value. Same pattern as regk11.
- funktion codes are 4–5 digit integers encoding the DST x.xx.xx account format (e.g., 2201 = 0.22.01, 32320 = 3.23.20 folkeskole). 355 distinct funktion values. Use ColumnValues("regk31", "funktion") with fuzzy_match_str to find relevant codes. There are no aggregate/total funktion codes in this table — funk1-level totals are only in regk11.
- art and dranst have the same aggregate/detail structure as regk11: art='TOT' for net totals, do not sum with UE or I.
- Use this table when you need detail at the function level (e.g., folkeskole, dagtilbud, ældreområdet). Use regk11 for main-account (funk1) aggregates.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
