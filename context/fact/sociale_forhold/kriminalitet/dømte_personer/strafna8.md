table: fact.strafna8
description: Skyldige personer efter område, afgørelsestype og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- afgorelse: values [11=11 Ubetinget frihedsstraf, 12=12 Betinget frihedsstraf, 2=2 Bødeafgørelse, 3=3 Tiltalefrafald, 4=4 Tiltale undladt, 5=5 Anden afgørelse, 511=511 Foranstaltningsdomme]
- tid: date range 2005-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). Code 0 (I alt) is not in the dim — filter to a specific niveau.
- afgorelse has 7 verdict types, no total row: 11=Ubetinget frihedsstraf, 12=Betinget frihedsstraf, 2=Bødeafgørelse, 3=Tiltalefrafald, 4=Tiltale undladt, 5=Anden afgørelse, 511=Foranstaltningsdomme. Same coding as strafna5/strfna11.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
- Map: kommune data (niveau 3) can be aggregated to politikredse via dim.politikredse (niveau 2 = kommuner, niveau 1 = 12 politikredse). Use context/geo/politikredse.parquet for boundaries.
