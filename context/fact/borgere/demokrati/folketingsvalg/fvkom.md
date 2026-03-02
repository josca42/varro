table: fact.fvkom
description: Folketingsvalg efter valgresultat, område og tid
measure: indhold (unit Antal)
columns:
- valres: values [GYLD_IALT=GYLDIGE STEMMER I ALT, 5891=A. Socialdemokratiet, 5893=B. Radikale Venstre, 5895=C. Det Konservative Folkeparti, 1675319=D. Nye Borgerlige ... 29=2i. Stemmeseddel ikke tilvejebragt af ministeren, 30=2j. Konvolut med påskrift eller påklæbning, 31=2k. Stemmeseddel med tegning, påskrift eller påklæbning, 32=2l. Udfyldt på bagsiden, iturevet mv., andet særpræg, VAELG=ANTAL VÆLGERE]
- omrade: join dim.nuts on omrade=kode; levels [3]
- tid: date range 2007-01-01 to 2022-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts niveau 3 only (99 kommuner). Clean 99/99 match. Use ColumnValues("nuts", "titel", for_table="fvkom") to browse kommuner.
- valres has 50 distinct values: aggregate summary codes (GYLD_IALT, UGYLD_IALT, BREV_IALT, PERS_IALT, UDENFOR_IALT, VAELG), party vote codes (numeric IDs like 5891=A), and 32 detailed invalid-ballot sub-codes (1–32). Never sum all valres — it wildly overcounts. Typical queries: filter valres to a specific party code, or use GYLD_IALT for total valid votes.
- Party codes are numeric DST IDs (same as fvkand and fvpandel). Use ColumnValues("fvkom", "valres") to see the full list.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode.
