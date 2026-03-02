table: fact.ev24tota
description: Europa-Parlamentsvalget 2024 efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 5897=F. SF - Socialistisk Folkeparti ... B5=3e. Den foreskrevne fremgangsmåde ved stemmeafgivning har ikke været fulgt, B6=3f. Brevstemmen var ikke afgivet indenfor de i loven nævnte frister, B7=3g. Vælgeren har afgivet mere end én brevstemme, B9=FOR SENT MODTAGNE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: values [0=HELE LANDET, 7=HOVEDSTADEN, 10=KØBENHAVNS STORKREDS, 20=1. ØSTERBRO, 2550043=1. Østerbro ... 2551336=HF&VUC Nord, Godsbanen, 2551337=Aalborghallen, 2551338=Vester Hassing Hallen, 2551339=Hals Skole, 2551340=Ulstedhallen]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- 2024 election only. Most granular geography: 1404 distinct omrade values representing individual polling stations (afstemningssteder). Superset of ev24tot — ev24tot has ~106 aggregated areas; this table adds the individual polling station breakdown.
- omrade values include hierarchical aggregates (0=hele landet, storkredse, valgkredse) plus individual polling station IDs (numeric IDs like 2550043). Labels come from inline coded values, no dim table.
- Same valres structure as ev24tot. GYLD_IALT = sum of party votes. Do not mix aggregate and party-level valres in the same query.
- Use this table when asked about results at a specific polling station. For electoral district/municipal level use ev24tot or evkom1.