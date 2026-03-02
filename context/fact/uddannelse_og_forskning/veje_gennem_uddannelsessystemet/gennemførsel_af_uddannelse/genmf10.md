table: fact.genmf10
description: Gennemførsel af uddannelsesgrupper efter startuddannelse i gruppen, herkomst, køn, status ved 1 og 5 år, alder ved start på gruppe og tid
measure: indhold (unit Antal)
columns:
- startud: values [TOT=I alt, H21=H21 Gymnasiale uddannelser, H2120=H2120 Gymnasiale uddannelser, H212010=H212010 Alment gymnasiale uddannelser, H212020=H212020 Erhvervsrettede gymnasiale uddannelser ... H808035=H808035 Naturvidenskab, Ph.d., H808039=H808039 Samfundsvidenskab, Ph.d., H808059=H808059 Teknisk videnskab, Ph.d., H808080=H808080 Jordbrug, natur og miljø, Ph.d., H808090=H808090 Sundhedsvidenskab, Ph.d.]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst herkomst]
- kon: values [10=Køn i alt, M=Mænd, K=Kvinder]
- stat: values [TOT=I alt, 0=I gang i gruppen efter 1 år, 1=Fuldført i gruppen inden for 1 år, 2=Bestået deleksamen inden for 1 år, 3=Tidligt afbrud i gruppen inden for 1 år, 4=Ingen 1-årsstatus, 5=I gang i gruppen efter 5 år, 6=Fuldført i gruppen inden for 5 år, 7=Frafald i gruppen inden for 5 år, 8=Ingen 5-årsstatus]
- startald: values [TOT=Alder i alt, -14=Under 15 år, 15=15 år, 16=16 år, 17=17 år ... 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-=50- år]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- stat is the most important column to understand. It mixes 1-year statuses (0=i gang efter 1 år, 1=fuldført inden 1 år, 2=bestået deleksamen, 3=tidligt afbrud, 4=ingen 1-årsstatus) and 5-year statuses (5=i gang efter 5 år, 6=fuldført inden 5 år, 7=frafald, 8=ingen 5-årsstatus). Both groups independently sum to TOT. Never sum across all stat values — it triples the count. To get a cohort size, use stat='TOT'. To get 5-year completion rates, filter stat IN ('5','6','7','8') and compute fractions.
- startud is a 3-level hierarchy encoded in the code length: TOT (grand total), 3-char codes (H21–H80, 7 main education types, sum to TOT), 5-char codes (sub-types, e.g. H2120), 7-char codes (71 detailed programmes). Filter to one level to avoid double-counting — e.g. WHERE LENGTH(startud)=3 AND startud != 'TOT' for the 7 main types. ColumnValues("genmf10", "startud") shows all 89 codes.
- herkomst total code is 'TOT' (not '0' like in ligeub5/ligeui5). Other values: 5=dansk oprindelse, 4=Indvandrere, 3=Efterkommere, 0=Uoplyst. No western/non-western split — use ligeub5 if that detail is needed.
- kon total is '10' (not 'TOT'). Values: 10=Køn i alt, M=Mænd, K=Kvinder.
- To get total students in a cohort without overcounting: SELECT startud, SUM(indhold) FROM fact.genmf10 WHERE stat='TOT' AND herkomst='TOT' AND kon='10' AND startald='TOT' AND LENGTH(startud)=3 AND startud != 'TOT' GROUP BY startud.
- No duplicate rows — data is clean (1.37M rows, all distinct keys).