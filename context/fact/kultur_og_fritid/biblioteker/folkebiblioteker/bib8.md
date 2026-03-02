table: fact.bib8
description: Årsværk på folkebiblioteker efter område, personalekategori og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- personkat: values [10000=Årsværk i alt, 10270=Assistenter, 10275=Assistenter i beskæftigelsesordning (-2015), 10260=Bibliotekarer, 10265=Bibliotekarer i beskæftigelsesordning (-2015), 10290=Øvrigt akademisk personale, 10291=Øvrigt akademisk personale i beskæftigelsesordning (-2015), 10280=Øvrigt personale, 10285=Øvrigt personale i beskæftigelsesordning (-2015), 10297=Personale i beskæftigelsesordning]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (97 kommuner). omrade=0 = Hele landet.
- personkat: 10000=Årsværk i alt (total FTE) — don't sum this with other categories. Always filter to one.
- Several codes are deprecated after 2015 (marked "-2015"): beskæftigelsesordning variants (10275, 10265, 10291, 10285). Use 10297=Personale i beskæftigelsesordning for the aggregate historical series.
- For normalized FTE per 1000 inhabitants, use laby42 instead (which already has this calculation by kommunegruppe).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
