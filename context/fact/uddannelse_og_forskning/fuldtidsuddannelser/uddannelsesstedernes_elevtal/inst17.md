table: fact.inst17
description: Professionshøjskoler efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101562=101562 CVU ØreSund, 151408=151408 CVU Storkøbenhavn, 219416=219416 Københavns Professionshøjskole (UCC), 219417=219417 Københavns Professionshøjskole, 340401=340401 Professionshøjskolen Absalon, 427402=427402 Den Frie Lærerskole, 461404=461404 Pædagoguddannelsen i Odense S, 461451=461451 Erhvervsakademiet Lillebælt, 561423=561423 Professionshøjskolen UC Syddanmark, 621411=621411 Professionshøjskolen Syd University College, 630401=630401 UCL Erhvervsakademi og Professionshøjskole, 751468=751468 Danmarks Medie- og Journalisthøjskole, 791413=791413 Professionshøjskolen VIA University College, 851454=851454 Professionshøjskolen University College Nordjylland]
- uddannelse: values [TOT=I alt, H40=H40 Korte videregående uddannelser, KVU, H4024=H4024 Medier og kommunikation, KVU, H402415=H402415 Multimediedesign, KVU, H4038=H4038 Samfundsfaglig, Økonomisk-Merkantil, KVU ... H508915=H508915 Ergo- og fysioterapeut, MVU, H508920=H508920 Jordemoder, MVU, H508930=H508930 Radiograf, MVU, H508935=H508935 Sygepleje og sundhedspleje, MVU, H508945=H508945 Andre sundhedsfaglige uddannelser, MVU]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse spans KVU (H40xx) and MVU (H50xx) — professionshøjskoler offer both. 2 hierarchy levels (5-char, 7-char) plus TOT. Filter to one level when grouping.
- alder: TOT plus 8 mutually exclusive age groups.
- kon total code is '10' (Køn i alt), not 'TOT'.
- herkomst total is 'TOT'. Individual: 5=dansk, 4=indvandrere, 3=efterkommere, 0=uoplyst.
- insti: ~14 professionshøjskoler (some historical institutions like CVU ØreSund that merged). Use ColumnValues("inst17", "insti") to browse.