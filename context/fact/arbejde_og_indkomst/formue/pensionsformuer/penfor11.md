table: fact.penfor11
description: Pensionsformue for personer bosat i Danmark efter pensionsform, beskatning, alder, køn, enhed og tid
measure: indhold (unit -)
columns:
- pensionsform: values [31=Alle pensionsformer, 5A=Livsvarig pension (ekskl. ATP), 6=Ratepension, 23=Aldersopsparing mv., 24=Kapitalopsparing mv., 25=ATP (livsvarig)]
- beskat: values [30=Pensionsformue i alt, 32=Pensionsformue efter skat (ikke-beskattede indgår med 60 pct.)]
- alder: values [TOT18=Alder i alt (18 år og derover), 18-24=18-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9000=90 år og derover]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- enhed: values [ANT=Personer i befolkningen d. 31.12 (antal), GNS=Gennemsnit (kr.), Q1=Nedre kvartil (kr.), MED=Median (kr.), Q3=Øvre kvartil (kr.)]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — every other dimension combination is repeated 5 times (ANT, GNS, Q1, MED, Q3). Always filter to exactly one enhed. For "how many persons" use ANT; for "average wealth" use GNS; for distribution use Q1/MED/Q3.
- beskat has 2 alternative valuations: 30=pensionsformue i alt (gross, before tax) and 32=pensionsformue efter skat (non-taxed savings counted at 60%). These are two different views of the same population — never sum beskat values.
- pensionsform=31 (alle pensionsformer) is the total; 5A/6/23/24/25 are components. Summing components 5A+6+23+24+25 equals 31. Filter to one value.
- alder=TOT18 is the aggregate (18+); remaining codes are 5-year bands. koen=MOK is the total.
- This table covers persons bosat i Danmark. Compare to penfor20 which also covers persons with pensions but residing abroad (popu=ALLE).