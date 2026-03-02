table: fact.fabpct
description: Folkeafstemninger efter valgresultat og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2), VAELG=ANTAL VÆLGERE]
- tid: date range 1971-01-01 to 2022-01-01

notes:
- National level only — no geographic breakdown. Despite "pct" in the table name, indhold is Antal (counts).
- valres has aggregate codes: GYLD_IALT = valid votes, UGYLD_IALT = invalid votes. GYLD_IALT + UGYLD_IALT ≠ VAELG (non-voters excluded). Do not sum across valres codes.
- Best table for long historical series of raw national vote counts (all referendums since 1971). For the Ja/Nej breakdown by referendum, use fakom or fa22tot.