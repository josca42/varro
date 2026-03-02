table: fact.sbr05
description: Sygehusbenyttelse i befolkningen efter nøgletal, sygehustype, alder, køn og tid
measure: indhold (unit -)
columns:
- bnogle: values [200600=Personer med ophold (antal), 200610=Personer med ophold (pct.), 200620=Ophold per person (antal), 200630=Personer med ophold på under 12 timer (antal), 200640=Personer med ophold på under 12 timer (pct.), 200650=Ophold på under 12 timer per person (antal), 200660=Personer med ophold på 12 timer eller derover (antal), 200670=Personer med ophold på 12 timer eller derover (pct.), 200680=Ophold på 12 timer eller derover per person (antal)]
- syghus: values [200700=Alle sygehustyper, 200710=Offentligt sygehus, 200720=Privat sygehus, 200725=Både offentligt og privat sygehus, 200730=Uoplyst sygehustype]
- alder: values [0000=Alder i alt, 0117=0-17 år, 18-29=18-29 år, 30-59=30-59 år, 6099=60 år og derover]
- kon: values [00=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- bnogle is a measurement selector — mix of counts (antal), percentages (pct.), and per-person rates. ALWAYS filter to exactly one bnogle value. Never sum across bnogle codes.
- syghus: code 200725 = "Både offentligt og privat sygehus" are persons who used both types — they overlap with 200710 and 200720. Do not sum across codes. Use 200700 (alle sygehustyper) for totals.
- alder uses broad 4-group scheme. Filter alder='0000' and kon='00' for totals.