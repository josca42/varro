table: fact.ej6
description: Prisindeks for ejendomssalg efter ejendomskategori, enhed og tid
measure: indhold (unit Indeks)
columns:
- ejendomskate: join dim.ejendom on ejendomskate=kode; levels [1, 2]
- tal: values [100=Indeks, 315=Ændring i forhold til året før (pct.)]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/ejendom.md

notes:
- `tal` is a measurement selector: 100=Indeks, 315=YoY% change. Always filter to one value.
- `ejendomskate` joins dim.ejendom. 9 niveau-1 and 10 niveau-2 codes present. Filter `d.niveau = 1` for main categories, `d.niveau = 2` for subcategories. Don't mix niveaus.
- Annual price index from 1992. For quarterly data, use ej5 instead. Note: ej6 ends 2024 while ej5 is current.