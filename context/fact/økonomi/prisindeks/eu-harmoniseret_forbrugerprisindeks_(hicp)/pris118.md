table: fact.pris118
description: EU-harmoniseret forbrugerprisindeks med konstante skatter (HICP-CT) efter varegruppe, enhed og tid
measure: indhold (unit -)
columns:
- varegr: join dim.ecoicop on varegr=kode::text [approx]
- tal: values [100=Indeks, 200=Ændring i forhold til måneden før (pct.), 300=Ændring i forhold til samme måned året før (pct.)]
- tid: date range 2001-01-01 to 2025-09-01
dim docs: /dim/ecoicop.md

notes:
- Identical structure to pris117 (HICP) but measures HICP with constant taxes (HICP-CT). Use this table to compare price changes stripping out tax effects.
- varegr uses the same 6-digit ECOICOP coding as pris117. Apply the exact same decode logic (see pris117 notes). Special aggregate code is 'HICPCT' (not 'HICP').
- tal is the measurement selector (identical meaning to enhed in pris117): 100=index, 200=mom%, 300=yoy%. Always filter to one tal value.
- Data starts 2001-01-01 vs pris117's 1996-01-01 — shorter series.