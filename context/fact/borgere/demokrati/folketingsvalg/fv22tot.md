table: fact.fv22tot
description: Folketingsvalget 2022 efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 1675319=D. Nye Borgerlige ... B5=3e. Den foreskrevne fremgangsmåde ved stemmeafgivning har ikke været fulgt, B6=3f. Brevstemmen var ikke afgivet indenfor de i loven nævnte frister, B7=3g. Vælgeren har afgivet mere end én brevstemme, B9=FOR SENT MODTAGNE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: values [0=HELE LANDET, 7=HOVEDSTADEN, 10=KØBENHAVNS STORKREDS, 20=1. ØSTERBRO, 21=2. SUNDBYVESTER ... 107=5. HIMMERLAND, 108=6. MARIAGERFJORD, 109=7. AALBORG ØST, 110=8. AALBORG VEST, 111=9. AALBORG NORD]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- 2022 election only. omrade has a 4-level hierarchy using its own fixed coding (NOT dim.nuts): 0=Hele landet, 7–9=Valglandsdele (3 codes), 10–19=Storkredse (10 codes), 20–111=Afstemningskredse (92 codes). Filter to one level; mixing levels double-counts.
- valres structure is identical to fvkom (50 values): aggregate codes (GYLD_IALT, VAELG, etc.), party codes (numeric), and detailed invalid-ballot sub-codes (1–32, B1–B9). Never sum all valres. Use GYLD_IALT for total valid votes, or filter to a specific party.
- For individual polling station breakdown, use fv22tota (1453 omrade codes). For candidate-level personal votes, use fv22kand (storkredse only).
- Map: storkreds-level data (omrade 10–19) → /geo/storkredse.parquet — merge on (omrade - 9)=dim_kode. Valgkreds-level data (omrade 20–111) → /geo/valgkredse.parquet — merge on (omrade - 19)=dim_kode.
