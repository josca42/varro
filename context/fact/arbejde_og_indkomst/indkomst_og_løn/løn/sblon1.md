table: fact.sblon1
description: Standardberegnet lønindeks efter branche (DB07), sektor, enhed og tid
measure: indhold (unit -)
columns:
- branche07: join dim.db on branche07=kode::text; levels [2]
- sektor: values [1000=Sektorer i alt, 1032=Offentlig forvaltning og service, 1016=Stat (inklusiv sociale kasser og fonde), 1018=Kommuner og regioner i alt, 1020=Regioner, 1025=Kommuner, 1046=Virksomheder og organisationer]
- varia1: values [100=Indeks, 215=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2016-01-01 to 2025-04-01
dim docs: /dim/db.md
notes:
- WARNING: The documented dim.db join (branche07=kode::text) is WRONG — same issue as lons40. The fact table uses DST aggregate codes (1-10, A-S, CA/CB/... sub-sections) that don't correspond to dim.db entries. Use ColumnValues("sblon1", "branche07") for correct labels (51 codes including sub-sections of C, J, M, Q).
- varia1 is a measurement-type selector: 100=index value, 215=year-on-year pct change. ALWAYS filter to one value — every branche07/sektor combination appears twice (once per measure type).
- sektor has overlapping aggregates: same structure as lons30. Filter to one value.
- Quarterly frequency (tid runs Q1 2016 to Q2 2025). Useful for tracking wage index trends over time by industry.
- For a simple wage index time series: WHERE varia1='100' AND sektor='1000' AND branche07='TOT'.
