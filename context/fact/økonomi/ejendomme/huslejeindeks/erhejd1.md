table: fact.erhejd1
description: Lejeindeks for erhvervsejendomme (eksperimentel statistik) efter ejendomskategori, enhed og tid
measure: indhold (unit Indeks)
columns:
- ejendomskate: values [564=Boliger, 566=Kontor, 568=Butik, 570=Industri]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2021-01-01 to 2025-07-01

notes:
- `tal` is a measurement selector — every ejendomskate repeats 3 times (100=Indeks, 210=QoQ%, 310=YoY%). Always filter to one value; `tal=100` for index levels.
- This is experimental statistics (eksperimentel statistik) — treat results as indicative rather than official.
- No regional breakdown — covers all of Denmark only.
- All four ejendomskate values (564=Boliger, 566=Kontor, 568=Butik, 570=Industri) are independent categories; do not sum them.