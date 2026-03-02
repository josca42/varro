table: fact.regk4
description: Kommunernes balancer efter område, funktion og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- funktion: values [92201=9.22.01 Kontante beholdninger, 92205=9.22.05 Indskud i pengeinstitutter m.v., 92207=9.22.07 Investerings- og placeringsforeninger, 92208=9.22.08 Realkreditobligationer, 92209=9.22.09 Kommunekreditobligationer ... 97592=9.75.92 Modpost for selvejende institutioners aktiver, 97593=9.75.93 Modpost for skattefinansierede aktiver, 97594=9.75.94 Reserve for opskrivninger, 97595=9.75.95 Modpost for donationer, 97599=9.75.99 Balancekonto]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts on omrade=kode. niveau=1 gives 5 regioner, niveau=3 gives kommuner. omrade=0 = "Hele landet" (not in dim.nuts — query directly without join).
- No prisenhed column — indhold is always in 1.000 kr.
- funktion codes are 5–6 digit integers for balance sheet items in the 9.xx.xx format. No aggregate total funktion exists in this table; sum across the detail codes you need.
- Asset items (likvide aktiver 9.22.xx, tilgodehavender 9.25/9.28/9.32) are positive; liability items (kortfristet gæld 9.50–9.52, langfristet gæld 9.55.xx) are negative in the data.
- This is the only regnskab table with regional balance sheet breakdown. regk63 covers the same data at national level only but includes explicit AKTIV/PASSIV aggregate codes. Use regk4 when you need a regional balance breakdown.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
