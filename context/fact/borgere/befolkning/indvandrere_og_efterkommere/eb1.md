table: fact.eb1
description: Børn af efterkommere 1. januar efter Oprindelig herkomst, køn, alder, oprindelsesland og tid
measure: indhold (unit Antal)
columns:
- opher: values [D=Oprindelig person med dansk oprindelse, E=Oprindelig efterkommer]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- ieland: join dim.lande_psd on ieland=kode; levels [3]
- tid: date range 2007-01-01 to 2025-01-01
dim docs: /dim/lande_psd.md

notes:
- opher = the herkomst of the grandparent/original immigrant: D=Oprindelig person med dansk oprindelse (grandparent was of Danish origin), E=Oprindelig efterkommer (grandparent was a descendant). No total row for opher.
- No total row for kon (1=Mænd, 2=Kvinder only). SUM across kon for gender-total counts.
- alder is in 5-year bands with 6099=60 år og derover as the top band. No total band.
- ieland is the original immigrant's origin country (niveau=3, ~146 countries present). No total code — SUM across ieland for all-country counts. Use ColumnValues("lande_psd", "titel", for_table="eb1") to see which countries are present.
- This table (along with eb2/eb3) covers the "børn af efterkommere" group — a 3rd generation category not present in standard herkomst classifications (folk1c/folk1e).