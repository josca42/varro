table: fact.regr4
description: Regionernes balance (1000 kr.) efter område, funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1]
- funktion: values [61001=6.10.01 Kontante beholdninger, 61005=6.10.05 Indskud i pengeinstitutter mv., 61007=6.10.07 Investerings- og placeringsforeninger , 61008=6.10.08 Realkreditobligationer, 61009=6.10.09 Kommunekredits obligationer ... 67595=6.75.95 Reserve for opskrivninger, 67596=6.75.96 Akkumuleret resultat for sundhedsområdet, 67597=6.75.97 Akkumuleret resultat for det regionale udviklingsområde, 67598=6.75.98 Akkumuleret resultat for det regionale udviklingsområde, 67599=6.75.99 Balancekonto]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Code 0 = national total (not in dim.nuts); codes 81-85 = 5 regions at niveau=1. JOIN filters out the national row.
- funktion has 69 detailed balance sheet account codes (assets and liabilities mixed). All appear to be leaf nodes — no AKTIV/PASSIV aggregate rows in this table. For national aggregated assets/liabilities totals, use regr63 instead.
- No prisenhed column — simpler than the regnskab tables. No art/dranst either. Just omrade × funktion × tid.
- The 6xxxxx codes follow the standard Danish public accounts balance sheet structure: 61xxx=likvide aktiver, 62xxx=kortfristede tilgodehavender, 63xxx=langfristede tilgodehavender, 64xxx=fonds/formue, 65xxx=gæld, 66xxx=hensatte forpligtelser, 67xxx=egenkapital.
- Map: context/geo/regioner.parquet — merge on omrade=dim_kode. Exclude omrade=0.