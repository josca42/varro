table: fact.inst15
description: Uddannelsesinstitutioner med erhvervsfaglige uddannelser efter status, institution, uddannelse, herkomst, køn, alder og tid
measure: indhold (unit Antal)
columns:
- fstatus: values [B=Elever pr. 1. oktober, F=Fuldført, T=Tilgang]
- insti: values [TOT=I alt, 101401=101401 NEXT Uddannelse København, 101403=101403 Hotel- og Restaurantskolen, 101429=101429 Skoleskibet Georg Stage, 101430=101430 Skoleskibet Danmark ... 851420=851420 AMU Nordjylland, 851452=851452 SOSU Nord, 851454=851454 Professionshøjskolen University College Nordjylland, 851455=851455 Tekstilhåndværkerskolen, 861403=861403 Erhvervsskolerne Aars]
- uddannelse: values [TOT=I alt, H29=H29 Erhvervsfaglige grundforløb, H2910=H2910 Omsorg, sundhed og pædagogik (OSP), grundforløb, H291010=H291010 Sundhed, omsorg og pædagogik, grundforløb, H2915=H2915 Kontor, handel og forretningsservice (KHF), grundforløb ... H3090=H3090 Andre erhvervsfaglige uddannelser, H309010=H309010 Erhvervsfiskeri mv., H309015=H309015 Maritime uddannelser, H309020=H309020 Forsvaret, H309025=H309025 Øvrige erhvervsfaglige uddannelser]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 9920=Under 20 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50OV=50 år og derover]
- tid: date range 2005-01-01 to 2024-01-01

notes:
- fstatus is a measurement selector — always filter to one value. B=elever pr. 1. oktober, F=fuldført, T=tilgang. Omitting this triples all sums.
- uddannelse has 2 levels (5-char parents, 7-char children) plus TOT. erhvervsfaglige uddannelser (EUD) use H29xx/H30xx codes with many sub-programs. Filter to one level when grouping to avoid double-counting.
- alder: TOT plus 8 age groups (9920=under 20, then 5-year bands up to 50OV). Groups are mutually exclusive and sum to TOT. EUD students skew young — 9920 (under 20) is typically the largest group.
- kon total code is '10' (Køn i alt), not 'TOT'.
- herkomst total is 'TOT'. Individual: 5=dansk, 4=indvandrere, 3=efterkommere, 0=uoplyst.
- insti: large number of institutions (erhvervsskoler, AMU centres, etc.). Use ColumnValues("inst15", "insti") to search by name.