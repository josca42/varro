table: fact.sbr03
description: Sygehusbenyttelse i befolkningen efter nøgletal, antal sygehusophold, alder, køn og tid
measure: indhold (unit -)
columns:
- bnogle: values [200600=Personer med ophold (antal), 200610=Personer med ophold (pct.), 200630=Personer med ophold på under 12 timer (antal), 200640=Personer med ophold på under 12 timer (pct.), 200660=Personer med ophold på 12 timer eller derover (antal), 200670=Personer med ophold på 12 timer eller derover (pct.)]
- antal_sygehusophold: values [200400=1 ophold, 200410=2 ophold, 200420=3-5 ophold, 200430=6 ophold eller derover]
- alder: values [0000=Alder i alt, 0AAR=0 år, 0109=1-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 90-=90 år og derover]
- kon: values [00=Køn i alt, M=Mænd, K=Kvinder]
- tid: date range 2017-01-01 to 2024-01-01

notes:
- bnogle is a measurement selector — every dimension combination appears once per bnogle value. Mix of counts (antal) and percentages (pct.). ALWAYS filter to exactly one bnogle value before summing. Never sum across bnogle codes.
- antal_sygehusophold classifies persons by number of stays (1, 2, 3-5, ≥6). These four categories are mutually exclusive and exhaustive for persons with any stay — summing them gives total persons hospitalised. No "i alt" total code, so summing all four is safe.
- pct. values in bnogle (200610, 200640, 200670) are percentages of the population — do not sum across antal_sygehusophold categories.
- alder uses the 0000/0AAR/0109/... scheme (same as sbr02). Filter alder='0000' and kon='00' for totals.