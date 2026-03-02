table: fact.bib2b
description: Folkebiblioteker efter område, aktivitet og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- aktivi: values [10310=Alle betjeningssteder, 10240=Servicepunkter, 10300=Betjeningssteder m. materialesamling, 10198=Hovedbiblioteker, 10200=Filialer ... 10340=Folketal (i 1.000), 10320=Folketal 0-13 år (i 1.000), 10330=Folketal 0-17 år (i 1.000), 10370=Abonnenter på lydavis, 10380=Abonnenter på servicen Biblioteket kommer]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (97 kommuner). omrade=0 = Hele landet.
- aktivi mixes different units: population counts (10340/10320/10330) are in 1.000 (thousands), while service location and subscriber counts are in Antal. Never sum across aktivi values.
- 10310=Alle betjeningssteder is the total service location count; 10198=Hovedbiblioteker and 10200=Filialer are subtypes — don't add them to the total.
- For folketal (population), use aktivi='10340' for total population in thousands.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
