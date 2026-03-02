table: fact.livmus03
description: Antal koncertarrangører efter arrangørtype, sektor, branche (DB07) og tid
measure: indhold (unit Antal)
columns:
- arrangeor: values [103005=Folkekirke, 103010=Kulturhus, 103015=Landsdelsorkester, 103020=Musikfestival, 103025=Musikforening, 103030=Regionalt spillested, 103035=Spillested, 103080=Professionel koncertarrangør, 103040=Øvrig koncertarrangør]
- sektor: values [TOT=I alt, 90=Statslig, 91=Kommunal, 92=Privat, 99=Uoplyst]
- branchekult: values [TOT=TOT Erhverv i alt, 1=1 Landbrug, skovbrug og fiskeri, 2=2 Industri, råstofindvinding og forsyningsvirksomhed, 3=3 Bygge og anlæg, 4=4 Handel og transport mv., 5=5 Information og kommunikation, 6=6 Finansiering og forsikring, 7=7 Ejendomshandel og udlejning, 8=8 Erhvervsservice, 9=9 Offentlig administration, undervisning og sundhed, 10=10 Kultur, fritid og anden service, 11=11 Uoplyst aktivitet]
- tid: date range 2018-01-01 to 2023-01-01

notes:
- sektor='TOT' and branchekult='TOT' are totals. To count organizers by sector, filter branchekult='TOT'. To count by industry branch, filter sektor='TOT'. Never sum across a column that includes a total code.
- arrangeor has no total code — all 9 values are individual organizer types, sum freely.
- branchekult covers all industries (1–11 + TOT). Most non-culture branches (1–9, 11) will have near-zero counts; branch 10 (Kultur, fritid og anden service) is the relevant one.