table: fact.bib6
description: Folkebibliotekernes økonomi efter område, indtægt/udgift og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- indtudg: values [17110=Bruttodriftregnskab, 17120=Lønudgifter, 17130=I alt, materialeudgifter, 17140=Materialeudgifter, bøger, 17150=Materialeudgifter, andre materialer, 17160=Øvrige udgifter, 17170=Indtægter, 17180=Nettodriftregnskab]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- indhold is in 1.000 kr. (thousands of DKK) for all rows.
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (97 kommuner). omrade=0 = Hele landet.
- indtudg contains aggregates and subtypes: 17110=Bruttodriftregnskab (gross total), 17180=Nettodriftregnskab (net = gross minus revenues). Don't sum across udtudg — always filter to one value.
- 17130=I alt materialeudgifter is the total for 17140 + 17150. 17120=Lønudgifter and 17130+17160=Øvrige are the main cost components summing to Bruttodrift.
- For per-library efficiency analysis, combine with bib2b (number of service locations) or laby42 (FTE per 1000 inhabitants).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
