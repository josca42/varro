table: fact.foubud
description: Offentligt forskningsbudget efter bevillingstype, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- bevilling: values [1000=Finanslovsbevillinger (mio. kr.), 2000=Internationale bevillinger i alt (mio. kr.), 2010=EU-bevillinger (mio. kr.), 2020=Bevillinger fra Nordisk Ministerråd (mio. kr.), 3000=Kommunale og regionale midler (mio. kr.), 4000=Danmarks Grundforskningsfond (mio. kr.), 4050=PSO (mio. kr.), 5000=Vækstfonden (mio. kr.), 6000=Det offentlige forskningsbudget i alt (mio. kr.), 7000=Nationale bevillinger i alt (mio. kr.), 8000=Nationale bevillinger i pct. af BNP, 9000=Offentlige bevillinger i pct. af BNP]
- prisenhed: values [AARPRIS=Løbende priser, 08PRIS=Faste priser]
- tid: date range 2001-01-01 to 2025-01-01
notes:
- CRITICAL: bevilling codes 8000 and 9000 are percentages of BNP (not mio. kr.), even though the unit header says "Mio. kr.". Always filter these out when computing monetary totals.
- bevilling hierarchy (mio. kr.): 6000 = Det offentlige forskningsbudget i alt = 1000 + 2000 + 3000 + 4000 + 4050 + 5000. 7000 = Nationale bevillinger i alt = 6000 − 2000. Sub-items: 2000 = 2010 + 2020. Never sum leaf codes together with their parent totals.
- prisenhed is a selector column: AARPRIS=løbende priser, 08PRIS=faste 2008-priser. Every bevilling/tid combination appears twice. Always filter to one prisenhed — use AARPRIS for current values, 08PRIS for real comparisons over time.
- Longest time series in the subject (2001–2025), useful for long-run budget trend analysis.
