table: fact.strfna11
description: Skyldige personer efter afgørelsestype, herkomst og tid
measure: indhold (unit Antal)
columns:
- afgorelse: values [11=11 Ubetinget frihedsstraf, 12=12 Betinget frihedsstraf, 2=2 Bødeafgørelse, 3=3 Tiltalefrafald, 4=4 Tiltale undladt, 5=5 Anden afgørelse, 511=511 Foranstaltningsdomme]
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 2000-01-01 to 2023-01-01
notes:
- afgorelse has 7 verdict types, no total row: 11=Ubetinget frihedsstraf, 12=Betinget frihedsstraf, 2=Bødeafgørelse, 3=Tiltalefrafald, 4=Tiltale undladt, 5=Anden afgørelse, 511=Foranstaltningsdomme. Same coding as strafna5/strafna8.
- herkomst is hierarchical: 21=Indvandrere i alt (sum of 24+25), 31=Efterkommere i alt (sum of 34+35). TOT=1+21+31. Pick one consistent level to avoid double-counting.
