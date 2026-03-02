table: fact.fv22tota
description: Folketingsvalget 2022 efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 1675319=D. Nye Borgerlige ... B5=3e. Den foreskrevne fremgangsmåde ved stemmeafgivning har ikke været fulgt, B6=3f. Brevstemmen var ikke afgivet indenfor de i loven nævnte frister, B7=3g. Vælgeren har afgivet mere end én brevstemme, B9=FOR SENT MODTAGNE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: values [0=HELE LANDET, 7=HOVEDSTADEN, 10=KØBENHAVNS STORKREDS, 20=1. ØSTERBRO, 1972214=1. Østerbro ... 1973556=HF&VUC Nord, Godsbanen, 1973557=Aalborghallen, 1973558=Vester Hassing Hallen, 1973559=Hals Skole, 1973560=Ulstedhallen]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- 2022 election only. Same structure as fv22tot but with individual afstemningssteder (polling stations) added: 1453 distinct omrade codes total. Low-numbered codes (0, 7–9, 10–19, 20–111) are the same geographic hierarchy as fv22tot; high-numbered codes (>1,000,000) are individual polling station IDs (afstemningssteder, e.g. Aalborghallen, specific school gyms).
- Use this table only when you need polling-station granularity. For afstemningskredse or storkredse, fv22tot is cleaner with fewer rows.
- valres identical to fvkom/fv22tot: 50 values. Filter to specific valres; never sum all.
- Map: storkreds-level data (omrade 10–19) → context/geo/storkredse.parquet — merge on (omrade - 9)=dim_kode. Valgkreds-level data (omrade 20–111) → context/geo/valgkredse.parquet — merge on (omrade - 19)=dim_kode. Polling station codes (omrade > 1,000,000) have no geo file.
