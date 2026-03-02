table: fact.foubud
description: Offentligt forskningsbudget efter bevillingstype, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- bevilling: values [1000=Finanslovsbevillinger (mio. kr.), 2000=Internationale bevillinger i alt (mio. kr.), 2010=EU-bevillinger (mio. kr.), 2020=Bevillinger fra Nordisk Ministerråd (mio. kr.), 3000=Kommunale og regionale midler (mio. kr.), 4000=Danmarks Grundforskningsfond (mio. kr.), 4050=PSO (mio. kr.), 5000=Vækstfonden (mio. kr.), 6000=Det offentlige forskningsbudget i alt (mio. kr.), 7000=Nationale bevillinger i alt (mio. kr.), 8000=Nationale bevillinger i pct. af BNP, 9000=Offentlige bevillinger i pct. af BNP]
- prisenhed: values [AARPRIS=Løbende priser, 08PRIS=Faste priser]
- tid: date range 2001-01-01 to 2025-01-01

notes:
- prisenhed is a measurement selector: AARPRIS=løbende priser, 08PRIS=faste 2008-priser. Every bevilling×tid row appears with both. Always filter to one: WHERE prisenhed='AARPRIS' for current prices.
- bevilling mixes two incompatible units — most codes (1000–7000) are Mio. kr. amounts, but 8000=Nationale bevillinger i pct. af BNP and 9000=Offentlige bevillinger i pct. af BNP are percentages. Never sum 8000 or 9000 with the others.
- bevilling hierarchy: 6000=Det offentlige forskningsbudget i alt aggregates multiple sources. 7000=Nationale bevillinger i alt is a sub-aggregate. 2000=Internationale i alt includes sub-item 2010 (EU) and 2020 (Nordisk Ministerråd). Don't double-count totals with their components.
- Annual (2001–2025). For detailed breakdown by sector and purpose, see foubud1/foubud4/foubud5.