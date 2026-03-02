table: fact.evkom1
description: Europa-Parlamentsvalg efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 5897=F. SF - Socialistisk Folkeparti, 5907=I. Liberal Alliance, 431970=J. Junibevægelsen, 1962293=M. Moderaterne, 431971=N. Folkebevægelsen mod EU, 5899=O. Dansk Folkeparti, 5903=V. Venstre, Danmarks Liberale Parti, 1968075=Æ. Danmarksdemokraterne - Inger Støjberg, 5905=Ø. Enhedslisten - De Rød/Grønne, 1487618=Å. Alternativet, PERS_IALT=PERSONLIGE STEMMER I ALT, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2), UGYLD_AO=1. UGYLDIGE STEMMER AFGIVET PÅ AFSTEMNINGSSTEDET, UGYLD_BREV=2. UGYLDIGE BREVSTEMMER, VAELG=ANTAL VÆLGERE]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at niveau 3 only (99 kommuner). Use ColumnValues("nuts", "titel", for_table="evkom1") to see available kommuner.
- valres mixes aggregate rows with party-level rows. GYLD_IALT = sum of all individual party votes exactly. Never select GYLD_IALT alongside individual party rows — it double-counts. Similarly UGYLD_IALT = UGYLD_AO + UGYLD_BREV. Filter valres to one category (e.g. individual parties OR GYLD_IALT, not both).
- VAELG (antal vælgere) and PERS_IALT are independent counts, not part of the GYLD/UGYLD hierarchy.
- No national total in omrade — this table only has kommuner (niveau 3). For national totals use evbpct.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode.