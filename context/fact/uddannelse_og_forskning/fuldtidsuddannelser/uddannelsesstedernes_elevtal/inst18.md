table: fact.inst18
description: Maritime uddannelsesinstitutioner efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101408=101408 Maskinmesterskolen København, 280938=280938 MARTEC - Maritime and Polytechnic University College, 443401=443401 Marstal Navigationsskole, 461403=461403 Odense Maskinmesterskole, 479404=479404 Kogtved Søfartsskole, 479412=479412 Svendborg International Maritime Academy, SIMAC, 561404=561404 Maritimt Uddannelsescenter Vest, 607403=607403 Fredericia Maskinmesterskole, 751405=751405 Aarhus Maskinmesterskole]
- uddannelse: values [TOT=I alt, H40=H40 Korte videregående uddannelser, KVU, H4038=H4038 Samfundsfaglig, Økonomisk-Merkantil, KVU, H403825=H403825 Handels- og markedsføringsøkonom mv., KVU, H4058=H4058 Teknisk, KVU, H405820=H405820 Elektronik og it, KVU, H405824=H405824 Installatør af stærkstrøms- og vvs-teknik, KVU, H4085=H4085 Maritimt, KVU, H408515=H408515 Skibsførere, KVU, H408595=H408595 Maritime uddannelser i øvrigt, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H5058=H5058 Teknisk, MVU, H505830=H505830 Maskinteknisk, MVU, H5085=H5085 Maritimt, MVU, H508515=H508515 Skibsførere, MVU, H508520=H508520 Skibsofficerer, MVU]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse spans KVU (H40xx) and MVU (H50xx) maritime programs — skibsførere and maskinteknisk. 2 hierarchy levels (5-char, 7-char) plus TOT.
- Small table: only 9 maritime institutions (maskinmesterskoler, navigationsskoler, SIMAC).
- alder: TOT plus 8 age groups.
- kon total code is '10', not 'TOT'.