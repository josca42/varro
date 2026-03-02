table: fact.iepct
description: Herkomstgruppernes andel af hele befolkningen 1. januar efter herkomst og tid
measure: indhold (unit Pct.)
columns:
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- tid: date range 1980-01-01 to 2025-01-01

notes:
- indhold is a percentage (share of total population). Never sum across herkomst groups — they overlap (21=Indvandrere i alt includes 24+25; 31=Efterkommere i alt includes 34+35; TOT=100%).
- To get the share of indvandrere: filter herkomst=21. For vest/ikke-vest breakdown: herkomst=24 and 25.
- Simple 2-column table — no overcounting risk beyond summing across herkomst levels.
- For counts instead of percentages, use folk2 (annual) or folk1e (quarterly).