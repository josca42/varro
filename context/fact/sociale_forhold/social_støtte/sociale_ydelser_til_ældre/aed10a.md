table: fact.aed10a
description: Forebyggende hjemmebesøg, personer og besøg efter område, hjemmebesøg, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- hjembesoeg: values [380=Personer der har modtaget et eller flere hjemmebesøg, 381=Gennemførte besøg]
- alder: values [50=Alder i alt, 450=Under 75 år, 900=75 år og derover, 550=75 år, 575=76-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2016-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner) present. Filter WHERE d.niveau=3 for kommuner or d.niveau=1 for regioner — mixing levels double-counts. omrade=0 is the national total (not in dim).
- hjembesoeg: 380=persons who received >=1 visit, 381=visits conducted. These measure different things (a person can receive multiple visits). Always filter to one value.
- alder=50 is the overall total. 450=under 75, 900=75+ are sub-totals. 550/575/600/700/800 are individual bands inside the 75+ sub-total. Do not sum sub-totals with individual bands. Use alder=50 for all-age totals.
- koen=100 is the total; 200=mænd, 300=kvinder. Filter koen=100 for gender-neutral totals.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
