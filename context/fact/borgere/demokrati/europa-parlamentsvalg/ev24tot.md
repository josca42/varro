table: fact.ev24tot
description: Europa-Parlamentsvalget 2024 efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 5897=F. SF - Socialistisk Folkeparti ... B5=3e. Den foreskrevne fremgangsmåde ved stemmeafgivning har ikke været fulgt, B6=3f. Brevstemmen var ikke afgivet indenfor de i loven nævnte frister, B7=3g. Vælgeren har afgivet mere end én brevstemme, B9=FOR SENT MODTAGNE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: values [0=HELE LANDET, 7=HOVEDSTADEN, 10=KØBENHAVNS STORKREDS, 20=1. ØSTERBRO, 21=2. SUNDBYVESTER ... 107=5. HIMMERLAND, 108=6. MARIAGERFJORD, 109=7. AALBORG ØST, 110=8. AALBORG VEST, 111=9. AALBORG NORD]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- 2024 election only. omrade uses electoral geography (not NUTS/kommuner): 0=hele landet, then storkredse (7–9), then valgkredse (10+). ~106 distinct omrade values. No dim table — omrade labels are inline coded values.
- valres mixes aggregate and party-level rows exactly like evkom1. GYLD_IALT = sum of all party votes. Do not mix aggregate and party rows in the same query.
- Includes detailed invalid postal ballot reason codes (B1–B9) in valres, useful for analysing specifc rejection reasons.
- For commune-level breakdown use evkom1 instead (NUTS kommuner). For polling-station-level data use ev24tota.
- Map: storkredse (omrade 10–19) → context/geo/storkredse.parquet, merge on (omrade - 9)=dim_kode. Valgkredse (omrade 20–111) → context/geo/valgkredse.parquet, merge on (omrade - 19)=dim_kode. Exclude omrade ≤ 9 (totals/sub-regional groups).