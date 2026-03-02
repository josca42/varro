table: fact.evbpct
description: Europa-Parlamentsvalg efter valgresultat og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2), VAELG=ANTAL VÆLGERE]
- tid: date range 1979-01-01 to 2024-01-01

notes:
- National-level counts only (no regional breakdown). Longest historical series: 1979–2024.
- The 4 valres values are independent counts. Do not sum them — GYLD_IALT, BREV_IALT, UGYLD_IALT, and VAELG each measure different things. VAELG = total eligible voters; GYLD_IALT = valid votes cast.
- For voter turnout rate use evpct (STEMPCT) instead of computing from this table.