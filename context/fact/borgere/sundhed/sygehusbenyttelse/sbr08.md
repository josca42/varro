table: fact.sbr08
description: Sygehusbenyttelse i befolkningen efter nøgletal, herkomst, alder, køn og tid
measure: indhold (unit -)
columns:
- bnogle: values [200600=Personer med ophold (antal), 200610=Personer med ophold (pct.), 200620=Ophold per person (antal), 200630=Personer med ophold på under 12 timer (antal), 200640=Personer med ophold på under 12 timer (pct.), 200650=Ophold på under 12 timer per person (antal), 200660=Personer med ophold på 12 timer eller derover (antal), 200670=Personer med ophold på 12 timer eller derover (pct.), 200680=Ophold på 12 timer eller derover per person (antal)]
- herkomst: join dim.herkomst on herkomst=kode [approx]
- alder: values [0000=Alder i alt, 0117=0-17 år, 18-29=18-29 år, 30-59=30-59 år, 6099=60 år og derover]
- kon: values [00=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2017-01-01 to 2024-01-01
dim docs: /dim/herkomst.md

notes:
- BROKEN DIM LINK: herkomst in this table uses codes 10/20/30/40, not 1/2/3/9 as in dim.herkomst. The join f.herkomst=d.kode returns 0 matches. Do NOT join dim.herkomst. Use inline values directly: 10=Personer med dansk oprindelse, 20=Indvandrere, 30=Efterkommere, 40=Uoplyst.
- bnogle is a measurement selector — mix of counts (antal), percentages (pct.), and per-person rates. ALWAYS filter to exactly one bnogle value. Never sum across bnogle codes.
- alder and kon have totals: filter alder='0000' and kon='00' for population totals.