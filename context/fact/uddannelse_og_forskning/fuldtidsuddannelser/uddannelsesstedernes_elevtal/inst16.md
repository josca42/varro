table: fact.inst16
description: Erhvervsakademier efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101401=101401 NEXT Uddannelse København, 101604=101604 Københavns Erhvervsakademi (KEA), 101605=101605 Erhvervsakademiet Copenhagen Business Academy, 259404=259404 Zealand Sjællands Erhvervsakademi, 561427=561427 Erhvervsakademi SydVest, 621413=621413 IBA Erhvervsakademi Kolding, 657418=657418 Erhvervsakademi MidtVest, 730401=730401 Erhvervsakademi Dania, 751470=751470 Erhvervsakademi Aarhus]
- uddannelse: values [TOT=I alt, H40=H40 Korte videregående uddannelser, KVU, H4024=H4024 Medier og kommunikation, KVU, H402415=H402415 Multimediedesign, KVU, H4030=H4030 Kunstnerisk, KVU ... H5080=H5080 Jordbrug, natur og miljø, MVU, H508020=H508020 Jordbrugsvidenskab, MVU, H508045=H508045 Landskabsarkitektur og -forvaltning, MVU, H5089=H5089 Sundhedsfaglig, MVU, H508945=H508945 Andre sundhedsfaglige uddannelser, MVU]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse spans both KVU (H40xx) and MVU (H50xx) levels — erhvervsakademier offer korte and mellemlange uddannelser. 2 hierarchy levels (5-char parents, 7-char children) plus TOT. Filter to one level when grouping.
- alder: TOT plus 8 age groups. KVU/MVU students are older on average than gymnasium students.
- kon total code is '10' (Køn i alt), not 'TOT'.
- herkomst total is 'TOT'. Individual: 5=dansk, 4=indvandrere, 3=efterkommere, 0=uoplyst.
- insti: 9 erhvervsakademier. Use ColumnValues("inst16", "insti") to see names.