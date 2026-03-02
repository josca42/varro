table: fact.strfna14
description: Skyldige personer efter statsborgerskab, herkomst, afgørelsestype og tid
measure: indhold (unit Antal)
columns:
- statsb: values [DANSK=Dansk, VEST=Vestligt, IKKEVEST=Ikke-vestligt]
- herkomst: values [5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere]
- afgorelse: values [0=I alt, 810=Ubetinget frihedsstraf, 820=Betinget frihedsstraf, 830=Bødestraf, 840=Tiltalefrafald, 850=Tiltale undladt, 860=Anden afgørelse, 870=Foranstaltningsdomme]
- tid: date range 2018-01-01 to 2023-01-01
notes:
- afgorelse uses a DIFFERENT coding scheme than strafna5/strafna8/strfna11. strfna14 uses 800-series codes: 0=I alt (total), 810=Ubetinget frihedsstraf, 820=Betinget frihedsstraf, 830=Bødestraf, 840=Tiltalefrafald, 850=Tiltale undladt, 860=Anden afgørelse, 870=Foranstaltningsdomme. Filter afgorelse=0 for the overall total.
- statsb: 3 values (DANSK, VEST, IKKEVEST) — no total.
- herkomst: simplified 3-way split (5=dansk oprindelse, 4=Indvandrere, 3=Efterkommere) — no total. Same coding as strfna12, different from strafna9/strfna11.
