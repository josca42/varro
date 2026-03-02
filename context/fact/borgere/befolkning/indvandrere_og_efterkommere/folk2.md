table: fact.folk2
description: Befolkningen 1. januar efter alder, køn, herkomst, statsborgerskab, oprindelsesland og tid
measure: indhold (unit Antal)
columns:
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- kon: values [M=Mænd, K=Kvinder]
- herkomst: values [5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere]
- statsb: values [DANSK=Dansk, UDLAND=Udenlandsk ]
- ieland: join dim.lande_psd on ieland=kode; levels [3]
- tid: date range 1980-01-01 to 2025-01-01
dim docs: /dim/lande_psd.md

notes:
- No total rows for kon (M/K only), herkomst (3/4/5 only), or statsb (DANSK/UDLAND only). To get population totals you must SUM across these columns explicitly.
- ieland is niveau=3 individual countries. ieland code 0 is in dim.lande_psd as "Helt uoplyst" — in this table it functions as the "I alt" aggregate across origins; use ieland=0 to sum across all countries.
- All 6 combinations of herkomst × statsb exist (e.g. herkomst=5 dansk oprindelse with statsb=UDLAND is non-zero — some people of Danish origin hold foreign citizenship). Don't assume herkomst and statsb are redundant.
- alder has individual years (0–125) with no total row. Must SUM across alder to get all-age counts.
- Goes back to 1980 — the longest annual herkomst × ieland series. Use this for historical trends by origin country.