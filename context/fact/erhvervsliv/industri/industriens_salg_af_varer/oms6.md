table: fact.oms6
description: Industriens salg (år) efter branche (DB07), omsætningstype og tid
measure: indhold (unit 1.000 kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- omstype: values [SAMLET=SAMLET OMSÆTNING, EGVARE=SALG AF EGNE VARER I ALT, EGVARET1=Salg af egenproducerede varer, EGVARET2=Salg af varer produceret af underleverandør, RABTIL=Fakturerede rabatter og tillæg, ikke fordelt på varekoder, TJENIALT=INDUSTRIELLE TJENESTEYDELSER I ALT, OPSTIL=Opstillingsarbejde for andre, REP=Reparationsarbejde for andre, LOEN=Lønarbejde for andre, HANDEL=Salg af handelsvarer, ANDEN=Anden omsætning]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/db.md

notes:
- Annual counterpart to oms5. No saeson column — one fewer filter needed.
- branche07 uses same custom survey classification as oms5 — dim.db join does NOT work. Use ColumnValues("oms6", "branche07") for labels.
- omstype is hierarchical — same structure as oms5. Filter to a single level: e.g., omstype='SAMLET' for total turnover. Do not sum across multiple omstype values.