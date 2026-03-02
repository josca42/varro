table: fact.sbr04
description: Sygehusbenyttelse i befolkningen efter nøgletal, sygehusvæsen, alder, køn og tid
measure: indhold (unit -)
columns:
- bnogle: values [200600=Personer med ophold (antal), 200610=Personer med ophold (pct.), 200620=Ophold per person (antal), 200630=Personer med ophold på under 12 timer (antal), 200640=Personer med ophold på under 12 timer (pct.), 200650=Ophold på under 12 timer per person (antal), 200660=Personer med ophold på 12 timer eller derover (antal), 200670=Personer med ophold på 12 timer eller derover (pct.), 200680=Ophold på 12 timer eller derover per person (antal)]
- sygehusvaesen: values [200500=Uanset sygehusvæsen, 200510=Somatik, 200520=Psykiatri, 200530=Både somatik og psykiatri]
- alder: values [0000=Alder i alt, 0117=0-17 år, 18-29=18-29 år, 30-59=30-59 år, 6099=60 år og derover]
- kon: values [00=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- bnogle is a measurement selector — mix of counts (antal), percentages (pct.), and per-person rates. ALWAYS filter to exactly one bnogle value. Never sum across bnogle codes.
- sygehusvaesen: code 200530 = "Både somatik og psykiatri" are persons counted in BOTH 200510 and 200520 — they overlap. Do not sum across all four codes. Use 200500 (uanset sygehusvæsen) for totals.
- alder uses broad 4-group scheme (0117, 18-29, 30-59, 6099) plus total (0000). Filter alder='0000' and kon='00' for population totals.