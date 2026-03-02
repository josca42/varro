table: fact.fa22tota
description: Folkeafstemning om Danmarks deltagelse i det europæiske samarbejde om sikkerhed og forsvar ved at afskaffe EU-forsvarsforbeholdet 2022 efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 434284=Ja, 434285=Nej, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2) ... B5=3e. Den foreskrevne fremgangsmåde ved stemmeafgivning har ikke været fulgt, B6=3f. Brevstemmen var ikke afgivet inden for de i loven nævnte frister, B7=3g. Vælgeren har afgivet mere end en brevstemme, B9=FOR SENT MODTAGNE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: values [0=HELE LANDET, 7=HOVEDSTADEN, 10=KØBENHAVNS STORKREDS, 20=1. ØSTERBRO, 1965154=1. Østerbro ... 1966505=HF&VUC Nord, Godsbanen, 1966506=Aalborghallen, 1966507=Vester Hassing Hallen, 1966508=Hals Skole, 1966509=Ulstedhallen]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- 2022 EU-forsvarsforbeholdet referendum only. Single tid value (2022-01-01).
- omrade extends fa22tot with afstemningssted (polling station) level: 1462 distinct omrade values. The rollup codes from fa22tot (0, 7-9, 10-19, 20+) are also present. Polling station codes are large integers (e.g. 1966232). Use ColumnValues("fa22tota", "omrade") to browse — the dataset is large.
- Same valres structure as fa22tot. Always filter valres to a specific code to avoid summing hierarchical aggregates.
- Use fa22tot if storkreds/opstillingskreds granularity is enough. Use fa22tota only when polling station level is required.