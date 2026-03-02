table: fact.fakom
description: Folkeafstemninger efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 434284=Ja, 434285=Nej, BREV_IALT=BREVSTEMMER I BETRAGTNING, UGYLD_IALT=UGYLDIGE STEMMER I ALT (1+2) ... 30=2j. Anden påskrift eller tegning eller særpræg iøvrigt, 31=2k. Stemmeseddel ikke tilvejebragt af ministeren, 32=2l. Andet eller mere end en stemmeseddel i konvolutten, 33=2m. Konvolut med påskrift eller påklæbning, VAELG=ANTAL VÆLGERE]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2014-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- Only covers 3 referendums: 2014 (Retsforbeholdet), 2015 (JHA-forbeholdet), 2022 (EU-forsvarsforbeholdet). Use tid to filter to a specific one.
- omrade joins dim.nuts at niveau=3 only (99 kommuner). Use ColumnValues("nuts", "titel", for_table="fakom") to see all 99.
- valres has hierarchical aggregate codes — always filter to avoid double-counting. Key codes: 434284=Ja, 434285=Nej, VAELG=antal vælgere, GYLD_IALT=gyldige stemmer i alt (=Ja+Nej), UGYLD_IALT=ugyldige stemmer i alt (=UGYLD_AO+UGYLD_BREV), BREV_IALT=brevstemmer i betragtning. Codes 1-11 are UGYLD_AO subcategories; 21-33 are UGYLD_BREV subcategories.
- For a simple Ja/Nej by kommune: filter valres IN ('434284', '434285') and pick a single tid. Example: SELECT d.titel, f.valres, f.indhold FROM fact.fakom f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.tid='2022-01-01' AND f.valres IN ('434284', '434285').
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.