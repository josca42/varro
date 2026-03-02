table: fact.kvbpct
description: Valg til kommunalbestyrelser efter valgresultat og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2), VAELG=ANTAL VÆLGERE]
- tid: date range 1970-01-01 to 2021-01-01

notes:
- National-level only — no regional breakdown. Three rows per election year: VAELG (registered voters), GYLD_IALT (total valid votes), UGYLD_IALT (total invalid votes). Filter valres to the count you need.
- For turnout and invalid rates (%) use kvpct. For regional breakdown of vote counts use kvres.