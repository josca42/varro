table: fact.fvbpct
description: Folketingsvalg efter valgresultat og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2), VAELG=ANTAL VÆLGERE]
- tid: date range 1971-01-01 to 2022-01-01

notes:
- National-level absolute counts. Four valres values: VAELG (total registered electors), GYLD_IALT (valid votes cast), UGYLD_IALT (invalid votes), BREV_IALT (postal votes counted). These overlap — GYLD+UGYLD ≈ total cast, not VAELG. Always filter to one valres at a time.
- Longest time series (1971–2022) for national election counts. Use fvpct for the corresponding percentages, fvkom for municipality breakdown.
