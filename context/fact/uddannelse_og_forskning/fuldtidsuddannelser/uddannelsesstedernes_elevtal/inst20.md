table: fact.inst20
description: Universiteter efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101530=101530 IT-Universitetet i København, 101561=101561 Det Informationsvidenskabelige Akademi, 101582=101582 Københavns Universitet, 147406=147406 Copenhagen Business School - Handelshøjskolen, 173405=173405 Danmarks Tekniske Universitet, 265407=265407 Roskilde Universitet, 461437=461437 Syddansk Universitet, 751465=751465 Aarhus Universitet, 851446=851446 Aalborg Universitet]
- uddannelse: values [TOT=I alt, H50=H50 Mellemlange videregående uddannelser, MVU, H5020=H5020 Pædagogisk, MVU, H502025=H502025 Andre pædagogiske uddannelser, MVU, H5024=H5024 Medier og kommunikation, MVU ... H805910=H805910 Teknisk videnskab uden nærmere angivelse, Ph.d., H8080=H8080 Jordbrug, natur og miljø, Ph.d., H808010=H808010 Jordbrug, natur og miljø uden nærmere angivelse, Ph.d., H8090=H8090 Sundhedsvidenskab, Ph.d., H809050=H809050 Medicin, Ph.d.]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse has 3 hierarchy levels: 3-char (H50=MVU, H60, H70=LVU, H80=Ph.d.), 5-char (subject group), 7-char (specific degree). TOT covers all. When grouping by uddannelse, filter to one level (e.g. WHERE LENGTH(uddannelse) = 7 for most detailed, or LENGTH = 3 for broad LVU/Ph.d. split). This is the only inst table with 3-level hierarchy.
- 9 universities: KU, DTU, CBS, RUC, SDU, AAU, AU, ITU, plus Det Informationsvidenskabelige Akademi.
- alder: TOT plus 8 age groups. University students skew older than gymnasium — significant presence in 20-24 and 25-29.
- kon total code is '10' (Køn i alt), not 'TOT'.
- herkomst total is 'TOT'. Includes Ph.d. students (often international) so herkomst breakdown can be more varied here.
- Use ColumnValues("inst20", "uddannelse") to search for specific degree programs by name.