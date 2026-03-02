table: fact.aulk09
description: Ledighedsforløb efter varighed, enhed, ydelsestype, køn og tid
measure: indhold (unit -)
columns:
- kmdr: values [26=26 uger, 39=39 uger, 52=52 uger, 78=78 uger, 104=104 uger, 130=130 uger, 156=156 uger]
- enhed: values [1=Personer(antal), 4=Personer i pct. af ledighedsberørte, 5=Personer per 1.000 i arbejdsstyrken   ]
- ydelsestype: values [TOT=I alt, 01=Dagpenge, 02=Kontanthjælp mv.]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-07-01 to 2025-05-01

notes:
- kmdr values are CUMULATIVE thresholds — persons with ≥N weeks of unemployment in the reference period. kmdr=52 is a strict subset of kmdr=26. Never sum across kmdr values. In 2024: kmdr=26 had 28,329 persons, kmdr=52 had 10,621 (subset).
- enhed is a measurement selector: 1=antal, 4=pct af ledighedsberørte, 5=per 1000 i arbejdsstyrken. Always filter to one enhed.
- ydelsestype: 01=Dagpenge and 02=Kontanthjælp are mutually exclusive components; TOT=I alt is their sum.
- Companion to aulk10 (same structure but alder instead of kon). National only.