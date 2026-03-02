table: fact.esspros1
description: Sociale udgifter efter Foranstaltning, ydelsestype og tid
measure: indhold (unit Mio. kr.)
columns:
- foranstalt: join dim.esspros on foranstalt=kode [approx]
- ydelsestype: values [1=Sociale udgifter i alt, 2=Kontantydelser før skat, 3=Kontantydelser efter skat, 4=Naturalieydelser]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/esspros.md

notes:
- foranstalt does NOT join dim.esspros. The dim uses codes 1–9 (niveau 1) and 11–50 (niveau 2), but foranstalt uses a completely different 4-digit system. Use ColumnValues("esspros1", "foranstalt") to get all 61 code-label pairs.
- foranstalt hierarchy: X000 = main category total, XX05/XX10/... = subcategories. E.g. 1000=total, 1100="1 SYGDOM OG SUNDHED", 1105="1.1 Offentlig sygeskring". Never mix X000 totals with their subcategories — that double-counts.
- ydelsestype is a measurement selector: 1=Sociale udgifter i alt, 2=Kontantydelser før skat, 3=Kontantydelser efter skat (subset of 2), 4=Naturalieydelser. Never sum across ydelsestype — always filter to a single value. For total expenditure use ydelsestype=1.
- Each (foranstalt, tid) combination has 4 rows (one per ydelsestype). Forgetting to filter ydelsestype quadruples the sum.