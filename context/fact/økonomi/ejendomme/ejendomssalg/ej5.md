table: fact.ej5
description: Prisindeks for ejendomssalg efter ejendomskategori, enhed og tid
measure: indhold (unit Indeks)
columns:
- ejendomskate: join dim.ejendom on ejendomskate=kode; levels [1, 2]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 1992-01-01 to 2025-04-01
dim docs: /dim/ejendom.md

notes:
- `tal` is a measurement selector: 100=Indeks, 210=QoQ% change, 310=YoY% change. Always filter to one value — omitting this triples the result. For price level, use `tal='100'`.
- `ejendomskate` joins dim.ejendom. 9 niveau-1 codes and 10 niveau-2 codes present (not the full dim). Filter `d.niveau = 1` for main property categories, `d.niveau = 2` for subcategories. Don't mix both niveaus or you'll double-count.
- Quarterly price index from 1992. For annual data, use ej6 instead.