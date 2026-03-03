table: fact.budkc
description: Kommunernes budgetter, grupperinger med tekst - efter område, dranst funktion og gruppering, ejerforhold, art, prisenhed og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- dranst1: values [102201999=Drift - 0.22.01 Fælles formål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102202999=Drift - 0.22.02 Boligformål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102203999=Drift - 0.22.03 Erhvervsformål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102204999=Drift - 0.22.04 Offentlige formål - Grp. 999 Sum af ikke-autoriserede grupperinger, 102205999=Drift - 0.22.05 Ubestemte formål - Grp. 999 Sum af ikke-autoriserede grupperinger ... 776895003=Finansiering - 7.68.95 Anden skat på fast ejendom - Grp. 3 Dækningsafgift af forretningsejendommes grundværdi, 776895999=Finansiering - 7.68.95 Skatter - Grp. 999 Sum af ikke-autoriserede grupperinger, 776896004=Finansiering - 7.68.96 Skatter - Grp. 4 Efterbetaling og bøder, 776896005=Finansiering - 7.68.96 Skatter - Grp. 5 Frigørelsesafgift, 785500999=Finansiering - 8.55.00 Forskydninger i langfristet gæld - Grp. 999 Sum af ikke-autoriserede grupperinger]
- ejer: values [1=Egne, 2=Selvejende/private, 3=Andre offentlige myndigheder, 4=Private leverandører af ikke-momsbelagte tjenesteydelser, 0=Ikke angivet]
- art: values [TOT=I alt (netto), UE=Bruttoudgifter, I=Indtægter, S0=0 Beregnede omkostninger, S1=1 Lønninger ... 89=8.9 Øvrige finansindtægter, 91=9.1 Overførte lønninger, 92=9.2 Overførte varekøb, 94=9.4 Overførte tjenesteydelser, 97=9.7 Interne indtægter]
- prisenhed: values [LOBM=Løbende priser (1.000 kr.), INDL=Pr. indbygger, løbende priser (kr.)]
- tid: date range 2019-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts (same pattern as regk100/budk100): niveau=1 regioner, niveau=3 kommuner. Extra codes not in dim.nuts: 0 (Hele landet), 910/920/930/940/960 (municipality-type groupings).
- prisenhed is a measurement selector (LOBM vs INDL) that doubles all rows — always filter to one value.
- dranst1 is a composite key encoding dranst+funktion+gruppering as a single integer with an embedded human-readable label. Use ColumnValues("budkc", "dranst1", fuzzy_match_str="<keyword>") to find relevant codes by label text.
- dranst1 key structure mirrors regkc: first digit = dranst, next 5 digits = funktion, last 3 digits = gruppering.
- art: TOT=netto (UE minus I). Do not sum TOT with UE or I.
- Budget (budgetter) not actuals, starts from 2019. For actual expenditure use regkc (2018+). For historical budget data before 2019 use budk100 (2017+) or budk32 (2007+).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
