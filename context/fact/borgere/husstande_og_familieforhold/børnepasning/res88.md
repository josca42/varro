table: fact.res88
description: Årstakster i børnepasning efter område, foranstaltningsart og tid
measure: indhold (unit Kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- institution: values [F47=Kommunal dagpleje (0-2 år) inklusiv frokost, F03=Vuggestue (0-2 år), F48=Kommunal dagpleje (3-5 år) inklusiv frokost, F50=Børnehave (3-5 år), F51=Aldersintegreret inst. (0-2 år), F52=Aldersintegreret inst. (3-5 år), F60=Aldersintegreret inst. (6-9 år), F53=Fritidshjem (6-9 år), F45=Fritidsklubber (10-13 år), F54=Ungdomsklubber (14-18 år), F55=Skolefritidsordninger (6-9 år), F56=Skolefritidsordninger (10-13 år), F58=Takst for frokost 0-2 år (2012- ), F59=Takst for frokost 3-5 år (2012- )]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/nuts.md
notes:
- omrade contains kode 0 (national total/average, not in dim.nuts) and niveau 3 (98 kommuner) only — no regional breakdown.
- indhold is an annual rate in Kr. (not a count). Do NOT sum across institution types — each institution type has an independent price. Compare rates across municipalities or over time for the same institution type.
- Not all institution types are available in all municipalities (e.g., F48=Kommunal dagpleje 3-5 år only reported in 3 kommuner; F45=Fritidsklubber only in 25). Filter to specific institution types and expect sparse data.
- F58 (frokost 0-2 år) and F59 (frokost 3-5 år) are separate frokost surcharge rates, only available from 2012. The main rates F47 and F50 already note "inklusiv frokost".
- Longest time series in subject: 2007-2025, making it useful for price trend analysis across institution types.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
