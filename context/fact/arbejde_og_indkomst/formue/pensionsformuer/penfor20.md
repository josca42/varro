table: fact.penfor20
description: Pensionsformue efter pensionsform, selskabstype, alder, population, beskatning, enhed og tid
measure: indhold (unit -)
columns:
- pensionsform: values [31=Alle pensionsformer, 5=Livsvarig pension, 6=Ratepension, 23=Aldersopsparing mv., 24=Kapitalopsparing mv.]
- seltype: values [8=Alle selskabstyper, 16=Pensionskasser, 17=Livsforsikringsselskaber, 10=Pengeinstitutter, 11=ATP, 14=Lønmodtagernes Dyrtidsfond]
- alder: values [TOT18=Alder i alt (18 år og derover), 18-24=18-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 75-79=75-79 år, 80-84=80-84 år, 85-89=85-89 år, 9000=90 år og derover]
- popu: values [DK=Personer bosat i Danmark d. 31. december, ALLE=Alle med pension i Danmark]
- beskat: values [30=Pensionsformue i alt, 32=Pensionsformue efter skat (ikke-beskattede indgår med 60 pct.)]
- enhed: values [ANTOPS=Personer med pensionsopsparing (antal), GNSOPS=Gennemsnit pr. person (kr.), SUMOPS=Sum (1.000 kr.)]
- tid: date range 2014-01-01 to 2024-01-01

notes:
- enhed is a measurement selector — every dimension combination is repeated 3 times (ANTOPS=antal, GNSOPS=gennemsnit pr. person kr., SUMOPS=sum i 1.000 kr.). Always filter to exactly one enhed.
- popu has two mutually exclusive populations: DK=personer bosat i Danmark pr. 31. december, ALLE=alle med pension i Danmark (inkl. udlandboende danskere). Never mix or sum across popu. Equal row counts confirm every combination exists for both.
- beskat has 2 alternative valuations: 30=i alt (before tax), 32=efter skat. Pick one; never sum across beskat.
- pensionsform=31 (alle pensionsformer) is the total; 5/6/23/24 are components. Note: ATP is not included in penfor20 (unlike penfor11 which has pensionsform=25=ATP).
- seltype=8 (alle selskabstyper) is the total; 16/17/10/11/14 are institutions. Never sum total + components.
- alder=TOT18 is the aggregate (18+); remaining codes are 5-year bands.
- This is the only pensionsformue table broken down by financial institution (seltype) — use it when the question is about which types of institutions hold the pension wealth.