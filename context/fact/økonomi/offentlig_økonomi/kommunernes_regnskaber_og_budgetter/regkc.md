table: fact.regkc
description: Kommunernes regnskaber på gruppering med tekst efter område, dranst funktion og gruppering, ejerforhold, art, prisenhed og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- dranst1: values [102201999=Drift - 0.22.01 Fælles formål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102202999=Drift - 0.22.02 Boligformål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102203999=Drift - 0.22.03 Erhvervsformål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102204999=Drift - 0.22.04 Offentlige formål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102205999=Drift - 0.22.05 Ubestemte formål - Grp. 999 Sum af ikke-autoriserede grupperinger ... 882201999=8 - 8.22.01 - Grp. 999 Kombination nedlagt, 882205999=8 - 8.22.05 - Grp. 999 Kombination nedlagt, 883227999=8 - 8.32.27 - Grp. 999 Kombination nedlagt, 893227002=Aktiver - 9.32.27 Deponerede beløb for lån m.v. - Grp. 2 Deponerede midler vedr. forsyningsvirksomheder, 893227003=Aktiver - 9.32.27 Deponerede beløb for lån m.v. - Grp. 3 Frigivne midler vedr. forsyningsvirksomheder]
- ejer: values [1=Egne, 2=Selvejende/private, 3=Andre offentlige myndigheder, 4=Private leverandører af ikke-momsbelagte tjenesteydelser, 0=Ikke angivet]
- art: values [TOT=I alt (netto), UE=Bruttoudgifter, I=Indtægter, S0=0 Beregnede omkostninger, S1=1 Lønninger ... 89=8.9 Øvrige finansindtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2018-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts (same pattern as regk11): niveau=1 regioner, niveau=3 kommuner. Extra codes not in dim.nuts: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings).
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value.
- dranst1 is a composite key encoding dranst+funktion+gruppering as a single 9-digit integer with an embedded human-readable label. 1894 distinct values. Use ColumnValues("regkc", "dranst1", fuzzy_match_str="<keyword>") to find relevant codes — fuzzy search on the text label is the fastest approach.
- dranst1 key structure: first digit = dranst (1=drift, 3=anlæg, 7=finansiering, 8=balance, 9=aktiver), next 5 digits = funktion code (same as regk31), last 3 digits = gruppering (001–999).
- art has the same aggregate/detail structure as regk11 (art='TOT' for net totals).
- Covers same granularity as regk100 but with the composite key instead of separate columns. Useful when you want to search by label text. Starts from 2018 only vs regk100 from 2007 — prefer regk100 for historical data.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
