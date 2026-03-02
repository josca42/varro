table: fact.aulk10
description: Ledighedsforløb efter varighed, enhed, ydelsestype, alder og tid
measure: indhold (unit -)
columns:
- kmdr: values [26=26 uger, 39=39 uger, 52=52 uger, 78=78 uger, 104=104 uger, 130=130 uger, 156=156 uger]
- enhed: values [1=Personer(antal), 4=Personer i pct. af ledighedsberørte, 5=Personer per 1.000 i arbejdsstyrken   ]
- ydelsestype: values [TOT=I alt, 01=Dagpenge, 02=Kontanthjælp mv.]
- alder: values [TOT=Alder i alt, 1629=16-29 år, 3049=30-49 år, 5099=50 år og derover]
- tid: date range 2008-07-01 to 2025-05-01

notes:
- kmdr values are CUMULATIVE thresholds (≥N weeks unemployed). Never sum across kmdr — each is a subset of the one before. See aulk09 for details.
- enhed is a measurement selector (1/4/5). Always filter to one.
- alder uses compact 3-band grouping (16-29/30-49/50+). Companion to aulk09 (alder vs kon breakdown).