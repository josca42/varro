table: fact.fa22tot
description: Folkeafstemning om Danmarks deltagelse i det europæiske samarbejde om sikkerhed og forsvar ved at afskaffe EU-forsvarsforbeholdet 2022 efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 434284=Ja, 434285=Nej, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2) ... B5=3e. Den foreskrevne fremgangsmåde ved stemmeafgivning har ikke været fulgt, B6=3f. Brevstemmen var ikke afgivet inden for de i loven nævnte frister, B7=3g. Vælgeren har afgivet mere end en brevstemme, B9=FOR SENT MODTAGNE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: values [0=HELE LANDET, 7=HOVEDSTADEN, 10=KØBENHAVNS STORKREDS, 20=1. ØSTERBRO, 21=2. SUNDBYVESTER ... 107=5. HIMMERLAND, 108=6. MARIAGERFJORD, 109=7. AALBORG ØST, 110=8. AALBORG VEST, 111=9. AALBORG NORD]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- 2022 EU-forsvarsforbeholdet referendum only. Single tid value (2022-01-01).
- omrade uses election geography (not NUTS): 0=national, 7-9=regions (Hovedstaden/Midtjylland/etc.), 10-19=storkredse (10 total), 20+=opstillingskredse. 106 distinct omrade values total. No dim table — use ColumnValues("fa22tot", "omrade") to browse all codes and labels.
- valres has the same hierarchical structure as fakom: 434284=Ja, 434285=Nej, GYLD_IALT=Ja+Nej, UGYLD_IALT=UGYLD_AO+UGYLD_BREV, BREV_IALT=brevstemmer, VAELG=vælgere. Additionally has B1-B9 mail ballot invalidity subcategories and BREV_EJ. Always filter to a specific valres to avoid summing aggregates.
- For national totals filter omrade='0'. For storkreds breakdown filter omrade BETWEEN '10' AND '19'.
- Map: storkreds-level data (omrade 10-19) can use /geo/storkredse.parquet — merge on (omrade::integer - 9)=dim_kode. Filter omrade BETWEEN '10' AND '19'.