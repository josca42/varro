table: fact.inst19
description: Politiet og forsvarets uddannelsesinstitutioner efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101452=101452 Søværnets Officersskole, 101512=101512 Forsvarsakademiet, 147411=147411 Hærens Officersskole, 153404=153404 Politiskolen, 189402=189402 Flyvevåbnets Officersskole, 205404=205404 Kriminalforsorgens Uddannelsescenter]
- uddannelse: values [TOT=I alt, H40=H40 Korte videregående uddannelser, KVU, H4095=H4095 Politi og forsvar mv., KVU, H409510=H409510 Politi og forsvar uden nærmere angivelse, KVU, H409515=H409515 Fængselsvæsnet, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H5095=H5095 Politi og forsvar mv., MVU, H509525=H509525 Officer i forsvaret, MVU, H70=H70 Lange videregående uddannelser, LVU, H7095=H7095 Politi og forsvar mv., LVU, H709525=H709525 Officer i forsvaret, LVU]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse spans KVU (H40xx), MVU (H50xx), and LVU (H70xx) — politi og forsvar have programs at all 3 levels. 2 hierarchy levels (5-char, 7-char) plus TOT. Filter to one level when grouping.
- Very small table: 6 institutions (Politiskolen, Forsvarsakademiet, Hærens/Søværnets/Flyvevåbnets Officersskole, Kriminalforsorgen).
- alder: TOT plus 8 age groups.
- kon total code is '10', not 'TOT'.